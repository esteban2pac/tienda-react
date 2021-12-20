from typing import Optional
from pydantic import BaseModel

class PlaceBase(BaseModel):
    name:str
    description: Optional[str] = None

class PlaceCreate(PlaceBase):
    pass

class PlaceUpdate(PlaceBase):
    pass

class PlaceInDBBase(PlaceBase):
    id: int

    class Config:
        orm_mode = True

class Place (PlaceInDBBase):
    pass

class PlaceInDB(PlaceInDBBase):
    pass