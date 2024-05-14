import requests

api_key = '6a3f2cc91e7c4aa8d6506c5f08f260e4'


def location_and_activity():
    """
    Gets users location and acivity
    """
    location = input("Please enter location: ")
    print("Location received.\nNow, please enter which type of outdoor activity in order to advise you wisely.\nYou can choose the following: Climbing or Hiking.\n")
    while True:
        
        activity = input("Please enter outdoor activity: ")
        climbing = None

        if activity.lower() == "climbing":
            while True:
                print("What type of climbing? Trad, Sport, or Boulder?\n")
                climbing = input("Please choose: ")
                if climbing.lower() == "trad":
                    print("You need trad gear.\n")
                    return location, activity, climbing
                elif climbing.lower() == "sport":
                    print("You need sport gear.\n")
                    return location, activity, climbing
                elif climbing.lower() == "boulder":
                    print("You need boulder gear.\n")
                    return location, activity, climbing
                else:
                    print("Please select the type of climbing from the options.\n")
            
        elif activity.lower() == "hiking":
            print("You need hiking gear\n")
            return location, activity, climbing
        else: 
            print("Please choose one of the activities above.\n")
    

# user_location = input('Enter city or location:\n')
# activity = input()

# weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=metric&APPID={api_key}")

# weather = weather_data.json()['weather'][0]['main']
# temp = weather_data.json()['main']['temp']

# # print(weather_data.json())



def main():
    """
    Run all the application functions
    """
    location, activity, climbing = location_and_activity()
    print(location)
    print(activity)
    print(climbing)

main()