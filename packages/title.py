import pygame
pygame.init()

class Title:
    def __init__(self, pos_x, pos_y, text, font):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = text
        self.font = font

    def render_title(self, surface):
        # Render the text surface
        text_surface = self.font.render(self.text, True, (255, 255, 255))  # White color
        text_rect = text_surface.get_rect()
        text_rect.center = (self.pos_x, self.pos_y)

        surface.blit(text_surface, text_rect.topleft)
