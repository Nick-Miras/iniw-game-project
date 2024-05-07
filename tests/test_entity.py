from datum.entity import Entity


player = Entity(name='iniw', damage=10, maximum_health=100, level=0)
print(player)
player.level_up(1000)
print(player)
