from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    dob: str
    is_active: bool
    gender: str


class UserCreate(UserBase):
  pass

class UserResponse(UserBase):
  id: int
  class Config:
    orm_mode = True