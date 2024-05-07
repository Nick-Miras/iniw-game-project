import random
from datum.entity import Mob, Entity


class Game:
    def __init__(self):
        # Define the mobs
        self.mob1 = Mob(name="Goblin", damage=10, maximum_health=50, level=1)
        self.mob2 = Mob(name="Orc", damage=15, maximum_health=70, level=1)
        self.mob3 = Mob(name="Ogre", damage=15, maximum_health=150, level=1)
        self.mob4 = Mob(name="slime", damage=5, maximum_health=50, level=1)
        self.mobs: list[Mob] = [self.mob1, self.mob2, self.mob3, self.mob4]

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
                        print(character.attack(current_mobs))
                        print(selected_mob.get_info())
                        break
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid input. Please enter a number.")


player_name = input("Enter Character Name: ")
while True:
    character = player_name
    if character.isalpha():
        character = Entity(name=f"{character}", damage=10, maximum_health=100, level=1)
        game = Game()
        game.start()
    else:
        print("Invalid")
