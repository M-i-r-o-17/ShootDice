import pygame
from Engine.Basic import Basic
from Engine.Basic import Vector2

class Position(Basic):

    def __init__(self, x, y, width, height, type = "Rect"):

        Basic.__init__(self)

        self.surface = pygame.Surface((width, height))

        self.position = Vector2(x, y)
        self.size = Vector2(width, height)

        if type == "Rect":
            self.base = pygame.Rect(0, 0, width, height)
        else:
            self.Error(0,"Not found type")

        scale = 10

        self.centerPoint = pygame.Rect(self.center.x - scale // 2,
                                       self.center.y - scale // 2,
                                       scale, scale)

    def Move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy
        
    def Update(self):
        pass

    def OnCollisionEnter(self, position):
        if   self.left.distance(position.right) <= 0.01: return True
        elif self.right.distance(position.left) <= 0.01: return True
        elif self.top.distance(position.bottom) <= 0.01: return True
        elif self.bottom.distance(position.top) <= 0.01: return True 
        else: return False
    
    def OnCollision(self, position):
        if   self.center.distance(position.right) <= self.width // 2:  return True
        elif self.center.distance(position.left)  <= self.width // 2:  return True
        elif self.center.distance(position.top)   <= self.height // 2: return True
        elif self.center.distance(position.bottom)   <= self.height // 2: return True
        else: return False
    
    @property
    def left(self):
        return Vector2(self.position.x, self.position.y + self.height // 2)

    @property
    def right(self):
        return Vector2(self.position.x + self.width, self.position.y + self.height // 2)

    @property
    def top(self):
        return Vector2(self.position.x + self.width // 2, self.position.y)

    @property
    def bottom(self):
        return Vector2(self.position.x + self.width // 2, self.position.y + self.height)

    @property
    def width(self):
        return self.size.x

    @property
    def height(self):
        return self.size.y

    @property
    def center(self):
        return Vector2(self.position.x + self.width // 2, self.position.y + self.height // 2)