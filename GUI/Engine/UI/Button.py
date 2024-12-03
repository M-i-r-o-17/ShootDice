import pygame
from Engine.Position import Position
from Engine.Basic import Vector2
from Engine.UI.Text import Text

class Button(Position):

    def __init__(self, text, x=0, y=0, width=64, height=64, callback = None):

        Position.__init__(self, x, y, width, height)

        self.color = (255, 255, 255)
        self.background = (60, 60, 60)

        self.label = Text(text, self.color, Vector2(0,0))

        self.label.position = Vector2(
            self.center.x - self.label.width // 2,
            self.center.y - self.label.height // 2
        )

        self.delay = 0

        self.callbackFun = callback

        self.addAll = True

    def OnClick(self, mouse):
        
        if (self.position.x < mouse.pos[0] < self.position.x + self.size.x and self.position.y < mouse.pos[1] < self.position.y + self.size.y and self.delay <= 0):
            self.Event()
            self.delay = 5
            return True
        
        return False
    
    def Update(self, screen):
        super().Update()
        if self.delay > 0: 
            self.background = (30, 30, 30)
            self.delay -= 1
        else: self.background = (60, 60, 60)
        self.Draw(screen)

    def Draw(self, surface):

        self.surface.fill((0, 0, 0))

        pygame.draw.rect(self.surface, self.background, self.base)

        surface.blit(self.surface, self.position.xy)
        self.label.Draw(surface)

    def Event(self):
        if self.callbackFun != None: return self.callbackFun()