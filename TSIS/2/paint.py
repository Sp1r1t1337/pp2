import pygame
from datetime import datetime
from tools import flood_fill, TextTool

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 700))
canvas = pygame.Surface((1000, 700))
canvas.fill((255, 255, 255)) # White background

# States
drawing = False
tool = "pencil" # pencil, line, fill, text
brush_size = 2
color = (0, 0, 0)
start_pos = None
text_tool = TextTool()

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Keyboard Shortcuts
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: brush_size = 2
            if event.key == pygame.K_2: brush_size = 5
            if event.key == pygame.K_3: brush_size = 10
            
            # Save functionality (Ctrl+S)
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                pygame.image.save(canvas, f"paint_{timestamp}.png")
                print(f"Saved as paint_{timestamp}.png")

            # Tool Selection
            if event.key == pygame.K_p: tool = "pencil"
            if event.key == pygame.K_l: tool = "line"
            if event.key == pygame.K_f: tool = "fill"
            if event.key == pygame.K_t: tool = "text"

            # Text Input Handling
            if text_tool.active:
                if event.key == pygame.K_RETURN:
                    # Render text permanently to canvas
                    text_tool.render(canvas, color)
                    text_tool.active = False
                elif event.key == pygame.K_ESCAPE:
                    text_tool.active = False
                elif event.key == pygame.K_BACKSPACE:
                    text_tool.backspace()
                else:
                    text_tool.add_char(event.unicode)

        # Mouse Handling
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = mouse_pos
            
            if tool == "fill":
                flood_fill(canvas, mouse_pos[0], mouse_pos[1], color)
            elif tool == "text":
                text_tool.start(mouse_pos)

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and tool == "line":
                pygame.draw.line(canvas, color, start_pos, mouse_pos, brush_size)
            drawing = False

    # Pencil continuous drawing
    if drawing and tool == "pencil":
        curr_pos = mouse_pos
        pygame.draw.line(canvas, color, start_pos, curr_pos, brush_size)
        start_pos = curr_pos

    # Rendering
    screen.fill((200, 200, 200)) # Background UI color
    screen.blit(canvas, (0, 0))  # Draw actual canvas

    # Draw Preview for Line Tool
    if drawing and tool == "line":
        pygame.draw.line(screen, color, start_pos, mouse_pos, brush_size)

    # Draw Active Text Preview
    text_tool.render(screen, color)

    # Simple Toolbar UI
    pygame.draw.rect(screen, (50, 50, 50), (0, 650, 1000, 50))
    font = pygame.font.SysFont("Arial", 16)
    ui_text = f"Tool: {tool} | Size: {brush_size} | [1,2,3]: Change Size | [P]: Pencil | [L]: Line | [F]: Fill | [T]: Text | Ctrl+S: Save"
    label = font.render(ui_text, True, (255, 255, 255))
    screen.blit(label, (10, 665))

    pygame.display.flip()

pygame.quit()
