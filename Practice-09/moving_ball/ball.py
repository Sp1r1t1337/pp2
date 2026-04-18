import pygame

class Ball:
    def __init__(self, x, y, radius, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity = 20

    def move(self, direction):
        
        if direction == "UP":
            if self.y - self.velocity >= self.radius:
                self.y -= self.velocity
        elif direction == "DOWN":
            if self.y + self.velocity <= self.screen_height - self.radius:
                self.y += self.velocity
        elif direction == "LEFT":
            if self.x - self.velocity >= self.radius:
                self.x -= self.velocity
        elif direction == "RIGHT":
            if self.x + self.velocity <= self.screen_width - self.radius:
                self.x += self.velocity

    def draw(self, surface):
        
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
