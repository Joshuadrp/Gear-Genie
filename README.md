# Gear Genie

![Screenshot of the website](/assets/images/responsive.png)

<p style="text-align: center;">
    <a href="https://gear-genie-753673ae0f6b.herokuapp.com/">Visit the live site here!</a>
</p>

## Introduction

Gear Genie is an app made for outdoor enthusiasts. User will input a location and based on basic weather data fetched from openweathermap API, user will decide if to continue or not. If user continues then he must choose an activity to perform, and based on that input, gear data will be fetch from google sheets and it will be displayed in a table format. 

## User Stories

### User's goals:

- As the user, I want to be able to get weather data.
- As the user, I want to know what gear to use in determined activity.
- As the user, I want the control to end program if I consider weather is not good.
- As the user, I want to know advanced weather data if I want to perform my activity.
- As the user, I want a visual representation of weather and gear data.

### Site Owner's goals:

- As the site owner, I want to create an app that displays weather and equipment to be used in certain activities.
- As the site owner, I want to create a table that displays said gear data.
- As the site owner, I want the user to feel comfortable with the app.

## Design

The program layout is simple to follow and understand, all the information is displayed in an appealing way and easy to read structure, giving a different color to the user's input and different color to the weather data displayed. Also, a table so its easier for the user to read the gear data.

## Features

### Starting Page

![Intro Message](/assets/images/intro.png)

When the program is first run, a banner with the app name is displayed and an introduction message which has some instructions for the user as well. Last but not least, the actual functionality of the app begins. The program asks the user to input a location. This location is validated, and cannot be a number. If location is not valid it will ask for an existing location again. An error code is fetched from the API in order to obtain a valid location. 

### Users Choice

![Users Choice](/assets/images/basicw_data.png)

After validating the location, basic weather information will be displayed. The app then will ask the user if he/she wishes to continue. If answer is no, then program will be terminated. If answer is yes, program will continue to run. 

### Activity

![Activity to perform](/assets/images/activity.png)

User will be asked to input which type of activity wishes to perform. Three options are given, and the input will be validated, if not valid then program will ask the user to input again. If user chooses climbing another three options will be given, if user chooses hiking the gear data for hiking will be fetched from google sheets and displayed. If User chooses other, a message will display stating that more activities will be available soon.

### Climbing

![Climbing](/assets/images/climbing.png)

If Climbing is chosen, then user will be asked which type of climbing. Three options are given, and each of them is validated as well, if not valid program will request user to input again. 

### Type of Climbing

![Type of Climbing](/assets/images/type_of_climbing.png)

When a type of climbing is chosen, then app will display a table populated with gear data for said type of climbing. Program is then terminated. 

### Hiking

![Hiking](/assets/images/hiking.png)

When hiking activity is chosen, then app will display a table populated with gear data for said type of activity. Program is then terminated.

### Other

![Other](/assets/images/other.png)

When other activity is selected, a message will be displayed stating that more activities will be available soon, and it will ask the user for another input(the two activities which the program has available)

## Logic Flow

Logic Flow was created before coding. Code structure and flow was influenced by this logic chart, this was easier when coming up with function names and functions proper flow, and code readability. 

![Logic](/assets/images/Logic_Flow.png)

### Future Features

More activities will be included. Currently there is an Other option, which in the future will be populated with different and amazing activities! 

## Testing

### Validation

Code was validated through Code Institute's [PEP8 Linter](https://pep8ci.herokuapp.com/#). At first several errors(most of them regarding code lines with too many characters) were encountered and fixed. In the end the final result was with zero errors as below. 

![validation](/assets/images/validation.png)

### Manual Testing

Once the project was completed, manual testing was performed on each feature of the game, using the deployed app on Heroku. All tests and their outcomes are outlined below.

#### Starting Page

| Feature Tested                                                        | Expected Outcome                                 | Actual Outcome                                   |
| --------------------------------------------------------------------- | ------------------------------------ | --------------------------------- |                             
| Input a valid location | Program proceeds to ask user if he/she wishes to continue after reviewing basic weather data. | Expected outcome             |
| Input an invalid location(digits) | Program proceeds to tell the user that location shouldn't be a number and asks for another input. | Expected outcome             |
| Input an invalid location(empty-string) | Error code and message are shown and asks the user for another input. | Expected outcome             |
| Input an invalid location(non-existent) | Error code and message are shown and asks the user for another input. | Expected outcome             |

The location had to be validated for digits specifically because the weahter API can take coordinates, and if digits are introduced the program takes them as coordinates, which causes the location to be valid even in the scenario in which user input random numbers. Thats why this program only takes existing locations.

#### Users Choice
| Feature Tested                                                        | Expected Outcome                                 | Actual Outcome                                   |
| --------------------------------------------------------------------- | ------------------------------------ | --------------------------------- |                             
| Input a valid choice(no) | Program terminates| Expected outcome             |
| Input a valid choice(yes) | Program proceeds and asks user to input desired activity.| Expected outcome             |
| Input an invalid choice(anything except yes or no) | Program asks user to input a valid choice. | Expected outcome             |

#### Activity
| Feature Tested                                                        | Expected Outcome                                 | Actual Outcome                                   |
| --------------------------------------------------------------------- | ------------------------------------ | --------------------------------- |                             
| Input a valid choice(climbing) | Program proceeds to ask what type of climbing the user want to perform. | Expected outcome             |
| Input a valid choice(hiking) | Program proceeds to display advanced weather data and displays a table with gear data to be used in that activity. | Expected outcome |
| Input a valid choice(other) | Program displays a message stating that new activities will be available soon and ask user for another input. | Expected outcome             |
| Input an invalid choice(anything but hiking,climbing,other.) | Program asks user to choose a valid activity. | Expected outcome             |

#### Type of Climbing
| Feature Tested                                                        | Expected Outcome                                 | Actual Outcome                                   |
| --------------------------------------------------------------------- | ------------------------------------ | --------------------------------- |                             
| Input a valid choice(trad climbing) | Program proceeds to display advanced weather data and displays a table with gear data to be used in that activity.  | Expected outcome |
| Input a valid choice(sport climbing) | Program proceeds to display advanced weather data and displays a table with gear data to be used in that activity.  | Expected outcome |
| Input a valid choice(bouldering) | Program proceeds to display advanced weather data and displays a table with gear data to be used in that activity.  | Expected outcome |
| Input an invalid choice(anything but trad climbing, sport climbing or bouldering) | Program asks user to choose a valid type of climbing. | Expected outcome |

## Bugs Encountered and Fixes Implemented

1. **Bug**: Location input accepts numeric values.
   - **Fix**: Added a condition to check if the location input is numeric and prompt the user to enter a valid location.

2. **Bug**: Incorrect condition to check if the location is valid.
   - **Fix**: Updated the condition to check if the API response status code is 200 to ensure the location is valid.

3. **Bug**: Invalid input handling in the function `display_weather_basic`.
   - **Fix**: Added lowercase conversion to the user's input to handle cases where the user enters 'yes' or 'no' with different capitalizations.

5. **Bug**: Missing return statement in `activity_input` function for the "hiking" activity.
   - **Fix**: Added a return statement for the "hiking" activity to ensure the function returns the activity and the corresponding column index.

6. **Bug**: Incorrect condition for climbing type input validation in `climbing_type_input`.
   - **Fix**: Corrected the condition to properly handle user input validation for climbing types.

7. **Bug**: Incorrect index used to fetch gear data in `fetch_gear_data` function.
   - **Fix**: Adjusted the column index to start fetching data from the second row, avoiding fetching the header row.

8. **Bug**: Program was not terminating when gear data was fetched for the activity.
   - **Fix**: Created an If statement in Main function to ensure proper function flow.

## Technologies Used

### Python Libraries:
- **requests**: For making HTTP requests to the OpenWeatherMap API to fetch weather data.
- **gspread**: To interact with Google Sheets and fetch/manage spreadsheet data.
- **pyfiglet**: To convert text into ASCII art fonts, providing a stylized introduction.
- **colorama**: To print colored text to the terminal, enhancing user interface aesthetics.
- **tabulate**: For creating well-formatted tables to display gear lists.
- **google.oauth2.service_account**: For creating service account credentials to authenticate and authorize access to Google Sheets.

### APIs:
- **OpenWeatherMap API**: For fetching current weather information based on user input.

### Google Services:
- **Google Sheets**: Used to store and retrieve gear data for various outdoor activities.

## Deployment

The project was deployed to Heroku using the following steps:

1. Sign in to Heroku and access the dashboard
2. In the top right corner, click the "New" dropdown menu and then click "Create new app"
3. Choose a name for your app, then change your region accordingly
4. Click "Create app"
5. On the next page that loads after clicking "Create app", click "Settings" in the top navigation bar
6. Click on "Reveal Config Vars"
7. Add new Config vars. For this project the API key and CREDS were added.
8. Next, scroll down to the "Buildpack" section and click "Add buildpack"
9. First add "Python", then add "nodejs" - they **must** be in this order
10. In the top navigation bar, click the "Deploy" tab
11. In the "Deployment Method" section, click on *GitHub* to connect to your GitHub account
12. After logging into your GitHub account, search for your GitHub repository name (for this project, it was "Gear-Genie")
13. Click on the repository once found to connect it
14. Scroll down to the section "Automatic Deploys" and click on the "Enable Automatic Deploys" button
15. Then underneath, make sure the branch for the project is "main" and click on the "Deploy" button
16. Wait for Heroku to display that the app was deployed successfully

### Code

- Code to fetch weather data was influened by openweathermap documentation [Open Weather Map API](https://openweathermap.org/current)
- Code to fetch data from google sheets was influenced by love sandwiches project [Love Sandwiches Project](https://github.com/Joshuadrp/LoveSandwiches.git)
- Code to convert text into ASCII art was influenced by pyfiglet documentation [PyFiglet Documentation](https://pypi.org/project/pyfiglet/) 
- Code to display gear data as a table was influenced by tabulate documentation and stack overflow comments. [Tabulate Documentation](https://pypi.org/project/tabulate/) 
- Code to give text another color was influenced by Colorama documentation. [Colorama Documentation](https://pypi.org/project/colorama/)

## Acknowledgements
- Thanks to Amy Richardson from CI for her constant and dedicated support every week.
- Thanks to my mentor Mitko Bachvarov for his support and advice throughout this project.

Click [here](#gear-genie) to return to the top of the page.