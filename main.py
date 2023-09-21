ENV = "prod" # dev or prod

import requests
import json
from pydantic import BaseModel
from typing import Optional


URL = 'http://localhost:8080' if ENV=='dev' else 'https://tether-s2ng.onrender.com'


# pydantic model for signal data
class SignalData(BaseModel):
    lat: float
    lng: float
    tower_distance: float
    altitude: float
    image: Optional[bytes] = None
    detection_data: Optional[str] = None
    signal_strength: float
    

# pydantic model for drone command
class DronePosition(BaseModel):
    lat: float
    lng: float


def get_plan():
    # make a get request to URL/drone-control/plan to get the plan
    r = requests.get(f'{URL}/drone-control/plan')
    # Parse json response
    plan = json.loads(r.text)
    return plan

def send_signal_data(signal_data: SignalData):
    # make a post request to URL/drone-control/signal-data to send the signal data
    r = requests.post(f'{URL}/signal-data', json=signal_data.model_dump())
    # Parse json response
    response = json.loads(r.text)
    return response

def send_drone_position(position: DronePosition):
    # make a post request to URL/drone-control/position to send the drone position
    r = requests.post(f'{URL}/drone-control/position', json=position.model_dump())
    # Parse json response
    response = json.loads(r.text)
    return response

# Example usage
pos = DronePosition(lat=23.7489144, lng= 90.3703079)
signal_data = SignalData(lat=100, lng=120, tower_distance=30, altitude=50, signal_strength=100)
# send_signal_data(signal_data)
# send_drone_position(pos)
print(get_plan())


