from Engine.GameObject import GameObject
from player import Player

class PlayerGUI(Player):

    def __init__(self, name):
        Player.__init__(self, name)

        self.dices = [
            [ GameObject(0,0,64,64), GameObject(0,0,64,64), GameObject(0,0,64,64) ],
            [ GameObject(0,0,64,64), GameObject(0,0,64,64), GameObject(0,0,64,64) ],
            [ GameObject(0,0,64,64), GameObject(0,0,64,64), GameObject(0,0,64,64) ],
        ]

p1 = PlayerGUI("sd")
for a in p1.dicesImages:
    print(a.name)