from typing import Optional, Union
from fastapi import APIRouter, Query
from typing_extensions import Annotated

router = APIRouter()  # -> you can think of APIRouter as a "mini FastAPI" class.


@router.get('/blog/unpublished')
def get_unpublished():
    return {'data': 'all unpublished data'}


@router.get('/blog/{id}')   # usage -> creating routing
def get_id(id: int):
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
def my_query(limit = 10, published : bool = False, sort: Union[str, None] = None): # -> sort is not required because of 
                                                                                   # the default value = None.
# " = None " -> tells FastAPI that this parameter is not required, NOT the " Union[str, None] "
    if published:
        return {'data': {'limit': f'Hey you got {limit} published blogs from database.', 'published': published}}
    else:
        return {'data':{'limit': "Sorry, you just got a few blogs", 'published': published}}
    
    
async def read_item(q: Annotated[ Union[str, None] , Query(min_length=2, max_length=50, pattern="^Mehrnaz$")] = None): 
# Union[str, None] = None <--the Same--> Annotated[Union[str, None]] = None
# q is optional + its length doesn't exceed 50 characters.
# pattern -> regex


    results = {"items": [{"item_id": "Mehrnaz"}, {"item_id": "Mehrshad"}]}
    if q:
        results.update({"q": q})
    return results



@router.get('/blog/{id}/comment')
def comment(id, limit = 10):
    return{'data':{id: {'1,2,3'}, 'limit': limit}}
