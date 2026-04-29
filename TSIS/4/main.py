import pygame
import json
from db import save_game_result, get_personal_best, get_leaderboard
from game import ObstacleManager, PowerUp

# Load Settings
try:
    with open('settings.json', 'r') as f: settings = json.load(f)
except:
    settings = {"snake_color": [0, 255, 0], "grid": True}

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

def game_loop(username):
    # Game variables
    score, level = 0, 1
    snake_list = [[300, 200]]
    length = 1
    direction = [0, 0]
    obstacles = ObstacleManager(level)
    power_up = None
    
    # Poison Food logic
    poison_pos = [random.randrange(0, 580, 20), random.randrange(0, 380, 20)]
    
    pb = get_personal_best(username)
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        # 1. Input / Direction
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: direction = [0, -20]
                elif event.key == pygame.K_DOWN: direction = [0, 20]
                elif event.key == pygame.K_LEFT: direction = [-20, 0]
                elif event.key == pygame.K_RIGHT: direction = [20, 0]

        # 2. Movement
        new_head = [snake_list[-1][0] + direction[0], snake_list[-1][1] + direction[1]]
        
        # 3. Collision Checks
        if new_head in snake_list or new_head in obstacles.blocks or \
           new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 400:
            save_game_result(username, score, level)
            return # Game Over

        snake_list.append(new_head)
        
        # Poison Food
        if new_head == poison_pos:
            length = max(0, length - 2)
            if length <= 1: 
                save_game_result(username, score, level)
                return
            snake_list = snake_list[-(length+1):]
            poison_pos = [random.randrange(0, 580, 20), random.randrange(0, 380, 20)]
        
        # Power Up Spawning
        if not power_up and random.randint(1, 100) == 1:
            power_up = PowerUp(snake_list, obstacles.blocks)
            
        if power_up:
            if pygame.time.get_ticks() > power_up.expiry:
                power_up = None
            elif new_head == power_up.pos:
                # Apply effect logic here (e.g., set speed timer)
                power_up = None

        if len(snake_list) > length:
            del snake_list[0]

        # 4. Drawing
        obstacles.draw(screen)
        pygame.draw.rect(screen, (139, 0, 0), [poison_pos[0], poison_pos[1], 20, 20]) # Poison
        for p in snake_list:
            pygame.draw.rect(screen, settings['snake_color'], [p[0], p[1], 20, 20])
        
        pygame.display.flip()
        clock.tick(10 + level)

game_loop("Player1")
