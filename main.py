import questionary
from geopy import Nominatim
import pandas as pd
import weather
import display
 

#Initialises Geolocator to be used for automatic City finding
geolocator=Nominatim(user_agent="Weather_Project_app")
terminate_program=False


def main_menu():
    """Displays the main menu and prompts the user to select an option.
    Options include selecting a preset city, entering a city name, entering latitude and longitude, or exiting the program.


    Returns:
        None: This function does not return any value. It displays the main menu and handles user input.

    """
    main_menu_selection = questionary.select("What would you like to do?",
                                             choices=["Select from a preset city", "Enter a City", "Enter Latitude and Longitude", "Exit"]).ask()

    
    
    match(main_menu_selection):
        case "Exit":
            global terminate_program
            terminate_program=True
            return
        
        case "Select from a preset city":
            city_selected=select_preset_city()

        case "Enter a City":
            city_selected=enter_city_name()

        case "Enter Latitude and Longitude":
            city_selected=enter_latitude_and_longitude()


    current_city_weather, hourly_city_weather=weather.fetch_weather_data(city_selected["latitude"], city_selected["longitude"])

    display.display_header(city_selected["city"])
    display.display_current_weather(current_city_weather)
    display.display_hourly_weather(hourly_city_weather)

    display.display_graphs(hourly_city_weather)
            

def select_preset_city():
    """Displays a list of preset cities for the user to select from.

    Returns:
        dict: A dictionary containing the selected city's name, latitude, and longitude.
    """

    city_selection = questionary.select("Select a city from the list below:",
                                        choices=["Southampton", "Winchester", "London", "New York"]).ask()

    return get_city_coordinates(city_selection)

def enter_city_name():
    """Prompts the user to enter a city name.

    Returns:
        dict: A dictionary containing the entered city's name, latitude, and longitude.
    """
    Entered_City= questionary.text("Please enter the name of the city:").ask()

    return get_city_coordinates(Entered_City)
    

def enter_latitude_and_longitude():
    """Prompts the user to enter latitude and longitude coordinates.

    Returns:
        dict: A dictionary containing the entered coordinates and the nearest city.
    """
    latitude = float(questionary.text("Please enter the latitude:").ask())
    longitude = float(questionary.text("Please enter the longitude:").ask())
    city=find_city_from_coordinates(latitude, longitude)
    print(f"The nearest city to the coordinates ({latitude}, {longitude}) is: {city}")

    return {
        "city": city,
        "latitude": latitude,
        "longitude": longitude
    }

def find_city_from_coordinates(latitude, longitude):
    """Finds the nearest city to the coordinates provided by the user.
    Args:
        latitude (float): The latitude coordinate.
        longitude (float): The longitude coordinate.

    Returns:
        str: The name of the nearest city.
    """
    #Uses the opposite function of geocode to find the city from the given coordinates
    location= geolocator.reverse((latitude, longitude))
    if location:
        return location.address
    else:
        return "City not found, Please Try Again"

def get_city_coordinates(city_name):
    """Gets the coordinates of a city.
    Args:
        city_name (str): The name of the city for which to get the coordinates.
        
    Returns:
        dict: A dictionary containing the city's name, latitude, and longitude.
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