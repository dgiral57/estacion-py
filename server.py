from multiprocessing.sharedctypes import Value
import uvicorn
from typing import Union
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

from settings import Settings

app = FastAPI()
settings = Settings()

valuesBuffer =[]

class Values(BaseModel):
    temperature:float
    humidity:float
    pressure:float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/values")
def serverValues(values:Values):
    response={"temperature":values.temperature,"humidity":values.humidity,"pressure":values.pressure,"time":datetime.utcnow()}
    valuesBuffer.append(response)
    return response

@app.get("/values")
def get_values():
    return valuesBuffer.pop(0) if len(valuesBuffer) > 0 else []

if __name__=="__main__":
    uvicorn.run(
        app,host="0.0.0.0",port=8080,loop="asyncio",workers=1,log_level="debug"
    )