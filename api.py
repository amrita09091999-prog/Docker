from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class RequestName(BaseModel):
    name : str

@app.get('/')
def intro():
    return {'message':'This is a simple app'}

@app.post('/display')
def display_name(payload: RequestName):
    return {'message':f"Hi {payload.name} - this app is up and running!"}