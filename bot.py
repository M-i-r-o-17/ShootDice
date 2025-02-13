from basic import Basic

from player import Player


class Bot(Player):
    """Класс реализующий бота для игры"""

    __niknames = ["Enemy", "Bot", "Your mom", "Pro", "Pro100 Bot"]

    __difficulty = ["Easy", "Medium", "Hard"]

    def __init__(self, difficulty=2, name=""):

        Player.__init__(
            self,
            (
                name
                if name != ""
                else self.__niknames[Basic.randint(0, len(self.__niknames) - 1)]
            ),
        )

        self.difficulty = self.__difficulty[difficulty]

    def __easy(self, enemy: Player) -> None:

        while True:

            num = Basic.randint(0, 2)

            if self.add(num):

                enemy.check_and_remove(self.curret_number, num)

                break

        return None

    def __medium(self, enemy) -> None:

        step_random = Basic.randint(1, 10)

        if step_random <= 4:

            self.__easy(enemy)
        else:

            self.__hard(enemy)

    def __hard(self, enemy: Player) -> None:

        # Стратегия 1: Ищим лучший столбец врага и рушим его по возможности
        best_col_enemy = -1

        if self.__find_number(enemy.zone) > 0:

            best = 0

            for col in range(3):

                if best < enemy.score_col(col):

                    best = enemy.score_col(col)

                    best_col_enemy = col

        if best_col_enemy > -1:

            coloum = self.__find_free_row(best_col_enemy)

            if coloum > -1:

                self.add(best_col_enemy)

                enemy.check_and_remove(self.curret_number, best_col_enemy)

                return None

        # Стартегия 2: Ищими идеальный шаг для нас

        row = -1
        col = -1

        count = self.__find_number()

        exploce_col = []

        while count > 0:

            if row == -1:

                col = self.__find_number_col(exception=exploce_col)

                if col != -1:

                    row = self.__find_free_row(col)

                    if row == -1:

                        exploce_col.append(col)

            count -= 1

        # Стартегия 3: Рандом)
        if col == -1:
            self.__easy(enemy)
            return None

        self.add(col)
        enemy.check_and_remove(self.curret_number, col)

        return None

    def __find_number(self, zone=None) -> int:
        """Функция для поиска числа на игровом поле


        Args:

            zone : Матрица игрового поля


        Returns:

            int : Количество искомых элементов на поле
        """

        count = 0

        zone = self.zone if zone is None else zone

        for row in range(3):

            for col in range(3):

                if self.curret_number == zone[row][col]:

                    count += 1

        return count

    def __find_number_col(self, zone=None, exception=[]) -> int:
        """Функция для нахождения столбца с число


        Args:

            exception : столбцы которые не нужно проверять. Defaults to []


        Returns:

            -1 (int): Нет столбцов, не входящих в исключение, с данным числом

            int (int): Номер столбца
        """

        if len(exception) >= 3:

            return -1

        zone = self.zone if zone is None else zone

        for row in range(3):

            for col in range(3):

                if col in exception:
                    continue
                else:

                    if zone[row][col] == self.curret_number:
                        return col

        return -1

    def __find_free_row(self, coloum) -> int:

        for row in range(3):

            if self.zone[row][coloum] == 0:

                return row

        return -1

    def __new_coloum_score(self, coloum) -> int:

        new_score_col = 0

        if self.zone[1][coloum] != self.zone[2][coloum]:
            if self.zone[1][coloum] == 0:
                new_score_col = self.curret_number * 4
            else:
                new_score_col = self.curret_number * 4 + (
                    self.zone[2][coloum]
                    if self.curret_number == self.zone[1][coloum]
                    else self.zone[1][coloum]
                )
        else:
            new_score_col = self.curret_number * 9

        return new_score_col

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
