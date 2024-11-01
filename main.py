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
    image_bg = pygame.image.load("sprites/background.jpg") #Loading up the image from the folder
    image_bg = pygame.transform.scale(image_bg, (1000, 600)) #Scaling the image into the same as the window (Since this is a background img)
    
    while True: #Game loop
        for event in pygame.event.get(): #Event handler loop (Continously checking inputs from the player)
            if event.type == pygame.QUIT: #End the function when the player click the exit button
                return
            

        #Image rendering
        screen.fill((0, 0, 0)) #Filling the screen with background color black
        screen.blit(image_bg, (0, 0)) #Placing the image into the screen

        title_text.render_title(screen)
        start_button.render_text(screen)
        options_button.render_text(screen)
        quit_button.render_text(screen)
    

        pygame.display.flip() #Refreshes the screen
        clock.tick(FPS) #Set the tick to the FPS


#Start the game menu
game_menu()
pygame.quit()
sys.exit()



