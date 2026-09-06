import questionary
from geopy import Nominatim

#Initialises Geolocator to be used for automatic City finding
geolocator=Nominatim(user_agent="Weather_Project_app")
terminate_program=False


def main_menu():
    """
    Displays the main menu and prompts the user to select an option.
    """
    main_menu_selection = questionary.select("What would you like to do?",
                                             choices=["Select from a preset City", "Enter a City", "Enter Latitude and Longitude", "Exit"]).ask()
    match(main_menu_selection):
        case "Exit":
            global terminate_program
            terminate_program=True
        
        case "Select from a Preset City":
            Select_Preset_City()

        case "Enter a City":
            Enter_City_Name()

        case "Enter Latitude and Longitude":
            Enter_Latitude_and_Longitude()
            

def Select_Preset_City():
    """
    Displays a list of preset cities for the user to select from.
    """
    City_Selection = questionary.select("Select a city from the list below:",
                                        choices=["Southampton", "London", "New York", "Winchester"]).ask()
    print(f"You selected: {City_Selection}")

def Enter_City_Name():
    """
    Prompts the user to enter a city name.
    """
    Entered_City= questionary.text("Please enter the name of the city:").ask()
    print(f"You entered: {Entered_City}")
    print(Get_City_Coordinates(Entered_City))
    return 

def Enter_Latitude_and_Longitude():
    """
    Prompts the user to enter latitude and longitude coordinates.
    """
    latitude = questionary.text("Please enter the latitude:").ask()
    longitude = questionary.text("Please enter the longitude:").ask()
    print(f"You entered: {latitude}, {longitude}")
    return latitude, longitude

def Get_City_Coordinates(city_name):
    """
    """

    location=geolocator.geocode(city_name)
    if location:
        return {
            "latitude": location.latitude,
            "longitude": location.longitude
        }
    else:
        print("City not found, Please Try Again")





while not terminate_program:
    main_menu()