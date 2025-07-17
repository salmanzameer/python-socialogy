from pydantic import BaseModel
from schemas.blog import BlogBase
from typing import List

class UserBase(BaseModel):
    first_name: str
    last_name: str
    dob: str
    is_active: bool
    gender: str
    email: str
    
class UserCreate(UserBase):
  pass

class UserResponse(UserBase):
  id: int
  full_name: str
  status: str
  blogs: List[BlogBase] = []
  class Config:
    orm_mode = True
  