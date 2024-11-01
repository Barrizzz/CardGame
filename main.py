import pygame, sys
from packages.menubuttons import Buttons
from packages.title import Title
pygame.init()

screen = pygame.display.set_mode((1000, 600)) # Setting up the window (Width, height)
clock = pygame.time.Clock() # Setting up the clock
FPS = 60 # Initialize the FPS

image_bg = pygame.image.load("sprites/background.jpg")
image_bg = pygame.transform.scale(image_bg, (1000, 600))

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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))

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



