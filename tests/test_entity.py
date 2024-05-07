from datum.entity import Entity

def test_entity():
    player = Entity(name='iniw', damage=10, maximum_health=100, level=0)
    print(player)
    player.level_up(10)
    print(player)
