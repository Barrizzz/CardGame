import pygame
import sys
from packages.menubuttons import Buttons
from packages.title import Title
from packages.cardanimation import Cardanimation
pygame.init()

# Setting up the display
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Countdown Timer")
clock = pygame.time.Clock()
FPS = 60

# Background Image
image_bg = pygame.image.load("sprites/background.jpg")
image_bg = pygame.transform.scale(image_bg, (1000, 600))

# Card Back Image
card_back_deck = pygame.image.load("sprites/card_back_cyan.png")
card_back_deck = pygame.transform.scale(card_back_deck, (100, 150))

# Create a list of card images
card_list = [pygame.transform.scale(card_back_deck, (100, 150)) for _ in range(10)]

# Target positions for the cards
target_positions = [
    (100, 150), (100, 370), (275, 150), (275, 370),
    (450, 370), (625, 150), (625, 370), (800, 150),
    (800, 370), (450, 150)
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

def game_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.mouse_hover(event.pos):
                    main_game()
                elif options_button.mouse_hover(event.pos):
                    options()
                elif quit_button.mouse_hover(event.pos):
                    pygame.quit()
                    sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(image_bg, (0, 0))
        title_text.render_title(screen)
       
        mouse_hover_checker(start_button, mouse_pos)
        mouse_hover_checker(options_button, mouse_pos)
        mouse_hover_checker(quit_button, mouse_pos)

        pygame.display.flip()
        clock.tick(FPS)

def mouse_hover_checker(button, mouse_pos):
    if button.mouse_hover(mouse_pos):
        button.font.set_underline(True)
        button.render_text(screen, (173, 7, 255))
    else:
        button.font.set_underline(False)
        button.render_text(screen)

def main_game():
    # Draw the background once
    screen.blit(image_bg, (0, 0))
    pygame.display.flip()  # Update display

    # Animation loop for cards
    for idx, card in enumerate(card_list):
        target_pos = target_positions[idx]
        card_pos = [450, 0]  # Start position for the animation
        animation_speed = [20, 20]  # Speed of the animation

        # Creating a class instance
        card_animator = Cardanimation(card_pos, target_pos, animation_speed)

        while True:
            # Render background (keep it persistent)
            screen.blit(image_bg, (0, 0))
            # Calling the card_animation function from the Cardanimation
            card_pos = card_animator.card_animation()

            # Draw all cards in their respective positions
            for i, drawn_card in enumerate(card_list):
                position = target_positions[i] if i < idx else (450, 0)
                if i == idx:
                    position = tuple(card_pos)  # Animate the current card
                screen.blit(drawn_card, position)

            pygame.display.flip()  # Update the display

            # Check if the card has reached its target position
            if card_pos[0] == target_pos[0] and card_pos[1] == target_pos[1]:
                break  # Exit the loop for this card

            clock.tick(FPS)  # Control the frame rate

    # After animating all cards, start the countdown
    countdown_timer()

def countdown_timer():
    countdown_time = 3
    start_ticks = pygame.time.get_ticks()

    # Load the ace of hearts image and resize it
    ace_of_hearts = pygame.image.load("sprites/ace_of_hearts.jpg")
    ace_of_hearts = pygame.transform.scale(ace_of_hearts, (100, 150))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate remaining time
        seconds_left = countdown_time - (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds_left < 0:
            seconds_left = 0

        # Render background
        screen.blit(image_bg, (0, 0))

        # Determine if we are in the first second of the countdown
        if seconds_left >= 0:  # This means we are in the first second
            # Render all cards as Ace of Hearts
            for i in range(len(card_list)):
                screen.blit(ace_of_hearts, target_positions[i])  # Draw ace of hearts
        else:
            # Render all cards in their final positions
            for i, card in enumerate(card_list):
                screen.blit(card, target_positions[i])  # Draw the cards in final positions

        # Render the countdown timer at the middle top
        timer_text = font_timer.render(str(seconds_left), True, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(center=(500, 70))  # Center at (500, 50)
        screen.blit(timer_text, timer_text_rect)  # Draw the timer text

        pygame.display.flip()  # Update the display

        # Break the loop when countdown reaches zero
        if seconds_left == 0:
            break

    # After the 10-second countdown is done, start a new 1-minute countdown
    start_main_countdown()

def start_main_countdown():
    countdown_time = 60  # 1 minute countdown
    start_ticks = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate remaining time
        seconds_left = countdown_time - (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds_left < 0:
            seconds_left = 0

        # Render background
        screen.blit(image_bg, (0, 0))

        # Render all cards as card backs
        for i in range(len(card_list)):
            screen.blit(card_back_deck, target_positions[i])  # Draw card backs

        # Render the countdown timer at the middle top
        timer_text = font_timer.render(str(seconds_left), True, (255, 255, 255))
        timer_text_rect = timer_text.get_rect(center=(500, 70))  # Center at (500, 50)
        screen.blit(timer_text, timer_text_rect)  # Draw the timer text

        pygame.display.flip()  # Update the display

        # Break the loop when countdown reaches zero
        if seconds_left == 0:
            break

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

# Start the game menu
game_menu()
