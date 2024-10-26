import pygame
pygame.init()

Gui_font = pygame.font.Font(None, 30) #Changing the font size (The first argument is on the font-type)

class Buttons:
    def __init__(self, text, width, height, pos,):
        #top rectangle
        self.top_rect = pygame.rect(pos, (width, height))
        self.top_color = '#497dd9'

        #text
        self.text_surface = Gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    #draw
    def draw(self):
        pygame.draw.rect()

        pass