from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate


def index(db: Session):
  return db.query(User).all()

def show(db: Session, id: int):
  user = db.query(User).filter(User.id == id).first()
  if not user:
    raise HTTPException(status_code=400, detail="User not found")
  return user 
  
def create(db: Session, user: UserCreate):
  user_exist = db.query(User).filter(User.email == user.email).first
  if user_exist:
    raise HTTPException(status_code=400, detail="Email already registered")

  db_user = User(**user.dict())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user
