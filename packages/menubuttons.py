import pygame
pygame.init()

class Buttons:
    def __init__(self, pos_x, pos_y, text, font):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = text
        self.font = font

    def render_text(self, surface):
        # Shadow settings
        shadow_padding = 14  # Padding around the text for the shadow
        shadow_color = (50, 50, 50)  # Dark gray shadow color

        # Render the text surface
        text_surface = self.font.render(self.text, True, (255, 255, 255))  # White color
        text_rect = text_surface.get_rect()
        text_rect.center = (self.pos_x, self.pos_y)

        # Create a shadow rectangle behind the text
        shadow_rect = text_rect.copy()
        shadow_rect.inflate_ip(shadow_padding, shadow_padding)  # Add padding to make it larger

        # Draw the shadow rectangle behind the text
        pygame.draw.rect(surface, shadow_color, shadow_rect, border_radius=5)  # Adjust `border_radius` for rounded corners

        # Draw the main text at the centered position
        surface.blit(text_surface, text_rect.topleft)
