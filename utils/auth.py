from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utils.jwt import decode_access_token
from sqlalchemy.orm import Session
from database import get_db
from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  payload = decode_access_token(token)
  if payload is None:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
  user_id = payload.get("sub")
  user = db.query(User).filter(User.id == int(user_id)).first()
  if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return user