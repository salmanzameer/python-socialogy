from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from serializers.user import serialize_user, serialize_user_with_blogs
import schemas
from utils.security import verify_password
from utils.jwt import create_access_token
from pydantic import BaseModel
from models.user import User

router = APIRouter()


class LoginData(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.email == data.email).first()
  if not user or not verify_password(data.password, user.password):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

  token = create_access_token({"sub": str(user.id)})

  return {"access_token": token, "token_type": "bearer"}