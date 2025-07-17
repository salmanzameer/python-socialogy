from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers import users_controller
import schemas
from database import get_db
from typing import List
from serializers.user import serialize_user, serialize_user_with_blogs


router = APIRouter()

@router.get('/users', response_model=List[schemas.user.UserResponse])
def index(db: Session = Depends(get_db)):
  users = users_controller.index(db)
  return [serialize_user_with_blogs(user) for user in users]

@router.get('/user/{id}', response_model=schemas.user.UserResponse)
def show(id: int, db: Session = Depends(get_db)):
  user = users_controller.show(db, id)
  return serialize_user_with_blogs(user)

@router.post('/users', response_model=schemas.user.UserResponse)
def create(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
  user =  users_controller.create(db, user)
  return serialize_user(user)