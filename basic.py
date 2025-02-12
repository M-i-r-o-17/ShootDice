import os
import random


class Basic:
    """Базавый класс для работы с консолью"""

    @staticmethod
    def clear_console() -> None:
        """Очищает консоль в разных ОС"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def randint(a: int, b: int) -> int:
        """Реализует функцию randint из класса random

        Args:
            a (int): От какого числа генерировать
            b (int): До какого числа генирировать

        Returns:
            int: Случайное число из диапозона [a,b]
        """
        return random.randint(a, b)

    @staticmethod
    def int_input(
        message: str,
        error_texts: str = "Не правильный формат данных попробуйте ещё раз",
    ) -> int:
        """Реализует стандартный ввод с клавитуры сразу в целое число

        Args:
            message (str): Cообщение для пользователя
            error_texts (str, optional): Сообщение ошибки. Defaults to "Не правильный формат данных попробуйте ещё раз"".

        Returns:
            int: Число от пользователя
        """

        while True:
            try:
                return int(input(message))
            except TypeError:
                print(error_texts)
