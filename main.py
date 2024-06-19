"""
Elemental Dex by Airfan Shahidi
------------------------------------------

Welcome to Elemental Dex!

In this text based RPG, your goal is to capture creatures and have the best Elemental Dex!

You can capture creatures by exploring and battling them.

You can also train your creatures to increase their levels and power.

You can save your progress regularly to avoid losing your progress.

Good luck and have fun!

"""
import sys
from game import Game

def display_main_menu():
  print("\nWelcome to Elemental Saga!")
  print("\n1. Start Adventure")
  print("\n2. View Instructions")
  print("\n3. Elemental Dex")
  print("\n4. Exit")

def get_user_choice():
  choice = input("\nEnter your choice (1-4): ")
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
      print("\nThank you for playing Elemental Saga!")
      sys.exit()
    else:
      print("\nInvalid choice. Please try again.")

def show_instructions():
  print("\nInstructions:")
  print("\n1. Explore the world to find and capture elemental creatures.")
  print("\n2. Train your elemental creatures to become stronger.")
  print("\n3. Battle other Elemental Guardians and prove your strength.")
  print("\n4. Save the world from the impending chaos.\n")
  input("\nPress Enter to Return to the Main Menu...")

def show_elemental_dex(game):
  print("\nElemental Dex:")
  if not game.player or not game.player.elemental_creatures:
    print("\nYou have not captured any elemental creatures yet.")
  else:
    for creature in game.player.elemental_creatures:
      print(f"Name: {creature.name}, Element: {creature.element}, Level: {creature.level}, Health: {creature.health}")
  input("\nPress Enter to Return to the Main Menu...")

if __name__ == "__main__":
  main()