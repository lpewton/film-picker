import random
import warnings
import gspread
from colorama import Fore, Style
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
MAX_RATING = 10
MIN_RATING = 0

films = SHEET.worksheet("films")


def set_up():
    """
    Sets introduction up.
    """
    print("\nWelcome to Film Picker!")
    print("Please choose an option:\n")
    print("1: See all available films")
    print("2: Get a random film suggestion based on a category")
    print("3: Add a new film to the system")
    print("4: Remove a film from the system\n")
    pick_option()


def pick_option():
    """
    Give user options to see a list of the films, choose a random
    film based on a category or add a film to the list.
    """
    try:
        options = input("Introduce option: ")
        if int(options) == 1:
            show_films()
            back_to_menu()
        elif int(options) == 2:
            print_categories()
            pick_category()
            pick_random_film(category)
        elif int(options) == 3:
            update_worksheet()
        elif int(options) == 4:
            delete_film()
        else:
            print(Fore.RED + "Please introduce one of the options")
            print(Fore.RESET)  # Requires separate line or line is too long
            pick_option()
    except ValueError:
        print(Fore.RED + "Please introduce one of the options\n" + Fore.RESET)
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
        film_rating = film[3]
        film_num = film_num + 1
        print(Fore.YELLOW + f"{film_num}: " + Style.RESET_ALL + f"{title}")
        print(Fore.YELLOW + "Genre: " + Style.RESET_ALL + f"{genre}")
        print(Fore.YELLOW + "Synopsis: " + Style.RESET_ALL + f"{descr}")
        print(Fore.YELLOW + "Rating: " + Style.RESET_ALL + f"{film_rating}\n")


def print_categories():
    """
    Prints all categories so user can pick one
    """
    print("\nPick a Category:")
    print("1: Comedy")
    print("2: Drama")
    print("3: Horror")
    print("4: History")
    print("5: Action")
    print("6: Crime")
    print("7: Romance")
    print("8: Fantasy")
    print("9: Mystery\n")


def pick_category():
    """
    Allows user to pick a category for a film
    """
    global category

    try:
        categories = int(input("Introduce category: "))
        if categories == 1:
            category = "Comedy"
        elif categories == 2:
            category = "Drama"
        elif categories == 3:
            category = "Horror"
        elif categories == 4:
            category = "History"
        elif categories == 5:
            category = "Action"
        elif categories == 6:
            category = "Crime"
        elif categories == 7:
            category = "Romance"
        elif categories == 8:
            category = "Fantasy"
        elif categories == 9:
            category = "Mistery"
        else:
            print(Fore.RED + "Please input a valid category\n" + Fore.RESET)
            pick_category()
    except ValueError:
        print(Fore.RED + "Please input a valid category\n" + Fore.RESET)
        pick_category()

    return category


def pick_random_film(category):
    """
    Picks a random film from the category the user picked
    """
    all_films = films.get_all_values()[1:]
    category_list = []
    for ind in range(len(all_films)):
        if category in all_films[ind]:
            category_list.append(all_films[ind])
    print(Fore.GREEN + f"\nYou chose {category}.")
    print(Fore.RESET)  # Requires separate line or line is too long
    print(f"This is a recommended {category} film:")
    random_num = random.randint(0, len(category_list))
    film = category_list[random_num]
    title = film[0]
    genre = film[1]
    descr = film[2]
    film_rating = film[3]
    print(Fore.YELLOW + "\nTitle: " + Style.RESET_ALL + f"{title}")
    print(Fore.YELLOW + "Genre: " + Style.RESET_ALL + f"{genre}")
    print(Fore.YELLOW + "Synopsis: " + Style.RESET_ALL + f"{descr}")
    print(Fore.YELLOW + "Rating: " + Style.RESET_ALL + f"{film_rating}\n")
    back_to_menu()


def add_movie():
    """
    Adds film caracteristics to a new list
    """
    print(Fore.GREEN + "\nYou chose to add a film\n" + Fore.RESET)
    new_movie = []
    movie_title = input("Movie title: ")
    new_movie.append(movie_title)
    print_categories()
    new_movie.append(pick_category())
    print(Fore.GREEN + f"You picked {category}\n" + Fore.RESET)
    movie_descr = input("Movie synopsis: ")
    new_movie.append(movie_descr)
    new_movie.append(validate_rating())

    return new_movie


def validate_rating():
    """
    Ensures that rating is a number from 0 to 10
    """
    try:
        global rating
        rating = float(input("\nIMDb Rating: "))
        if rating > MAX_RATING:
            print(Fore.RED + "Rating must be between 0 and 10" + Fore.RESET)
            validate_rating()
        elif rating < MIN_RATING:
            print(Fore.RED + "Rating must be between 0 and 10" + Fore.RESET)
            validate_rating()
    except ValueError:
        print(Fore.RED + "Please input a valid number" + Fore.RESET)
        validate_rating()

    return rating


def update_worksheet():
    """
    Adds new film list to worksheet
    """
    movie = add_movie()
    films.append_row(movie)
    print(Fore.GREEN + "\nMovie added successfully\n" + Fore.RESET)
    films.sort()
    show_films()
    back_to_menu()


def delete_film():
    """
    Shows all films and deletes the one user chooses
    """
    print("\nPlease choose a film to delete:\n")
    show_films()
    remove_film()


def remove_film():
    """
    Removes a film from the worksheet
    """
    all_films = films.get_all_values()
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    try:
        delete = int(input("Please enter a valid film number to delete: "))
        if delete <= 0:
            print(Fore.RED + "Please enter one of the film options")
            print(Fore.RESET)  # Requires separate line or line is too long
            remove_film()
        elif delete < len(all_films) + 1:
            deleted_film = delete + 1
            films.delete_row(deleted_film)
            print(Fore.GREEN + "\nFilm deleted successuflly\n" + Fore.RESET)
            back_to_menu()
            # 1 is necessary here because excel list starts at
            # 1 and terminal printed list starts at 0
        else:
            print(Fore.RED + "Please enter one of the film options")
            print(Fore.RESET)  # Requires separate line or line is too long
            remove_film()
    except ValueError:
        print(Fore.RED + "Please enter one of the film options\n" + Fore.RESET)
        remove_film()


def back_to_menu():
    """
    Gives the user the option to go back to the initial menu
    """
    print("Please choose an option")
    print("     M: Go back to the initial menu")
    print("     E: Exit program\n")
    back_to_menu_option = input("Enter option (M/E): ")
    answer = back_to_menu_option.upper()
    if answer == "E":
        print(Fore.BLUE + "\nGOODBYE\n" + Fore.RESET)
    elif answer == "M":
        set_up()
    else:
        print(Fore.RED + "Please enter one of the options\n" + Fore.RESET)
        back_to_menu()


set_up()
