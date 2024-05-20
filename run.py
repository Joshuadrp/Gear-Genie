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
    Gets weather depending on users input! 
    """
    while True:
        location = input("Please enter desired location: ")
        weather = None
        temp = None
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")
        error_code = weather_data.json()['cod']
    
        if error_code == 200:
            print("Location is valid.")
            weather = weather_data.json()['weather'][0]['main']
            temp = weather_data.json()['main']['temp']
            return weather, temp
        else:
            print("Location is invalid, please provide another one.")

        # print(weather, temp)
        # print(error_code)
        # print(weather_data.json())

def display_weather_basic(weather, temp):
    """
    Displays basic weather info for user and let user choose to continue with app or terminate it.
    """
    print(f"Weather is currently {weather}, with temperature of {temp}.\nAfter reviewing the weather data, do you wish to continue?\n1.Yes\n2.No")
    while True:
        user_agree = input("Please choose: ")
        if(user_agree.lower() == "yes"):
            activity_input()
            return 
        elif(user_agree.lower() == "no"):
            print("Program will be terminated.")
            return
        else:
            print("Please select a valid option.")


def activity_input():
    """
    Gets users location and acivity
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
                    print("You need trad gear.\n")
                    column_index = 0 #this will only give the basic gear, need to update it later. 
                    fetch_gear_data(climbing, column_index)
                    return
                elif climbing.lower() == "sport climbing":
                    print("You need sport gear.\n")
                    column_index = 0 #this will only give the basic gear, need to update it later.
                    fetch_gear_data(climbing, column_index)
                    return 
                    
                elif climbing.lower() == "bouldering":
                    print("You need boulder gear.\n")
                    column_index = 0 #this will only give the basic gear, need to update it later.
                    fetch_gear_data(climbing, column_index)
                    return 
                else:
                    print("Please select the type of climbing from the options.\n")
            
        elif activity.lower() == "hiking":
            print("You need hiking gear.\n")
            column_index = 0 #this will only give the basic gear, need to update it later.
            fetch_gear_data(activity, column_index)
            return
        else: 
            print("Please choose one of the activities above.\n")

    

def fetch_gear_data(user_activity, column_index):
    """
    Fetch data for hiking and climbing activities.
    """
    gear = SHEET.worksheet(f"{user_activity}").get_all_values()
    column_data = [row[column_index] for row in gear]
    print(column_data)
    return 

def main():
    """
    Run all the application functions
    """
    weather, temp = get_weather()
    display_weather_basic(weather, temp)

    # column_index, user_activity = activity_input()
    # fetched_gear = fetch_gear_data(user_activity, column_index)

    # print(fetched_gear)
    
    # print(weather)
    # print(temp)
    # print(location)
    # print(activity)
    # print(climbing)

main()