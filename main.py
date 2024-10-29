import pygame, sys
from packages.menubuttons import Buttons
pygame.init()

screen = pygame.display.set_mode((1000, 600)) #Setting up the window (Width, height)
clock = pygame.time.Clock() #Setting up the clock
FPS = 60 #Initialize the FPS
Gui_font = pygame.font.Font(None, 30) #Changing the font size (The first argument is on the font-type)

button1 = Buttons('Start', 200, 40, (400, 200))

def game_menu():
    image_bg = pygame.image.load("blits/background.jpg") #Loading up the image from the folder
    image_bg = pygame.transform.scale(image_bg, (1000, 600)) #Scaling the image into the same as the window (Since this is a background img)
    
    while True: #Game loop
        for event in pygame.event.get(): #Event handler loop (Continously checking inputs from the player)
            if event.type == pygame.QUIT: #End the function when the player click the exit button
                return 

        #Image rendering
        screen.fill((0, 0, 0)) #Filling the screen with background color black
        screen.blit(image_bg, (0, 0)) #Placing the image into the screen

        #Draw the button
        button1.draw(screen)
        
        
        pygame.display.update() #Updating the display
        clock.tick(FPS) #Set the tick to the FPS


#Start the game menu
game_menu()
pygame.quit()
sys.exit()



