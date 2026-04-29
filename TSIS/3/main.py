import pygame, sys
from racer import Player, Obstacle, PowerUp
from ui import Button, draw_text
from persistence import update_leaderboard, load_data, save_data

pygame.init()
SCREEN = pygame.display.set_mode((400, 600))
CLOCK = pygame.time.Clock()

# Load Settings
settings = load_data('settings.json', {"sound": True, "color": "blue", "difficulty": 1})

def main_menu():
    user_name = ""
    entering_name = True
    
    while True:
        SCREEN.fill((255, 255, 255))
        draw_text(SCREEN, "INFINITE RACER", 40, 40, 100)
        
        # Name Entry
        draw_text(SCREEN, f"Enter Name: {user_name}", 20, 50, 200)
        
        btn_play = Button("PLAY", 100, 300, 200, 50, (0, 200, 0))
        btn_leader = Button("LEADERBOARD", 100, 370, 200, 50, (0, 0, 200))
        btn_play.draw(SCREEN)
        btn_leader.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: user_name = user_name[:-1]
                elif len(user_name) < 10: user_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.is_clicked(event.pos) and user_name != "":
                    game_loop(user_name)
        
        pygame.display.update()

def game_loop(name):
    speed = 5 + settings['difficulty']
    score = 0
    distance = 0
    active_powerup = None
    powerup_timer = 0
    shield_active = False
    
    player = Player() # Use your existing Player class or updated one
    enemies = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)

    SPAWN_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ENEMY, 1500)

    running = True
    while running:
        dt = CLOCK.tick(60)
        SCREEN.fill((255, 255, 255))
        
        distance += speed / 10
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == SPAWN_ENEMY:
                new_enemy = Obstacle(400, speed)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Power-up Logic
        if powerup_timer > 0:
            powerup_timer -= dt
            if powerup_timer <= 0:
                active_powerup = None
                speed -= 5 # Remove nitro effect

        # Collisions
        if pygame.sprite.spritecollideany(player, enemies):
            if shield_active:
                shield_active = False
                # Remove the specific enemy hit
                pygame.sprite.spritecollide(player, enemies, True)
            else:
                update_leaderboard(name, int(score), int(distance))
                return # Game Over

        # Update and Draw
        all_sprites.update()
        all_sprites.draw(SCREEN)
        
        draw_text(SCREEN, f"Dist: {int(distance)} Score: {int(score)}", 18, 10, 10)
        if active_powerup:
            draw_text(SCREEN, f"{active_powerup}: {powerup_timer//1000}s", 18, 10, 40, (255, 0, 0))

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
