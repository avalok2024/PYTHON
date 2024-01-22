# REQUIRED : POSTMAN APP

from typing import Union,Optional
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import FastAPI, Response, status, HTTPException
from random import randrange
import psycopg2
from psycopg2.extras import RealDictConnection

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None
try:
    conn = psycopg2.connect(host="localhost", Database='fastapi', user='postgres',
                            password='avalok2024.postgres', port=5432, cursor_factory=RealDictConnection)
    cursor = conn.cursor()
    print("Database is succesfully connected")
except Exception as error:
    print('Connecting to Database Failed!')
    print('Error : ', error )

my_posts = [{'title' :"This is post 1", "content":"content of post 1", 'id': 1},
            {'title' : "Favroute foods ", "content": "I like pizza","id" : 2}, 
            {"title": "this is new title ", "content" :"this is a new content", "id" : 3}]

 
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p 

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


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
    
 
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    # deleteing posts
    # find the index in the array that has required ID 
    # my_posts.pop(index) 
    index = find_index_post(id)
    if index == None:                                       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id:{id} does not exits")
    my_posts.pop(index)
    return {"message" : "post was succesfully deleted"}
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}")
def update_posts(id : int, post: Post):
    index = find_index_post(id)

    if index == None:  
        raise HTTPException(status_code=status.HTTP_200_OK)

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"message": post_dict}   