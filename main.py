import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()

    print("Starting asteroids!")
    print("Screen width: %s" % (SCREEN_WIDTH))
    print("Screen height: %s" % (SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    field = AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for update in updatable:
            update.update(dt)

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
