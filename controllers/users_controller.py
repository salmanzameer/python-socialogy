from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate


def index(db: Session):
  return db.query(User).all()

def show(db: Session, id: int):
  return db.query(User).filter(User.id == id).first

def create(db: Session, user: UserCreate):
  db_user = User(**user.dict())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user
