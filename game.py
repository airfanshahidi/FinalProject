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

class Player:
  def __init__(self, name):
    self.name = name
    self.hp = 100
    self.elemental_creatures = []

  def __repr__(self):
    return f"Player(name={self.name}, hp={self.hp}, creatures={self.elemental_creatures})"