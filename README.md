# Film Picker:

Picking a film can be a complicated task when choosing what to watch, especially if there are more than one interested. This program is a useful tool that suggests a random film from a film database or shows you which films are included.

This program is useful both for personal purposes, for families, groups of friends or an individual person, and for professional purposes, like for film clubs or film watching activities.

Aside from the part the user sees, the program also contains an excel database which can be altered by the user. Films can be entered to or removed from the database.

You can find the link here:
https://film-picker-lpewton.herokuapp.com/

## Features:
 * **Database:**
 This is an excel sheet that contains the films and their genre, synopsis and rating.
* **Visible section:**
This part allows the user to interact with the program, it offers them the different options. The options are the following:
  * **Show all films:**
This allows the user to see a list of all the films in the database, along with their genre, synopsis and rating.
  * **Pick a random film:**
This generates a random film for the user from on the genre they chose.
  * **Add a new film to the system:**
Allows the user to introduce a new film into the database,along with its genre, synopsis and rating.
  * **Remove a film from the system:**
 Allows the user to remove one of the films from the system.

## Features left to implement:
In the future a front-end part could be included in the program, to make it more user-friendly. In this user-frinedly zone we could even include the trailer link for the randmly picked film, although for this more time is required.

## Testing:
* This webpage was tested on the following browsers: Firefox, ¿Safari? and Chrome. It worked on all of them.
* All of the options do their correct function and all exceptions have been handled appropriately.

## Bugs:
* Along the creation of the website, some bugs appeared, but they were solved as they came up.
* Some exception handling did not work, this was fixed by changing the order of the functions.

## Unsolved Bugs:
* There are no unsolved bugs in the program.

## Validator testing:

* Accessibility: HOW TO TEST RESULTS??

## Deployment:
* The site is deployed on Heroku. The steps followed to deploy it are the following:
  *  Create a new app
  * In the Settings page, navigate to: config var 
  * Add the CREDS key and give it the value which will be a copu of the creds.json file
  * Add a PORT key and give it a value of 8000
  * Add the following Buildpacks:
    * Python
    * NodeJs
 * Navigate to the Deploy page
 * Click on Enable Automatic Deploys
 * Wait for your app to be built
  
## Credits:
* All film synopsis and ratings have been extarcted from the Wikipedia pages.

## Acknowledgements:
* I would like to thank my tutor for giving me support and help throughout the project.
