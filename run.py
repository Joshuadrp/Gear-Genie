import requests

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

def activity_input():
    """
    Gets users location and acivity
    """
    print("Location received.\nNow, please enter which type of outdoor activity in order to advise you wisely.\nYou can choose the following:\n1.Climbing\n2.Hiking.\n")
    while True:
        
        activity = input("Please enter outdoor activity: ")
        climbing = None

        if activity == "1":
            while True:
                print("What type of climbing?\n1.Trad\n2.Sport\n3.Boulder")
                climbing = input("Please choose: ")
                if climbing == "1":
                    print("You need trad gear.\n")
                    return activity, climbing
                elif climbing == "2":
                    print("You need sport gear.\n")
                    return activity, climbing
                elif climbing == "3":
                    print("You need boulder gear.\n")
                    return activity, climbing
                else:
                    print("Please select the type of climbing from the options.\n")
            
        elif activity == "2":
            print("You need hiking gear.\n")
            return activity, climbing
        else: 
            print("Please choose one of the activities above.\n")

def display_weather_basic(weather, temp):
    """
    Displays basic weather info for user and let user choose to continue with app or terminate it.
    """
    print(f"Weather is currently {weather}, with temperature of {temp}.\nAfter reviewing the weather data, do you wish to continue?\n1.Yes\n2.No")
    while True:
        user_agree = input("Please choose: ")
        if(user_agree == "1"):
            activity_input()
            return 
        elif(user_agree == "2"):
            print("Program will be terminated.")
            return
        else:
            print("Please select a valid option.")

    
def main():
    """
    Run all the application functions
    """
    weather, temp = get_weather()
    display_weather_basic(weather, temp)
    
    # print(weather)
    # print(temp)
    # print(location)
    # print(activity)
    # print(climbing)

main()