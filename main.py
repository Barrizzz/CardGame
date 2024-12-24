import random as rnd
import pygame, sys
from packages.menubuttons import Buttons
from packages.title import Title
from packages.cardanimation import Cardanimation
from packages.card_randomizer import Cardrandomizer
from packages.showing_cards import Cardfaces
from packages.jumpscares import Jumpscares
from packages.music import Music
pygame.init()
pygame.mixer.init()

# Setting up the display
screen = pygame.display.set_mode((1000, 600))

# Clock and FPS
clock = pygame.time.Clock()
FPS = 120

# Pygame icon image, and caption
icon = pygame.image.load("sprites/cardface/bar_card.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Match The Cards")

# Background Image
image_bg = pygame.image.load("sprites/background.jpg")
image_bg = pygame.transform.scale(image_bg, (1000, 600))

# Card Back Image
card_back_deck = pygame.image.load("sprites/card_back_cyan.png")
card_back_deck = pygame.transform.scale(card_back_deck, (100, 150))

# Create a list of card back images
card_back_list = [pygame.transform.scale(card_back_deck, (100, 150)) for _ in range(12)]

# Target positions for the cards
divisions = 1000 / 6
target_positions = [
    (divisions - 131, 150), (divisions - 131, 370), (divisions * 2 - 131, 150), (divisions * 2 - 131, 370),
    (divisions * 3 - 131, 370), (divisions * 3 - 131, 150), (divisions * 4 - 131, 370), (divisions * 4 - 131, 150),
    (divisions * 5 - 131, 370), (divisions * 5 - 131, 150), (divisions * 6 - 131, 150), (divisions * 6 - 131, 370)
]

# Fonts
title_font = pygame.font.Font("fonts/forward.ttf", 72)
font = pygame.font.Font("fonts/eurostile.ttf", 60)
font_timer = pygame.font.Font("fonts/eurostile.ttf", 60)

# Title and Buttons
title_text = Title(500, 150, "MATCH THE CARDS", title_font)
start_button = Buttons(500, 320, "Start Game", font)
quit_button = Buttons(500, 420, "Quit", font)

'''Configurations'''
main_time = 60 # Main countdown time in seconds
main_countdown_time = main_time # This is to ensure that the initial countdown is 60 seconds
minimum_time = (8, 12) # Minimum countdown time

# Configure the main volume
volume = 0.2

# Music
music = Music(volume)

'''Round tracker'''
current_round = 0

def game_menu():
    global current_round

    music.play_main_music()
    current_round = 0 # Resets the current_round when it is in the game menu (when the main game is done)

    while True:
        mouse_pos = pygame.mouse.get_pos()  # Update the mouse position

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the close button
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicks the mouse
                if start_button.mouse_hover(mouse_pos): # Checks the postion of the mouse, if it's on the start_button, start the main game             
                    start_main_game()
                elif quit_button.mouse_hover(mouse_pos): # Checks the postion of the mouse, if it's on the quit_button, quit the game
                    pygame.quit()
                    sys.exit()

        screen.blit(image_bg, (0, 0)) # Blit the image background
        title_text.render_title(screen) # Render the title

        # Checks mouse positions for hover effect
        start_button.mouse_hover_effect(start_button, mouse_pos, screen)
        quit_button.mouse_hover_effect(quit_button, mouse_pos, screen)
       
        pygame.display.flip() # Update the display
        clock.tick(FPS) # Control the frame rate
    
def start_main_game():
    global main_countdown_time, main_time, decrement, current_round

    # Updates the current_round
    current_round += 1

    # Start Animations
    animation = Cardanimation()
    animation.start_animation(screen, card_back_list, target_positions, image_bg)

    # To randomize the cards
    random = Cardrandomizer()

    # Randomize cards, and show cards
    random.create_random_cards()
    random_card_list = random.get_random_card_list() # This list contains the name of the cards that will be displayed
    random_card_list_blit = random.get_random_card_list_blit() # This list contains the cards surfaces that will be blitted

    #print(random_card_list)
    #print(random_card_list_blit)
    animation.memorize_cards(screen, image_bg, font_timer, target_positions, random_card_list_blit)
    
    # Accessing the class for opening the card faces
    show_card = Cardfaces(card_back_deck, card_back_list, random_card_list_blit, target_positions)

    flipped_card_indexes = []  # Track indexes of flipped cards, which is going to be the same as the indexes of random_card_list
    turn_card_back = False  # Flag to indicate whether to turn back the cards after a match

    # Bonus time and time penalty system
    track_success_attempts = 0 # Track the successive success attempts
    track_fail_attempts = 0 # Track the successive fail attempts
    
    # This is if the success attempt is three in a row, this is for checking if the success attempt reaches three in a row again
    no_more_failures_attempts = False

    '''The game will access the data of sucessive fail or success attempts using the index in these variables'''
    difficulty_level_1 = [3, 3, 3] # This is the first difficulty level, 3 and 3 means the amount of success attempts so that the bonus time is added, the last 3 is for the failed attempts
    difficulty_level_2 = [4, 2, 2] # This is the second difficulty level, 4 and 2 means the amount of success attempts so that the bonus time is added, the last 2 is for the failed attempts
    difficulty_level_3 = [6, 10, 1] # This is the third difficulty level, 6 means the amount of success attempts so that the bonus time is added, why 10 because it is impossible for the user to have that much more success attempts, and 1 is for the failed attempts

    # Jumpscares
    jumpscare = Jumpscares(volume)
    display_jumpscare = False
    display_final_jumpscare = False
    jumpscare_time = 0  # Initialize jumpscare_time
    death_screen = None  # Initialize death_screen variable

    jumpscareType2 = False  # Add a flag to control the display flip
    fadeout_alpha = 255  # Initialize fadeout alpha value

    pulse_size = 60  # Initialize pulse size
    pulse_size_direction = 1  # Initialize pulse size direction

    # Get the start_ticks right before the game loop starts
    start_ticks = pygame.time.get_ticks()

    while True:
        card_rects = show_card.get_card_rect()  # Get the card rects
        mouse_pos = pygame.mouse.get_pos()  # Update mouse position

        if current_round <= 10:
            difficulty_level = difficulty_level_1
        elif 10 < current_round <= 30:
            difficulty_level = difficulty_level_2
        elif current_round > 30:
            difficulty_level = difficulty_level_3

        '''Event handling'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not turn_card_back and not display_jumpscare:
                for i, rect in enumerate(card_rects):
                    if rect.collidepoint(mouse_pos) and not show_card.flipped_cards[i]:
                        show_card.set_flipped_cards(i)
                        flipped_card_indexes.append(i)

                        if len(flipped_card_indexes) == 2: # If the user has flipped two cards
                            index1, index2 = flipped_card_indexes
                            if random_card_list[index1] == random_card_list[index2]: # As we can see we use random_card_list's index for matching
                                flipped_card_indexes.clear()  # Reset the list for the next pair
                                waiting_time = pygame.time.get_ticks() + 1000  # Set the time to wait before starting the game again
                                
                                track_success_attempts += 1
                                track_fail_attempts = 0
                            else:
                                turn_card_back = True
                                turning_time = pygame.time.get_ticks() + 700 # Set the time to turn back cards
                                
                                track_fail_attempts += 1
                                track_success_attempts = 0
                                no_more_failures_attempts = False # Set to false since the user failed

        '''Turn back non-matching cards after a delay'''
        if turn_card_back and pygame.time.get_ticks() >= turning_time:
            show_card.set_flipped_cards(flipped_card_indexes[0], False)
            show_card.set_flipped_cards(flipped_card_indexes[1], False)
            flipped_card_indexes.clear()
            turn_card_back = False

        '''Very funny jumpscare mechanism'''
        if track_fail_attempts == difficulty_level[2] and not display_jumpscare: # If the user fails a certain amount of times in a row and a jumpscare is not displayed
            display_jumpscare = True # Set the display_jumpscare to True
            
            decrement = rnd.randint(3, 5)  # Set the decrement when the user fails
            main_countdown_time -= decrement
            
            jumpscare_time = pygame.time.get_ticks() + 2000  # Set jumpscare display duration

        if display_jumpscare:
            # Stop all the background music
            music.stop_all_music()

            # Finding the jumpscare type according to the music played
            if jumpscare.current_sound_name != 'ah_hell_nah.mp3': # This is assumed as jumpscareType1
                jumpscare.display_jumpscare(screen)
                pygame.display.flip()
            else:
                jumpscareType2 = True

            if pygame.time.get_ticks() >= jumpscare_time:
                display_jumpscare = False # Stops the parent if statement

                # Resets jumpscare and track attempts
                jumpscare.reset_jumpscare()
                track_fail_attempts = 0
                track_success_attempts = 0

                music.play_weird_music() # Play the weird music

        # Render background and cards (This creates the flickering jumpscare effect, since the card is being rendered after the jumpscare), fun fact it was initially a bug but then I decided to use it :)
        screen.blit(image_bg, (0, 0))
        show_card.render_cards()

        '''This is all about time management and the countdown timer'''
        # Calculate remaining time
        seconds_left = main_countdown_time - (pygame.time.get_ticks() - start_ticks) // 1000 # Divided by 100 because pygame ticks is in miliseconds
        if seconds_left < 0: seconds_left = 0 # Ensure the time does not go below zero

        # Render the countdown timer at the middle top with pulsing effect for the last 10 seconds
        if seconds_left <= 10: # If the time is less than 10 seconds
            if 3 < seconds_left <= 5: 
                pulse_size += pulse_size_direction * 2  # By multiplying by two, it means the time it takes for the font to get big is faster
            elif seconds_left <= 3: 
                pulse_size += pulse_size_direction * 4  # By multiplying by three, it means the time it takes for the font to get big is faster than before
            else:
                pulse_size += pulse_size_direction # For each iteration the pulse size (basically the font size) will be added by 1 or subtracted by 1

            # If the pulse size reaches 100 or more, it will be subtraction else addition
            if pulse_size <= 60 or pulse_size >= 100: 
                pulse_size_direction *= -1 # Changing the direction of the pulse size by multiplying with -1, if it then reaches 60 or less, it will change the direction (since -1 * -1 = 1)

            font_timer_pulse = pygame.font.Font("fonts/eurostile.ttf", pulse_size)
            timer_text = font_timer_pulse.render(str(seconds_left), True, (255, 0, 0))
        else:
            timer_text = font_timer.render(str(seconds_left), True, (255, 255, 255))
        
        timer_text_rect = timer_text.get_rect(center=(500, 70))  # get the rect of the text and centers it to (500, 70)
        screen.blit(timer_text, timer_text_rect)  # Draw the timer text

        '''Bonus time and time penalty system'''
        if track_success_attempts == difficulty_level[0] and not no_more_failures_attempts: # Note: no_more_failures_attempts is initially False
            main_countdown_time += rnd.randint(4, 7) # Add bonus time between (4-7), for 3 successive success attempts
            track_success_attempts = 0
            no_more_failures_attempts = True # Set the flag to True, so that it can check if 3 more sucsessful attempts are made
        elif track_success_attempts == difficulty_level[1] and no_more_failures_attempts:
            main_countdown_time += rnd.randint(10, 12) # Add bonus time between (10-12), for 6 successive success attempts
            track_success_attempts = 0
            no_more_failures_attempts = False # Resets the flag

        '''Some logic on the countdown music'''
        if seconds_left <= 25 and seconds_left > 20:
            music.play_countdown_sounds(0)
        elif seconds_left <= 20 and seconds_left > 10:
            music.play_countdown_sounds(1)
        elif seconds_left <= 10 and seconds_left > 5:
            music.play_countdown_sounds(2)
        elif seconds_left <= 5 and seconds_left > 0:
            music.play_countdown_sounds(3)
            
        '''More about jumpscare mechanism (Jumpscare Type 2 non-flickering)'''
        if jumpscareType2:
            jumpscare.display_jumpscare(screen)
            # Fadeout effect
            if fadeout_alpha > 0:
                # Create a fadeout surface, and set the alpha value
                fadeout_surface = pygame.Surface((1000, 600))
                fadeout_surface.set_alpha(fadeout_alpha)
                fadeout_surface.fill((0, 0, 0))

                # Blit the fadeout surface
                screen.blit(fadeout_surface, (0, 0))

                fadeout_alpha -= 5  # Decrease alpha value for each iteration, creating a fadeout effect
            if pygame.time.get_ticks() >= (jumpscare_time - 200): # Make the jumpscare time a little faster
                display_jumpscare = False
                jumpscareType2 = False

                # Resets jumpscare and track attempts
                jumpscare.reset_jumpscare()
                track_fail_attempts = 0
                track_success_attempts = 0

                # Play the weird music
                music.play_weird_music()
                fadeout_alpha = 255  # Resets the fadeout alpha value

        '''This is if the player won'''
        # Start the game again if all the cards are facing up
        if all(show_card.flipped_cards) and pygame.time.get_ticks() >= waiting_time: # Check if flipped_cards list is all True and the waiting time is over, so that the last card can still be shown
            main_countdown_time = seconds_left # Calculate the remaining time to be set to the main time for the next round
            if main_countdown_time <= 10: main_countdown_time = rnd.randint(minimum_time[0], minimum_time[1])  # Minimum countdown time
            start_main_game()  # Restart the game

        '''This is if the timer ran out (Player lose)'''
        # Break the loop when countdown reaches zero
        if seconds_left == 0 and not display_final_jumpscare and not all(show_card.flipped_cards):
            track_fail_attempts = 0 # So that if the user is in a jumpscare phase, it will exit it in the next iteration
            if display_jumpscare: display_jumpscare = False # Same as before, so that the death screen and the flickering jumpscare does not collide
            
            display_final_jumpscare = True
            jumpscare_time = pygame.time.get_ticks() + 5000
            
            # To ensure that the death screen is only taken one time
            if death_screen is None:
                death_screen = jumpscare.get_death_screen()  # Store the death screen image
                jumpscare.stop_jumpscare_sounds()  # Stop all the jumpscare sounds
                jumpscare.play_death_screen_sound()  # Play the death screen sound

        if display_final_jumpscare:
            # Blit the image and text
            screen.blit(death_screen, (0, 0))  # Blit the death_screen image
            lose_text = font_timer.render("You Lose!", True, (255, 0, 0))
            lose_text_rect = lose_text.get_rect(center=(500, 70))
            screen.blit(lose_text, lose_text_rect)

            # Stops all the music including the countdown music
            music.stop_all_music()
            music.stop_all_countdown_music()

            # If the current game tick is bigger than the jumpscare_time which is 5 seconds
            if pygame.time.get_ticks() >= jumpscare_time:
                jumpscare.reset_jumpscare() # Stop the death screen

                main_countdown_time = main_time # Set the countdown time back to the main time, because we are going to go back to the main menu
                decrement = 0 # Set the decrement back to zero

                jumpscare.stop_jumpscare_sounds() # Stop the sound

                display_final_jumpscare = False # Stop the parent if statement
                game_menu() # Go back to main menu

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Control the frame rate

# Start the game menu
game_menu()
