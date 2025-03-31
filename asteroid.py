import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x, self.position.y),self.radius, width=1)

    def update(self, dt):
        self.wrap()
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        deg = random.uniform(20,50)
        l = Asteroid(self.position.x,self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        l.velocity = self.velocity.rotate(deg) * 1.2
        r = Asteroid(self.position.x,self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        r.velocity = self.velocity.rotate(-deg) * 1.2
