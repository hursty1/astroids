import pygame
from constants import *
class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
    def wrap(self):
        if self.position.x + self.radius < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x - self.radius > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y + self.radius < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y - self.radius > SCREEN_HEIGHT:
            self.position.y = 0
    def draw(self, screen):
        pass

    def update(self,dt):
        pass

    def collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius