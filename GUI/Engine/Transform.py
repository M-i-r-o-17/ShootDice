import pygame
from Engine.Basic import Vector2
from Engine.Position import Position

class Transform(Position):

    def __init__(self, x = 0, y = 0, width = 64, height = 64, speed=(0,0), type = "Rect"):
        Position.__init__(self, x, y, width, height, type)
        self.speed = Vector2(0,0)

    def Update(self):
        super().Update()
        if not(self.speed == self.speed.zero): self.Move(self.speed.x, self.speed.y)
