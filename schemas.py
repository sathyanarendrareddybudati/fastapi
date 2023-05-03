from pydantic import BaseModel

class CollegeIn(BaseModel):
    name: str
    place: str

class CollegeOut(BaseModel):
    name:str
    place:str

    class Config:
        orm_mode=True

class SchoolsIn(BaseModel):
    name:str
    place:str

class SchoolsOut(BaseModel):
    name:str
    place:str

    class Config:
        orm_mode=True