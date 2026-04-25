import pygame
import math
import sys

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
    
    # Stores a static snapshot of the screen to allow 'previewing' shapes while dragging
    canvas = screen.copy()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Tool selection keys
                if event.key == pygame.K_r: current_tool = 'rect'
                if event.key == pygame.K_c: current_tool = 'circle'
                if event.key == pygame.K_b: current_tool = 'brush'
                if event.key == pygame.K_e: current_tool = 'eraser'
                if event.key == pygame.K_s: current_tool = 'square'
                if event.key == pygame.K_t: current_tool = 'right_tri'
                if event.key == pygame.K_q: current_tool = 'equi_tri'
                if event.key == pygame.K_h: current_tool = 'rhombus'
                
                # Color selection keys
                if event.key == pygame.K_1: current_color = BLACK
                if event.key == pygame.K_2: current_color = RED
                if event.key == pygame.K_3: current_color = GREEN
                if event.key == pygame.K_4: current_color = BLUE

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                # Capture canvas state at the moment the click starts
                canvas = screen.copy()

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                # Finalize the drawing onto the canvas snapshot
                canvas = screen.copy()

        if drawing:
            # For shapes, we redraw the saved canvas every frame to clear the 'ghost' previews
            if current_tool not in ['brush', 'eraser']:
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

            elif current_tool == 'square':
                # Force width and height to be equal based on largest mouse displacement
                width = mouse_pos[0] - start_pos[0]
                height = mouse_pos[1] - start_pos[1]
                side = max(abs(width), abs(height))
                s_x = start_pos[0] if width > 0 else start_pos[0] - side
                s_y = start_pos[1] if height > 0 else start_pos[1] - side
                pygame.draw.rect(screen, current_color, (s_x, s_y, side, side), 2)
            
            elif current_tool == 'circle':
                # Calculate Euclidean distance for radius
                radius = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
                if radius > 0:
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)

            elif current_tool == 'right_tri':
                # Connect start, corner (start_x, mouse_y), and current mouse position
                points = [start_pos, (start_pos[0], mouse_pos[1]), mouse_pos]
                pygame.draw.polygon(screen, current_color, points, 2)

            elif current_tool == 'equi_tri':
                # Use trigonometry to find height: (sqrt(3)/2) * side_length
                dx = mouse_pos[0] - start_pos[0]
                dy = mouse_pos[1] - start_pos[1]
                side = int(math.sqrt(dx**2 + dy**2))
                h = int(side * math.sqrt(3) / 2)
                p1 = start_pos
                p2 = (start_pos[0] + side, start_pos[1])
                p3 = (start_pos[0] + side // 2, start_pos[1] - h)
                pygame.draw.polygon(screen, current_color, [p1, p2, p3], 2)

            elif current_tool == 'rhombus':
                # Create four points at the midpoints of the bounding box
                dx = mouse_pos[0] - start_pos[0]
                dy = mouse_pos[1] - start_pos[1]
                p1 = (start_pos[0] + dx // 2, start_pos[1])           # Top center
                p2 = (start_pos[0] + dx, start_pos[1] + dy // 2)      # Right center
                p3 = (start_pos[0] + dx // 2, start_pos[1] + dy)      # Bottom center
                p4 = (start_pos[0], start_pos[1] + dy // 2)           # Left center
                pygame.draw.polygon(screen, current_color, [p1, p2, p3, p4], 2)

        pygame.display.set_caption(f"Tool: {current_tool} | S:Sq, T:RTri, Q:ETri, H:Rhombus")
        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()
