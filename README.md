# 🔐 AI Security Middleware with Behavioral Threat Detection

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Defense--in--Depth-red)
![Status](https://img.shields.io/badge/Project-Production--Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 👤 Author  
**Louis Okperiruisi**  
Cybersecurity Analyst | SOC | AI Security | Detection Engineering  

---

## 📌 Overview

This project implements a **defense-in-depth AI security system** designed to protect applications from modern threats such as:

- Prompt injection attacks  
- Sensitive data (PII) exposure  
- Behavioral anomalies  
- Brute-force login attempts  
- Insider threats  

It combines **frontend and backend protections** to ensure sensitive data is sanitized before and after transmission, while continuously analyzing user behavior for real-time threat detection.

---
## 📸 Screenshots

### 🔹 **Secure Frontend Input (PII Masking)**
![Frontend UI](ai_security_platform/screenshots/frontend-ui.png)

---

### 🔹 **API Response with Sanitized Data**
![API Response](ai_security_platform/screenshots/api-response.png)

---

### 🔹 **Behavioral Threat Detection Output**
![Threat Detection](ai_security_platform/screenshots/threat-detection.png)

---

### 🔹 **Blocked Malicious Request (403)**
![Blocked Request](ai_security_platform/screenshots/blocked-request.png)

---

## 🧠 Key Features

### 🔐 Multi-Layer Security Architecture

- Authentication validation  
- Rate limiting enforcement  
- Prompt injection detection  
- PII sanitization (client + server)  
- Behavioral threat scoring  
- Secure logging  

---

### 🧾 PII Protection (Defense-in-Depth)

| Layer | Description |
|------|------------|
| Frontend | Masks PII before sending request |
| Backend | Re-validates and sanitizes input |
| Logging | Prevents raw PII exposure |

**Detected PII:**
- Emails → `[EMAIL]`  
- Phone numbers → `[PHONE]`  
- Date of Birth → `[DOB]`  

---
### 🧠 Behavioral Threat Detection

The system evaluates user activity using:

- Failed login patterns  
- IP address anomalies  
- After-hours access  
- Sensitive endpoint usage  
- High-risk actions (e.g., data export, privilege escalation)  

#### 🚨 Threat Levels
- Low  
- Medium  
- High  
- Critical  

#### 🔒 Automated Actions
- Account lockout  
- IP blacklisting  
- Request blocking (403)  

---

## 🚨 Example Detection Scenarios

| Scenario | Outcome |
|--------|--------|
| Multiple failed logins | Flagged |
| Failed + successful login | High risk |
| Sensitive endpoint + export | Blocked |
| Repeated attacks | IP blacklisted |

---

## 🏗️ Architecture
Client Input
↓
Frontend PII Masking (JavaScript)
↓
FastAPI Backend
↓
PII Sanitization (Python)
↓
Authentication Check
↓
Rate Limiting
↓
Behavioral Threat Detection
↓
Prompt Injection Detection
↓
Secure Logging
↓
Response


---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)  
- **Frontend:** HTML + JavaScript  
- **Security Modules:**
  - Regex-based PII detection  
  - Behavioral analytics engine  
  - Rate limiting system  
  - Injection detection logic  

---
## 📂 Project Structure
ai_security_platform/
│
├── main.py
├── index.html
├── screenshots/
│
├── security/
│ ├── auth.py
│ ├── injection.py
│ ├── pii.py
│ ├── rate_limit.py
│ ├── logger.py
│ ├── behavioral_threat.py
│
└── requirements.txt


---
## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt

---
### 2. Run FastAPI server
uvicorn main:app --reload
---

### 3. Open API Docs
http://127.0.0.1:8000/docs
---

### 4. Run Frontend

Open: index.html (from project folder/ local Disk C)


---

## 🧪 Testing

### 🔴 Failed Login Simulation
{
"user": "attacker",
"token": "anyvalue",
"prompt": "Testing failed login",
"ip": "192.168.1.50",
"action": "login",
"status": "failed",
"endpoint": "/login"
}


Repeat 5 times → triggers:
- Account lockout  
- IP blacklist  
- Request blocking  

---

### 🔴 High-Risk Behavior
{
"user": "insider_user",
"token": "anyvalue",
"prompt": "Export all user records",
"ip": "192.168.1.88",
"action": "data_export",
"status": "success",
"endpoint": "/api/export"
}


---

## 📊 Measurable Impact

- Prevented raw PII exposure using dual-layer sanitization (frontend + backend)  
- Detected and blocked brute-force login attacks after 5 failed attempts  
- Implemented behavioral threat scoring with automated blocking  
- Reduced prompt injection risk using input validation  

---

## 🔒 Security Design Principles

- Defense-in-depth  
- Least privilege access  
- Input validation & sanitization  
- Behavioral analytics  
- Zero trust mindset  

---

## 🎯 Why This Project Matters

Modern AI systems are vulnerable to prompt injection, data leakage, and behavioral attacks.  
This project demonstrates how traditional cybersecurity principles can be combined with AI-aware controls to secure intelligent systems.

---

## 📈 Future Improvements

- Geo-IP anomaly detection  
- Machine learning-based threat scoring  
- Real-time dashboard (SIEM-style)  
- Database-backed logging (ELK/Splunk integration)   

---

## 📬 Contact

- GitHub: https://github.com/louisky2001  
- LinkedIn: *(Add your LinkedIn link here)*  

---

## ⭐ Final Note

This project showcases how modern systems can integrate **AI-aware security controls with traditional cybersecurity practices** to protect applications against evolving threats.


