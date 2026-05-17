from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRE_MIN = int(os.getenv("ACCES_TOKEN_EXPIRE_MINUTE", "60"))

def create_access_token(data: dict) -> str :
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_MIN)
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict :
    try :
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError :
        return None