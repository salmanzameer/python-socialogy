from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers import blogs_controller
import schemas 
from database import get_db
from typing import List
router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to the Blog API"}

@router.get('/blogs', response_model=List[schemas.blog.BlogResponse])
def index(db: Session = Depends(get_db)):
  return blogs_controller.index(db)

@router.post('/blogs', response_model=schemas.blog.BlogResponse)
def create(blog: schemas.blog.BlogCreate, db: Session = Depends(get_db)):
  return blogs_controller.create(db, blog)


