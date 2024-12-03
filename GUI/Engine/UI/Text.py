import pygame

from Engine.Basic import *

class Text(Basic):

    def __init__(self, text:str, color, position:Vector2, background = None, font = "Engine/UI/font/Menlo-Regular", size:int = 25):
        Basic().__init__()
        pygame.font.init()

        self.size = size

        try:
            self.font = pygame.font.match_font(font)
        except:
            self.font = None

        self.FONT = pygame.font.Font(self.font, size)

        
        self.position = position

        self.text = text
        self.color = color
        self.background = background


    @property
    def surface(self): return self.FONT.render(f"{self.text}", 1, self.color, self.background)

    @property
    def rect(self): return self.surface.get_rect()

    @property
    def width(self): return self.rect.width

    @property
    def height(self): return self.rect.height

    def NewFont(self, font):
        self.font = pygame.font.match_font(font)
        self.Upgrade()

    def Resize(self, size):
        self.size = size
        self.Upgrade()

    def Upgrade(self):
        self.FONT = pygame.font.Font(self.font, self.size)

    def Draw(self, surface):
        surface.blit(self.surface, self.position.xy)