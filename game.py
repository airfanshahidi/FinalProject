from os import name
import random

class Game:
  def __init__(self):
    self.player = None
    self.running = False

  def start(self):
    self.running = True
    self.initialize_player()
    self.game_loop()

  def initialize_player(self):
    player_name = input("Enter your Guardian name: ")
    self.player = Player(player_name)
    print(f"Welcome, {self.player.name}! Prepare to master the elements.")

  def game_loop(self):
    while self.running:
      print("\nGame Loop Running...")
      command = input("Enter command (or 'quit' to exit): ")
      if command == 'quit':
        self.running = False
    print("Exiting game...")

  def explore(self):
    print("Exploring...")
    creature = self.find_creature()
    if creature:
      print(f"You have encountered a wild {creature.name}!")
      action = input("Do you want to capture it? (yes/no): ")
      if action.lower() == 'yes':
        self.capture_creature(creature)
    else:
      print("No creatures found.")

  def find_creature(self):
    creatures = [
      ElementalCreature("Flameling", "Fire", 50),
      ElementalCreature("Aqualing", "Water", 50),
      ElementalCreature("Terraling", "Earth", 50),
      ElementalCreature("Zephyrling", "Wind", 50)
    ]
    if random.choice([True, False]):
      return random.choice(creatures)
    return None

  def capture_creature(self, creature):
    self.player.elemental_creatures.append(creature)
    print(f"{creature.name} has been added to your ElementalDex!")

  def train(self):
    if not self.player.elemental_creatures:
      print("You don't have any elemental creatures to train.")
      return
    print("Training your creatures...")
    for creature in self.player.elemental_creatures:
      creature.level_up()
      print(f"{creature.name} leveled up to level {creature.level}")

  def battle(self):"
    if not self.player.elemental_creatures:"
      print("You have no creatures to battle with.")
      return
      print("Battling...")
      opponent = ElementalCreature("Aqualing", "Water, 60")
      print(f"A wild {opponent.name} appears!")
      player_creature = self.player.choose_creature_for_battle()
      if player_creature:
        if player_creature.level >= opponent.level:
          print(f"Your {player_creature.name} defeated the {opponent.name}!")
        else:
          print(f"Your {player_creature.name} was defeated by the {opponent.name}.")
      else:
        print("You don't have any creatures to battle with.")

  def display_elemental_dex(self):
    if not self.player.elemental_creatures:
      print("You have no captured creatures.")
      return
    for creature in self.player.elemental_creatures:
      print(f"Name: {creature.name}, Element: {creature.element}, Level: {creature.level}")

class Player:
  def __init__(self, name):
    self.name = name
    self.elemental_creatures = []

  def choose_creature_for_battle(self):
    if not self.elemental_creatures:
      return None
      print("Choose a creature to battle with:")
      for idx, creature in enumerate(self.elemental_creatures):
        print(f"{idx + 1}. {creature.name} (Level: {creature.level})")
      choice = int(input("Enter the number of the creature you want to choose:")) - 1
      if 0 <= choice < len(self.elemental_creatures):
        return self.elemental_creatures[choice]
      else:
        print("Invalid Choice")
        return None

class ElementalCreature:
  def __init__(self, name, element, level:
               self.name = name
               self.element = element
               self.level = level

  def level_up():
    self.level += 1
    print(f"{self.name} leveled up to level {self.level}!")
  
  
  
      