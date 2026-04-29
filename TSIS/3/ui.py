import pygame

class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.font = pygame.font.SysFont("Verdana", 20)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surf, (self.rect.x + (self.rect.width - text_surf.get_width())//2, 
                                 self.rect.y + (self.rect.height - text_surf.get_height())//2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_text(surface, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.SysFont("Verdana", size)
    surf = font.render(text, True, color)
    surface.blit(surf, (x, y))
