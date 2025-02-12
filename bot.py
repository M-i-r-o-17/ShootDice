from player import Player
from basic import Basic
from random import randint


class Bot(Player):
    """Класс реализующий бота для игры"""

    __niknames = ["Enemy", "Bot", "Your mom", "Pro", "Pro100 Bot"]
    __difficulty = ["Easy", "Medium", "Hard"]

    def __init__(self, difficulty=0, name=""):

        Player.__init__(
            self,
            (
                name
                if name != ""
                else self.__niknames[randint(0, len(self.__niknames) - 1)]
            ),
        )

        self.difficulty = self.__difficulty[difficulty]

    def __easy(self, enemy):
        pass

    def __medium(self, enemy):
        pass

    def __hard(self, enemy):
        pass

    def step(self, enemy):

        self.curret_number = self.random_number
        enemy.curret_number = ""

        Basic.clear_console()

        enemy.display()
        self.display()

        if self.difficulty == "Easy":
            self.__easy(enemy)
        elif self.difficulty == "Medium":
            self.__medium(enemy)
        elif self.difficulty == "Hard":
            self.__hard(enemy)

        self.select = False
        enemy.select = True

        return None
