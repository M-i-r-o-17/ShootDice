from Engine.GameObject import GameObject
import pygame
import sys

BLACK = (0,0,0)
WHITE = (255,255,255)
isDebug = True

pygame.init()
pygame.display.set_caption("Тестируем GameObject")

screen = pygame.display.set_mode((800, 600))
objects = []

dices = [
    GameObject(0,0,64,64), GameObject(64,0,64,64), GameObject(128,0,64,64),
    GameObject(0,64,64,64), GameObject(64,64,64,64), GameObject(128,64,64,64)
]

for i in range(6):
    dices[i].imagePath = f"img/{i+1}.png"
    dices[i].color = WHITE
    objects.append(dices[i])


def Start():
    pass

def Main():
    pass

def Update():

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for gameObject in objects:
        gameObject.Update(screen)
    
    Main()

    pygame.time.Clock().tick(60)
    pygame.display.update()