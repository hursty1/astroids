import sys
import pygame
from asteroidfield import AsteroidField
from constants import *
from healthIcon import HealthIcon
from player import Player
from asteroid import Asteroid
from shot import Shot
import pygame.freetype

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    #fonts
    GAME_FONT = pygame.freetype.SysFont('serif', 30)

    #state
    SCORE = 0
    LIVES = 5
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    life_group = pygame.sprite.Group()
    #things
    Player.containers = (updatable, drawable) #overriding the class not the instance
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    HealthIcon.containers = (drawable,life_group)

    #spawn
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,PLAYER_RADIUS)
    AsteroidField()


    #health Icons
    for i in range(0,LIVES):
        HealthIcon(50 + 40*i, 70, i+1)
    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
        for entity in updatable:
            entity.update(dt)
            
        for asteroid in asteroids:
            if player.inv_timer < 0:
                collision = player.collision(asteroid)
                collision = False
                if collision:
                    
                    for l in life_group:
                        # print(l.index)
                        if l.index == LIVES:
                            l.kill()
                    LIVES -= 1
                    player.take_damage(LIVES)
                    if LIVES < 0:
                        running = False
                    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,PLAYER_RADIUS)
                    player.spawn()
                # sys.exit("player died")
            else:
                # print('player inv')
                pass
        for entity in drawable:
            entity.draw(screen)
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    SCORE += 5
                    asteroid.split()
                    bullet.kill()

        GAME_FONT.render_to(screen, (75,15), str(SCORE), "white")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__=="__main__":
    main()