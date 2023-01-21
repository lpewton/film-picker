# Film Picker:

Picking a film can be a complicated task when choosing what to watch, especially if there is more than one person deciding. This app is a useful tool that suggests a random film from a film database or shows you which films are included.

This program is useful both for personal purposes (for families, groups of friends or an individual person) and for professional purposes (for film clubs or film watching activities).

Aside from the visible section, the program also contains an excel database which can be altered by the user. In this app, the user has the ability to enter or remove films from the database.

You can find the live link here:
https://film-picker-lpewton.herokuapp.com/

## Features:
 * **Database:**
 This is an excel sheet that contains the films and their genre, synopsis and rating.
 ![Screen Shot 2023-01-17 at 01 32 50](https://user-images.githubusercontent.com/114712846/212784982-0d4f7a24-f9c6-4d27-af20-d2278636785a.png)

* **Visible section:**
This part allows the user to interact with the program, it offers them the different options. The options are the following:

![Screen Shot 2023-01-17 at 01 29 01](https://user-images.githubusercontent.com/114712846/212785115-11234eca-113f-4bd8-b930-ce06a88fbdef.png)

  * **Show all films:**
This allows the user to see a list of all the films in the database, along with their genre, synopsis and rating.
![Screen Shot 2023-01-17 at 01 29 49](https://user-images.githubusercontent.com/114712846/212785141-3045253f-ba16-4b07-8240-ffb7e5f34cdf.png)

  * **Pick a random film:**
This generates a random film for the user from the genre they chose.
![Screen Shot 2023-01-20 at 01 19 44](https://user-images.githubusercontent.com/114712846/213590826-849b5241-91f8-42a1-873a-f9ab3779c4e6.png)

  * **Add a new film to the system:**
Allows the user to introduce a new film into the database, along with its genre, synopsis and rating.
![Screen Shot 2023-01-20 at 01 22 32](https://user-images.githubusercontent.com/114712846/213591117-6d40874f-60be-4339-80c7-c8b4c90853e1.png)


  * **Remove a film from the system:**
 Allows the user to remove one of the films from the system.
![Screen Shot 2023-01-20 at 01 25 17](https://user-images.githubusercontent.com/114712846/213591565-9cf1abc0-7055-48c9-a2de-c23130492d6f.png)

 * **Back to menu option:**
This section allows the user to go back to the initial menu or to exit the program.
![Screen Shot 2023-01-20 at 01 28 02](https://user-images.githubusercontent.com/114712846/213591883-b31856c6-f2c7-4447-9a32-ee3d13a6c8bc.png)


## Features left to implement:
In the future a front-end part could be included in the app, to make it more user-friendly. In this user-friendly zone we could even include the trailer link for the randomly picked film, although for this more time is required.
I would also like to get the program to sort the films in order for the user to be able to find them more easily and for the possibility to add new categories to the app.

## Testing:
* The Heroku program does not seem to work on the newer version of Iphones, though that is a global Heroku issue, not one of the app.
* All of the options do their correct function and all exceptions have been handled appropriately.
* App was tested through manual input of various erroneous answers (letters when numbers were required, blank spaces, negative or out of range numbers...). The app was not broken by any of them. 
* Code passed through CI Python Linter with no errors: https://pep8ci.herokuapp.com/#. 
![Screen Shot 2023-01-21 at 20 33 16](https://user-images.githubusercontent.com/114712846/213884068-c28ffc92-3f39-4f09-91a5-4ef2b8cd8285.png)


## Bugs:
* Along the creation of the app, some bugs appeared, but they were solved as they came up.
* Some exception handling did not work, this was fixed by changing the order of the functions.

## Unsolved Bugs:
* There are no unsolved bugs in the app.

## Deployment:
* This app is deployed on Heroku. The steps followed to deploy it are the following:
  *  Create a new app
  * In the Settings page, navigate to: config var 
  * Add the CREDS key and give it the value which will be a copy of the creds.json file
  * Add a PORT key and give it a value of 8000
  * Add the following Buildpacks:
    * Python
    * NodeJs
 * Navigate to the Deploy page
 * Click on Enable Automatic Deploys
 * Wait for your app to be built
  
## Credits:
* All film synopsis and ratings have been extracted from the Wikipedia pages.
* The information on how to import Colorama and the other libraries was obtained from Stack Overflow

## Acknowledgements:
* I would like to thank my tutor for giving me support and help throughout the project.
* I would also like to appreciate the Stack Overflow community for providing me with information on different libraries and techniques that were used in this project.
