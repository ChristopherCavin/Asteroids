import pygame
import sys
from player import Player
from asteroidfield import AsteroidField
from asteroids import Asteroid
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH)
from logger import (log_state, log_event)
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    score = 0
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Your score is {score}")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    score += 1
                    asteroid.split()
                    log_event("asteroid_shot")

        pygame.display.flip()


if __name__ == "__main__":
    main()
  
