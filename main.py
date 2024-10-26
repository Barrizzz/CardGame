import pygame, sys
pygame.init()

class Buttons:
    def __init__(self, text, width, height, pos):
        #top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#497dd9'

        #text
        self.text_surface = Gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    #draw
    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit(self.text_surface, self.text_rect)


screen = pygame.display.set_mode((1000, 600)) #Setting up the window
clock = pygame.time.Clock() #Setting up the clock
FPS = 60 #Initialize the FPS
Gui_font = pygame.font.Font(None, 30) #Changing the font size (The first argument is on the font-type)

button1 = Buttons('Start', 200, 40, (400, 200))

def game_menu():
    image_bg = pygame.image.load("background.jpg") #Loading up the image from the folder
    image_bg = pygame.transform.scale(image_bg, (1000, 600)) #Scaling the image into the same as the window (Since this is a background img)
    
    while True: #Game loop
        for event in pygame.event.get(): #Event handler loop (Continously checking inputs from the player)
            if event.type == pygame.QUIT: #End the function when the player click the exit button
                return 

        #Image rendering
        screen.fill((0, 0, 0)) #Filling the screen with background color black
        screen.blit(image_bg, (0, 0)) #Placing the image into the screen
        button1.draw()
        pygame.display.update() #Updating the display

        clock.tick(FPS) #Set the tick to the FPS


game_menu()
pygame.quit()
sys.exit()