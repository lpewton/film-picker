import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("film_picker")

films = SHEET.worksheet("films")

def set_up():
    """
    Sets introduction up snd gives you the option to see a list of the films,
    choose a random film based on a category or add a film to the list.
    """
    print("Welcome to Film Picker!")
    print("Please choose an action:\n")
    print("1: See all available films")
    print("2: Get a random film suggestion based on a category")
    print("3: Add a new film to the system\n")
    pick_option()

def pick_option():
    options = input("Introduce option: ")
    try:
        if int(options) == 1:
            show_films()
        elif int(options) == 2:
            print("2")
        elif int(options) == 3:
            print("3")
        else:
            print("Please introduce one of the options")
            pick_option()
    except:
        print("Please introduce one of the options")
        pick_option()

    

def show_films():
    """
    Show a list of the films with their respectives categories, genre,
    synopsis and rating
    """
    all_films = films.get_all_values()[1:]
    film_num = 0
    for ind in range(len(all_films)):
        film = all_films[ind]
        title = film[0]
        genre = film[1]
        descr = film[2]
        rating = film[3]
        film_num = film_num + 1
        print(f"\n{film_num}: {title}")
        print(f"Genre: {genre}")
        print(f"Synopsis: {descr}")
        print(f"Rating: {rating}\n")

def main():
    set_up()

main()
