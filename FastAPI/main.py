from typing import Union,Optional
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import FastAPI, Response, status, HTTPException
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

my_posts = [{'title' :"This is post 1", "content":"content of post 1", 'id': 1},
            {'title' : "Favroute foods ", "content": "I like pizza","id" : 2}]

 
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p 


@app.get("/")
async def root():
    return {"Hello": "Welcome to the Fast api"}
    

@app.get("/posts")
def get_posts():
    return {"data": my_posts}     


@app.post("/posts", status_code=status.HTTP_201_CREATED) 
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0 ,1000000)
    my_posts.append(post_dict)
    return {"data" : post}


@app.get("/posts/latest")
def latest_posts():
    post = my_posts[len(my_posts)-1]
    return {"details" : post}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail={"message" : f"post with id : {id} was not found"})
        # Response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"post with id : {id} was not found"}
    return {"post details": post}
 