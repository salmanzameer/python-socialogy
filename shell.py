from sqlalchemy.orm import Session
from database import SessionLocal
import models

db: Session = SessionLocal()

print("Interactive DB shell loaded.")
print("Available: db, models (e.g., db.query(models.Blog).all())")