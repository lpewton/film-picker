import gspread
import random
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
    Sets introduction up.
    """
    print("Welcome to Film Picker!")
    print("Please choose an option:\n")
    print("1: See all available films")
    print("2: Get a random film suggestion based on a category")
    print("3: Add a new film to the system\n")
    pick_option()

def pick_option():
    """ 
    Give user options to see a list of the films, choose a random 
    film based on a category or add a film to the list.
    """

    options = input("Introduce option: ")
    try:
        if int(options) == 1:
            show_films()
        elif int(options) == 2:
            pick_random_category()
        elif int(options) == 3:
            print("3")
        else:
            print("Please introduce one of the options")
            pick_option()
    except ValueError:
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

def pick_random_category():
    """
    Allows user to pick a category for film to watch
    """
    print(f"\nPick a Category:")
    print("1: Comedy")
    print("2: Drama")
    print("3: Horror")
    print("4: History")
    print("5: Action")
    print("6: Crime")
    print("7: Romance")
    print("8: Fantasy")
    print("9: Mystery\n")
    categories = int(input("Introduce category: "))
    if categories == 1:
        category = "Comedy"
    if categories == 2:
        category = "Drama"
    if categories == 3:
        category = "Horror"
    if categories == 4:
        category = "History"
    if categories == 5:
        category = "Action"
    if categories == 6:
        category = "Crime"
    if categories == 7:
        category = "Romance"
    if categories == 8:
        category = "Fantasy"
    if categories == 9:
        category = "Mistery"

    pick_random_film(category)
    
def pick_random_film(category):
    """
    Picks a random film from the category the user picked
    """
    all_films = films.get_all_values()[1:]
    category_list = []
    for ind in range(len(all_films)):
        if category in all_films[ind]:
            category_list.append(all_films[ind])
    print(f"\nYou chose {category}. This is a recommended {category} film:")
    random_num = random.randint(0, len(category_list))
    film = category_list[random_num]
    title = film[0]
    genre = film[1]
    descr = film[2]
    rating = film[3]
    print(f"\nTitle: {title}")
    print(f"Genre: {genre}")
    print(f"Synopsis: {descr}")
    print(f"Rating: {rating}\n")

def main():
    set_up()

main()
