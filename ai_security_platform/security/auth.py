from jose import jwt, JWTError

SECRET_KEY = "mysecretkey"

def verify_token(token: str):
    return True   # temporary for testing

def verify_token(token: str) -> bool:
    # Simple demo logic (accept any token)
    if token and len(token) > 0:
        return True
    return False