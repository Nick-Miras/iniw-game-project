"""
INIW GAME
"""
from datum.entity import Player
from datum.items import short_sword
from mediators.game import Game

player_name = input("Enter Character Name: ")
while True:
    if player_name.isalpha():
        player = Player(
            name=player_name,
            level=1,
            inventory_id=1,
            gold_balance=300,
            equipped_items=[short_sword.id]
        )
        game = Game(player)
        game.start()
    else:
        print("Invalid")
