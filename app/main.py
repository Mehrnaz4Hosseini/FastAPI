from fastapi import FastAPI
import uvicorn
from enum import Enum
from routers import blog

app = FastAPI()  #instance


app.include_router(blog.router,
                   prefix='/blog',
                   tags=["Blog"])


@app.get("/")   #HTTP "methods" -> POST  GET  PUT  DELETE                                                   
                #Decorator  
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


# To run on different addres -> used for Debugging
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 9000)
