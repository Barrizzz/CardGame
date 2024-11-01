import pygame
pygame.init()

class Buttons:
    def __init__(self, pos_x, pos_y, text, font):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = text
        self.font = font
        self.text_rect = None  # Store the text rect for hover checks

    def render_text(self, surface, text_color=(255, 255, 255)):
        # Shadow settings
        shadow_padding = 14  # Padding around the text for the shadow
        shadow_color = (50, 50, 50)  # Dark gray shadow color

        # Render the text surface
        text_surface = self.font.render(self.text, True, text_color)  # White color
        # Gets the text rectangle and centers it around the button position
        self.text_rect = text_surface.get_rect(center = (self.pos_x, self.pos_y))

        # Create a shadow rectangle behind the text
        shadow_rect = self.text_rect.copy()
        shadow_rect.inflate_ip(shadow_padding, shadow_padding)  # Add padding

        # Draw the shadow rectangle and then the text
        pygame.draw.rect(surface, shadow_color, shadow_rect, border_radius=5)
        surface.blit(text_surface, self.text_rect.topleft)

    def mouse_hover(self, mouse_pos):
        # Check if the mouse is hovering over the button
        if self.text_rect and self.text_rect.collidepoint(mouse_pos):
            return True
        return False
    
