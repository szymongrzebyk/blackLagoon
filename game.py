import os
import sys


# main menu
def display_main_menu():
    os.system("clear")
    print("MAIN MENU\n"
          "1. New game\n"
          "2. Load game\n"
          "3. Settings\n"
          "4. Authors\n"
          "5. Quit game")


def main_menu():
    display_main_menu()
    while True:
        try:
            choice = int(input("Choose option: "))
            if choice not in range(1, 6):
                raise ValueError
            break
        except ValueError:
            display_main_menu()
            print("You've inserted wrong number")
    return choice


player_choice = main_menu()
match player_choice:
    case 1:
        print("Starting new game.")
        # new_game()
    case 2:
        print("Loading game.")
        # load_game()
    case 3:
        print("Displaying settings.")
        # display_settings()
    case 4:
        print("Presenting authors.")
        # display_authors()
    case 5:
        print("Quiting the game...")
        sys.exit()
# the game
# while True:




    # turn
    #