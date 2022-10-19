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
def root():
    return {"message": "Hello World"}

@app.post("/values")
def serverValues(values:Values):
    conn = sqlite3.connect('datos.db', check_same_thread=False)
    c = conn.cursor()
    try: 
        c.execute("CREATE TABLE IF NOT EXISTS datos (id INTEGER PRIMARY KEY AUTOINCREMENT, Temperature real, humidity real, pressure real, date text)")
    except:
        pass
    
    now = datetime.utcnow()
    response={"temperature":values.temperature,"humidity":values.humidity,"pressure":values.pressure,"time":now}
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    c.execute('''INSERT INTO datos (Temperature, humidity, pressure, date)
                        VALUES (?, ?, ?, ?)''', (values.temperature, values.humidity, values.pressure, date_time))
    res = c.execute("SELECT * FROM datos ORDER BY id DESC LIMIT :size",{"size":1})
    print(res.fetchall())
    conn.commit()
    conn.close()

    return response

@app.get("/values/")
def get_values(size: int = 10):
    conn = sqlite3.connect('datos.db', check_same_thread=False)
    c = conn.cursor()
    res = c.execute("SELECT * FROM datos ORDER BY id DESC LIMIT :size",{"size": size})
    tupla = res.fetchall()
    conn.close()
    response = []
    for x in range(size):
        data = tupla.pop()
        response.append({"temperature": data[1], "humidity": data[2], "pressure": data[3], "time": data[4]})
    return response

if __name__=="__main__":
    uvicorn.run(
        app,host="0.0.0.0",port=8080,loop="asyncio",workers=1,log_level="debug"
    )


