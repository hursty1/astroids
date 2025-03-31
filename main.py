import sys
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #things
    Player.containers = (updatable, drawable) #overriding the class not the instance
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #spawn
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,PLAYER_RADIUS)
    AsteroidField()
    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
        for entity in updatable:
            entity.update(dt)
            
        for asteroid in asteroids:
            collision = player.collision(asteroid)
            if collision:
                print("Game over!")
                running = False
                # sys.exit("player died")
        for entity in drawable:
            entity.draw(screen)
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    print('dead')
                    asteroid.split()
                    bullet.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__=="__main__":
    main()