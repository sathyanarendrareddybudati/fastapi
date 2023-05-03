from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from models import Schools
from database import get_database_session
from schemas import SchoolsIn,SchoolsOut

router = APIRouter(
    tags=['SCHOOLS']
)

@router.get("/schools/")
def School(db:Session=Depends(get_database_session)):
    schools=db.query(Schools).all()
    return {"data":schools, "message":"data get successfully"}

@router.get("/schools/{school_id}")
def School(school_id:int, db:Session=Depends(get_database_session)):
    schools=db.query(Schools).filter(Schools.id==school_id).first()
    return {"data":schools, 'message':"data get successfully"}

@router.post("/schools/", status_code=status.HTTP_201_CREATED,response_model=SchoolsOut)
def School(school:SchoolsIn, db:Session=Depends(get_database_session)):
    # school_add = Schools(name=school.name,place=school.place)
    school_add=Schools(**school.dict())
    if school_add.name == school_add.name:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED)
    db.add(school_add)
    db.commit()
    db.refresh(school_add)
    return school_add

@router.delete("/schools")
def School(school_id:int, db:Session=Depends(get_database_session)):
    schools=db.query(Schools).filter(Schools.id==school_id)
    if not schools:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='school with this id was not found')
    schools.delete(synchronize_session=False)
    db.commit()
    return {"message":"data deleted successfully"}

@router.put("/schools")
def School(school_id:int,schools_update:SchoolsIn, db:Session=Depends(get_database_session)):
    schools=db.query(Schools).filter(Schools.id==school_id)
    if not schools.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='school with this id was not found')
    schools.update(schools_update, synchronize_session=False)
    db.commit()
    return {"message":"data was updated"}
