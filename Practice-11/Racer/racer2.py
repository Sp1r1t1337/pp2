import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_COUNT = 0
COIN_THRESHOLD = 5

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD  = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)

DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infinite Racer - Coin Edition")
FramePerSec = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("CRASH", True, BLACK)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((30, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        chance = random.randint(1, 100)
        if chance <= 70:
            self.value = 1
            self.color = BRONZE
        elif chance <= 90:
            self.value = 5
            self.color = SILVER
        else:
            self.value = 10
            self.color = GOLD
            
        self.image = pygame.Surface((20, 20))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > 600:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 2500)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2      
            
        if event.type == SPAWN_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURFACE.fill(WHITE)
    
    scores = font_small.render(f"Score: {SCORE}  Coins: {COIN_COUNT}", True, BLACK)
    DISPLAYSURFACE.blit(scores, (10,10))

    for entity in all_sprites:
        DISPLAYSURFACE.blit(entity.image, entity.rect)
        entity.move()

    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        SCORE += coin.value
        COIN_COUNT += 1
        if COIN_COUNT % COIN_THRESHOLD == 0:
            SPEED += 1.0

    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURFACE.fill(RED)
        DISPLAYSURFACE.blit(game_over, (90, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
