import pygame

from Engine.Transform import Transform

class GameObject(Transform):

    def __init__(self,x, y, width, height, type = "Rect", surface = None):
        Transform.__init__(self, x, y, width, height)
        self.tag   = "Untaget"

        self.imagePath = "None"
        self.image = None
        self.failLoadImage = False

        self.color = (255, 0, 255)

    def DrawRect(self):
        self.surface.fill((0, 0, 0))
        pygame.draw.rect(self.surface, self.color, self.base)
        
    def Draw(self, surface):

        if self.image == None and self.failLoadImage == False:

            if self.imagePath == "None":
                self.Warning("Image path is empty!")
                self.failLoadImage = True
            else:
                self.image = pygame.image.load(self.imagePath).convert_alpha()

                if not(self.image == None):
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                else:
                    self.Error(1, f"Do not find file with path \"{self.imagePath}\"")
                    self.failLoadImage = True

        self.DrawRect()
        
        if not(self.image == None):
            self.surface.blit(self.image, self.image.get_rect())

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
