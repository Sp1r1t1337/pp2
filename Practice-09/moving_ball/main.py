import pygame
import sys
from ball import Ball


WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")
clock = pygame.time.Clock()


my_ball = Ball(WIDTH // 2, HEIGHT // 2, 25, RED, WIDTH, HEIGHT)

def main():
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    my_ball.move("UP")
                elif event.key == pygame.K_DOWN:
                    my_ball.move("DOWN")
                elif event.key == pygame.K_LEFT:
                    my_ball.move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    my_ball.move("RIGHT")

        
        screen.fill(WHITE)
        my_ball.draw(screen)

       
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
