import requests
import pandas as pd

url="https://api.open-meteo.com/v1/forecast"
#Parameters Used in the API Request
params = {
    "latitude": 50.909698,
    "longitude": -1.404351,
    "timezone": "GMT",
    "current": ["temperature_2m", "apparent_temperature", "precipitation", "cloud_cover", "wind_speed_10m", "wind_direction_10m", "soil_temperature_0cm"],
    "forecast_hours":1,
    "hourly": ["temperature_2m"]
}


#Basic HTTP GET Request
response=requests.get(url, params=params)

#200 means working, otherwise it is not working
print(response.status_code)

#Using .head() for testing with a small amount of data
pd.DataFrame(response.json()).head()
print(response.json())

