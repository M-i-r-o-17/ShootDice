from Engine.GameObject  import GameObject
from Engine.Sprite      import Sprite
from Engine.Basic       import *
from Engine.UI.Text     import Text

from player import Player

class PlayerGUI(Player):

    def __init__(self, name, zonePosition:Vector2):

        Player.__init__(self, name)

        self.basic = Basic()
        self.position =  zonePosition
        self.coloum = -1
        self.basicDices = [
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64)
        ]

        self.bigDices = [
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64),
            GameObject(0,0,64,64)
        ]


        for i in range(1,7):
            self.basicDices[i - 1].sprite = Sprite(f"img/{i}.png", Vector2(32,32), Vector2(16,16))
            self.bigDices[i - 1].sprite = Sprite(f"img/{i}.png", Vector2(140,140), Vector2(25,25))

        self.dices = [
            [ GameObject(self.position.x, self.position.y), GameObject(self.position.x + 69, self.position.y), GameObject(self.position.x + 138, self.position.y) ],
            [ GameObject(self.position.x, self.position.y + 69), GameObject(self.position.x + 69, self.position.y + 69), GameObject(self.position.x + 138, self.position.y + 69) ],
            [ GameObject(self.position.x, self.position.y + 138), GameObject(self.position.x + 69, self.position.y + 138), GameObject(self.position.x + 138, self.position.y + 138) ],
        ]

        self.scores = [
            Text("", (255,255,255), Vector2(0,0)),
            Text("", (255,255,255), Vector2(0,0)),
            Text("", (255,255,255), Vector2(0,0)),
        ]

        self.curretDice = GameObject(5,5, 190, 190)
        self.curretDice.color = (30, 30, 30)

        self.nickLabel = Text(name, (255,255,255), Vector2(5,5), None, size=55)
        self.scoreLabel = Text("Score", (255,255,255), Vector2(5,5), None, size=35)

    def getDice(self, number, isBig = False):
        if 1 <= number <= 6:
            if isBig: return self.bigDices[number - 1].sprite
            else:     return self.basicDices[number - 1].sprite
        else:
            return None
    
        
    def DisplayZone(self, surface):

        for row in range(3):

            for col in range(3):
                
                self.dices[row][col].sprite = self.getDice(self.zone[row][col])
                self.dices[row][col].color = (255,255,255)
                self.dices[row][col].Draw(surface)

            self.scores[row].text = self.ScoreCol(row)

            self.scores[row].position = Vector2(
                self.dices[2][row].position.x + (69 - self.scores[row].width) // 2,
                self.dices[2][row].position.y + 69
                )

            self.scores[row].Draw(surface)

        self.curretDice.sprite = self.getDice(self.randomNumber, True) 
        self.curretDice.Draw(surface)

        self.nickLabel.Draw(surface)
        self.scoreLabel.Draw(surface)

    def AddNumber(self, col):
        answer = super().AddNumber(col)
        return answer