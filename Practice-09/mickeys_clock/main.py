import pygame
import datetime
import os
from clock import get_rotation_angle, rotate_hand


pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock = pygame.time.Clock()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, 'images', 'mickey_hand.png')
BACKGROUND_PATH = os.path.join(BASE_DIR, 'images', 'main-clock.png') # Optional background

hand_img = pygame.image.load(IMAGE_PATH).convert_alpha()


CENTER = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    
    screen.fill((255, 255, 255))
    

    
    min_angle = get_rotation_angle(minutes)
    min_hand, min_rect = rotate_hand(hand_img, min_angle, CENTER)
    screen.blit(min_hand, min_rect)

    
    sec_angle = get_rotation_angle(seconds)
    sec_hand, sec_rect = rotate_hand(hand_img, sec_angle, CENTER)
    screen.blit(sec_hand, sec_rect)

    
    pygame.display.flip()
    clock.tick(60) # Smooth 60 FPS

pygame.quit()
