import math
import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rel_shape = self.generate_random_shape()
    def draw(self,screen):
        self.draw_shape(screen)

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


    def draw_shape(self, screen):
        pts_arr = [(int(self.position.x + v.x), int(self.position.y + v.y)) for v in self.rel_shape]
        pygame.draw.polygon(screen,"white", points=pts_arr, width=1)

    def get_point_array(self, num_pts=15) -> list:
        l = []
        for i in range(num_pts):
            angle = (i / num_pts) * 2 * math.pi  # angle in radians
            vec = pygame.Vector2(
                math.cos(angle) * self.radius,
                math.sin(angle) * self.radius
            ) + self.position  # Center it at the asteroid's position
            l.append((int(vec.x), int(vec.y)))  # Convert to point tuple
        return l
    def generate_random_shape(self, num_pts=15):
        l = []
        for i in range(num_pts):
            angle = (i / num_pts) * 2 * math.pi
            r = self.radius + random.uniform(-self.radius * 0.3, self.radius * 0.3)
            vec = pygame.Vector2(math.cos(angle) * r, math.sin(angle) * r)
            l.append(vec)
        return l