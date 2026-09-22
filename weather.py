import requests
import pandas as pd


def fetch_weather_data(latitude, longitude):
    url="https://api.open-meteo.com/v1/forecast"
    #Parameters Used in the API Request
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "wind_speed_unit": "mph",
        "timezone": "GMT",
        "current": ["temperature_2m", "apparent_temperature", "precipitation", "cloud_cover", "wind_speed_10m", "wind_direction_10m", "soil_temperature_0cm"],
        "forecast_days":1,
        "hourly": ["temperature_2m", "cloud_cover", "wind_speed_10m", "precipitation"]
    }
    response=None
    try:
        #Basic HTTP GET Request
        response=requests.get(url, params=params)

    except requests.exceptions.RequestException as e:
        print(f"An Error Occurred when trying to fetch the weather data of your selected location: {e}")
        return None, None
    
    if response.status_code != 200:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None, None
    #Using .head() for testing with a small amount of data
    # print(pd.DataFrame(response.json()).head())
    current_weather= pd.DataFrame([response.json()["current"]])
    hourly_weather = pd.DataFrame(response.json()["hourly"])    
    
    return current_weather, hourly_weather


if __name__ == "__main__":
    # Example usage
    current_weather, hourly_weather = fetch_weather_data(51.5074, -0.1278)  # Example coordinates for London
    print(current_weather)
    print(hourly_weather.head())