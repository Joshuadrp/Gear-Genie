import requests
import gspread
from pyfiglet import figlet_format
from colorama import Fore, Style
from tabulate import tabulate
from google.oauth2.service_account import Credentials

# Google Sheets setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('geargenie')

# Weather API key
API_KEY = '6a3f2cc91e7c4aa8d6506c5f08f260e4'


def introduction():
    """
    Introduces the user to the app and provides relevant information.
    """
    print(figlet_format("Gear Genie\nJust for you!", font="doom"))
    print(
        "This app was made for outdoor enthusiasts! You will know what type "
        "of gear you need to perform certain activities weather depending. "
        "Instructions:\n1. Input location\n2. Input choice if to continue "
        "or not.\n3. Select activity to perform.\n4. Analyze gear needed for "
        "that activity. Now we are all sorted, here we go!\n"
    )


def get_weather():
    """
    Gets weather from OpenWeatherMap API based on user's input.
    """
    while True:
        print(Fore.BLUE)
        location = input("Please enter desired location:\n")
        print(Fore.RESET)

        if location.isdigit():
            print(
                "Location should not be a number, please provide an existing "
                "location."
            )
            continue

        try:
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={location}"
                f"&units=metric&APPID={API_KEY}"
            )
            weather_data.raise_for_status()
            weather_json = weather_data.json()

            if weather_json.get('cod') == 200:
                print("Location is valid.")
                weather = weather_json['weather'][0]['description']
                temp = weather_json['main']['temp']
                feeling = weather_json['main']['feels_like']
                min_temp = weather_json['main']['temp_min']
                humidity = weather_json['main']['humidity']
                wind = weather_json['wind']['speed']
                return weather, temp, feeling, min_temp, humidity, wind
            else:
                print("Location is invalid, please provide another one.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}. Please try again.")


def display_weather_basic(weather, temp):
    """
    Displays basic weather info and lets the user choose to continue or
    terminate the app.
    """
    print(
        f"The forecast in your area is: {Fore.BLUE}{weather}{Fore.RESET}.\n"
        f"Temperature is currently {Fore.BLUE}{temp} degrees Celsius."
        f"{Fore.RESET}\n"
        "After reviewing the weather, do you wish to continue?\n1.Yes\n2.No"
    )
    while True:
        user_agree = input(Fore.BLUE + "Please choose:\n" + Fore.RESET).lower()
        if user_agree == "yes" or user_agree == "1":
            return True
        elif user_agree == "no" or user_agree == "2":
            print(Fore.RED + "Program will be terminated." + Fore.RESET)
            return False
        else:
            print("Please select a valid option.\n1. Yes\n2. No")


def activity_input():
    """
    Gets the user's chosen activity.
    """
    print(
        "Location received.\nNow, please enter which type of outdoor activity "
        "in order to advise you wisely.\nYou can choose the following:\n"
        "1. Climbing\n2. Hiking\n3. Other"
    )
    while True:
        print(Fore.BLUE)
        activity = input("Please enter outdoor activity:\n").lower()
        print(Fore.RESET)
        if activity == "climbing" or activity == "1":
            return climbing_type_input()
        elif activity == "hiking" or activity == "2":
            return "hiking", 0
        elif activity == "other" or activity == "3":
            print(
                "More sports will be available soon! In the meantime, you can "
                "get started with the two activities we support. 1. Climbing "
                "or 2. Hiking"
            )
        else:
            print(
                "Please choose one of the activities we support. 1.Climbing "
                ", 2.Hiking or 3.Other\n"
            )


def climbing_type_input():
    """
    Gets the type of climbing activity from the user.
    """
    while True:
        print(
            "What type of climbing?\n1. Trad Climbing\n2. Sport Climbing\n3. "
            "Bouldering"
        )
        climbing = input(Fore.BLUE + "Please choose:\n" + Fore.RESET).lower()
        if climbing == "trad climbing" or climbing == "1":
            return "trad climbing", 0
        elif climbing == "sport climbing" or climbing == "2":
            return "sport climbing", 0
        elif climbing == "bouldering" or climbing == "3":
            return "bouldering", 0
        else:
            print("Please select the type of climbing from the options.\n")


def fetch_gear_data(user_activity, col_index):
    """
    Fetches data from Google Sheets for hiking and climbing activities.
    """
    gear = SHEET.worksheet(user_activity).get_all_values()
    column_data = [row[col_index] for row in gear[1:]]

    # Creating a table with an index column
    table = [(index + 1, value) for index, value in enumerate(column_data)]
    return tabulate(table, headers=["", user_activity], tablefmt="grid")


def final_message(
    user_activity, col_index, weather, temp, feeling, min_temp, humidity, wind
):
    """
    Displays final message with all the necessary information for the chosen
    activity.
    """
    gear_list = fetch_gear_data(user_activity, col_index)
    print(
        f"You chose to go {user_activity}.\nHere's the weather forecast: "
        f"{Fore.CYAN}{weather}{Fore.RESET}\n"
        f"With a temperature of:{Fore.CYAN}{temp}°C (feels like {feeling}°C), "
        f"and a minimum temperature of "
        f"{min_temp}°C{Fore.RESET}\n"
        f"Humidity: {Fore.CYAN}{humidity}%, Wind: {wind} m/s{Fore.RESET}\n"
        f"Recommended gear:\n {gear_list}\n"
        f"We hope this information was helpful, see you later!\n"
    )
    while True:
        print(Fore.BLUE)
        terminate = input(
            "Do you want to terminate program? Select 1.Yes or 2.No\n"
        )
        print(Fore.RESET)
        if terminate.lower() == "yes" or terminate == "1":
            print(f"{Fore.RED}Program will be terminated.{Fore.RESET}")
            return True
        elif terminate.lower() == "no" or terminate == "2":
            print(f"{Fore.RED}Program will restart!!{Fore.RESET}")
            return False
        else:
            print("Please select a valid option. 1.Yes or 2.No")


def main():
    """
    Runs all the application functions.
    """
    introduction()
    while True:
        weather, temp, feeling, min_temp, humidity, wind = get_weather()
        if display_weather_basic(weather, temp):
            user_activity, col_index = activity_input()
            if final_message(
                user_activity, col_index, weather, temp, feeling, min_temp,
                humidity, wind
            ):
                break
        else:
            break


main()
