print("main loaded")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import security.auth as auth
import security.injection as injection
import security.pii as pii
import security.rate_limit as rate_limit
import security.logger as logger
import security.behavioral_threat as behavioral_threat


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


@app.get("/")
def home():
    return {"status": "AI Security Platform Running"}


@app.post("/query")
def secure_query(data: QueryRequest):

    user = data.user
    token = data.token

    # 1. Mask PII immediately
    clean_prompt = pii.mask_pii(data.prompt)

    # 2. Authentication check
    if not auth.verify_token(token):
        logger.log_event(f"Unauthorized access attempt by {user}")
        raise HTTPException(status_code=401, detail="Invalid token")

    # 3. Rate limiting check
    if not rate_limit.check_rate_limit(user):
        logger.log_event(f"Rate limit exceeded by {user}")
        raise HTTPException(status_code=429, detail="Too many requests")

    # 4. Behavioral threat detection
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

    # 5. Prompt injection detection
    if injection.detect_prompt_injection(clean_prompt):
        logger.log_event(f"Prompt injection attempt blocked for user: {user}")

        return {
            "status": "blocked",
            "reason": "Prompt injection detected",
            "threat_analysis": threat_result
        }

    # 6. Safe logging only
    logger.log_event(
        f"ALLOWED | user={user} | ip={data.ip} | endpoint={data.endpoint} | score={threat_result['threat_score']}"
    )

    return {
        "status": "success",
        "response": f"Processed: {clean_prompt}",
        "threat_analysis": threat_result
    }