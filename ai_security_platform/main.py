print("main loaded")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai_security_platform.security import auth
from ai_security_platform.security import injection
from ai_security_platform.security import pii
from ai_security_platform.security import rate_limit
from ai_security_platform.security import logger
from ai_security_platform.security import behavioral_threat
from ai_security_platform.security import phishing_detector


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    user: str
    token: str
    prompt: str
    ip: str = "127.0.0.1"
    action: str = "query"
    status: str = "success"
    endpoint: str = "/query"

    email_subject: str = ""
    email_body: str = ""
    email_headers: str = ""


@app.get("/")
def home():
    return {"status": "AI Security Platform Running"}


@app.post("/query")
def secure_query(data: QueryRequest):

    user = data.user
    token = data.token

    clean_prompt = pii.mask_pii(data.prompt)

    if not auth.verify_token(token):
        logger.log_event(f"Unauthorized access attempt by {user}")
        raise HTTPException(status_code=401, detail="Invalid token")

    if not rate_limit.check_rate_limit(user):
        logger.log_event(f"Rate limit exceeded by {user}")
        raise HTTPException(status_code=429, detail="Too many requests")

    phishing_result = None

    if data.action == "email_scan":
        phishing_result = phishing_detector.analyze_phishing_email(
            subject=data.email_subject,
            body=data.email_body,
            raw_headers=data.email_headers
        )

        if phishing_detector.should_block_email(phishing_result):
            logger.log_event(f"Phishing email blocked for user: {user}")

            raise HTTPException(
                status_code=403,
                detail={
                    "status": "blocked",
                    "message": "Email blocked due to phishing indicators",
                    "phishing_analysis": phishing_result
                }
            )

    event = {
        "user": user,
        "ip": data.ip,
        "action": data.action,
        "status": data.status,
        "endpoint": data.endpoint
    }

    threat_result = behavioral_threat.calculate_threat_score(event)

    if behavioral_threat.should_block(threat_result):
        logger.log_event(
            f"BLOCKED | user={user} | ip={data.ip} | threat_level={threat_result['threat_level']} | score={threat_result['threat_score']}"
        )

        raise HTTPException(
            status_code=403,
            detail={
                "status": "blocked",
                "message": "Request blocked due to behavioral threat detection",
                "threat_analysis": threat_result
            }
        )

    if injection.detect_prompt_injection(clean_prompt):
        logger.log_event(f"Prompt injection attempt blocked for user: {user}")

        return {
            "status": "blocked",
            "reason": "Prompt injection detected",
            "threat_analysis": threat_result,
            "phishing_analysis": phishing_result
        }

    logger.log_event(
        f"ALLOWED | user={user} | ip={data.ip} | endpoint={data.endpoint} | score={threat_result['threat_score']}"
    )

    return {
        "status": "success",
        "response": f"Processed: {clean_prompt}",
        "threat_analysis": threat_result,
        "phishing_analysis": phishing_result
    }