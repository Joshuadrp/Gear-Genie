import requests

api_key = '6a3f2cc91e7c4aa8d6506c5f08f260e4'


def location_and_activity():
    location = input("Please enter location:\n")
    print("Location received. Now, please enter which type of outdoor activity in order to adivse you wisely.\nYou can choose the following: Climbing, Hiking")
    activity = input("Please enter outdoor activity:")
    climbing = None

    if (activity == "Climbing" or activity == "climbing"):
        print("What type of climbing? Trad, Sport or boulder?")
        climbing = input("Please choose:")
        if(climbing == "Trad" or climbing == "trad"):
            print("You need trad gear.")
        elif(climbing == "sport" or climbing == "sport"):
             print("You need sport gear.")
        elif(climbing == "boulder" or climbing == "Boulder"):
             print("You need boulder gear.")
        else:
            print("Please select the type of climbing from the options.")
    
    elif(activity == "Hiking" or activity == "hiking"):
        print("You need hiking gear")
        return location, activity, climbing
    else: 
        print("Please choose one of the activities above.")

   
        
    return location, activity, climbing


# user_location = input('Enter city or location:\n')
# activity = input()

# weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=metric&APPID={api_key}")

# weather = weather_data.json()['weather'][0]['main']
# temp = weather_data.json()['main']['temp']

# # print(weather_data.json())

location, activity, climbing = location_and_activity()
print(activity)
print(climbing)

