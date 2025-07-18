from sqlalchemy.orm import Session
from models.blog import Blog
from schemas.blog import BlogCreate
from models.user import User

def index(db: Session, current_user: User):
    return db.query(Blog).filter(Blog.user_id == current_user.id)

def show(db: Session, id: int):
  return db.query(Blog).filter( Blog.id == id).first()

def create(db: Session, blog: BlogCreate, current_user: User):
  db_blog = Blog(**blog.dict(exclude={'user_id'}), user_id = current_user.id)
  db.add(db_blog)
  db.commit()
  db.refresh(db_blog)
  return db_blog