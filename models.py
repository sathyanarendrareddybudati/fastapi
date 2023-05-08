from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
# from pydantic import BaseModel
# from sqlalchemy.types import String, Integer,DECIMAL


class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255))
    place = Column(String(255))

class Schools(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255))
    place = Column(String(255))