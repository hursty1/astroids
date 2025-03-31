import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0.3
    #overrides
    def draw(self, screen):
        # return super().draw(screen)
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def update(self,dt):
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            # print(self.PLAYER_SHOOT_COOLDOWN)
            self.PLAYER_SHOOT_COOLDOWN -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= dt * PLAYER_TURN_SPEED
        if keys[pygame.K_d]:
            self.rotation += dt * PLAYER_TURN_SPEED
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            return
        self.PLAYER_SHOOT_COOLDOWN = 0.3
        s = Shot(self.position.x,self.position.y)
        s.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED



    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]