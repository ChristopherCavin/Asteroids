from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import (log_state, log_event)
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            self.angle = random.uniform(20, 50)
            self.split1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            self.split2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            self.split1.velocity = self.velocity * 1.2
            self.split2.velocity = self.velocity * 1.2
            self.split1.velocity = self.split1.velocity.rotate(self.angle)
            self.split2.velocity = self.split2.velocity.rotate(-(self.angle))

