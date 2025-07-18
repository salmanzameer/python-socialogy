from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers import blogs_controller
import schemas 
from database import get_db
from typing import List
from models.user import User
from utils.auth import get_current_user

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to the Blog API"}

@router.get('/blogs', response_model=List[schemas.blog.BlogResponse])
def index(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return blogs_controller.index(db, current_user)

@router.get('/blog/{id}', response_model=schemas.blog.BlogResponse)
def show(id: int, db: Session = Depends(get_db)):
  return blogs_controller.show(db, id)


@router.post('/blogs', response_model=schemas.blog.BlogResponse)
def create(blog: schemas.blog.BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return blogs_controller.create(db, blog, current_user)


