from fastapi import FastAPI
from typing import Optional

app = FastAPI()  #instance


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