import pygame
import pygame.freetype

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.freetype.SysFont(None, 30)
        self.active = False
        self.color_inactive = (240, 128, 128) #pygame.Color('lightskyblue3')
        self.color_active = (255, 70, 147)   #pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text_surface, _ = self.font.render(self.text, self.color)

    def handle_event(self, event, list_inp):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    list_help = self.text.strip().split()
                    for item in list_help:
                        list_inp.append(int(item))
                    print(self.text)
                    self.text = 'data received'
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surface, _ = self.font.render(self.text, self.color)

    def update(self):
        width = max(200, self.text_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        self.font.render_to(screen, (self.rect.x+5, self.rect.y+15), self.text, self.color)
        pygame.draw.rect(screen, self.color, self.rect, 2)
