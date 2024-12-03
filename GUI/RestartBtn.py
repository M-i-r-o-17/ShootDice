import pygame
from Engine.UI.Button import Button

class RestartButton(Button):

    def __init__(self, text, x=0, y=0, width=64, height=64):
        Button.__init__(self, text, x, y, width, height)
        self.coloum = 0
        self.player = None

    def Event(self):
        if self.player != None: 
            self.player.coloum = self.coloum
        return False
