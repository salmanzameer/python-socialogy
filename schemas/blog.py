from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    content: str
    published: bool
    user_id: int
class BlogCreate(BlogBase):
    pass

class BlogResponse(BlogBase):
    id: int
    user_id: Optional[int] = None
    class Config:
        orm_mode = True
