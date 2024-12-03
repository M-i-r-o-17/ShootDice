from Engine.GameObject import GameObject
from PlayerGUI import PlayerGUI
from Engine.Basic import Vector2
from SelectColoum import SelectColoum
from Engine.UI.Text import Text
from Engine.UI.Button import Button

import pygame
import sys
from random import randint

BLACK = (0,0,0)
WHITE = (255,255,255)
isDebug = True

pygame.init()
pygame.display.set_caption("Shoot Dice")

screen = pygame.display.set_mode((900, 600))
objects = []
uIElements = []

leftPanel = GameObject(0,0, 200, 600)
middlePanel = GameObject(200,0, 700, 600)
rightPanel = GameObject(700,0, 200, 600)

leftPanel.color = (50,50,50)
middlePanel.color = (30,30,30)
rightPanel.color = (50,50,50)

p1 = PlayerGUI("Miro_17", Vector2(350, 300))
p1.curretDice.position = Vector2(5, 85)
p1.nickLabel.position  = Vector2(5 + (200 - p1.nickLabel.width) // 2, 20)


p2 = PlayerGUI("Enemy", Vector2(350, 32))
p2.curretDice.position = Vector2(705, 85)
p2.nickLabel.position  = Vector2(705 + (200 - p2.nickLabel.width) // 2, 20)

p1.scoreLabel.text = f"Score: {p1.score}"
p1.scoreLabel.position = Vector2(5 + (200 - p1.scoreLabel.width) // 2, 385)
p2.scoreLabel.text = f"Score: {p2.score}"
p2.scoreLabel.position = Vector2(705 + (200 - p2.scoreLabel.width) // 2, 385)



btn1 = SelectColoum("1", 5, 300, 60, 60);   btn1.coloum = 0; btn1.player = p1
btn2 = SelectColoum("2", 70, 300, 60, 60);  btn2.coloum = 1; btn2.player = p1
btn3 = SelectColoum("3", 135, 300, 60, 60); btn3.coloum = 2; btn3.player = p1

delayTimer = 0
delay = 30
gameOver = False

globalPanel = GameObject(0,0,900,600)
globalPanel.color = (30,30,30)
endText = Text("WIN:", (255,255,255), Vector2(0,0), size=75)

def StartGame():
    global p1,p2,btn1,btn2,btn3,leftPanel,middlePanel,rightPanel,objects,uIElements

    leftPanel = GameObject(0,0, 200, 600)
    middlePanel = GameObject(200,0, 700, 600)
    rightPanel = GameObject(700,0, 200, 600)

    leftPanel.color = (50,50,50)
    middlePanel.color = (30,30,30)
    rightPanel.color = (50,50,50)

    p1 = PlayerGUI("M_i_r_o17", Vector2(350, 300))
    p1.curretDice.position = Vector2(5, 85)
    p1.nickLabel.position  = Vector2(5 + (200 - p1.nickLabel.width) // 2, 20)


    p2 = PlayerGUI("Enemy", Vector2(350, 32))
    p2.curretDice.position = Vector2(705, 85)
    p2.nickLabel.position  = Vector2(705 + (200 - p2.nickLabel.width) // 2, 20)

    p1.scoreLabel.text = f"Score: {p1.score}"
    p1.scoreLabel.position = Vector2(5 + (200 - p1.scoreLabel.width) // 2, 385)
    p2.scoreLabel.text = f"Score: {p2.score}"
    p2.scoreLabel.position = Vector2(705 + (200 - p2.scoreLabel.width) // 2, 385)

    btn1 = SelectColoum("1", 5, 300, 60, 60);   btn1.coloum = 0; btn1.player = p1
    btn2 = SelectColoum("2", 70, 300, 60, 60);  btn2.coloum = 1; btn2.player = p1
    btn3 = SelectColoum("3", 135, 300, 60, 60); btn3.coloum = 2; btn3.player = p1

    monet = randint(1,2)
    if monet == 1: p1.select = True

    objects = []
    uIElements = []
    Start()




btnRESTART = Button("RESTART", 150, 400 ,600, 100, callback=StartGame)
btnRESTART.addAll = False

def EndScreen():

    globalPanel.Draw(screen)

    if(p1.score > p2.score): endText.text = f"WIN: {p1.name}"
    else: endText.text = f"WIN: {p2.name}"

    endText.position = Vector2(450 - endText.width // 2, 200)
    endText.Draw(screen)
    btnRESTART.Update(screen)

def Start():

    objects.append(leftPanel)
    objects.append(middlePanel)
    objects.append(rightPanel)

    uIElements.append(btn1)
    uIElements.append(btn2)
    uIElements.append(btn3)
    uIElements.append(btnRESTART)

    for element in uIElements:
        if element.addAll:
            objects.append(element)

    monet = randint(1,2)
    if monet == 1: p1.select = True

def Main():
    global p1,p2,btn1,btn2,btn3,delayTimer,delay

    gameOver = p1.isEnd or p2.isEnd

    if gameOver:
        EndScreen()
        return

    if p1.select == True:
        if p1.randomNumber == 0:
            p1.randomNumber = p1.random
            p2.randomNumber = 0
            delayTimer = delay
            p1.coloum = -1

        if p1.coloum > -1 and p1.AddNumber(p1.coloum) > -1:
            p2.CheckAndRemove(p1.randomNumber, p1.coloum)
            p1.select = False
            p1.scoreLabel.text = f"Score: {p1.score}"
            p1.scoreLabel.position = Vector2(5 + (200 - p1.scoreLabel.width) // 2, 385)
            p2.scoreLabel.text = f"Score: {p2.score}"
            p2.scoreLabel.position = Vector2(705 + (200 - p2.scoreLabel.width) // 2, 385)
    else:
        if p2.randomNumber == 0:
            p2.randomNumber = p2.random
            p1.randomNumber = 0
            delayTimer = delay
            p2.coloum = -1

        if delayTimer > 0: delayTimer -= 1
        else:
            if p2.coloum > -1 and p2.AddNumber(p2.coloum) > -1:
                p1.CheckAndRemove(p2.randomNumber, p2.coloum)
                p1.select = True
                p1.scoreLabel.text = f"Score: {p1.score}"
                p2.scoreLabel.text = f"Score: {p2.score}"
            else:
                p2.coloum = randint(0,2)

    p1.DisplayZone(screen)
    p2.DisplayZone(screen)

def Update():

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in uIElements:
                element.OnClick(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for gameObject in objects:
        gameObject.Update(screen)
    
    Main()

    pygame.time.Clock().tick(60)
    pygame.display.update()