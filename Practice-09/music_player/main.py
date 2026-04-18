import pygame
import os
from player import MusicPlayer


pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Music Controller")
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()


music_dir = os.path.join(os.path.dirname(__file__), 'music')
player = MusicPlayer(music_dir)

def draw_text(text, x, y, color=(0, 0, 0)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

running = True
while running:
    screen.fill((240, 240, 240)) # Light Gray Background
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False

    
    draw_text("Music Player Controls:", 50, 50, (50, 50, 50))
    draw_text("[P] Play   [S] Stop   [N] Next   [B] Back   [Q] Quit", 50, 90, (100, 100, 100))
    
    
    status = "Playing" if player.is_playing else "Stopped"
    draw_text(f"Status: {status}", 50, 180, (0, 128, 0) if player.is_playing else (200, 0, 0))
    draw_text(f"Now Playing: {player.get_current_track_name()}", 50, 220)
    
   
    progress = player.get_progress()
    draw_text(f"Time Elapsed: {progress}s", 50, 260, (150, 150, 150))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
