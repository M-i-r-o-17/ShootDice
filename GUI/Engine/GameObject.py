import pygame

from Engine.Transform import Transform
from Engine.Sprite import Sprite

class GameObject(Transform):

    def __init__(self,x, y, width, height, type = "Rect", surface = None):
        Transform.__init__(self, x, y, width, height)
        self.tag   = "Untaget"

        self.sprite = None

        self.drawRect = True
        self.color = (255, 0, 255)
        
    def Draw(self, surface):

        self.surface.fill((0, 0, 0))

        if self.drawRect:
            pygame.draw.rect(self.surface, self.color, self.base)
        
        if(self.sprite != None):
            self.sprite.Draw(self.surface)

        if self.DEBUG:
            pygame.draw.rect(self.surface, (255, 0, 0), self.centerPoint)
        
        surface.blit(self.surface, (self.position.x, self.position.y))

    def Update(self, surface):
        
        super().Update()

        self.Draw(surface)

    def IsCollideCenter(self, collider):
        return self.OnCollision(collider)
    
    def IsCollideLeft(self, collider):
        return self.left.distance(collider.right) <= 0.01
    
    def IsCollideRight(self, collider):
        return self.right.distance(collider.left) <= 0.01
    
    def IsCollideTop(self, collider):
        return self.top.distance(collider.bottom) <= 0.01
    
    def IsCollideBottom(self, collider):
        return self.bottom.distance(collider.top) <= 0.01
