import random

import database
from datum.entity import Mob, Player
from datum.enumerations import AttackType
from datum.items import stick
from mediators.shop import Shop, shop_inventory_1


class Game:
    def __init__(self, new_game):
        try:
            old_player = database.get_player(1)
        except ValueError:  # if player doesn't exist
            print("Player Does Not Exist Yet... Creating New Player.")
        else:
            database.delete_player(old_player.id)
            database.delete_inventory(old_player.inventory_id)
            if new_game is False:
                self.player = old_player
        finally:
            if new_game is True:
                self.player = create_new_player()
                database.create_player(self.player)

        # Define the mobs
        self.mobs: list[Mob] = [
            Mob(id=1,name="Goblin", damage=10, maximum_health=100, level=random.randint(1, 10)),
            Mob(id=2,name="Orc", damage=15, maximum_health=170, level=random.randint(1, 10)),
            Mob(id=3,name="Ogre", damage=15, maximum_health=250, level=random.randint(1, 10)),
            Mob(id=4,name="slime", damage=5, maximum_health=70, level=random.randint(1, 10))
        ]
        self.play()

    def start(self, attack_type):
        # Determine the number of enemies based on probabilities
        num_enemies = random.choices([1, 2, 3], weights=[30, 60, 10])[0]

        # Randomly select mobs from the list
        current_mobs = random.sample(self.mobs, num_enemies)

        print("Number of enemies:", num_enemies)
        print("Current mobs:", [mob.name for mob in current_mobs])

        # Perform actions
        self.attack_action(current_mobs, attack_type)

    def attack_action(self, current_mobs, attack_type):
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
                        print(self.player.attack(current_mobs, attack_type))
                        print(selected_mob.get_info())
                        selected_mob.is_target_mob = False
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid input. Please enter a number.")
    def play(self):
        # ui for what the player want to choose after every battle
        print("1. Dungeon".center(160))
        print("2. Shop".center(160))
        while True:
            option = input("Enter Choice: ")
            if option == '1':
                self.game_actions()
            elif option == '2':
                shop_inventory_1.display_information_of_items()
            else:
                print("Invalid Choice".center(160))

    def game_actions(self):
        # ui in game actions
        print("1. Attack")
        print("2. Inventory")
        print("3. Show Player info")
        while True:
            option = input("Enter Choice: ")
            if option == '1':
                self.game_attack_actions()
            elif option == '2':
                inventory = database.get_inventory(self.player.inventory_id)
                inventory.display_information_of_items()
            elif option == '3':
                self.player.get_info()
            else:
                print("Invalid Choice".center(160))

    def game_attack_actions(self):
        print("1. Basic Attack".center(160))
        print("2. Skill Attack".center(160))
        print("3. Ultimate Attack".center(160))
        while True:
            option = input("Enter Choice: ")
            if option == '1':
                self.start(attack_type=AttackType.BasicAttack)
            elif option == '2':
                self.start(attack_type=AttackType.SkillAttack)
            elif option == '3':
                self.start(attack_type=AttackType.UltimateAttack)


def initialize_player_and_inventory(player, inventory):
    database.create_player(player)
    database.create_inventory(inventory)

def create_new_player():
    player_name = input("Player Name:")
    if player_name.isalpha():
        return Player(
            id=1,
            name=player_name,
            level=1,
            current_health=100,
            damage=10,
            inventory_id=1,
            equipped_item=stick.id,
            gold_balance=300
        )
    else:
        print("Player Name Must Be Alphabetical".center(160))


def menu():
    #ui for menu
    print("-=Iniw Game=-".center(160))
    print("1.New Game".center(160))
    print("2.Continue".center(160))
    while True:
        option = input("Enter Choice:")
        if option == '1':
            Game(new_game=True)
        elif option == '2':
            Game(new_game=False)
        else:
            print("Invalid Choice".center(160))

