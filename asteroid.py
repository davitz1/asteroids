from constants import *
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def checkCollision(self, otherCircle):
        distance = self.position.distance_to(otherCircle.position)
        if distance < self.radius + otherCircle.radius:
            return True
        return False
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = vector1 * 1.2
        child2.velocity = vector2 * 1.2
        
