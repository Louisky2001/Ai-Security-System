from datetime import datetime, time, timedelta
from collections import defaultdict


# In-memory trackers
failed_login_tracker = defaultdict(int)
user_ip_tracker = defaultdict(set)
locked_users = {}
blacklisted_ips = set()


BUSINESS_START = time(8, 0)
BUSINESS_END = time(18, 0)

FAILED_LOGIN_LIMIT = 5
LOCKOUT_MINUTES = 15
BLOCK_SCORE = 80


SENSITIVE_ENDPOINTS = [
    "/admin",
    "/finance",
    "/hr",
    "/security/logs",
    "/api/users",
    "/api/export"
]


HIGH_RISK_ACTIONS = [
    "privilege_escalation",
    "data_export",
    "disable_security",
    "delete_logs",
    "mass_download"
]


def is_after_hours():
    now = datetime.now().time()
    return now < BUSINESS_START or now > BUSINESS_END


def is_user_locked(user):
    if user not in locked_users:
        return False

    lock_expiry = locked_users[user]

    if datetime.now() >= lock_expiry:
        del locked_users[user]
        failed_login_tracker[user] = 0
        return False

    return True


def lock_user(user):
    locked_users[user] = datetime.now() + timedelta(minutes=LOCKOUT_MINUTES)


def blacklist_ip(ip):
    blacklisted_ips.add(ip)


def calculate_threat_score(event):
    score = 0
    reasons = []

    user = event.get("user")
    ip = event.get("ip")
    action = event.get("action")
    status = event.get("status")
    endpoint = event.get("endpoint")

    # 1. Blacklisted IP
    if ip in blacklisted_ips:
        score += 100
        reasons.append("Request came from a blacklisted IP address")

    # 2. Locked account
    if is_user_locked(user):
        score += 100
        reasons.append("User account is temporarily locked")

    # 3. After-hours activity
    if is_after_hours():
        score += 20
        reasons.append("Activity occurred outside business hours")

    # 4. Failed login tracking
    if action == "login" and status == "failed":
        failed_login_tracker[user] += 1

        if failed_login_tracker[user] >= 3:
            score += 30
            reasons.append("Multiple failed login attempts detected")

        if failed_login_tracker[user] >= FAILED_LOGIN_LIMIT:
            score += 60
            reasons.append("Failed login threshold exceeded")
            lock_user(user)
            blacklist_ip(ip)

    # 5. Successful login after repeated failures
    if action == "login" and status == "success":
        if failed_login_tracker[user] >= 3:
            score += 40
            reasons.append("Successful login after multiple failed attempts")

        failed_login_tracker[user] = 0

    # 6. Multiple IPs for same user
    user_ip_tracker[user].add(ip)

    if len(user_ip_tracker[user]) > 2:
        score += 25
        reasons.append("User accessed system from multiple IP addresses")

    # 7. Sensitive endpoint access
    if endpoint in SENSITIVE_ENDPOINTS:
        score += 25
        reasons.append("Sensitive endpoint accessed")

    # 8. High-risk action
    if action in HIGH_RISK_ACTIONS:
        score += 50
        reasons.append("High-risk user action detected")

    # 9. Determine threat level
    if score >= 90:
        level = "critical"
    elif score >= 70:
        level = "high"
    elif score >= 40:
        level = "medium"
    else:
        level = "low"

    return {
        "user": user,
        "ip": ip,
        "endpoint": endpoint,
        "action": action,
        "status": status,
        "failed_login_count": failed_login_tracker[user],
        "account_locked": is_user_locked(user),
        "ip_blacklisted": ip in blacklisted_ips,
        "threat_score": score,
        "threat_level": level,
        "reasons": reasons
    }


def should_block(threat_result):
    return (
        threat_result["threat_score"] >= BLOCK_SCORE
        or threat_result["account_locked"]
        or threat_result["ip_blacklisted"]
    )