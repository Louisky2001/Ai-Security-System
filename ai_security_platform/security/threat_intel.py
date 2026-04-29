import requests

VT_API_KEY = "edd3fd32eff30859f66aa7aa2a4e89c58ac206c1838d4e3ac1582711f04f3eec"


def check_url_virustotal(url):
    headers = {
        "x-apikey": VT_API_KEY
    }

    try:
        response = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=headers,
            data={"url": url}
        )

        if response.status_code != 200:
            return {"error": "Failed to submit URL"}

        url_id = response.json()["data"]["id"]

        report = requests.get(
            f"https://www.virustotal.com/api/v3/analyses/{url_id}",
            headers=headers
        )

        stats = report.json()["data"]["attributes"]["stats"]

        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)

        return {
            "malicious": malicious,
            "suspicious": suspicious,
            "harmless": stats.get("harmless", 0),
            "verdict": "malicious" if malicious > 0 else "suspicious" if suspicious > 0 else "clean"
        }

    except Exception as e:
        return {"error": str(e)}