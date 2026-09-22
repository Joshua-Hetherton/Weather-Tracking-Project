import questionary
from geopy import Nominatim
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

    
    city_selected=None
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

    if city_selected is None:
        print("No valid city selected. Returning to main menu.")
        return


    current_city_weather, hourly_city_weather=weather.fetch_weather_data(city_selected["latitude"], city_selected["longitude"])

    if current_city_weather is None or hourly_city_weather is None:
        print("Failed to fetch weather data. Returning to main menu.")
        return

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
    selected=get_city_coordinates(city_selection)
    if selected is None:
        return select_preset_city()

    return selected

def enter_city_name():
    """Prompts the user to enter a city name.

    Returns:
        dict: A dictionary containing the entered city's name, latitude, and longitude.
    """
    entered_city= questionary.text("Please enter the name of the city:").ask()
    selected=get_city_coordinates(entered_city)
    if selected is None:
            return enter_city_name()
    return selected
    

def enter_latitude_and_longitude():
    """Prompts the user to enter latitude and longitude coordinates.

    Returns:
        dict: A dictionary containing the entered coordinates and the nearest city.
    """
    try:
        latitude = float(questionary.text("Please enter the latitude:").ask())
        longitude = float(questionary.text("Please enter the longitude:").ask())
    except ValueError:
        print("Invalid input. Please enter numeric values for latitude and longitude.")
        return enter_latitude_and_longitude()

    #Latitude and Longitude have set limits, which causes a crash if exceeded
    if latitude < -90 or latitude > 90:
        print("Invalid latitude. Please enter a value between -90 and 90.")
        return enter_latitude_and_longitude()
    
    elif longitude < -180 or longitude > 180:
        print("Invalid longitude. Please enter a value between -180 and 180.")
        return enter_latitude_and_longitude()
    
    else:
        city=find_city_from_coordinates(latitude, longitude)
        if city is None:
            return enter_latitude_and_longitude()
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
    try:
        location= geolocator.reverse((latitude, longitude))
    except Exception as e:
        print(f"An Error Occurred when fetching the data from geopy: {e}")
        print("Taking you back to main menu")
        return None
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
    #Using the early return pattern with try catch to avoid any unwanted errors
    location=None
    try:
        location=geolocator.geocode(city_name)
    except Exception as e:
        print(f"An Error Occurred when fetching the data from geopy: {e}")
        print("Taking you back to main menu")
        return None
    
    #If Geocode works, but returns None, something has gone wrong with the query, 
    # as Geocode returns None if the city isnt found or if something else has gone wrong in the query
    if location is None:
        print("City not found, Please Try Again")
        return None

    #Everything is working as expected, so it returns the city name etc.
    return {
        "city": city_name,
        "latitude": location.latitude,
        "longitude": location.longitude
    }


while not terminate_program:
    main_menu()