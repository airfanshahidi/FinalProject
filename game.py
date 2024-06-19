import random
import json

# Class to represent an attack move
class AttackMove:
  def __init__(self, name, power, element):
    self.name = name
    self.power = power
    self.element = element

# Dictionary to define elemental advantages
elemental_advantages = {
  "Fire": ["Earth", "Air"],
  "Water": ["Fire"],
  "Earth": ["Water"],
  "Air": ["Earth", "Water"]
}

# Class to represent an elemental creature
class ElementalCreature:
  def __init__(self, name, element, level):
    self.name = name
    self.element = element
    self.level = level
    self.health = level * 10 # Health is determined by level
    self.moves = [] # List to store the moves the creature can use

  # Method for a creature to learn a new move
  def learn_move(self, move):
    self.moves.append(move)

  # Method to level up the creature
  def level_up(self):
    if self.level < 999:
      self.level += 1
      self.health = self.level * 10 # Restore health to full when leveling up
      for move in self.moves:
        move.power += 5 # Increase the power of all moves

  # Method for a creature to attack another creature
  def attack(self, target, move):
    print(f"{self.name} used {move.name}!")
    if move.element == target.element:
      damage = move.power // 2  # Reduced damage if the same element
    else:
      damage = move.power
    target.health -= damage
    target.health = max(0, target.health)  # Ensure health doesn't go negative
    print(f"{target.name} took {damage} damage and now has {target.health} health.")

# Class to represent a player
class Player:
  def __init__(self, name):
    self.name = name
    self.elemental_creatures = [] # List to store the player's elemental creatures

  # Method for the player to choose a creature for battle
  def choose_creature_for_battle(self):
    if not self.elemental_creatures:
      print("\nYou have no creatures to battle with.")
      return None

    print("\nChoose a creature for battle:")
    for idx, creature in enumerate(self.elemental_creatures):
      print(f"\n{idx + 1}. {creature.name} (Level: {creature.level}, Health: {creature.health})")

    choice = int(input("\nEnter the number of the creature you want to use: ")) - 1
    if 0 <= choice < len(self.elemental_creatures):
      return self.elemental_creatures[choice]
    else:
      print("\nInvalid choice.")
      return None

# Class to represent the game
class Game:
  def __init__(self):
    self.player = None
    self.running = True

  # Method to display the main menu
  def main_menu(self):
    print("\nWelcome to Elemental Saga!")
    while self.running:
      print("\n1. Start Adventure")
      print("\n2. View Instructions")
      print("\n3. Elemental Dex")
      print("\n4. Exit")
      choice = input("\nEnter your choice (1-4): ")
      if choice == '1':
        self.start_adventure()
      elif choice == '2':
        self.view_instructions()
      elif choice == '3':
        self.display_elemental_dex()
      elif choice == '4':
        self.quit()
      else:
        print("\nInvalid choice. Please try again.")

  # Method to start the adventure
  def start_adventure(self):
    name = input("\nEnter your name: ")
    self.player = Player(name)
    print(f"\nWelcome, {self.player.name}!")
    if self.load_game():
      print("\nLoaded saved game.")
    else:
      print("\nNo saved game found. Starting a new adventure.")
    self.game_loop()

  # Main game loop
  def game_loop(self):
    while self.running:
      print("\n1. Explore")
      print("\n2. Train")
      print("\n3. Battle")
      print("\n4. Save Game")
      print("\n5. Main Menu")
      choice = input("\nEnter your choice (1-5): ")
      if choice == '1':
        self.explore()
      elif choice == '2':
        self.train()
      elif choice == '3':
        self.battle()
      elif choice == '4':
        self.save_game()
      elif choice == '5':
        return
      else:
        print("\nInvalid choice. Please try again.")

  # Method to explore and possibly find a new creature
  def explore(self):
    print("\nExploring the wild...")
    if random.random() < 0.5:  # 50% chance to find a new creature
      new_creature = self.generate_random_creature()
      print(f"\nYou found a wild {new_creature.name}!")
      capture = input("\nDo you want to capture this creature? (yes/no): ")
      if capture.lower() == 'yes':
        self.player.elemental_creatures.append(new_creature)
        print(f"\nYou captured {new_creature.name}!")
      else:
        print(f"\nYou let {new_creature.name} go.")
    else:
      print("\nYou didn't find any creatures this time.")

  # Method to train a creature to level up
  def train(self):
    creature = self.player.choose_creature_for_battle()
    if creature:
      print(f"\nTraining {creature.name}...")
      creature.level_up()
      print(f"\n{creature.name} leveled up to level {creature.level}!")

  # Method to initiate a battle
  def battle(self):
    print("\nEntering battle...")
    player_creature = self.player.choose_creature_for_battle()
    if not player_creature:
      return

    opponent_creature = self.generate_random_creature()
    print(f"\nAn opponent {opponent_creature.name} appeared!")

    while player_creature.health > 0 and opponent_creature.health > 0:
      print("\nYour moves:")
      for idx, move in enumerate(player_creature.moves):
        print(f"\n{idx + 1}. {move.name} (Power: {move.power})")

      choice = int(input("\nChoose a move: ")) - 1
      if 0 <= choice < len(player_creature.moves):
        player_move = player_creature.moves[choice]
        player_creature.attack(opponent_creature, player_move)
      else:
        print("\nInvalid move choice.")
        continue

      if opponent_creature.health > 0:
        opponent_move = random.choice(opponent_creature.moves)
        opponent_creature.attack(player_creature, opponent_move)

    if player_creature.health > 0:
      print("\nYou won the battle!")
      player_creature.level_up()
    else:
      print("\nYou lost the battle.")

  # Method to generate a random creature
  def generate_random_creature(self):
    names = ["Flameon", "Aquata", "Terradon", "Galeon"]
    elements = ["Fire", "Water", "Earth", "Air"]
    name = random.choice(names)
    element = random.choice(elements)
    level = random.randint(1, 10)
    creature = ElementalCreature(name, element, level)
    moves = self.generate_moves_for_creature(element)
    for move in moves:
      creature.learn_move(move)
    return creature

  # Method to generate moves for a creature based on its element
  def generate_moves_for_creature(self, element):
    moves = []
    if element == "Fire":
      moves.append(AttackMove("Blaze", 10, "Fire"))
      moves.append(AttackMove("Flame Burst", 15, "Fire"))
    elif element == "Water":
      moves.append(AttackMove("Splash", 10, "Water"))
      moves.append(AttackMove("Tidal Wave", 15, "Water"))
    elif element == "Earth":
      moves.append(AttackMove("Rock Throw", 10, "Earth"))
      moves.append(AttackMove("Earthquake", 15, "Earth"))
    elif element == "Air":
      moves.append(AttackMove("Gust", 10, "Air"))
      moves.append(AttackMove("Tornado", 15, "Air"))
    return moves

  # Method to view game instructions
  def view_instructions(self):
    print("\nInstructions:")
    print("\n1. In 'Start Adventure', you can explore, train, and battle with your elemental creatures.")
    print("\n2. In 'Explore', you have a chance to find and capture new creatures.")
    print("\n3. In 'Train', you can level up your creatures by training them.")
    print("\n4. In 'Battle', you can fight against wild creatures to earn experience and level up.")
    print("\n5. In 'Elemental Dex', you can view information about different elemental creatures.")
    print("\n6. Use 'Save Game' to save your progress.")
    print("\n7. Use 'Main Menu' to return to the main menu.")

  # Method to display the Elemental Dex
  def display_elemental_dex(self):
    print("\nElemental Dex:")
    for element, advantages in elemental_advantages.items():
      print(f"\n{element}:")
      print("\nAdvantages over:", ", ".join(advantages))

  # Method to save the game state
  def save_game(self):
    try:
      game_state = {
        'player_name': self.player.name,
        'elemental_creatures': [
          {
            'name': creature.name,
            'element': creature.element,
            'level': creature.level,
            'health': creature.health,
            'moves': [{'name': move.name, 'power': move.power, 'element': move.element} for move in creature.moves]
          }
          for creature in self.player.elemental_creatures
        ]
      }
      with open('savegame.json', 'w') as save_file:
        json.dump(game_state, save_file)
        print("\nGame saved successfully!")
    except Exception as e:
      print(f"\nAn error occurred while saving the game: {e}")

  # Method to load the game state
  def load_game(self):
    try:
      with open('savegame.json', 'r') as save_file:
        game_state = json.load(save_file)
        self.player = Player(game_state['player_name'])
        for creature_data in game_state['elemental_creatures']:
          creature = ElementalCreature(
            creature_data['name'],
            creature_data['element'],
            creature_data['level']
          )
          creature.health = creature_data['health']
          for move_data in creature_data['moves']:
            move = AttackMove(
              move_data['name'],
              move_data['power'],
              move_data['element']
            )
            creature.learn_move(move)
          self.player.elemental_creatures.append(creature)
        return True
    except FileNotFoundError:
      return False
    except Exception as e:
      print(f"\nAn error occurred while loading the game: {e}")
      return False

  # Method to quit the game
  def quit(self):
    print("\nThank you for playing Elemental Saga! Goodbye!")
    self.running = False

if __name__ == "__main__":
  game = Game()
  game.main_menu()