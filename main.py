from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    name:str
    age:int
    single : bool= True
    rating : Optional[int]=None
    

@app.get("/")
def read():
    return {'message':'Hello'}


@app.post("/create")
def create(payload: Post):
    print(payload.rating)
    return {'message':f"name {payload.name.capitalize()} age {payload.age} single {payload.single} {payload.rating}"}

        
        


