from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    content: str
    published: bool
    
class BlogCreate(BlogBase):
    pass

class BlogResponse(BlogBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True
