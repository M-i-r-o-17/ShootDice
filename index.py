import os
from time import sleep
from player import Player
from random import randint

gameLoop = True
gameSelect = 0

def Clear():
    if os.name == "nt": os.system("cls")
    else: os.system("clear")

def MainMenu(message = False):

    Clear()

    if message:
        print("**************************")
        print("* Error: Такого меню нет *")

    print("**************************")
    print("* [1] Игра против бота   *")
    print("* [2] Игра против игрока *")
    print("* [3] Выход              *")
    print("**************************")

def Print(t1:Player, t2:Player):
    Clear()
    t1.Print()
    t2.Print()
    

def PVE():
    nick = ["Enemy", "Bot", "Your mom", "Pro", "Pro100 Bot"]
    bot = Player(nick[randint(0, len(nick) - 1)])
    player = Player(input("Введите ник: "))

    monet = randint(1,2)
    game = True
    if monet == 1: player.select = True
        
    while game:

        if bot.isEnd or player.isEnd:
            game = False
            continue

        bot.select = not(player.select)

        if player.select:
            
            player.randomNumber = player.random
            bot.randomNumber = ""

            Print(bot, player)

            while True:
                try:
                    num = int(input("Выберите колоннку(1,2,3): "))
                except:
                    print("* Error: Я не знаю что это! *")
                    num = 9

                if not(num == 1 or num == 2 or num == 3): continue
                num = num - 1
                if player.AddNumber(num):
                    bot.CheckAndRemove(player.randomNumber, num )
                    
                    break
            Print(bot, player)
            player.select = False
        else:

            player.randomNumber = ""
            bot.randomNumber = bot.random

            while True:
                num = randint(0,2)
                if bot.AddNumber(num): 
                    player.CheckAndRemove(bot.randomNumber,num)
                    break
            Print(bot, player)
            player.select = True

        Print(bot, player)
        sleep(1)

    for timer in range(5,0,-1):
        Print(bot, player)
        print("Игра окончена! Выйграл: ", end='')

        if player.score > bot.score: print(player.name)
        else: print(bot.name)

        print(f"Выход через: {timer}...")

        sleep(1)

def PVP():
    bot = Player(input("Введите ник первого игрока: "))
    player = Player(input("Введите ник второго игрока: "))

    monet = randint(1,2)
    game = True
    if monet == 1: player.select = True
        
    while game:

        if bot.isEnd or player.isEnd:
            game = False
            continue

        bot.select = not(player.select)

        if player.select:
            
            player.randomNumber = player.random
            bot.randomNumber = ""

            Print(bot, player)

            while True:
                try:
                    num = int(input("Выберите колоннку(1,2,3): "))
                except:
                    print("* Error: Я не знаю что это! *")
                    num = 9

                if not(num == 1 or num == 2 or num == 3): continue
                num = num - 1
                if player.AddNumber(num):
                    bot.CheckAndRemove(player.randomNumber, num )
                    
                    break
            Print(bot, player)
            player.select = False
        else:

            player.randomNumber = ""
            bot.randomNumber = bot.random

            while True:
                try:
                    num = int(input("Выберите колоннку(1,2,3): "))
                except:
                    print("* Error: Я не знаю что это! *")
                    num = 9

                if not(num == 1 or num == 2 or num == 3): continue
                num = num - 1
                if bot.AddNumber(num):
                    player.CheckAndRemove(player.randomNumber, num )
                    break
            Print(bot, player)
            player.select = True

        Print(bot, player)
        sleep(1)

    for timer in range(5,0,-1):
        Print(bot, player)
        print("Игра окончена! Выйграл: ", end='')

        if player.score > bot.score: print(player.name)
        else: print(bot.name)

        print(f"Выход через: {timer}...")

        sleep(1)

while gameLoop:

    if gameSelect == 1:
        PVE()
        gameSelect = 0
    elif gameSelect == 2:
        PVP()
        gameSelect = 0
    elif gameSelect == 3:
        gameLoop = False
        gameSelect = 0
    else:
        MainMenu(not(gameSelect == 0))
        gameSelect = int(input("* Ваш выбор: "))


