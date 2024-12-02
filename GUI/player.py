from random import randint

from time import sleep

class Player():

    def __init__(self, name):

        self.name = name                            # Ник игрока
        self.zone =  [[0,0,0], [0,0,0], [0,0,0]]    # Игровое поле
        self.randomNumber = 0                       # Последнее случайное число
        self.select = False
        self.debug = True

    @property
    def one(self):      return self.zone[0][0]      # 1
    @property
    def two(self):      return self.zone[0][1]      # 2
    @property
    def three(self):    return self.zone[0][2]      # 3
    @property
    def four(self):     return self.zone[1][0]      # 4
    @property
    def five(self):     return self.zone[1][1]      # 5
    @property
    def six(self):      return self.zone[2][2]      # 6
    @property
    def seven(self):    return self.zone[2][0]      # 7
    @property
    def eight(self):    return self.zone[2][1]      # 8
    @property
    def nine(self):     return self.zone[2][2]      # 9
    @property
    def random(self):   return randint(1,6)         # Случайное число на кости
    
    @property
    def isEnd(self):                                # Заполнено ли поле

        for row in self.zone:
            for num in row:
                if num == 0: return False

        return True
    
    @property
    def score(self):                                # Общий рекорд игрока
        score = 0

        for i in range(3): score += self.ScoreCol(i)

        return score

    def CheckAndRemove(self, value:int, col:int):  # Проверяем и удаляем одинаковые числа из столбца

        for i in range(3):
            if self.zone[i][col] == value: self.zone[i][col] = 0

        self.Normolized(col)

    def CheckCorrect(self, col:int):                # Проверяем последовательность в столбце

        if self.zone[0][col] == 0 and self.zone[1][col] == 0 and self.zone[2][col] == 0: return False
        elif self.zone[0][col] > 0 and self.zone[1][col] == 0 and self.zone[2][col] == 0: return False
        elif self.zone[0][col] > 0 and self.zone[1][col] > 0 and self.zone[2][col] == 0: return False
        elif self.zone[0][col] > 0 and self.zone[1][col] > 0 and self.zone[2][col] > 0: return False
        else: return True

    def Normolized(self, col:int):                  # Преводим столбец к нужной форме

        while self.CheckCorrect(col):
            for i in range(3):
                if i + 1 <= 2 and self.zone[i][col] == 0:
                    self.zone[i][col] = self.zone[i+1][col] 
                    self.zone[i+1][col] = 0

    def ScoreCol(self, col:int):                    # Вычесляем счётчик столбца

        if self.zone[0][col] == self.zone[1][col] and self.zone[1][col] == self.zone[2][col]: return (self.zone[0][col] + self.zone[1][col] + self.zone[1][col]) * 3

        if self.zone[0][col] == self.zone[1][col] and not(self.zone[1][col] == self.zone[2][col]): return (self.zone[0][col] + self.zone[1][col]) * 2 + self.zone[2][col]
        if self.zone[0][col] == self.zone[2][col] and not(self.zone[1][col] == self.zone[2][col]): return (self.zone[0][col] + self.zone[2][col]) * 2 + self.zone[1][col]

        if self.zone[1][col] == self.zone[2][col] and not(self.zone[0][col] == self.zone[1][col]): return (self.zone[1][col] + self.zone[2][col]) * 2 + self.zone[0][col]
        return self.zone[0][col] + self.zone[1][col] + self.zone[2][col]
    
    def Print(self):                                # Выводим данные игрока на экран
        print("*" * 48)
        print(f"* [ {self.one}  ][ {self.two}  ][ {self.three}  ] * Nick: {self.name[0:15]} " + " " * (16 - len(self.name)) +" *")
        print(f"* [ {self.four}  ][ {self.five}  ][ {self.six}  ] * "  + f"Curret: {self.randomNumber}" + " " * 15 +"*" )
        print(f"* [ {self.seven}  ][ {self.eight}  ][ {self.nine}  ] * " +f"Your step: {self.select}"+ " " * 8 +"*") 
        print("* " + "|" * 44 + " *")
        print(f"* ",end='')
        for i in range(3):
            value = self.ScoreCol(i)
            if(value < 10): print(f"[ {value}  ]",end='')
            else: print(f"[ {value} ]", end='')
        print(' * ' + f"Score: {self.score} " + " " * (24 -len(f"Score: {self.score} ")) + "*")
        print("*" * 48)

    def AddNumber(self, col:int):                   # Добовляем число на поле

        for i in range(3):

            if self.zone[i][col] == 0:

                self.zone[i][col] = self.randomNumber

                return True

        return False