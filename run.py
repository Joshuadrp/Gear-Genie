import requests

api_key = '6a3f2cc91e7c4aa8d6506c5f08f260e4'

def get_weather(location):
    """
    Gets weather depending on previous users input!
    """
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    error_code = weather_data.json()['cod']

    # print(weather, temp)
    print(error_code)
    # print(weather_data.json())

    return weather, temp, error_code

def location_input():
    """
    Asks for users desired location and displays weather data.
    """
    location = input("Please enter desired location: ")
    print("""Location received.\nNow, please enter which type of outdoor activity in order to advise you wisely.\nYou can choose the following:\n1.Climbing\n2.Hiking.\n""")
    return location

def activity_input():
    """
    Gets users location and acivity
    """
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
    
def main():
    """
    Run all the application functions
    """
    location = location_input()
    activity, climbing = activity_input()
    weather, temp, error_code = get_weather(location)

    # print(weather)
    # print(temp)
    # print(location)
    # print(activity)
    # print(climbing)

main()