from fastapi import FastAPI
from routers import blog, models
#import uvicorn

app = FastAPI()  #instance


app.include_router(blog.router,
                   tags=["Blog"])
app.include_router(models.router, 
                   tags= ["Models"])




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




# To run on different addres -> used for Debugging
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port = 9000)
