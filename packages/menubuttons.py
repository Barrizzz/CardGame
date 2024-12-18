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
        shadow_color = (50, 50, 50)  # Dark gray shadow color

        # Render the text surface (the boolean value in the middle is for anti-aliasing)
        text_surface = self.font.render(self.text, True, text_color)  # White color
        
        # Gets the text rectangle and centers it around the button position
        self.text_rect = text_surface.get_rect(center = (self.pos_x, self.pos_y))

        # Create a shadow rectangle behind the text
        shadow_rect = self.text_rect.copy()
        shadow_rect.inflate_ip(15, 15)  # Adds padding

        # Draw the shadow rectangle and then the text
        pygame.draw.rect(surface, shadow_color, shadow_rect, border_radius=10) # Draw the shadow rectangle with a certain border radius
        surface.blit(text_surface, self.text_rect.topleft) # Blit the text surface to the screen

    def mouse_hover(self, mouse_pos):
        # Check if the mouse is hovering over the button
        if self.text_rect and self.text_rect.collidepoint(mouse_pos):
            return True
        return False
    
    # Mouse hover checker and mouse actions
    def mouse_hover_checker(self, button, mouse_pos, screen):
        if button.mouse_hover(mouse_pos):
            button.render_text(screen, (173, 7, 255))  # Change color to purple when hovered
        else:
            button.render_text(screen)

