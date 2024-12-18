import random as rnd
import pygame, sys
from packages.menubuttons import Buttons
from packages.title import Title
from packages.cardanimation import Cardanimation
from packages.card_randomizer import Cardrandomizer
from packages.showing_cards import Cardfaces
from packages.jumpscares import Jumpscares
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

# Main volume
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
title_font = pygame.font.Font("fonts/forward.ttf", 75)
font = pygame.font.Font("fonts/eurostile.ttf", 55)
font_timer = pygame.font.Font("fonts/eurostile.ttf", 60)

# Title and Buttons
title_text = Title(500, 150, "MATCH THE CARDS", title_font)
start_button = Buttons(500, 320, "Start Game", font)
quit_button = Buttons(500, 420, "Quit", font)

main_time = 60 # Main countdown time in seconds
main_countdown_time = main_time # This is to ensure that the initial countdown is 60 seconds

# This is for sounds
main_music = pygame.mixer.Sound("sounds/happy_quiz.mp3")
let_it_snow = pygame.mixer.Sound("sounds/let_it_snow.mp3")
thick_of_it = pygame.mixer.Sound("sounds/ThickOfIt_Jazz.mp3")

main_music_list = [main_music, let_it_snow, thick_of_it]
main_music = None

weird_music = pygame.mixer.Sound("sounds/weird_song.mp3")

countdown_25sec = pygame.mixer.Sound("sounds/25_second_countdwn.mp3")
countdown_20sec = pygame.mixer.Sound("sounds/20_second_countdwn.mp3")
countdown_10sec = pygame.mixer.Sound("sounds/10_second_countdwn.mp3")
countdown_5sec = pygame.mixer.Sound("sounds/5_second_countdwn.mp3")

current_countdown_sound = None

jumpscare_sound = pygame.mixer.Sound("sounds/ascending_jumpscare.mp3")
jumpscare_sound2 = pygame.mixer.Sound("sounds/ah_hell_nah.mp3")
plankton_funny = pygame.mixer.Sound("sounds/plankton_funny.mp3")

def game_menu():
    global main_music

    # Play the main music
    main_music = rnd.choice(main_music_list)
    main_music.play(loops = -1)
    if main_music == thick_of_it:
        main_music.set_volume(volume + 0.4)
    else:
        main_music.set_volume(volume + 0.2)

    while True:
        mouse_pos = pygame.mouse.get_pos()  # Update mouse position

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.mouse_hover(mouse_pos):             
                    start_main_game()
                elif quit_button.mouse_hover(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(image_bg, (0, 0))
        title_text.render_title(screen)
       
        start_button.mouse_hover_checker(start_button, mouse_pos, screen)
        quit_button.mouse_hover_checker(quit_button, mouse_pos, screen)

        pygame.display.flip()
        clock.tick(FPS)
    
def start_main_game():
    global main_countdown_time, main_time, decrement, current_countdown_sound, main_music

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
    
    # This is if the success attempt is three in a row, this is for checking if the success attempt reaches five in a row
    no_more_failures_attempts = False

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

    while True:
        card_rects = open_card.get_card_rect()  # Get the card rects
        mouse_pos = pygame.mouse.get_pos()  # Update mouse position
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not turn_card_back and not display_jumpscare:
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

        '''Turn back non-matching cards after a delay'''
        if turn_card_back and pygame.time.get_ticks() >= turning_time:
            open_card.set_flipped_cards(flipped_card_indexes[0], False)
            open_card.set_flipped_cards(flipped_card_indexes[1], False)
            flipped_card_indexes.clear()
            turn_card_back = False

        '''Very funny jumpscare mechanism'''
        if track_fail_attempts == 3 and not display_jumpscare:
            display_jumpscare = True
            decrement = rnd.randint(3, 5)  # Set the decrement when the user fails
            main_countdown_time -= decrement
            jumpscare_time = pygame.time.get_ticks() + 2000  # Set jumpscare display duration

        if display_jumpscare:
            # Stop all the background music
            main_music.stop()
            weird_music.stop()

            # Finding the jumpscare type according to the music played
            if jumpscare.current_sound_name != 'ah_hell_nah.mp3': # This is assumed as jumpscareType1
                jumpscare.display_jumpscare(screen)
                pygame.display.flip()
            else:
                jumpscareType2 = True

            if pygame.time.get_ticks() >= jumpscare_time:
                display_jumpscare = False
                jumpscare.reset_jumpscare()
                track_fail_attempts = 0
                track_success_attempts = 0
                weird_music.play(loops = -1)
                weird_music.set_volume(volume + 0.3)

        # Render background and cards (This creates the flickering jumpscare effect, since the card is being rendered after the jumpscare), fun fact it was initially a bug but then I decided to use it :)
        screen.blit(image_bg, (0, 0))
        open_card.render_cards()

        '''This is all about time management and the countdown timer'''
        # Calculate remaining time
        seconds_left = main_countdown_time - (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds_left < 0: seconds_left = 0

        # Render the countdown timer at the middle top with pulsing effect for the last 10 seconds
        if seconds_left <= 10: # If the time is less than 10 seconds
            if seconds_left <= 5: # Condition for the last 5 seconds
                pulse_size += pulse_size_direction * 2  # By multiplying by two, it means the time it takes for the font to get big is faster
            else:
                pulse_size += pulse_size_direction # For each iteration the pulse size (basically the font size) will be added by 1 or subtracted by 1

            if pulse_size <= 60 or pulse_size >= 100: # If the pulse size reaches 100 or more, it will be subtraction else addition
                pulse_size_direction *= -1

            font_timer_pulse = pygame.font.Font("fonts/eurostile.ttf", pulse_size)
            timer_text = font_timer_pulse.render(str(seconds_left), True, (255, 0, 0))
        else:
            timer_text = font_timer.render(str(seconds_left), True, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(center=(500, 70))  # get the rect of the text and centers it to (500, 70)
        screen.blit(timer_text, timer_text_rect)  # Draw the timer text

        '''Bonus time and time penalty system'''
        if track_success_attempts == 3:
            main_countdown_time += rnd.randint(4, 7) # Add bonus time between (4-7), for 3 successive success attempts
            track_success_attempts = 0
            no_more_failures_attempts = True
        elif track_success_attempts == 2 and no_more_failures_attempts:
            main_countdown_time += rnd.randint(10, 12) # Add bonus time between (10-12), for 5 successive success attempts
            track_success_attempts = 0
            no_more_failures_attempts = False

        '''Some logic on the countdown music'''
        if seconds_left <= 25 and seconds_left > 20:
            main_music.stop()
            weird_music.stop()
            if current_countdown_sound != countdown_25sec:
                if current_countdown_sound:
                    current_countdown_sound.stop()
                countdown_25sec.play(loops = -1)
                countdown_25sec.set_volume(volume + 0.3)
                current_countdown_sound = countdown_25sec
        elif seconds_left <= 20 and seconds_left > 10:
            main_music.stop()
            weird_music.stop()
            if current_countdown_sound != countdown_20sec:
                if current_countdown_sound:
                    current_countdown_sound.stop()
                countdown_20sec.play(loops = -1)
                countdown_20sec.set_volume(volume + 0.3)
                current_countdown_sound = countdown_20sec
        elif seconds_left <= 10 and seconds_left > 5:
            main_music.stop()
            weird_music.stop()
            if current_countdown_sound != countdown_10sec:
                if current_countdown_sound:
                    current_countdown_sound.stop()
                countdown_10sec.play(loops = -1)
                countdown_10sec.set_volume(volume + 0.3)
                current_countdown_sound = countdown_10sec
        elif seconds_left <= 5 and seconds_left > 0:
            main_music.stop()
            weird_music.stop()
            if current_countdown_sound != countdown_5sec: # Check if the current countdown is not the same, so that the logic in this if statement on iterates once
                if current_countdown_sound: # Check if there is a countdown sound playing
                    current_countdown_sound.stop() # Stop it once
                countdown_5sec.play(loops = -1)
                countdown_5sec.set_volume(volume + 0.4)
                current_countdown_sound = countdown_5sec
        elif seconds_left == 0:
            if current_countdown_sound:
                current_countdown_sound.stop()

        '''More about jumpscare mechanism'''
        if jumpscareType2:
            jumpscare.display_jumpscare(screen)
            # Fadeout effect
            if fadeout_alpha > 0:
                fadeout_surface = pygame.Surface((1000, 600))
                fadeout_surface.set_alpha(fadeout_alpha)
                fadeout_surface.fill((0, 0, 0))
                screen.blit(fadeout_surface, (0, 0))
                fadeout_alpha -= 5  # Decrease alpha value for each iteration, creating a fadeout effect
            if pygame.time.get_ticks() >= (jumpscare_time - 200): # Make the jumpscare time a little faster
                display_jumpscare = False
                jumpscareType2 = False
                jumpscare.reset_jumpscare()
                track_fail_attempts = 0
                track_success_attempts = 0
                weird_music.play(loops = -1)
                weird_music.set_volume(volume + 0.3)
                fadeout_alpha = 255  # Reset the fadeout alpha when jumpscare is done

        '''This is if the player won'''
        # Start the game again if all the cards are facing up
        if all(open_card.flipped_cards) and pygame.time.get_ticks() >= waiting_time: # Check if flipped_cards list is all True and the waiting time is over, so that the last card can still be shown
            main_countdown_time = seconds_left # Calculate the remaining time to be set to the main time for the next round
            decrement = 0 #randint(3, 5) # Set the decrement when the user won, and starting the game again
            main_countdown_time -= decrement  # Ensure the countdown time is decremented when the player wins
            if main_countdown_time <= 10: main_countdown_time = rnd.randint(8, 12)  # Ensure minimum countdown time
            start_main_game()  # Restart the game

        '''This is if the timer ran out (Player lose)'''
        # Break the loop when countdown reaches zero
        if seconds_left == 0 and not display_final_jumpscare and not all(open_card.flipped_cards):
            track_fail_attempts = 0 # So that if the user is in a jumpscare phase, it will exit it in the next iteration
            if display_jumpscare: display_jumpscare = False # Same as before, so that the death screen and the flickering jumpscare does not collide
            
            jumpscare.stop_jumpscare_sounds()
            display_final_jumpscare = True
            jumpscare_time = pygame.time.get_ticks() + 5000
            
            if death_screen is None:
                death_screen = jumpscare.get_death_screen()  # Store the death screen image
                plankton_funny.play()
            
            # Stop all the background music
            main_music.stop() 
            weird_music.stop()

        if display_final_jumpscare:
            # Blit the image and text
            screen.blit(death_screen, (0, 0))  
            lose_text = font_timer.render("You Lose!", True, (255, 0, 0))
            lose_text_rect = lose_text.get_rect(center=(500, 70))
            screen.blit(lose_text, lose_text_rect)

            # If the current game tick is bigger than the jumpscare_time which is 5 seconds
            if pygame.time.get_ticks() >= jumpscare_time:
                display_final_jumpscare = False # Stop the parent if statement
                jumpscare.reset_jumpscare() # Stop the death screen
                main_countdown_time = main_time # Set the countdown time back to the main time, because we are going to go back to the main menu
                decrement = 0 # Set the decrement back to zero
                plankton_funny.stop() # Stop the sound
                game_menu() # Go back to main menu

        pygame.display.flip()  # Update the display
        clock.tick(FPS + 80) # make the fps bigger

# Start the game menu
game_menu()
