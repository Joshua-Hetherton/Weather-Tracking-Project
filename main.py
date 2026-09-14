import questionary
from geopy import Nominatim
import pandas as pd
import weather
 

#Initialises Geolocator to be used for automatic City finding
geolocator=Nominatim(user_agent="Weather_Project_app")
terminate_program=False
city_selected=pd.DataFrame()

def main_menu():
    """
    Displays the main menu and prompts the user to select an option.
    """
    main_menu_selection = questionary.select("What would you like to do?",
                                             choices=["Select from a preset city", "Enter a City", "Enter Latitude and Longitude", "Exit"]).ask()

    
    
    match(main_menu_selection):
        case "Exit":
            global terminate_program
            terminate_program=True
        
        case "Select from a preset city":
            city_selected=select_preset_city()

        case "Enter a City":
            city_selected=enter_city_name()

        case "Enter Latitude and Longitude":
            city_selected=enter_latitude_and_longitude()


    current_city_weather, hourly_city_weather=weather.fetch_weather_data(city_selected["latitude"], city_selected["longitude"])
    print(f"""Current Weather in {city_selected['city']}:
    {current_city_weather}
    -----------------
    Hourly Weather:
    {hourly_city_weather}

    """)
            

def select_preset_city():
    """
    Displays a list of preset cities for the user to select from.
    """
    City_Selection = questionary.select("Select a city from the list below:",
                                        choices=["Southampton", "Winchester", "London", "New York"]).ask()
    print(f"You selected: {City_Selection}")

    return get_city_coordinates(City_Selection)

def enter_city_name():
    """
    Prompts the user to enter a city name.
    """
    Entered_City= questionary.text("Please enter the name of the city:").ask()
    print(f"You entered: {Entered_City}")
    print(get_city_coordinates(Entered_City))

    return get_city_coordinates(Entered_City)
    

def enter_latitude_and_longitude():
    """
    Prompts the user to enter latitude and longitude coordinates.
    """
    latitude = questionary.text("Please enter the latitude:").ask()
    longitude = questionary.text("Please enter the longitude:").ask()
    city=find_city_from_coordinates(latitude, longitude)
    print(f"The nearest city to the coordinates ({latitude}, {longitude}) is: {city}")

    return {
        "city": city,
        "latitude": latitude,
        "longitude": longitude
    }

def find_city_from_coordinates(latitude, longitude):
    """
    Finds the nearest city to the coordinates provided by the user.
    """
    #Uses the opposite function of geocode to find the city from the given coordinates
    location= geolocator.reverse((latitude, longitude))
    if location:
        return location.address
    else:
        return "City not found, Please Try Again"

def get_city_coordinates(city_name):
    """
    Gets the coordinates of a city.
    """

    location=geolocator.geocode(city_name)
    if location:
        return {
            "city": city_name,
            "latitude": location.latitude,
            "longitude": location.longitude
        }
    else:
        print("City not found, Please Try Again")
        return None


while not terminate_program:
    main_menu()