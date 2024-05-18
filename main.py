"""
INIW GAME
"""
import random
from datum.entity import Mob, Entity, Player
from datum.items import small_health_potion, short_sword
from mediators.game import Game

player_name = input("Enter Character Name: ")
while True:
    if player_name.isalpha():
        character = Player(
            name=player_name,
            level=1,
            inventory_id=1,
            gold_balance=300,
            equipped_items=[short_sword.id]
        )
        game = Game(character)
        game.start()
    else:
        print("Invalid")
