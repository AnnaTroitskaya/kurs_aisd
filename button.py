import pygame
import sys

class Text:
    def __init__(self, text, size, color, x, y):
        self.text = text
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont('Verdana', self.size)
        self.surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont('Verdana', 40)
            text = font.render(self.text, True, (30, 40, 20))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_clicked(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            return True
        return False