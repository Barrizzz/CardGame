import pygame, sys
from packages.menubuttons import Buttons
from packages.title import Title
pygame.init()

screen = pygame.display.set_mode((1000, 600)) # Setting up the window (Width, height)
clock = pygame.time.Clock() # Setting up the clock
FPS = 60 # Initialize the FPS
width = 90
height = 140

image_bg = pygame.image.load("sprites/background.jpg")
image_bg = pygame.transform.scale(image_bg, (1000, 600))
card_back_deck = pygame.image.load("sprites/card_back_cyan.png")
card_back_deck = pygame.transform.scale(card_back_deck, (width, height))
card_back1 = pygame.transform.scale(card_back_deck, (width, height))
card_back2 = pygame.transform.scale(card_back_deck, (width, height))
card_back3 = pygame.transform.scale(card_back_deck, (width, height))

# Define initial positions
card_pos = (441, 9) # Initial x, y position of the card
target_pos = (100, 100)  # Target x, y position where the card should stop  
animation_speed = (20, 5) # Animation speed for the card movement



title_font = pygame.font.Font("fonts/forward.ttf", 70)
font = pygame.font.Font("fonts/eurostile.ttf", 40)

title_text = Title(500, 150, "MATCH THE CARDS", title_font)
start_button = Buttons(500, 300, "Start Game", font)
options_button = Buttons(500, 370, "Options", font)
quit_button = Buttons(500, 440, "Quit", font)

def game_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.mouse_hover(event.pos):
                    main_game()
                elif options_button.mouse_hover(event.pos):
                    options()
                elif quit_button.mouse_hover(event.pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()

        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Rendering
        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))
        title_text.render_title(screen)

        mouse_hover_checker(start_button, mouse_pos)
        mouse_hover_checker(options_button, mouse_pos)
        mouse_hover_checker(quit_button, mouse_pos)

        pygame.display.flip()
        clock.tick(FPS)
        
def mouse_hover_checker(button_type, mouse_pos):
# Check and render each button with hover effect
    if button_type.mouse_hover(mouse_pos):
        button_type.font.set_underline(True) # Underline effect on hover
        button_type.render_text(screen, (173, 7, 255))  # Red when hovered
    else:
        button_type.font.set_underline(False)
        button_type.render_text(screen)  # Defaults to white

def main_game():
    global card_pos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))
        screen.blit(card_back_deck, (450, 0))
        
        screen.blit(card_back1, (447, 3))
        screen.blit(card_back2, (444, 6))

        # Card placing animation
        card_x, card_y = card_pos  # Unpack current position
        target_x, target_y = target_pos  # Unpack target position
        animation_speed_x, animation_speed_y = animation_speed

        # Move the card in the x direction
        if card_x > target_x:  # Continue moving until it reaches the target x
            card_x -= animation_speed_x  # Move left by animation_speed_x
        # Move the card in the y direction
        if card_y < target_y:  # Move down until it reaches the target y
            card_y += animation_speed_y  # Move down by animation_speed_y
        elif card_y > target_y:  # Move up if it's above target_y
            card_y -= animation_speed_y  # Move up by animation_speed_y

        # Prevent bouncing by snapping to target position
        if target_x <= card_x <= target_x + animation_speed_x:
            card_x = target_x  # Snap to target_x
        if target_y <= card_y <= target_y + animation_speed_y:
            card_y = target_y  # Snap to target_y

        card_pos = (card_x, card_y)  # Update card_pos with new position
        screen.blit(card_back3, card_pos)  # Draw the card at the new position


        pygame.display.flip()
        clock.tick(FPS)

def options():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)


#Start the game menu
game_menu()
pygame.quit()
sys.exit()



