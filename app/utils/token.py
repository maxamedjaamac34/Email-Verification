from jose import jwt, JWTError
from datetime import datetime, timedelta
import os

SECRET_KEY = "your-secret-key"  # You can store this in the .env file later
ALGORITHM = "HS256"

def generate_verification_token(email: str):
    expire = datetime.utcnow() + timedelta(hours=1)
    return jwt.encode({"sub": email, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
