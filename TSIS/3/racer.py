import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen_width, speed, type="car"):
        super().__init__()
        self.type = type
        self.image = pygame.Surface((30, 50))
        self.image.fill((255, 0, 0) if type == "car" else (100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), -50)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, screen_width, effect):
        super().__init__()
        self.effect = effect # "nitro", "shield", "repair"
        self.image = pygame.Surface((20, 20))
        colors = {"nitro": (255, 165, 0), "shield": (0, 255, 255), "repair": (0, 255, 0)}
        self.image.fill(colors[effect])
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), -50)

    def update(self):
        self.rect.y += 3
        if self.rect.top > 600:
            self.kill()
