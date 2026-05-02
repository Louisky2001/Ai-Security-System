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
- **Malware Behavior Detection & Automated Response module**

---

## 📸 Screenshots

### 🔹 Phishing Email Detection (Blocked)
![Phishing Blocked](ai_security_platform/screenshots/phishing-blocked-email.png)

---

### 🔹 VirusTotal Threat Intelligence
![Threat Intel](ai_security_platform/screenshots/virustotal-threat-intel.png)

---

### 🔹 Behavioral Threat Detection Output
![Threat Detection](ai_security_platform/screenshots/threat-detection.png)

---

### 🔹 Secure API Response (PII Masked)
![API Response](ai_security_platform/screenshots/api-response.png)

---

## 🧠 Key Features

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
- Malware Behavior Detection (Credential Dumping, Ransomware, C2 Activity)  
- PII Masking (Client + Backend Protection)  
- API Rate Limiting & Abuse Prevention  
- Threat Intelligence Integration (VirusTotal)
---

## 📧 Phishing Email Detection & Response

### 🧠 Header Analysis
- SPF, DKIM, DMARC validation  
- Sender spoofing detection  
- Suspicious mail routing  

### 📩 Content Analysis
- Social engineering keyword detection  
- Suspicious URL extraction  

### 🌍 Threat Intelligence
- URLs enriched using **VirusTotal API**  
- Detects malicious and suspicious domains  

### 🚫 Automated Response
- High-risk emails → **Blocked (HTTP 403)**  
- Events logged for investigation  

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
- High-risk actions  

### 🚨 Response
- Account lockout  
- IP blacklisting  
- Request blocking  

---

## 🔄 System Workflow
