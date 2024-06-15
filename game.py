import random
import json

class AttackMove:
    def __init__(self, name, power, element):
        self.name = name
        self.power = power
        self.element = element

elemental_advantages = {
    "Fire": ["Earth", "Air"],
    "Water": ["Fire"],
    "Earth": ["Water"],
    "Air": ["Earth", "Water"]
}

class ElementalCreature:
    def __init__(self, name, element, level):
        self.name = name
        self.element = element
        self.level = level
        self.health = level * 10 
        self.moves = []

    def learn_move(self, move):
        self.moves.append(move)

    def level_up(self):
        if self.level < 999:
            self.level += 1
            self.health = self.level * 10 
            for move in self.moves:
                move.power += 5

    def attack(self, target, move):
        print(f"{self.name} attacks {target.name} with {move.name}!")
        if move.element in elemental_advantages[self.element]:
            damage = move.power * 1.5 
        else:
            damage = move.power
        target.health -= damage
        print(f"{target.name} takes {damage} damage and now has {target.health} health left.")

class Player:
    def __init__(self, name):
        self.name = name
        self.elemental_creatures = []

    def choose_creature_for_battle(self):
        if not self.elemental_creatures:
            print("You have no creatures to battle with.")
            return None

        print("Choose a creature for battle:")
        for idx, creature in enumerate(self.elemental_creatures):
            print(f"{idx + 1}. {creature.name} (Level: {creature.level}, Health: {creature.health})")

        choice = int(input("Enter the number of the creature you want to use: ")) - 1
        if 0 <= choice < len(self.elemental_creatures):
            return self.elemental_creatures[choice]
        else:
            print("Invalid choice.")
            return None

class Game:
    def __init__(self):
        self.player = None
        self.running = True

    def main_menu(self):
        print("Welcome to Elemental Saga!")
        while self.running:
            print("1. Start Adventure")
            print("2. View Instructions")
            print("3. Elemental Dex")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")
            if choice == '1':
                self.start_adventure()
            elif choice == '2':
                self.view_instructions()
            elif choice == '3':
                self.display_elemental_dex()
            elif choice == '4':
                self.quit()
            else:
                print("Invalid choice. Please try again.")

    def start_adventure(self):
        name = input("Enter your name: ")
        self.player = Player(name)
        print(f"Welcome, {self.player.name}!")
        if self.load_game():
            print("Loaded saved game.")
        else:
            print("No saved game found. Starting a new adventure.")
        self.game_loop()

    def game_loop(self):
        while self.running:
            print("1. Explore")
            print("2. Train")
            print("3. Battle")
            print("4. Save Game")
            print("5. Main Menu")
            choice = input("Enter your choice (1-5): ")
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
                print("Invalid choice. Please try again.")

    def explore(self):
        print("Exploring...")
        creature = self.find_creature()
        if creature:
            print(f"You encountered a wild {creature.name}!")
            action = input("Do you want to capture it? (yes/no): ")
            if action.lower() == 'yes':
                self.capture_creature(creature)
            else:
                print("You let the creature go.")
        else:
            print("No creatures found.")

    def find_creature(self):
        creatures = [
            ElementalCreature("Flameling", "Fire", random.randint(1,10)),
            ElementalCreature("Aqualing", "Water", random.randint(1,10)),
            ElementalCreature("Terraling", "Earth", random.randint(1,10)),
            ElementalCreature("Zephyrling", "Air", random.randint(1,10))
        ]
        creature = random.choice(creatures)
        creature.learn_move(AttackMove("Basic Attack", 10, creature.element))
        if creature.name == "Flameling":
            creature.learn_move(AttackMove("Flame Burst", 15, "Fire"))
        elif creature.name == "Aqualing":
            creature.learn_move(AttackMove("Water Jet", 15, "Water"))
        elif creature.name == "Terraling":
            creature.learn_move(AttackMove("Rock Slide", 15, "Earth"))
        elif creature.name == "Zephyrling":
            creature.learn_move(AttackMove("Gust", 15, "Air"))
        return creature

    def capture_creature(self, creature):
        self.player.elemental_creatures.append(creature)
        print(f"{creature.name} has been added to your ElementalDex!")

    def train(self):
        print("Training...")
        creature = self.player.choose_creature_for_battle()
        if creature:
            creature.level_up()
            print(f"{creature.name} has leveled up to level {creature.level}!" )

    def battle(self):
        print("Battle!")
        player_creature = self.player.choose_creature_for_battle()
        if not player_creature:
            print("No creature selected for battle.")
            return
        enemy_creature = self.find_creature()
        if not enemy_creature:
            print("No enemy creature found for battle.")
            return
        print(f"A wild {enemy_creature.name} (Level: {enemy_creature.level}, Health: {enemy_creature.health}) appeared!")
        while player_creature.health > 0 and enemy_creature.health > 0:
            print(f"\n{player_creature.name} (Health: {player_creature.health}) vs {enemy_creature.name} (Health: {enemy_creature.health})")
            if not player_creature.moves:
                print(f"{player_creature.name} has no moves to use in battle!")
                break
            print("Choose your move:")
            for idx, move in enumerate(player_creature.moves):
                print(f"{idx + 1}. {move.name} (Power: {move.power}, Element: {move.element})")
            move_choice = int(input("Enter the number of the move you want to use: ")) - 1
            if 0 <= move_choice < len(player_creature.moves):
                player_move = player_creature.moves[move_choice]
                player_creature.attack(enemy_creature, player_move)
                if enemy_creature.health <= 0:
                    print(f"{enemy_creature.name} is defeated!")
                    player_creature.level_up()
                    print(f"{player_creature.name} leveled up to {player_creature.level}!")
                    break
                enemy_move = random.choice(enemy_creature.moves)
                enemy_creature.attack(player_creature, enemy_move)
                if player_creature.health <= 0:
                    print(f"{player_creature.name} is defeated!")
                    break
            else:
                print("Invalid move choice. Please try again.")        
    def save_game(self):
        with open("savegame.json", "w") as savefile:
            json.dump({
                "player_name": self.player.name,
                "elemental_creatures": [
                    {
                        "name": c.name,
                        "element": c.element,
                        "level": c.level,
                        "health": c.health,
                        "moves": [
                            {
                                "name": m.name,
                                "power": m.power,
                                "element": m.element
                            } for m in c.moves
                        ]
                    } for c in self.player.elemental_creatures
                ]
            }, savefile)
        print("Game saved successfully.")

    def load_game(self):
        try:
            with open("savegame.json", "r") as savefile:
                data = json.load(savefile)
                if "player_name" in data and "elemental_creatures" in data:
                    self.player = Player(data["player_name"])
                    for c_data in data["elemental_creatures"]:
                        creature = ElementalCreature(c_data["name"], c_data["element"], c_data["level"])
                        creature.health = c_data["health"]
                        for m_data in c_data["moves"]:
                            move = AttackMove(m_data["name"], m_data["power"], m_data["element"])
                            creature.learn_move(move)
                        self.player.elemental_creatures.append(creature)
                    print("Game loaded successfully!")
                    return True
                else:
                    print("Save file is corrupted or missing required keys. Starting a new game.")
                    return False
        except FileNotFoundError:
            print("No save file found. Starting a new game.")
            return False


    def view_instructions(self):
        print("Instructions:")
        print("1. Capture new creatures to build your ElementalDex.")
        print("2. Train your creatures to increase their levels and power.")
        print("3. Battle wild creatures to test your strength.")
        print("4. Save your progress regularly to avoid losing your progress.")
        print("5. Return to the main menu anytime to explore other options.")

    def display_elemental_dex(self):
        if not self.player or not self.player.elemental_creatures:
            print("ElementalDex is empty. Go capture some creatures!")
            return

        print("ElementalDex:")
        for creature in self.player.elemental_creatures:
            print(f"{creature.name} (Element: {creature.element}, Level: {creature.level}, Health: {creature.health})")
            for move in creature.moves:
                print(f"  - Move: {move.name} (Power: {move.power}, Element: {move.element})")

    def quit(self):
        save_prompt = input("Do you want to save your progress before exiting? (yes/no): ").lower()
        if save_prompt == 'yes':
            self.save_game()
        self.running = False
        print("Thank you for playing Elemental Saga!")

    def check_end_goal(self):
        for creature in self.player.elemental_creatures:
            if creature.level >= 10:
                print(f"Congratulations! {creature.name} You have reached the end goal of leveling up your creatures to level 10!")
                self.running = False
                break

if __name__ == "__main__":
    game = Game()
    while game.running:
        game.main_menu()
        game.check_end_goal()


