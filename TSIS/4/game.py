import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, snake_list, obstacles):
        self.type = random.choice(["speed", "slow", "shield"])
        self.pos = self.get_valid_pos(snake_list, obstacles)
        self.expiry = pygame.time.get_ticks() + 8000
        self.color = (0, 255, 255) # Cyan

    def get_valid_pos(self, snake_list, obstacles):
        while True:
            pos = [random.randrange(0, 580, 20), random.randrange(0, 380, 20)]
            if pos not in snake_list and pos not in obstacles:
                return pos

class ObstacleManager:
    def __init__(self, level):
        self.blocks = []
        if level >= 3:
            for _ in range(level * 2): # Increase blocks with level
                self.blocks.append([random.randrange(0, 580, 20), random.randrange(0, 380, 20)])
    
    def draw(self, screen):
        for b in self.blocks:
            pygame.draw.rect(screen, (100, 100, 100), [b[0], b[1], 20, 20])
