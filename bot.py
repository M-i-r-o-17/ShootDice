from random import randint
from player import Player


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

    def __easy(self, enemy) -> None:

        while True:

            num = randint(0, 2)

            if self.add(num):

                enemy.check_and_remove(self.curret_number, num)

                break

        return None

    def __medium(self, enemy) -> None:

        pass

    def __hard(self, enemy) -> None:

        pass

    def step(self, enemy) -> None:

        if self.difficulty == "Easy":
            self.__easy(enemy)

        elif self.difficulty == "Medium":
            self.__medium(enemy)

        elif self.difficulty == "Hard":

            self.__hard(enemy)

        self.select = False

        enemy.select = True

        return None
