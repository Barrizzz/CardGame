import pygame
from packages.menubuttons import Buttons
pygame.init()

class Title(Buttons): # Inheritance from Buttons class
    def render_title(self, surface):
        # Render the text surface
        text_surface = self.font.render(self.text, True, (255, 255, 255))  # White color
        text_rect = text_surface.get_rect(center = (self.pos_x, self.pos_y))

        surface.blit(text_surface, text_rect)
