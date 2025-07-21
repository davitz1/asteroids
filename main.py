import pygame
from pygame.display import update
import sys
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0
    
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.checkCollision(asteroid):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")


        for each in drawable:
            each.draw(screen)
        pygame.display.flip() 

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
