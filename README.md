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

Modern systems are vulnerable to:
- Phishing attacks  
- Prompt injection  
- Data leakage  
- Insider threats  

👉 This project demonstrates how to **detect and automatically respond to these threats using layered security controls and real-time decision logic.**

---

## 📌 Overview

This project implements a **defense-in-depth AI security system** designed to protect modern applications from evolving cyber threats.

It integrates multiple layers to detect and respond to:

- Prompt injection attacks  
- Sensitive data (PII) exposure  
- Behavioral anomalies  
- Brute-force login attempts  
- Insider threats  
- **Phishing email attacks (header + content + threat intelligence)**  
- **Malware Behavior Detection & Automated Response**  

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

This platform implements a defense-in-depth approach combining:

- Prompt Injection Detection Layer  
- Phishing Email Analysis Engine  
- Behavioral Threat Scoring System  
- Malware Behavior Detection Module  
- Threat Intelligence Integration (VirusTotal)  
- PII Protection Layer  

Each layer operates independently and collectively to detect, analyze, and block threats in real time.

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

## 🧠 MITRE ATT&CK Mapping

This system aligns with the **MITRE ATT&CK framework**, providing structured detection across key attack stages:

### 🔓 Credential Access (TA0006)
- **Technique:** OS Credential Dumping (T1003)  
- Detects LSASS access, memory dumps, credential extraction tools  

### ⬆️ Privilege Escalation (TA0004)
- **Technique:** Abuse Elevation Control Mechanism (T1548)  
- Detects `runas`, PowerShell elevation, token/privilege abuse  

### ⚙️ Execution (TA0002)
- **Technique:** Command and Scripting Interpreter (T1059)  
- Detects encoded PowerShell commands and script-based execution  

### 🧷 Persistence (TA0003)
- **Technique:** Boot or Logon Autostart Execution (T1547)  
- Detects registry run keys and startup persistence  

### 🌐 Command & Control (TA0011)
- **Technique:** Application Layer Protocol (T1071)  
- Detects suspicious outbound connections to malicious IP ranges  

### 🔐 Impact (TA0040)
- **Technique:** Data Encrypted for Impact (T1486)  
- Detects ransomware behavior and file encryption patterns  

### 🎣 Initial Access (TA0001)
- **Technique:** Phishing (T1566)  
- Detects malicious emails using header, content, and threat intelligence analysis  

### 🧠 Discovery / Credential Access
- **Techniques:**  
  - Brute Force (T1110)  
  - Valid Accounts (T1078)  
- Detects abnormal login patterns and insider threats  

---

## 📧 Phishing Email Detection & Response

### 🧠 Header Analysis
- SPF, DKIM, DMARC validation  
- Sender spoofing detection  
- Suspicious routing  

### 📩 Content Analysis
- Social engineering detection  
- Malicious URL extraction  

### 🌍 Threat Intelligence
- URLs validated using **VirusTotal API**  

### 🚫 Automated Response
- High-risk emails → **Blocked (HTTP 403)**  
- Logged for SOC investigation  

---

## 🧾 PII Protection

| Layer | Description |
|------|------------|
| Frontend | Masks sensitive data |
| Backend | Re-validates input |
| Logging | Prevents exposure |

---

## 🧠 Behavioral Threat Detection

Detects:
- Failed login patterns  
- IP anomalies  
- After-hours access  
- Insider threat activity  

### 🚨 Response
- Account lockout  
- IP blacklisting  
- Request blocking  

---

## 💀 Malware Detection & Response Engine

Detects and blocks:

- Credential dumping (LSASS access)  
- Privilege escalation attempts (runAs, PowerShell elevation)  
- Suspicious PowerShell execution  
- Ransomware behavior (file encryption patterns)  
- Persistence mechanisms (registry modification)  
- Command-and-control (C2) communication  

### 🚫 Automated Response
- High-risk behavior → **Blocked (HTTP 403)**  
- Events logged for forensic analysis  

---

## 🔄 System Workflow
