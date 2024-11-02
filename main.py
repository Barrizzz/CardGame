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
    card_pos = (441, 9)  # Initial x, y position of the card
    target_pos = (100, 100)  # Target x, y position where the card should stop  
    animation_speed = (20, 5)  # Animation speed for the card movement

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))
        screen.blit(card_back_deck, (450, 0))
        
        screen.blit(card_back1, (447, 3))
        screen.blit(card_back2, (444, 6))
        
        # Update the position of the card with each frame
        card_pos = card_animation(card_pos, target_pos, animation_speed)
        screen.blit(card_back3, card_pos)

        pygame.display.flip()
        clock.tick(FPS)

def card_animation(card_pos, target_pos, animation_speed):
    # Find the delta_x and delta_y of the card (relative x,y distances)
    delta_x = target_pos[0] - card_pos[0]
    delta_y = target_pos[1] - card_pos[1]

    # Snapping the card if it reaches the target_pos
    if abs(delta_x) == 0 and abs(delta_y) == 0:
        return target_pos

    # Moving the card itself (This is pretty complicated)
    ''' 
    The min function is needed to determine whether the distance or the animation speed is smaller, 
    then it takes the smaller value (this is how you "limit the amount of distance the card take") For example:
    animation speed = 10; 
    delta = 100;
    
    then the image cannot pass the 10px limit, therefore it takes the min() which is 10px

    if it is already close to the target, we need to take the value of delta;
    So that it will not overshoot, and it will be perfectly on target.

    not that these assignment will be run every time the screen updates

    the if and else statements are for determining the direction of movement.
    '''
    move_x = min(abs(delta_x), animation_speed[0]) * (1 if delta_x > 0 else -1) 
    move_y = min(abs(delta_y), animation_speed[1]) * (1 if delta_y > 0 else -1)

    # Update the card's position
    card_x = card_pos[0]
    card_y = card_pos[1]
    card_x += move_x
    card_y += move_y
    card_pos = (card_x, card_y)

    return (card_pos) # Return the updated position


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



