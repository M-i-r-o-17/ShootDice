import pygame
from Engine.Basic import *



class Sprite(Basic):

    def __init__(self, path:str, size:Vector2 = Vector2(64, 64), convert:int = 0, color = (255, 0, 255)):

        Basic.__init__(self)

        self.faild = False
        self.image = None
        self.convert = convert
        self.size = size

        try:
            if convert == 0:
                image = pygame.image.load(path).convert_alpha()
            else:
                image = pygame.image.load(path).convert()
        except:
            self.faild = True
            self.Error(1, f"Do not find file with path \"{path}\"")

        if self.faild: return

        self.image = pygame.transform.scale(image, size.xy)

    def Draw(self, surface):

        if self.faild: return

        surface.blit(self.image, (self.position.x, self.position.y))

    def LoadImage(self, path):
        try:
            if self.convert == 0:
                self.image = pygame.image.load(path).convert_alpha()
            else:
                self.image = pygame.image.load(path).convert()
            self.faild = False
            self.image = pygame.transform.scale(self.image, self.size.xy)
        except:
            self.faild = True
            self.Error(1, f"Do not find file with path \"{path}\"")

        
