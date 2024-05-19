import random

import database
from custom_types import ID
from datum.entity import Mob, Player
from datum.enumerations import AttackType
from datum.inventory import Inventory, InventoryItemProperties
from datum.items import stick
from mediators.shop import Shop, shop_inventory_1
from mediators import actions


class Game:
    def __init__(self, new_game: bool):
        if new_game:
            try:
                old_player = database.get_player(1)
            except ValueError:  # if player doesn't exist
                print("Player Does Not Exist Yet... Creating New Player.")
            else:
                database.delete_player(old_player.id)
                database.delete_inventory(old_player.inventory_id)

            self.player = create_new_player()
            initialize_player(self.player)
            initialize_inventory(self.player.inventory_id)
        else:
            try:
                self.player = database.get_player(1)
            except ValueError:
                print("No existing player found. Starting a new game.")
                self.player = create_new_player()
                initialize_player(self.player)
                initialize_inventory(self.player.inventory_id)

        self.player.ultimate_points = 0
        self.player.skill_points = 3

        # Define the mobs
        self.mobs: list[Mob] = [
            Mob(id=1,name="Goblin", damage=10, maximum_health=100, level=random.randint(1, 10)),
            Mob(id=2,name="Orc", damage=15, maximum_health=170, level=random.randint(1, 10)),
            Mob(id=3,name="Ogre", damage=15, maximum_health=250, level=random.randint(1, 10)),
            Mob(id=4,name="slime", damage=5, maximum_health=70, level=random.randint(1, 10))
        ]
        self.play()

    def randomize_enemies(self):

        # Determine the number of enemies based on probabilities
        num_enemies = random.choices([1, 2, 3], weights=[30, 60, 10])[0]

        # Randomly select mobs from the list
        current_mobs = random.sample(self.mobs, num_enemies)

        return num_enemies, current_mobs

    def current_battle_enemies(self):
        num_enemies, current_mobs = self.randomize_enemies()

        print("Number of enemies:", num_enemies)
        print(f"Encounter mobs:", [f"{mob.name} level {mob.level}" for mob in current_mobs])

        return num_enemies, current_mobs

    def start(self, attack_type, num_enemies, current_mobs):

        print("Number of enemies:", num_enemies)
        print("Current mobs:", [f"{mob.name} level {mob.level}" for mob in current_mobs])

        # Perform actions
        self.attack_action(current_mobs, attack_type)

    def attack_action(self, current_mobs, attack_type):
            if all(mob.current_health == 0 for mob in current_mobs) is False:
                for mob in current_mobs:
                    if mob.current_health == 0:
                        self.player.level_up(mob.level)

                print("Select which mob to attack:")
                for i, mob in enumerate(current_mobs, start=1):
                    print(f"{i}. Attack {mob.name}")

                option = input(": ")
                if option.isdigit():
                    option = int(option)
                    if 1 <= option <= len(current_mobs):
                        selected_mob: Mob = current_mobs[option - 1]
                        if selected_mob.current_health != 0:
                            selected_mob.is_target_mob = True
                            # Assuming character is defined elsewhere
                            print(self.player.attack(current_mobs, attack_type))
                            print(selected_mob.get_info())
                            selected_mob.is_target_mob = False
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid input. Please enter a number.")

            if all(mob.current_health == 0 for mob in current_mobs) is True:
                print("Mobs are dead.")
                database.update_player(self.player)
                self.play()

    def play(self):
        # ui for what the player want to choose after every battle
        while True:
            try:
                print("1. Dungeon".center(160))
                print("2. Shop".center(160))
                option = input("Enter Choice: ")
                if option == '1':
                    self.game_actions()
                elif option == '2':
                    shop_inventory_1.display_information_of_items()
                    shop = Shop(self.player, shop_inventory_1)
                    print("Pls. Enter The Item Id You Want To Buy")
                    choice = int(input("Buy Item: "))
                    amount = int(input("Amount: "))
                    shop.buy(choice, amount)
                else:
                    print("Invalid Choice".center(160))
            except ValueError as err:
                print(err)

    def game_actions(self):
        # ui in game actions
        while True:
            try:
                print("1. Enter Battle".center(160))
                print("2. Inventory".center(160))
                print("3. Show Player info".center(160))
                option = input("Enter Choice: ")
                if option == '1':
                    self.game_attack_actions()
                elif option == '2':
                    inventory = database.get_inventory(self.player.inventory_id)
                    inventory.display_information_of_items()
                    print("Pls. Enter The Item Id You Want To Use")
                    choice = int(input("Use Item:"))
                    self.player.use_item(item_id=choice)
                elif option == '3':
                    print(self.player.get_info())

                else:
                    print("Invalid Choice".center(160))
            except ValueError as err:
                print(err)

    def game_attack_actions(self):
        num_enemies, enemies = self.current_battle_enemies()
        while True:
            try:
                print(self.player.current_info())
                print("1. Basic Attack".center(160))
                print("2. Skill Attack".center(160))
                print("3. Ultimate Attack".center(160))
                option = input("Enter Choice: ")
                if option == '1':
                    self.start(attack_type=AttackType.BasicAttack, num_enemies=num_enemies, current_mobs=enemies)
                elif option == '2':
                    self.start(attack_type=AttackType.SkillAttack, num_enemies=num_enemies, current_mobs=enemies)
                elif option == '3':
                    self.start(attack_type=AttackType.UltimateAttack, num_enemies=num_enemies, current_mobs=enemies)
            except ValueError as err:
                print(err)

def initialize_player(player):
    database.create_player(player)

def initialize_inventory(inventory_id: ID):
    database.create_inventory(Inventory(id=inventory_id, items=[InventoryItemProperties(id=2, amount=1)]))

def create_new_player():
    while True:
        player_name = input("Player Name:")
        if player_name.isalpha():
            return Player(
                id=1,
                name=player_name,
                level=1,
                maximum_health=100,
                damage=10,
                inventory_id=1,
                equipped_item=stick.id,
                gold_balance=9999300
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

