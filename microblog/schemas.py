from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str = ''
    text: str = ''

        
        
class PostList(PostBase):
    id: int
    date: Optional[datetime]
    

class PostSingle(PostList):
    children: List[PostBase]
    
class PostCreate(PostBase):
    parent_id: Optional[int] = None
    
    class Config:
        orm_mode = True
