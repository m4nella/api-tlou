from typing import Optional

from pydantic import BaseModel

class Character(BaseModel):
    id: Optional[int] = None
    name: str 
    status: str
    part: str
    gender: str
    
    
    