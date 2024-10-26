import pygame

class Buttons:
    def __init__(self, text, width, height, pos):
        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#497dd9'

        # text
        self.text_surface = pygame.font.Font(None, 30).render(text, True, '#FFFFFF')
        self.text_rect = self.text_surface.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit(self.text_surface, self.text_rect)
