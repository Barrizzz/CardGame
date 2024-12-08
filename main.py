import pygame, sys
from random import randint
from packages.menubuttons import Buttons
from packages.title import Title
from packages.cardanimation import Cardanimation
from packages.card_randomizer import Cardrandomizer
from packages.showing_cards import Cardfaces
pygame.init()
pygame.mixer.init()

# Setting up the display
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Countdown Timer")
clock = pygame.time.Clock()
FPS = 60

# Background Image
image_bg = pygame.image.load("sprites/background.jpg")
image_bg = pygame.transform.scale(image_bg, (1000, 600))

# jumpscares
jumpscare_load = [pygame.image.load("sprites/mikel.jpg"), pygame.image.load("sprites/jason.png")]
jumpscares = []
for i in jumpscare_load:
    jumpscares.append(pygame.transform.scale(i, (1000, 600)))
#print(jumpscares)

#Volumes
volume = 0.1

# Card Back Image
card_back_deck = pygame.image.load("sprites/card_back_cyan.png")
card_back_deck = pygame.transform.scale(card_back_deck, (100, 150))

# Create a list of card images
card_list = [pygame.transform.scale(card_back_deck, (100, 150)) for _ in range(12)]

# Target positions for the cards
divisions = 1000 / 6
target_positions = [
    (divisions - 131, 150), (divisions - 131, 370), (divisions * 2 - 131, 150), (divisions * 2 - 131, 370),
    (divisions * 3 - 131, 370), (divisions * 3 - 131, 150), (divisions * 4 - 131, 370), (divisions * 4 - 131, 150),
    (divisions * 5 - 131, 370), (divisions * 5 - 131, 150), (divisions * 6 - 131, 150), (divisions * 6 - 131, 370)
]

# Fonts
title_font = pygame.font.Font("fonts/forward.ttf", 70)
font = pygame.font.Font("fonts/eurostile.ttf", 40)
font_timer = pygame.font.Font("fonts/eurostile.ttf", 60)

# Title and Buttons
title_text = Title(500, 150, "MATCH THE CARDS", title_font)
start_button = Buttons(500, 300, "Start Game", font)
options_button = Buttons(500, 370, "Options", font)
quit_button = Buttons(500, 440, "Quit", font)

main_time = 60 # Main countdown time in seconds
main_countdown_time = main_time # This is to ensure that the initial countdown is 60 seconds

# This is for sounds
jumpscare_sound = pygame.mixer.Sound("sounds/ascending_jumpscare.mp3")

def game_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()  # Update mouse position

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.mouse_hover(mouse_pos):             
                    start_main_game()
                elif options_button.mouse_hover(mouse_pos):
                    options()
                elif quit_button.mouse_hover(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(image_bg, (0, 0))
        title_text.render_title(screen)
       
        start_button.mouse_hover_checker(start_button, mouse_pos, screen)
        options_button.mouse_hover_checker(options_button, mouse_pos, screen)
        quit_button.mouse_hover_checker(quit_button, mouse_pos, screen)

        pygame.display.flip()
        clock.tick(FPS)

def options():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))  # Draw the background

        pygame.display.flip()
        clock.tick(FPS)
    
def start_main_game():
    global main_countdown_time, main_time, decrement

    # Start Animations
    animation = Cardanimation()
    animation.start_animation(screen, card_list, target_positions, image_bg)

    # Randomize the cards
    random_card_list = []
    random_card_list_blit = []
    random = Cardrandomizer(random_card_list, random_card_list_blit)

    # Randomize cards, and show cards
    random.create_random_cards()
    random_card_list = random.random_card_list
    random_card_list_blit = random.random_card_list_blit

    #print(random_card_list)
    #print(random_card_list_blit)
    animation.memorize_cards(screen, image_bg, font_timer, target_positions, random_card_list_blit)

    start_ticks = pygame.time.get_ticks()
    # Accessing the class for opening the card faces
    open_card = Cardfaces(card_back_deck, card_list, random_card_list_blit, target_positions)

    flipped_card_indexes = []  # Track indexes of flipped cards, which is going to be the same as the indexes of random_card_list
    turn_card_back = False  # Flag to indicate whether to turn back the cards after a match

    track_success_attempts = 0 # Track the successive success attempts
    track_fail_attempts = 0 # Track the successive fail attempts
    
    # Jumpscare variables
    display_jumpscare = False
    display_final_jumpscare = True
    jumpscare_time = 0

    select_jumpscare_flag = True

    # This is if the success attempt is three in a row, this is for checking if the success attempt reaches five in a row
    no_more_failures_attempts = False

    while True:
        card_rects = open_card.get_card_rect()  # Get the card rects
        mouse_pos = pygame.mouse.get_pos()  # Update mouse position
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not turn_card_back:
                for i, rect in enumerate(card_rects):
                    if rect.collidepoint(mouse_pos) and not open_card.flipped_cards[i]:
                        open_card.set_flipped_cards(i)
                        flipped_card_indexes.append(i)

                        if len(flipped_card_indexes) == 2:
                            index1, index2 = flipped_card_indexes
                            if random.random_card_list[index1] == random.random_card_list[index2]: # As we can see we use random_card_list's index for matching
                                flipped_card_indexes.clear()  # Reset the list for the next pair
                                waiting_time = pygame.time.get_ticks() + 1000  # Set the time to wait before starting the game again
                                track_success_attempts += 1
                                track_fail_attempts = 0
                            else:
                                turn_card_back = True
                                turning_time = pygame.time.get_ticks() + 700 # Set the time to turn back cards
                                track_fail_attempts += 1
                                track_success_attempts = 0
                                no_more_failures_attempts = False

        # Turn back non-matching cards after a delay
        if turn_card_back and pygame.time.get_ticks() >= turning_time:
            open_card.set_flipped_cards(flipped_card_indexes[0], False)
            open_card.set_flipped_cards(flipped_card_indexes[1], False)
            flipped_card_indexes.clear()
            turn_card_back = False

        '''Very funny jumpscare mechanism'''
        if select_jumpscare_flag: 
            select_jumpscare = randint(0, 1)
            select_jumpscare_flag = False

        # Render jumpscare conditions
        if track_fail_attempts == 3 and not display_jumpscare: # display_jumpscare is initially False
            display_jumpscare = True
            jumpscare_sound.play()
            jumpscare_sound.set_volume(volume)
            jumpscare_time = pygame.time.get_ticks() + 1000
        
        # Render the jumpscare image
        if display_jumpscare:
            screen.blit(jumpscares[select_jumpscare], (0, 0))
            pygame.display.flip()  # Update the display to show the jumpscare image
            if pygame.time.get_ticks() >= jumpscare_time:
                main_countdown_time -= randint(5, 10) # Random time penalty
                track_fail_attempts = 0
                select_jumpscare_flag = True
                display_jumpscare = False
        
        # Render background
        screen.blit(image_bg, (0, 0))
        # Render all cards
        open_card.render_cards()

        '''This is all about the time management'''
        # Calculate remaining time
        seconds_left = main_countdown_time - (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds_left < 0: seconds_left = 0

        # Render the countdown timer at the middle top
        timer_text = font_timer.render(str(seconds_left), True, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(center=(500, 70))  # get the rect of the text and centers it to (500, 70)
        screen.blit(timer_text, timer_text_rect)  # Draw the timer text

        '''This is if the player won'''
        # Start the game again if all the cards are facing up
        if all(open_card.flipped_cards) and pygame.time.get_ticks() >= waiting_time: # Check if flipped_cards list is all True and the waiting time is over, so that the last card can still be shown
            main_countdown_time = seconds_left # Calculate the remaining time to be set to the main time for the next round
            decrement = 0 #randint(3, 5) # Set the decrement when the user won, and starting the game again
            main_countdown_time -= decrement  # Ensure the countdown time is decremented when the player wins
            if main_countdown_time <= 10: main_countdown_time = randint(8, 12)  # Ensure minimum countdown time
            start_main_game()  # Restart the game

        '''Bonus time and time penalty system'''
        if track_success_attempts == 3:
            main_countdown_time += randint(4, 7) 
            track_success_attempts = 0
            no_more_failures_attempts = True
        elif track_success_attempts == 2 and no_more_failures_attempts:
            main_countdown_time += randint(10, 12)
            track_success_attempts = 0
            no_more_failures_attempts = False

        '''This is if the timer ran out (Player lose)'''
        # Break the loop when countdown reaches zero
        if seconds_left == 0 and display_final_jumpscare: 
            display_final_jumpscare = False
            jumpscare_time = pygame.time.get_ticks() + 3000
            jumpscare_sound.play()
            jumpscare_sound.set_volume(volume)

        if not display_final_jumpscare:
            screen.blit(jumpscares[select_jumpscare], (0, 0))
            lose_text = font_timer.render("You Lose!", True, (255, 0, 0))
            lose_text_rect = lose_text.get_rect(center=(500, 70))
            screen.blit(lose_text, lose_text_rect)
            if pygame.time.get_ticks() >= jumpscare_time:
                display_final_jumpscare = False
                main_countdown_time = main_time
                decrement = 0
                game_menu()

        pygame.display.flip()  # Update the display
        clock.tick(FPS + 100) # make the fps bigger

# Start the game menu
game_menu()
