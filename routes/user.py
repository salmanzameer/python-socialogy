from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers import users_controller
import schemas
from database import get_db
from typing import List

router = APIRouter()

@router.get('/users', response_model=List[schemas.user.UserResponse])
def index(db: Session = Depends(get_db)):
  return users_controller.index(db)

@router.post('/users', response_model=schemas.user.UserResponse)
def create(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
  users_controller.create(db, user)