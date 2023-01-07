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
    print("3: Add a new film to the system")
    pick_option()


def show_films():
    """
    Show a list of the films with their respectives categories, genre, synopsis and rating
    """
    all_films = films.get_all_values()
    film_num = 0
    for ind in range(len(all_films)):
        film = all_films[ind + 1]
        title = film[0]    
        genre = film[1]
        descr = film[2]
        rating = film[3]
        film_num = film_num + 1    
        print(f"{film_num}: {title}. Genre: {genre}. Synopsis: {descr} Rating: {rating}\n")   

def main():
    set_up()

main()
