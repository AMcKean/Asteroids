from constants import *
from asteroid import Asteroid
import player
import pygame
import asteroidfield


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    player.Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids_group, updateable, drawable)
    asteroidfield.AsteroidField.containers = (updateable,)

    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()

    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

        for asteroid in asteroids_group:
            if player1.collision(asteroid):
                print("Game over!")
                import sys

                sys.exit()

        screen.fill(SCREEN_COLOR)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
