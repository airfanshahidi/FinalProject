import sys
from game import Game

def display_main_menu():
    print("Welcome to Elemental Saga!")
    print("1. Start Adventure")
    print("2. View Instructions")
    print("3. Elemental Dex")
    print("4. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-4): ")
    return choice

def main():
    game = Game()
    while True:
        display_main_menu()
        choice = get_user_choice()
        if choice == '1':
            game.start_adventure()
        elif choice == '2':
            show_instructions()
        elif choice == '3':
            show_elemental_dex(game)
        elif choice == '4':
            print("Thank you for playing Elemental Saga!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def show_instructions():
    print("\nInstructions:")
    print("1. Explore the world to find and capture elemental creatures.")
    print("2. Train your elemental creatures to become stronger.")
    print("3. Battle other Elemental Guardians and prove your strength.")
    print("4. Save the world from the impending chaos.\n")
    input("Press Enter to Return to the Main Menu...")

def show_elemental_dex(game):
    print("\nElemental Dex:")
    if not game.player or not game.player.elemental_creatures:
        print("You have not captured any elemental creatures yet.")
    else:
        for creature in game.player.elemental_creatures:
            print(f"Name: {creature.name}, Element: {creature.element}, Level: {creature.level}, Health: {creature.health}")
    input("Press Enter to Return to the Main Menu...")

if __name__ == "__main__":
    main()