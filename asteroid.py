import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Get the groups before killing the asteroid
        groups = self.groups()

        # Kill the asteroid
        self.kill()

        # If it's too small, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate random angle and new velocities
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2

        # Add them to all groups this asteroid was in
        for group in groups:
            group.add(asteroid1)
            group.add(asteroid2)
