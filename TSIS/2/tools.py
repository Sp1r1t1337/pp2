import pygame

def flood_fill(surface, x, y, new_color):
    """Fills a closed area with a new color using a stack-based algorithm."""
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    pixels_to_fill = [(x, y)]
    width, height = surface.get_size()

    while pixels_to_fill:
        curr_x, curr_y = pixels_to_fill.pop()
        if not (0 <= curr_x < width and 0 <= curr_y < height):
            continue
        
        if surface.get_at((curr_x, curr_y)) == target_color:
            surface.set_at((curr_x, curr_y), new_color)
            pixels_to_fill.append((curr_x + 1, curr_y))
            pixels_to_fill.append((curr_x - 1, curr_y))
            pixels_to_fill.append((curr_x, curr_y + 1))
            pixels_to_fill.append((curr_x, curr_y - 1))

class TextTool:
    def __init__(self):
        self.active = False
        self.text = ""
        self.pos = (0, 0)
        self.font = pygame.font.SysFont("Arial", 24)

    def start(self, pos):
        self.active = True
        self.pos = pos
        self.text = ""

    def add_char(self, char):
        self.text += char

    def backspace(self):
        self.text = self.text[:-1]

    def render(self, surface, color):
        if self.active:
            text_surf = self.font.render(self.text + "|", True, color)
            surface.blit(text_surf, self.pos)
