from fastapi import APIRouter
from enum import Enum

router = APIRouter()


@router.get("/models")
async def get_models():
    return {'data': {'This is the first model.'}}


class Model_name(str, Enum):
    Mehrnaz = "Mehrnaz"
    Mehrshad = "Mehrshad"

@router.get('/models/{model_name}')
def get_model_name(model_name: Model_name):
    if model_name is model_name.Mehrnaz:
        return {'model_name': {f'Hey, the model name is {model_name}.'}}
    elif model_name.value == "Mehrshad":
        return {'model_name': {f"Hi, the model name is the same as Mehrnaz brother's name, {model_name}"}}
    else:
        return {'model_name': {"Well, the model has some"}}