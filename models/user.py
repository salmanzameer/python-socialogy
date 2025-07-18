from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    email = Column(String, nullable=False, unique=True)
    blogs = relationship("Blog", back_populates="user")   
    password = Column(String, nullable=False)     

