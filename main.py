from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from enum import Enum

app = FastAPI()  #instance


@app.get("/")   #HTTP "methods" -> POST  GET  PUT  DELETE
                #Decorator                                                      
@app.get("/")   #Decorator  
                #main URL ( get --> get request)  
                # ('/') -> Route/Endpoint/Path(FastAPI) 
                #base path 
                # get -> is called operation (operation on the path)
                # @app -> is called path operation decorator

def read_root():# is called <<Path operation function>>
    return {'name': {'firstName':'Mehrnaz'}}


@app.get("/about")   #about path
def about():
    return {'data': {'This is about page.'}}


@app.get('/blog/unpublished')
def get_unpublished():
    return {'data': 'all unpublished data'}


@app.get('/blog/{id}')   # usage -> creating routing
def get_id(id: int):
    # fetch blog with id = id 
    # fetch -> API Requests: In the context of web development, “fetch” is often used to refer to the process of
    # requesting data from an API.
    return {'data': id}

# Query parameter -> 1. type
#                    2. Default value
#                    3. Optional[ <type> ] = None
@app.get('/blog')

def my_query(limit = 10, published : bool = True, sort: Optional[str] = None):
    if published == 1:
        return {'data': {'limit': f'Hey you got {limit} published blogs from database.', 'published': published}}
    else:
        return {'data':{'limit': "Sorry, you just got a few blogs", 'published': published}}


# if the name in in path -> path parameter
# else                   -> query parameter

@app.get('/blog/{id}/comment')
def comment(id, limit = 10):
    return{'data':{id: {'1,2,3'}, 'limit': limit}}


@app.get("/models")
async def get_models():
    return {'data': {'This is the first model.'}}


class Model_name(str, Enum):
    Mehrnaz = "Mehrnaz"
    Mehrshad = "Mehrshad"

@app.get('/models/{model_name}')
def get_model_name(model_name: Model_name):
    if model_name is model_name.Mehrnaz:
        return {'model_name': {f'Hey, the model name is {model_name}.'}}
    elif model_name.value == "Mehrshad":
        return {'model_name': {f"Hi, the model name is the same as Mehrnaz brother's name, {model_name}"}}
    else:
        return {'model_name': {"Well, the model has some"}}



######################################################################################################################

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')  # POST decorator -> request
def create_blog(request: Blog):
    if request.published:
        return {'data': f"the blog is created as {request.title} and the blog is published."}
    else:
        return {'data': f"the blog is created as {request.title}."}


# To run on different addres -> used for Debugging
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port = 9000)