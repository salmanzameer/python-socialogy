from jose import jwt, JWTError
from datetime import datetime, timedelta


SECRET_KEY = "sdfhjwhefuwhfnxczn2wh237dhskdhscznmnczxncnqqxmxAFAJSAJFJ7ADLQDQ72"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta = None):
  to_encode = data.copy()
  expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
  to_encode.update({"exp": expire})
  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
  try:
      return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  except JWTError:
      return None