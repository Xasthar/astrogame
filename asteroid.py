import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, screen):
            pygame.draw.circle(screen, white, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
            self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        ast1_velocity = self.velocity.rotate(random_angle)
        ast2_velocity = self.velocity.rotate(-random_angle)
        ast_new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, ast_new_radius)
        asteroid1.velocity = ast1_velocity * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, ast_new_radius)
        asteroid2.velocity = ast2_velocity * 1.2