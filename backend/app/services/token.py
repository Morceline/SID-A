from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "segredo_super_forte"
ALGORITHM = "HS256"

def criar_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=10)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)