from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from models import College
from database import get_database_session
from schemas import CollegeIn,CollegeOut
from typing import List


router = APIRouter(
    tags=['COLLEGES']
)

@router.get("/colleges/{college_id}")
def Colleges(college_id:int, db: Session = Depends(get_database_session)):
    post = db.query(College).filter(College.id==college_id).first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'college with id was not found')
    return {"data":post, "message":"data get successfully"}


@router.get("/colleges",status_code=status.HTTP_200_OK,response_model=List[CollegeOut])
def Colleges(db: Session = Depends(get_database_session)):
    colleges = db.query(College).all()
    return colleges


@router.post("/colleges",status_code=status.HTTP_201_CREATED,response_model=CollegeOut)
def Colleges(college:CollegeIn,db: Session = Depends(get_database_session)):
    # colleges_add = models.College(name=college.name,place=college.place)
    college_add = College(**college.dict())
    db.add(college_add)
    db.commit()
    db.refresh(college_add)
    return college_add

@router.delete("/colleges")
def Colleges(college_id:int, db:Session=Depends(get_database_session)):
    college_add=db.query(College).filter(College.id==college_id)
    if college_add.first == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'college with id was not found')
    college_add.delete(synchronize_session=False)     
    db.commit()
    return {"message":"data deleted successfully"}


@router.put("/colleges",response_model=CollegeOut)
def Colleges(college_id:int, college_update:CollegeIn, db:Session=Depends(get_database_session)):
    college = db.query(College).filter(College.id==college_id)
    if college.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'college with this id was not found')
    college.update(college_update.dict(), synchronize_session=False)
    db.commit()
    return college.first()