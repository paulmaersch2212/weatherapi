from pydantic import BaseModel

class Weather(BaseModel):

    clothes: str
    risk: str
    umbrella: str