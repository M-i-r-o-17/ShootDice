from random import randint
from time import sleep
from basic import Basic


class Player:
    """Базовый класс, реализующий основные механики игры"""

    def __init__(self, name):

        self.name = name

        self.zone = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.random_number = 0
        self.curret_number = 0

        self.select = False
        self.is_top_zone = False
        self.debug = False

    @property
    def one(self) -> int:
        """Кость первой ячейки"""
        return self.zone[0][0]  # 1

    @property
    def two(self) -> int:
        """Кость второй ячейки"""
        return self.zone[0][1]  # 2

    @property
    def three(self) -> int:
        """Кость третей ячейки"""
        return self.zone[0][2]  # 3

    @property
    def four(self) -> int:
        """Кость четвертой ячейки"""
        return self.zone[1][0]  # 4

    @property
    def five(self) -> int:
        """Кость пятой ячейки"""
        return self.zone[1][1]  # 5

    @property
    def six(self) -> int:
        """Кость шестой ячейки"""
        return self.zone[2][2]  # 6

    @property
    def seven(self) -> int:
        """Кость седьмой ячейки"""
        return self.zone[2][0]  # 7

    @property
    def eight(self) -> int:
        """Кость восьмой ячейки"""
        return self.zone[2][1]  # 8

    @property
    def nine(self) -> int:
        """Кость девятой ячейки"""
        return self.zone[2][2]  # 9

    @property
    def random(self) -> int:
        """Случайное число от 1 до 6"""
        return randint(1, 6)  # Случайное число (1-6)

    @property
    def is_end(self) -> bool:
        """Переменная проверяющая заполненость поля

        Returns:
            bool: True - Поле заполнено False - Поле не заполнено
        """
        answer = True

        for row in self.zone:
            if 0 in row:
                answer = False

        return answer

    @property
    def score(self) -> int:
        """Переменная отслеживающая текущий результат поля

        Returns:
            int: Значение всех костей
        """
        score: int = 0
        for coloum in range(3):
            score += self.score_col(coloum)
        return score

    def score_col(self, coloum: int) -> int:
        """Функция подсчёта конкретной колонуи

        Args:1
            coloum (int): Колонка, чей счёт нужно посчитать

        Returns:
            int: Количесвто очков в колонке
        """

        if self.zone[0][coloum] == self.zone[1][coloum] == self.zone[2][coloum]:
            return self.zone[0][coloum] * 9
        elif (
            self.zone[0][coloum] == self.zone[1][coloum]
            and self.zone[0][coloum] != self.zone[2][coloum]
        ):
            return self.zone[0][coloum] * 4 + self.zone[2][coloum]
        elif (
            self.zone[0][coloum] == self.zone[2][coloum]
            and self.zone[0][coloum] != self.zone[1][coloum]
        ):
            return self.zone[0][coloum] * 4 + self.zone[1][coloum]
        elif (
            self.zone[2][coloum] == self.zone[1][coloum]
            and self.zone[2][coloum] != self.zone[0][coloum]
        ):
            return self.zone[2][coloum] * 4 + self.zone[0][coloum]
        else:
            return self.zone[0][coloum] + self.zone[1][coloum] + self.zone[2][coloum]

    def check_and_remove(self, value: int, coloum: int) -> None:
        """Функция для проверки в столбце похожих костей

        Args:
            value (int): Значение кости
            coloum (int): Столбец
        """
        for row in range(3):
            if self.zone[row][coloum] == value:
                self.zone[row][coloum] = 0

        self.normolized(coloum)

        return None

    def check_correct(self, coloum: int) -> bool:
        """Функция для проверки корректности отображения

        Args:
            coloum (int): Столбец, который проверяем

        Returns:
            False: Если всё расположенно в парвельной последовательности. Сортировка не требуется
            True:  Если порядок нарушен. Требуется сортировка
        """
        if self.is_top_zone:
            if (
                self.zone[0][coloum] == 0
                and self.zone[1][coloum] == 0
                and self.zone[2][coloum] == 0
            ):
                return False
            elif (
                self.zone[0][coloum] == 0
                and self.zone[1][coloum] == 0
                and self.zone[2][coloum] > 0
            ):
                return False
            elif (
                self.zone[0][coloum] == 0
                and self.zone[1][coloum] > 0
                and self.zone[2][coloum] > 0
            ):
                return False
            elif (
                self.zone[0][coloum] > 0
                and self.zone[1][coloum] > 0
                and self.zone[2][coloum] > 0
            ):
                return False
            else:
                return True
        else:
            if (
                self.zone[0][coloum] == 0
                and self.zone[1][coloum] == 0
                and self.zone[2][coloum] == 0
            ):
                return False
            elif (
                self.zone[0][coloum] > 0
                and self.zone[1][coloum] == 0
                and self.zone[2][coloum] == 0
            ):
                return False
            elif (
                self.zone[0][coloum] > 0
                and self.zone[1][coloum] > 0
                and self.zone[2][coloum] == 0
            ):
                return False
            elif (
                self.zone[0][coloum] > 0
                and self.zone[1][coloum] > 0
                and self.zone[2][coloum] > 0
            ):
                return False
            else:
                return True

    def normolized(self, coloum: int) -> None:
        """Преводит столбец к нужному виду

        Args:
            coloum (int): столбец
        """
        while self.check_correct(coloum):
            for i in range(3):
                if self.is_top_zone:
                    if i - 1 >= 0 and self.zone[i][coloum] == 0:
                        self.zone[i][coloum] = self.zone[i - 1][coloum]
                        self.zone[i - 1][coloum] = 0
                else:
                    if i + 1 <= 2 and self.zone[i][coloum] == 0:
                        self.zone[i][coloum] = self.zone[i + 1][coloum]
                        self.zone[i + 1][coloum] = 0

        return None

    def display(self) -> None:
        """Функция отбражения информации о классе в терминале"""
        print("*" * 48)
        print(
            f"* [ {self.one}  ][ {self.two}  ][ {self.three}  ] * Nick: {self.name[0:15]} "
            + " " * (16 - len(self.name))
            + " *"
        )
        print(
            f"* [ {self.four}  ][ {self.five}  ][ {self.six}  ] * "
            + f"Curret: {self.curret_number}"
            + " " * 15
            + "*"
        )
        print(
            f"* [ {self.seven}  ][ {self.eight}  ][ {self.nine}  ] * "
            + f"Your step: {self.select}"
            + " " * 8
            + "*"
        )
        print("* " + "|" * 44 + " *")
        print("* ", end="")
        for i in range(3):
            value = self.score_col(i)
            if value < 10:
                print(f"[ {value}  ]", end="")
            else:
                print(f"[ {value} ]", end="")
        print(
            " * "
            + f"Score: {self.score} "
            + " " * (24 - len(f"Score: {self.score} "))
            + "*"
        )
        print("*" * 48)

        return None

    def add(self, coloum: int) -> bool:
        """Функция для добовления новой кости

        Args:
            coloum (int): Колонка в которую нужно добавить

        Returns:
            True: Если получилось добавить кость
            False: Если нет свободного места под кость
        """

        for i in range(3):

            if self.zone[i][coloum] == 0:

                self.zone[i][coloum] = self.curret_number

                return True

        return False

    def step(self, enemy) -> None:
        """Функция выполнения хода

        Args:
            enemy (Player): Второй игрок
        """

        while_step = 500

        while while_step >= 0:

            while_step -= 1

            if while_step == 0:
                print("[Error 0] Закончились попытки ввода")
                return None

            try:
                num = int(input("Выберите колоннку(1,2,3): "))
            except ValueError:
                print("[Error 1] Я не знаю что это!")
                num = 9

            if not (num == 1 or num == 2 or num == 3):
                continue

            num = num - 1

            if self.add(num):
                enemy.check_and_remove(self.curret_number, num)
                break

        self.select = False
        enemy.select = True

        return None
