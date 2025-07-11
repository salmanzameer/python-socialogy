from sqlalchemy.orm import Session
from models.blog import Blog
from schemas.blog import BlogCreate

def index(db: Session):
    return db.query(Blog).all()

def show(db: Session, id: int):
  return db.query(Blog).filter( Blog.id == id).first

def create(db: Session, blog: BlogCreate):
  db_blog = Blog(**blog.dict())
  db.add(db_blog)
  db.commit()
  db.refresh(db_blog)
  return db_blog