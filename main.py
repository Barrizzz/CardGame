import pygame, sys
from packages.menubuttons import Buttons
from packages.title import Title
pygame.init()

screen = pygame.display.set_mode((1000, 600)) #Setting up the window (Width, height)
clock = pygame.time.Clock() #Setting up the clock
FPS = 60 #Initialize the FPS

title_font = pygame.font.Font("fonts/forward.ttf", 70)
font = pygame.font.Font("fonts/eurostile.ttf", 40)

title_text = Title(500, 150, "MATCH THE CARDS", title_font)
start_button = Buttons(500, 300, "Start Game", font)
options_button = Buttons(500, 370, "Options", font)
quit_button = Buttons(500, 440, "Quit", font)

def game_menu():
    image_bg = pygame.image.load("sprites/background.jpg")
    image_bg = pygame.transform.scale(image_bg, (1000, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.mouse_hover(event.pos):
                    print("start")
                elif options_button.mouse_hover(event.pos):
                    print("options")
                elif quit_button.mouse_hover(event.pos):
                    print("quit")

        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Rendering
        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))

        title_text.render_title(screen)

        # Check and render each button with hover effect
        if start_button.mouse_hover(mouse_pos):
            start_button.font.set_underline(True) # Underline effect on hover
            start_button.render_text(screen, (173, 7, 255))  # Red when hovered
        else:
            start_button.font.set_underline(False)
            start_button.render_text(screen)  # Defaults to white

        # Options button color based on hover
        if options_button.mouse_hover(mouse_pos):
            options_button.font.set_underline(True)
            options_button.render_text(screen, (173, 7, 255))  # Red when hovered
        else:
            options_button.font.set_underline(False)
            options_button.render_text(screen)  # Defaults to white

        # Quit button color based on hover
        if quit_button.mouse_hover(mouse_pos):
            quit_button.font.set_underline(True)
            quit_button.render_text(screen, (173, 7, 255))  # Red when hovered
        else:
            quit_button.font.set_underline(False)
            quit_button.render_text(screen)  # Defaults to white

        pygame.display.flip()
        clock.tick(FPS)



#Start the game menu
game_menu()
pygame.quit()
sys.exit()



