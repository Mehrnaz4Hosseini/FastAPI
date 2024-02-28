from typing import Optional, Union
from fastapi import APIRouter, Query
from typing_extensions import Annotated
from pydantic import BaseModel

router = APIRouter()  # -> you can think of APIRouter as a "mini FastAPI" class.


@router.get('/blog/unpublished')
def get_unpublished_blog():
    return {'data': 'all unpublished data'}





@router.get('/blog/{id}')   # usage -> creating routing
def get_blog_id(id: int):
    # fetch blog with id = id 
    # fetch -> API Requests: In the context of web development, “fetch” is often used to refer to the process of
    # requesting data from an API.
    return {'data': id}





# Query parameter -> 1. not in the path 
#                    2. Default value
#                    3. Optional[ <type> ] = None

# if the name in in path -> path parameter
# else                   -> query parameter
@router.get('/blog')
def my_blog_introduction(limit = 10, published : bool = False, sort: Union[str, None] = None): # -> sort is not required because of 
                                                                                   # the default value = None.
# " = None " -> tells FastAPI that this parameter is not required, NOT the " Union[str, None] "
    if published:
        return {'data': {'limit': f'Hey you got {limit} published blogs from database.', 'published': published}}
    else:
        return {'data':{'limit': "Sorry, you just got a few blogs", 'published': published}}
    

async def read_blog_item(
        q: Annotated[
             Union[str, None] ,
               Query(
                   min_length=2,
                   max_length=50,
                   pattern="^Mehrnaz$",
                   deprecated= True, # recommanded not to use
                   include_in_schema= False # Do not show a query parameter in the generated OpenAPI schema
                   )
                   ] = None): 
# Union[str, None] = None <--the Same--> Annotated[Union[str, None]] = None
# q is optional + its length doesn't exceed 50 characters.
# pattern -> regex


    results = {"items": [{"item_id": "Mehrnaz"}, {"item_id": "Mehrshad"}]}
    if q:
        results.update({"q": q})
    return results

def get_blog_item(
        item: Annotated[ 
            Union[str, None],
              Query(
                  title= "Query string",
                  description= "Query string for the items to search in the database that have a good match",
                  pattern= "^Mehr",
                  alias= "item-query" # when clients make a request to your API, they will use the alias
                                      # instead of the original parameter name -> in python we use original name "item"
                                      # e.g.) http://127.0.0.1:8000/items/?item-query=foodbaritems
                  )
                  ] = ... # ... -> something is required
                  ): 
                                                                                 # it even requires None)
    if item:
        return {'New data': item}


# if we get item Multiple Times -> e.g) http://localhost:8000/blog/?q=Mehrnaz&q=Mehrshad
def get_repeated_item_in_blog_path( 
        q: Annotated[
             Union[ list , None], Query()] = ['Me', 'You']): # Query parameter be list? -> use Query
                                                             # Otherwise -> request body
    query_item = {'new_item': q}
    return query_item




@router.get('/blog/{id}/comment')
def blog_comment(id, limit = 10):
    return{'data':{id: {'1,2,3'}, 'limit': limit}}



######################################################################################################################

#request -> data sent by the client to your API
#response -> data your API sends to the client
    
#send data -> POST (the more common), PUT, DELETE or PATCH.
    

class Blog(BaseModel):
    title: str
    body: Union[str, None] = None
    published: Optional[bool] = None


@router.post('/blog/customer')  # POST decorator -> request
def create_blog(request: Blog):
    if request.published:
        return {'data': f"the blog is created as {request.title} and the blog is published."}
    else:
        sum = request.published + request.title
        return {'data': [f"the blog is created as {request.title}.", sum]}



@router.put('/blog/customer_update/{blog_id}')  
# PUT ->  UPDATE an existing resource or create a new resource if it does not exist

async def update_item(blog_id: int, request: Blog):
    return {'data': blog_id, **request.dict(), **request.model_dump()}
#  **request.dict() -> convert a Pydantic model into a dictionary
#  The new recommended method to achieve this is -> model_dump


async def update_item_2(blog_id: int, request: Blog, q: Union[str, None] = None):
    result = {'data': blog_id, **request.model_dump()}
    if q:
        return result.update({'q': q})  # update -> add an additional key-value pair to the result dictionary
    else:
        return result




