import os


class Basic:
    """Базавый класс для работы с консолью"""

    @staticmethod
    def clear_console() -> None:
        """Очищает консоль в разных ОС"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
