import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    
    screen.fill(WHITE)
    
    current_tool = 'brush'
    current_color = BLACK
    drawing = False
    start_pos = None
    
    canvas = screen.copy()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: current_tool = 'rect'
                if event.key == pygame.K_c: current_tool = 'circle'
                if event.key == pygame.K_b: current_tool = 'brush'
                if event.key == pygame.K_e: current_tool = 'eraser'
                if event.key == pygame.K_1: current_color = BLACK
                if event.key == pygame.K_2: current_color = RED
                if event.key == pygame.K_3: current_color = GREEN
                if event.key == pygame.K_4: current_color = BLUE

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                canvas = screen.copy()

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                canvas = screen.copy()

        if drawing:
            if current_tool in ['rect', 'circle']:
                screen.blit(canvas, (0, 0))
            
            if current_tool == 'brush':
                pygame.draw.circle(screen, current_color, mouse_pos, 5)
            
            elif current_tool == 'eraser':
                pygame.draw.circle(screen, WHITE, mouse_pos, 20)
            
            elif current_tool == 'rect':
                width = mouse_pos[0] - start_pos[0]
                height = mouse_pos[1] - start_pos[1]
                rect = pygame.Rect(start_pos[0], start_pos[1], width, height)
                rect.normalize()
                pygame.draw.rect(screen, current_color, rect, 2)
            
            elif current_tool == 'circle':
                radius = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
                if radius > 0:
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)

        pygame.display.set_caption(f"Tool: {current_tool} | 1-4: Colors | B, R, C, E: Tools")
        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()
