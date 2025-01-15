import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "lightblue",
            self.position,
            self.radius,
            2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.create_child(angle, new_radius)
        self.create_child(-angle, new_radius)
        
    def create_child(self, angle, radius):
        asteroid = Asteroid(self.position.x, self.position.y,radius)
        asteroid.velocity = self.velocity.rotate(angle) * 1.2
        
        


