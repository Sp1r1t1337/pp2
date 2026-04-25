import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS_START = 10

WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 102)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Pro: Weighted Food & Timers")
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_ui(score, level, timer):
    value = score_font.render(f"Score: {score}  Lvl: {level}", True, YELLOW)
    timer_val = font_style.render(f"Food Timer: {max(0, timer // 1000)}s", True, WHITE)
    screen.blit(value, [10, 10])
    screen.blit(timer_val, [10, 50])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

def generate_food(snake_list):
    while True:
        food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        
        chance = random.randint(1, 100)
        if chance <= 60:
            weight = 1
            color = GREEN
            life_span = 7000
        elif chance <= 90:
            weight = 3
            color = YELLOW
            life_span = 5000
        else:
            weight = 7
            color = RED
            life_span = 3000
            
        if [food_x, food_y] not in snake_list:
            return food_x, food_y, weight, color, pygame.time.get_ticks() + life_span

def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    
    score = 0
    level = 1
    current_fps = FPS_START

    food_x, food_y, food_weight, food_color, food_expiry = generate_food(snake_list)

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font_style.render("Lost! Press C-Play Again or Q-Quit", True, RED)
            screen.blit(msg, [WIDTH / 6, HEIGHT / 3])
            display_ui(score, level, 0)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if pygame.time.get_ticks() > food_expiry:
            food_x, food_y, food_weight, food_color, food_expiry = generate_food(snake_list)

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, food_color, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        
        time_left = food_expiry - pygame.time.get_ticks()
        display_ui(score, level, time_left)
        
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            score += food_weight
            length_of_snake += 1
            
            if score // 10 >= level:
                level += 1
                current_fps += 2
                
            food_x, food_y, food_weight, food_color, food_expiry = generate_food(snake_list)

        clock.tick(current_fps)

    pygame.quit()
    sys.exit()

game_loop()
