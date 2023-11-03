from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    sport:str
    best_player:str

@app.get("/")
async def root():
    return {'message':'Hello binay raj parajuli'}
    
@app.get("/home")
def root(): 
    return {'msg':'hello'}

@app.post("/create_post")
def create_post(post:Post):
    print(post.sport)
    return {"new_post":post} 
                