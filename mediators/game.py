import random

import database
from datum.entity import Mob, Player
from datum.items import stick
from mediators.shop import Shop


class Game:
    def __init__(self, player, new_game):
        try:
            old_player = database.get_player(1)
        except ValueError:  # if player doesn't exist
            self.player = player
        else:
            if new_game is True:
                self.player = player
                database.delete_player(old_player.id)
                database.delete_inventory(old_player.inventory_id)
            else:  # use saved data
                self.player = old_player

        # Define the mobs
        self.mobs: list[Mob] = [
            Mob(name="Goblin", damage=10, maximum_health=100, level=random.randint(1, 10)),
            Mob(name="Orc", damage=15, maximum_health=170, level=random.randint(1, 10)),
            Mob(name="Ogre", damage=15, maximum_health=250, level=random.randint(1, 10)),
            Mob(name="slime", damage=5, maximum_health=70, level=random.randint(1, 10))
        ]

    def start(self):
        # Determine the number of enemies based on probabilities
        num_enemies = random.choices([1, 2, 3], weights=[30, 60, 10])[0]

        # Randomly select mobs from the list
        current_mobs = random.sample(self.mobs, num_enemies)

        print("Number of enemies:", num_enemies)
        print("Current mobs:", [mob.name for mob in current_mobs])

        # Perform actions
        self.action(current_mobs)

    def action(self, current_mobs):
        while True:
            print("Select Action: A. Attack B.Inventory C.Player Info")
            option = str.upper(input(": "))
            if option == 'A':
                self.attack_action(current_mobs)
            elif option == 'B':
                pass
            elif option == 'C':
                pass
            else:
                print("Invalid option.")

    def attack_action(self, current_mobs):
        while True:
            if not any(mob.current_health > 0 for mob in current_mobs):
                break
            else:
                print("Select which mob to attack:")
                for i, mob in enumerate(current_mobs, start=1):
                    print(f"{i}. Attack {mob.name}")

                option = input(": ")
                if option.isdigit():
                    option = int(option)
                    if 1 <= option <= len(current_mobs):
                        selected_mob: Mob = current_mobs[option - 1]
                        selected_mob.is_target_mob = True
                        # Assuming character is defined elsewhere
                        print(self.player.attack(current_mobs))
                        print(selected_mob.get_info())
                        selected_mob.is_target_mob = False
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid input. Please enter a number.")

def initialize_player_and_inventory(player, inventory):
    database.create_player(player)
    database.create_inventory(inventory)

def menu():
    #ui for menu
    print("-=Iniw Game=-".center(160))
    print("1.New Game".center(160))
    print("2.Continue".center(160))
    while True:
        option = input("Enter Choice:")
        if option == '1':
            while True:
                player_name = input("Player Name: ")
                if player_name.isalpha():
                    player =
                    play(Player(
                        id=1,
                        name=player,
                        level=1,
                        current_health=100,
                        damage=10,
                        inventory_id=1,
                        equipped_item=stick.id,
                        gold_balance=300
                    ))
                else:
                    print("Player Name Must Be Alphabetical".center(160))
        elif option == '2':
            Game()
        else:
            print("Invalid Choice".center(160))


def play(player):
    #ui for what the player want to choose after every battle
    print("1. Dungeon".center(160))
    print("2. Shop".center(160))
    while True:
        option = input("Enter Choice")
        if option == '1':
            game_actions()
        elif option == '2':
            shop = Shop(player)
        else:
            print("Invalid Choice".center(160))


def game_actions():
    #ui in game actions
    print("1. Attack")
    print("2. Inventory")
    print("3. Show Player info")
    while True:
        option = input("Enter Choice: ")
        if option == '1':
            game_attack_actions()
        elif option == '2':
            game_attack_actions()
        elif option == '3':
            game_attack_actions()
        else:
            print("Invalid Choice".center(160))


def game_attack_actions():
    print("1. Basic Attack".center(160))
    print("2. Skill Attack".center(160))
    print("3. Ultimate Attack".center(160))
    while True:
        option = input("Enter Choice: ")
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
