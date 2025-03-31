import pygame
from constants import *


class HealthIcon(pygame.sprite.Sprite):
    def __init__(self,x,y,index):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.index = index
        self.radius = PLAYER_RADIUS
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def update(self,dt):
        pass

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]