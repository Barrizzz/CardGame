import pygame
import sys
pygame.init()

class Cardanimation:
    def __init__(self):
        self.target_pos = 0
        self.card_pos = [450, 0]
        self.animation_speed = [20, 20]
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def card_animation(self):
        delta_x = self.target_pos[0] - self.card_pos[0]
        delta_y = self.target_pos[1] - self.card_pos[1]

        # Check if the card is close enough to stop
        if abs(delta_x) < self.animation_speed[0] and abs(delta_y) < self.animation_speed[1]:
            self.card_pos = list(self.target_pos)  # Snap to target position
            return self.card_pos

        # Calculate movement along x and y based on the speed
        move_x = min(abs(delta_x), self.animation_speed[0]) * (1 if delta_x > 0 else -1)
        move_y = min(abs(delta_y), self.animation_speed[1]) * (1 if delta_y > 0 else -1)

        # Update the card's position
        self.card_pos[0] += move_x
        self.card_pos[1] += move_y
        return self.card_pos
    
    def start_animation(self, screen, card_list, target_positions, image_bg):
        clock = self.clock
        FPS = self.FPS
        # Draw the background once
        screen.blit(image_bg, (0, 0))

        # Animation loop for cards
        for index in range(len(card_list)):
            self.target_pos = target_positions[index]
            self.card_pos = [450, 0]  # Reset card position for each loop

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                # Render background (keep it persistent)
                screen.blit(image_bg, (0, 0)) 
                # Calling the card_animation function from the Cardanimation
                card_pos = self.card_animation()

                # Draw all cards in their respective positions
                for i, drawn_card in enumerate(card_list):
                    if i < index:
                        position = target_positions[i]  
                    else:
                        position = (450, 0)

                    if i == index:
                        position = tuple(card_pos)  # Animate the current card
                    screen.blit(drawn_card, position)

                # Check if the card has reached its target position
                if card_pos[0] == self.target_pos[0] and card_pos[1] == self.target_pos[1]:
                    break  # Exit the loop for this card

                pygame.display.flip()  # Update the display
                clock.tick(FPS)  # Control the frame rate
    
    def memorize_cards(self, screen, image_bg, font_timer, target_positions, random_card_list_blit):
        clock = self.clock
        FPS = self.FPS

        memorizing_time = 2  # Initial countdown for memorizing the cards
        start_ticks = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Render background
            screen.blit(image_bg, (0, 0))
            
            # Calculate remaining time
            seconds_left = memorizing_time - (pygame.time.get_ticks() - start_ticks) // 1000
            if seconds_left < 0: seconds_left = 0 
            
            # Rendering the timer text
            timer_text = font_timer.render('Memorize The Card!', True, (255, 255, 255))  # The middle boolean is for antialiasing
            timer_text_rect = timer_text.get_rect(center=(500, 70))  # Center at (500, 50)
            screen.blit(timer_text, timer_text_rect)  # Draw the timer text

            # Render the cards only if the countdown is not over
            if seconds_left > 0:  
                # Render all cards from the randomized card list (random_card_list)
                for i, card in enumerate(random_card_list_blit):
                    screen.blit(card, target_positions[i])

            # Break the loop when countdown reaches zero
            if seconds_left == 0: break

            pygame.display.flip()  # Update the display
            clock.tick(FPS)