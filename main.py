from typing import Union
from fastapi import FastAPI

app = FastAPI()   # instance


@app.get("/")
def read_root():
    return {"Hello": "World"}
