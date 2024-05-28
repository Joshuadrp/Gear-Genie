import requests
import gspread
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

def get_weather():
    """
    Gets weather from openweathermap API depending on user's input!
    """
    while True:
        location = input("Please enter desired location: ")
        
        # Check if the input is a number (integer or float)
        try:
            float(location)
            print("Location should not be a number, please provide an existing location.")
            continue
        except ValueError:
            pass  # Input is not a number, proceed with the request

        # Proceed with API request if input is valid
        try:
            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")
            weather_data.raise_for_status()  # Raise an HTTPError for bad responses
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
        user_agree = input("Please choose: ")
        if user_agree.lower() == "yes":
            return True
        elif user_agree.lower() == "no":
            print("Program will be terminated.")
            return False
        else:
            print("Please select a valid option.\n1.Yes\n2.No")

def activity_input():
    """
    Gets users location and activity
    """
    print("Location received.\nNow, please enter which type of outdoor activity in order to advise you wisely.\nYou can choose the following:\n1.Climbing\n2.Hiking.\n")
    while True:
        activity = input("Please enter outdoor activity: ")
        climbing = None
        column_index = None

        if activity.lower() == "climbing":
            while True:
                print("What type of climbing?\n1.Trad Climbing\n2.Sport Climbing\n3.Bouldering")
                climbing = input("Please choose: ")
                if climbing.lower() == "trad climbing":
                    column_index = 0  # this will only give the basic gear, need to update it later. 
                    return climbing, column_index
                elif climbing.lower() == "sport climbing":
                    column_index = 0  # this will only give the basic gear, need to update it later.
                    return climbing, column_index
                elif climbing.lower() == "bouldering":
                    column_index = 0  # this will only give the basic gear, need to update it later.
                    return climbing, column_index
                else:
                    print("Please select the type of climbing from the options.\n")
        elif activity.lower() == "hiking":
            column_index = 0  # this will only give the basic gear, need to update it later.
            return activity, column_index
        else:
            print("Please choose one of the activities above.\n")

def fetch_gear_data(user_activity, column_index):
    """
    Fetch data from google sheets for hiking and climbing activities.
    """
    gear = SHEET.worksheet(f"{user_activity}").get_all_values()
    column_data = [row[column_index] for row in gear]
    return column_data

def final_message(user_activity, column_index, weather, temp, feeling, min_temp, humidity, wind):
    """
    Displays final message with all the necessary information for the activity to be performed according to users input.
    """
    gear_list = fetch_gear_data(user_activity, column_index)
    print(f"You chose to go {user_activity}. Here's the weather forecast: {weather}\n"
          f"With a temperature of: {temp}°C (feels like {feeling}°C), and a minimum temperature of {min_temp}°C\n"
          f"Humidity: {humidity}%, Wind: {wind} m/s\n"
          f"Recommended gear: {', '.join(gear_list)}")

def main():
    """
    Run all the application functions
    """
    weather, temp, feeling, min_temp, humidity, wind = get_weather()
    if display_weather_basic(weather, temp):
        user_activity, column_index = activity_input()
        final_message(user_activity, column_index, weather, temp, feeling, min_temp, humidity, wind)

main()
