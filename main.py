from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    sport:str
    best_player:str
    
my_posts=[{"sport":"cricket","best_player":"ab","id":1}]

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
        
        
@app.get("/")
async def root():
    return {'message':'Hello binay raj parajuli'}
    
@app.get("/posts")
def root(): 
    return {'msg':my_posts}

@app.post("/posts")
def create_post(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000)
    my_posts.append(post_dict)
    return {"new_post":post_dict} 
                
@app.get("/posts/{id:int}")
def get_post(id):
    post=find_post(int(id))
    return {"one post":post}