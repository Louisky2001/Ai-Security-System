# 🔐 AI Security Middleware with Behavioral Threat Detection & Phishing Defense

🚨 **A production-style security system that simulates how a Security Operations Center (SOC) detects, analyzes, and blocks real-world cyber threats in real time.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Defense--in--Depth-red)
![Status](https://img.shields.io/badge/Project-Production--Ready-brightgreen)
![SOC Ready](https://img.shields.io/badge/SOC-Ready-blue)

---

## 👤 Author  
**Louis Okperiruisi**  
Cybersecurity Analyst | SOC | Detection Engineering | AI Security  

---

## 🚀 Why This Project Matters

Modern applications face evolving threats including:

- Phishing attacks  
- Credential theft  
- Insider threats  
- Prompt injection (AI systems)  
- Malware execution and persistence  

👉 This project demonstrates how to **proactively detect, analyze, and automatically respond to these threats using layered security controls and real-time decision logic.**

---

## 📌 Overview

This project implements a **defense-in-depth AI security middleware** designed to protect APIs and modern applications.

It integrates multiple detection layers to:

- Identify malicious behavior  
- Correlate threat signals  
- Automatically block high-risk activity  
- Provide SOC-style visibility into security events  

---

## 🧠 System Architecture
User Request → FastAPI Endpoint
↓
┌────────────────────────────┐
│ Security Middleware Layer │
├────────────────────────────┤
│ ✔ Auth Verification │
│ ✔ Rate Limiting │
│ ✔ PII Masking │
│ ✔ Prompt Injection Check │
│ ✔ Behavioral Analysis │
│ ✔ Phishing Detection │
│ ✔ Malware Detection │
└────────────────────────────┘
↓
Decision Engine
(Allow / Block / Log)


👉 Each layer operates independently and collectively to enforce **defense-in-depth security**

---

## 📁 Project Structure
AI-Security-Middleware/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── security/
│ │ ├── auth.py # Authentication & token validation
│ │ ├── injection.py # Prompt injection detection
│ │ ├── pii.py # PII masking (email, phone, etc.)
│ │ ├── rate_limit.py # Rate limiting & abuse prevention
│ │ ├── behavioral_threat.py # Behavioral threat scoring engine
│ │ ├── phishing_detector.py # Phishing analysis (headers + content)
│ │ ├── malware_detector.py # Malware behavior detection engine
│ │ └── logger.py # Security event logging
│
├── screenshots/ # Project demo images
├── tests/ # Test scenarios & validation
├── requirements.txt # Dependencies
├── README.md # Documentation
├── .gitignore # Ignored files (logs, env, etc.)


👉 The system is modularized to reflect **real-world SOC pipelines**, where each component independently analyzes threats and contributes to final security decisions.

---

## 📸 Screenshots

### 🔹 Phishing Email Detection (Blocked)
![Phishing Blocked](ai_security_platform/screenshots/phishing-blocked-email.png)

### 🔹 VirusTotal Threat Intelligence
![Threat Intel](ai_security_platform/screenshots/virustotal-threat-intel.png)

### 🔹 Behavioral Threat Detection Output
![Threat Detection](ai_security_platform/screenshots/threat-detection.png)

### 🔹 Secure API Response (PII Masked)
![API Response](ai_security_platform/screenshots/api-response.png)

---

## 🔐 Multi-Layer Security Architecture

This platform combines:

- Prompt Injection Detection Layer  
- Phishing Email Analysis Engine  
- Behavioral Threat Scoring System  
- Malware Behavior Detection Engine  
- Threat Intelligence Integration (VirusTotal)  
- PII Protection Layer  

---

## 🛡️ Security Capabilities

- Prompt Injection Detection & Blocking  
- Phishing Email Detection & Automated Response  
- Behavioral Threat Analysis (Anomaly Detection, Brute-force, Insider Risk)  
- Malware Behavior Detection (Credential Dumping, Privilege Escalation, Ransomware, C2 Activity)  
- PII Masking (Client + Backend Protection)  
- API Rate Limiting & Abuse Prevention  
- Threat Intelligence Integration (VirusTotal)  

---

## 🎯 Security Impact (SOC Perspective)

This system simulates real SOC capabilities:

- Detects and blocks phishing attempts before credential compromise  
- Identifies credential dumping (LSASS targeting)  
- Detects abnormal login behavior and insider threats  
- Prevents prompt injection in AI-driven workflows  
- Blocks malware-like execution patterns in real time  

👉 **Outcome:**
- Reduced attack surface  
- Faster threat detection  
- Automated response to high-risk activity  
- Shift from reactive monitoring → proactive defense  

---

## 🧪 Test Scenarios

| Attack Type | Detection Method | Response |
|------------|----------------|---------|
| Phishing Email | Header + URL + Threat Intel | Blocked (403) |
| Credential Dumping | LSASS access detection | Blocked |
| Privilege Escalation | runAs / PowerShell patterns | Blocked |
| Prompt Injection | Pattern detection | Blocked |
| Rate Abuse | Request frequency analysis | 429 |
| Insider Threat | Behavioral scoring | Blocked |

---

## 🧠 MITRE ATT&CK Mapping

### 🔓 Credential Access (TA0006)
- T1003 – OS Credential Dumping  

### ⬆️ Privilege Escalation (TA0004)
- T1548 – Abuse Elevation Control Mechanism  

### ⚙️ Execution (TA0002)
- T1059 – Command and Scripting Interpreter  

### 🧷 Persistence (TA0003)
- T1547 – Autostart Execution  

### 🌐 Command & Control (TA0011)
- T1071 – Application Layer Protocol  

### 🔐 Impact (TA0040)
- T1486 – Data Encrypted for Impact  

### 🎣 Initial Access (TA0001)
- T1566 – Phishing  

---

## 💀 Malware Detection & Response Engine

Detects:

- Credential dumping (LSASS access)  
- Privilege escalation attempts  
- Suspicious PowerShell execution  
- Ransomware activity  
- Persistence mechanisms  
- Command-and-control communication  

### 🚫 Response
- High-risk behavior → Blocked (HTTP 403)  
- Logged for forensic analysis  

---

## 🔄 System Workflow

1. User sends request  
2. Request passes through security layers  
3. Each module evaluates risk  
4. Threat score is calculated  
5. Decision engine:
   - Allow  
   - Block  
   - Log  

---

## 🚀 Future Enhancements

- SIEM integration (Wazuh / ELK)  
- Real-time alerting (Slack / Email)  
- ML-based anomaly detection  
- Threat correlation engine  

---

## 🔗 Links

- 🌐 Portfolio: https://louisky.vercel.app  
- 💻 GitHub: https://github.com/Louisky2001  

---

## 🧠 Final Note

This project demonstrates **practical cybersecurity engineering** — not just theory.

👉 Built to reflect how modern SOC teams detect, analyze, and respond to threats in real environments.

