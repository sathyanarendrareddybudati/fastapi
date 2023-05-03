from fastapi import FastAPI
from database import Base,engine
from routes import colleges,schools

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(colleges.router)
app.include_router(schools.router)

@app.get("/")
def Crud_opertion():
    return {"message":"welcome to crud opertions"}