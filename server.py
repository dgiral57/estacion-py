import uvicorn
import sqlite3
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
    conn = sqlite3.connect('datos.db', check_same_thread=False)
    c = conn.cursor()
    try: 
        c.execute("CREATE TABLE IF NOT EXISTS datos (Temperature real, humidity real, pressure real, date text)")
    except:
        pass
    response={"temperature":values.temperature,"humidity":values.humidity,"pressure":values.pressure,"time":datetime.utcnow()}
    now = datetime.utcnow()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    c.execute('''INSERT INTO datos (Temperature, humidity, pressure, date)
                        VALUES (?, ?, ?, ?)''', (values.temperature, values.humidity, values.pressure, date_time))
    c.execute("SELECT * FROM datos")
    print(c.fetchall())
    valuesBuffer.append(response)
    conn.commit();
    conn.close();
    return response

@app.get("/values")
def get_values():
    return valuesBuffer.pop(0) if len(valuesBuffer) > 0 else []

if __name__=="__main__":
    uvicorn.run(
        app,host="0.0.0.0",port=8080,loop="asyncio",workers=1,log_level="debug"
    )


