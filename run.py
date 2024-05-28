import requests
import colorama
import gspread
from pyfiglet import figlet_format
from colorama import Fore, Back, Style

from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('geargenie')

hiking_gear = SHEET.worksheet('hiking')
hiking_data = hiking_gear.get_all_values()

# weather api key
api_key = '6a3f2cc91e7c4aa8d6506c5f08f260e4'

def introduction():
    "Introduces the user to the app and provides relevant information."

    f = figlet_format("Gear Genie\nJust for you!", font="doom")
    print(f)
    print("This app was made for outdoor enthusiasts! You will know what type of gear you need to perform certain activities weather depending. Instructions:\n"
          "1.Input location\n2.Input choice if to continue or not.\n3.Select activity to perform.\n4.Analyze gear needed for that activity. "
          "Now we are all sorted, here we go!\n" )
    
def get_weather():
    """
    Gets weather from openweathermap API depending on user's input!
    """
    while True:
        location = input(Fore.BLUE + "Please enter desired location:\n")
        print(Fore.RESET)
        
        try:
            float(location)
            print("Location should not be a number, please provide an existing location.")
            continue
        except ValueError:
            pass 

        # Proceed with API request if input is valid
        try:
            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")
            weather_data.raise_for_status() 
            error_code = weather_data.json().get('cod')

            if error_code == 200:
                print("Location is valid.")
                weather = weather_data.json()['weather'][0]['description']
                temp = weather_data.json()['main']['temp']
                feeling = weather_data.json()['main']['feels_like']
                min_temp = weather_data.json()['main']['temp_min']
                humidity = weather_data.json()['main']['humidity']
                wind = weather_data.json()['wind']['speed']

                return weather, temp, feeling, min_temp, humidity, wind
            else:
                print("Location is invalid, please provide another one.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}. Please try again.")

def display_weather_basic(weather, temp):
    """
    Displays basic weather info for user and let user choose to continue with app or terminate it.
    """
    print(f"The forecast in your area is: {weather}.\nTemperature is currently {temp} degrees celsius.\nAfter reviewing the weather data, do you wish to continue?\n1.Yes\n2.No")
    while True:
        user_agree = input(Fore.BLUE + "Please choose:\n")
        print(Fore.RESET)
        if user_agree.lower() == "yes":
            return True
        elif user_agree.lower() == "no":
            print(f"{Fore.RED}Program will be terminated.{Fore.RESET}")
            return False
        else:
            print("Please select a valid option.\n1.Yes\n2.No")

def activity_input():
    """
    Gets users location and activity
    """
    print("Location received.\nNow, please enter which type of outdoor activity in order to advise you wisely.\nYou can choose the following:\n1.Climbing\n2.Hiking\n3.Other")
    while True:
        activity = input(Fore.BLUE + "Please enter outdoor activity:\n")
        print(Fore.RESET)
        climbing = None
        column_index = None

        if activity.lower() == "climbing":
            while True:
                print("What type of climbing?\n1.Trad Climbing\n2.Sport Climbing\n3.Bouldering")
                climbing = input(Fore.BLUE + "Please choose:\n")
                print(Fore.RESET)
                if climbing.lower() == "trad climbing":
                    climbing = "trad climbing"
                    column_index = 0  # this will only give the basic gear, need to update it later. 
                    return climbing, column_index
                elif climbing.lower() == "sport climbing":
                    climbing = "sport climbing"
                    column_index = 0  # this will only give the basic gear, need to update it later.
                    return climbing, column_index
                elif climbing.lower() == "bouldering":
                    climbing = "bouldering"
                    column_index = 0  # this will only give the basic gear, need to update it later.
                    return climbing, column_index
                else:
                    print("Please select the type of climbing from the options.\n")
        elif activity.lower() == "hiking":
            activity = "hiking"
            column_index = 0  # this will only give the basic gear, need to update it later.
            return activity, column_index
        elif activity.lower() == "other":
            print("More sports will be available soon! In the meantime, you can get started with the two activities we support. 1.Climbing or 2.Hiking")
        else:
            print("Please choose one of the activities we support. 1.Climbing or 2.Hiking\n")

def fetch_gear_data(user_activity, column_index):
    """
    Fetch data from google sheets for hiking and climbing activities.
    """
    gear = SHEET.worksheet(f"{user_activity}").get_all_values()
    column_data = [row[column_index] for row in gear]

    



def final_message(user_activity, column_index, weather, temp, feeling, min_temp, humidity, wind):
    """
    Displays final message with all the necessary information for the activity to be performed according to users input.
    """
    gear_list = fetch_gear_data(user_activity, column_index)
    print(f"You chose to go {user_activity}. Here's the weather forecast: {Fore.CYAN}{weather}{Fore.RESET}\n"
          f"With a temperature of: {Fore.CYAN}{temp}°C (feels like {feeling}°C), and a minimum temperature of {min_temp}°C{Fore.RESET}\n"
          f"Humidity: {Fore.CYAN}{humidity}%, Wind: {wind} m/s{Fore.RESET}\n"
          f"Recommended gear: {', '.join(gear_list)}\n"
          f"We hope this information was helpful, see you later!\n{Fore.RED}Program will be terminated.{Fore.RESET}")

def main():
    """
    Run all the application functions
    """
    introduction()
    weather, temp, feeling, min_temp, humidity, wind = get_weather()
    if display_weather_basic(weather, temp):
        user_activity, column_index = activity_input()
        final_message(user_activity, column_index, weather, temp, feeling, min_temp, humidity, wind)

main()
