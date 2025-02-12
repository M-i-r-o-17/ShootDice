import os
from time import sleep
from player import Player
from bot import Bot
from basic import Basic


def player_vs_bot() -> None:
    """Функция запускающая игру против бота"""

    player1 = Player(input("Введите ник игрока: "))
    bot = Bot()

    return game(bot, player1)


def player_vs_player() -> None:
    """Функция запускающая игру для 2х игроков"""

    player1 = Player(input("Введите ник игрока: "))
    player2 = Player(input("Введите ник игрока: "))

    return game(player1, player2)


def game(p1: Player, p2: Player) -> None:
    """Основная функция игры

    Args:
        p1 (Player): Первый игрок
        p2 (Player): Второй игрок
    """
    who_first = Basic.randint(1, 2)

    if who_first == 1:
        p1.select = True
        p2.select = False

    p1.is_top_zone = True
    p2.is_top_zone = False

    while not p1.is_end and not p2.is_end:

        p1.curret_number = p1.random if p1.select else ""
        p2.curret_number = p2.random if p2.select else ""

        Basic.clear_console()
        p1.display()
        p2.display()

        if p1.select:
            p1.step(p2)
        else:
            p2.step(p1)

        sleep(1)

    for timer in range(5, 0, -1):
        Basic.clear_console()
        p1.display()
        p2.display()

        if p1.score > p2.score:
            print(p1.name)
        else:
            print(p2.name)

        print(f"Выход через: {timer}...")

        sleep(1)


if __name__ == "__main__":
    GAME_LOOP = True
    MAIN_MENU_SELECT = 0
    ERRORS = []

    while GAME_LOOP:

        if MAIN_MENU_SELECT == 1:
            player_vs_bot()
            MAIN_MENU_SELECT = 0
        elif MAIN_MENU_SELECT == 2:
            player_vs_player()
            MAIN_MENU_SELECT = 0
        elif MAIN_MENU_SELECT == 3:
            GAME_LOOP = False
            continue
        else:
            ERRORS.append("[Error 2] Нет такого пункта меню")

        Basic.clear_console()

        for error in ERRORS:
            print("**************************")
            print(error)

        print("**************************")
        print("* [1] Игра против бота   *")
        print("* [2] Игра против игрока *")
        print("* [3] Выход              *")
        print("**************************")

        MAIN_MENU_SELECT = Basic.int_input("* Ваш выбор:")
