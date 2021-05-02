from fastapi import FastAPI
#from pydantic import BaseModel
from typing import List
from typing import Optional
import requests


app = FastAPI()

def get_clothes(temp: float):
    if temp > 12:
        clothes = "tshirt"
    elif temp <= 5:
        clothes = "coat"
    elif temp <= 12:
        clothes = "sweater"
    else:
        clothes = "no clothes detectable"
    return clothes

def get_risk(uvi: float):
    if uvi <= 2:
        risk = "low"
    elif uvi <= 5:
        risk = "moderate"
    elif uvi > 5:
        risk = "high"
    else:
        risk = "no value for risk"
    return risk

def get_umbrella(pop: float):
    if pop < 0.1:
        umbrella = "no"
    else:
        umbrella = "yes" 
    return umbrella

@app.post("/")
async def get_lat_lon(latitude: float, longitude: float):
    global lat
    lat = latitude
    global lon
    lon = longitude
    return lat, lon

global response 
global temp
temp = 0.0
global uvi
uvi = 0.0
global pop
pop = 0.0

@app.get("/")
async def out_put():
    api_url = 'https://api.openweathermap.org/data/2.5/onecall?lat='+str(lat)+'&lon='+str(lon)+'&exclude=current,minutely,daily,alerts&appid=ae1644bb20ae46fe9b7cdb772c1dab25&units=metric'
    response = requests.get(api_url)
    response = response.json()

    uvi = response['hourly'][1]['uvi']
    pop = response['hourly'][1]['pop']
    temp = response['hourly'][1]['temp']

    '''get_clothes(temp)
    get_risk(uvi)
    get_umbrella(pop)'''

    if temp > 12:
        clothes = "tshirt"
    elif temp <= 5:
        clothes = "coat"
    elif temp <= 12:
        clothes = "sweater"
    else:
        clothes = "no clothes detectable"
    
    if uvi <= 2:
        risk = "low"
    elif uvi <= 5:
        risk = "moderate"
    elif uvi > 5:
        risk = "high"
    else:
        risk = "no value for risk"

    if pop < 0.1:
        umbrella = "no"
    elif pop >= 0.1:
        umbrella = "yes"
    else:
        umbrella = "i don't know" 

    return {'clothes': clothes, 'risk': risk, 'umbrella': umbrella}
