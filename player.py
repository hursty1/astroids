import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0.3
        self.inv_timer = 0.5
        self.color = 'white'
    #overrides
    def draw(self, screen):
        #wrap screen
        self.wrap()
        pygame.draw.polygon(screen,self.color,self.triangle(),2)

    def update(self,dt):
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            # print(self.PLAYER_SHOOT_COOLDOWN)
            self.PLAYER_SHOOT_COOLDOWN -= dt
        self.inv_timer -= dt
        if self.inv_timer < 0:
            self.color = 'white'
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= dt * PLAYER_TURN_SPEED
        if keys[pygame.K_d]:
            self.rotation += dt * PLAYER_TURN_SPEED
        if keys[pygame.K_w]:
            self.move(dt)
        # if keys[pygame.K_s]:
        #     self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.position += self.velocity * dt
    def shoot(self):
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            return
        self.PLAYER_SHOOT_COOLDOWN = 0.3
        s = Shot(self.position.x,self.position.y)
        s.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def take_damage(self, lives):
        self.inv_timer = 0.5
        print(f"Player has taken Damage and has {lives} left")
        self.kill()

    def spawn(self):
        self.inv_timer = 1.5
        self.color = 'red'
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        # self.position += forward * PLAYER_SPEED * dt
        self.velocity += forward * PLAYER_ACCEL
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]