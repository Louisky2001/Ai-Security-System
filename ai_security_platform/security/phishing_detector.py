import re
from email.parser import Parser

from ai_security_platform.security import threat_intel


PHISHING_KEYWORDS = [
    "verify your account",
    "password expires",
    "urgent action required",
    "click here",
    "login immediately",
    "account suspended",
    "confirm your identity",
    "update your payment",
    "unauthorized login",
    "reset your password"
]


SUSPICIOUS_TLDS = [
    ".ru", ".cn", ".tk", ".xyz", ".top", ".zip"
]


def extract_urls(text):
    if not text:
        return []

    return re.findall(r"https?://[^\s]+", text)


def extract_domain(email_address):
    match = re.search(r"@([\w.-]+)", email_address or "")
    return match.group(1).lower() if match else ""


def analyze_email_headers(raw_headers):
    score = 0
    reasons = []

    headers = Parser().parsestr(raw_headers or "")

    from_header = headers.get("From", "")
    return_path = headers.get("Return-Path", "")
    reply_to = headers.get("Reply-To", "")
    message_id = headers.get("Message-ID", "")
    auth_results = headers.get("Authentication-Results", "").lower()
    received = headers.get_all("Received", [])

    from_domain = extract_domain(from_header)
    return_path_domain = extract_domain(return_path)
    reply_to_domain = extract_domain(reply_to)
    message_id_domain = ""

    msg_match = re.search(r"@([\w.-]+)>?", message_id)
    if msg_match:
        message_id_domain = msg_match.group(1).lower()

    if "spf=fail" in auth_results:
        score += 30
        reasons.append("SPF authentication failed")

    if "dkim=fail" in auth_results:
        score += 30
        reasons.append("DKIM authentication failed")

    if "dmarc=fail" in auth_results:
        score += 40
        reasons.append("DMARC authentication failed")

    if from_domain and return_path_domain and from_domain != return_path_domain:
        score += 25
        reasons.append("From domain does not match Return-Path domain")

    if reply_to_domain and from_domain and reply_to_domain != from_domain:
        score += 20
        reasons.append("Reply-To domain does not match sender domain")

    if message_id_domain and from_domain and from_domain not in message_id_domain:
        score += 15
        reasons.append("Message-ID domain does not match sender domain")

    for item in received:
        lowered = item.lower()

        if "unknown" in lowered or any(tld in lowered for tld in SUSPICIOUS_TLDS):
            score += 15
            reasons.append("Suspicious Received header path detected")
            break

    return {
        "from_domain": from_domain,
        "return_path_domain": return_path_domain,
        "reply_to_domain": reply_to_domain,
        "message_id_domain": message_id_domain,
        "received_hops": len(received),
        "header_score": score,
        "header_reasons": reasons
    }


def analyze_email_body(subject, body):
    score = 0
    reasons = []
    threat_intel_results = []

    subject = subject or ""
    body = body or ""

    combined_text = f"{subject} {body}".lower()

    for keyword in PHISHING_KEYWORDS:
        if keyword in combined_text:
            score += 15
            reasons.append(f"Suspicious phishing phrase detected: {keyword}")

    urls = extract_urls(body)

    if len(urls) > 0:
        score += 10
        reasons.append("Email contains external URL(s)")

    for url in urls:
        if any(tld in url.lower() for tld in SUSPICIOUS_TLDS):
            score += 25
            reasons.append(f"Suspicious URL detected: {url}")

        vt_result = threat_intel.check_url_virustotal(url)

        threat_intel_results.append({
            "url": url,
            "virustotal": vt_result
        })

        if vt_result.get("malicious", 0) > 0:
            score += 40
            reasons.append(f"Malicious URL detected via VirusTotal: {url}")

        elif vt_result.get("suspicious", 0) > 0:
            score += 25
            reasons.append(f"Suspicious URL detected via VirusTotal: {url}")

    return {
        "urls": urls,
        "body_score": score,
        "body_reasons": reasons,
        "threat_intel": threat_intel_results
    }


def analyze_phishing_email(subject, body, raw_headers):
    header_result = analyze_email_headers(raw_headers)
    body_result = analyze_email_body(subject, body)

    total_score = header_result["header_score"] + body_result["body_score"]

    if total_score >= 80:
        risk_level = "critical"
    elif total_score >= 55:
        risk_level = "high"
    elif total_score >= 30:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "phishing_score": total_score,
        "phishing_risk": risk_level,
        "header_analysis": header_result,
        "body_analysis": body_result,
        "reasons": header_result["header_reasons"] + body_result["body_reasons"]
    }


def should_block_email(phishing_result):
    return phishing_result["phishing_score"] >= 80