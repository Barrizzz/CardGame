import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 600))

class Cardfaces:
    def __init__(self, card_back_deck, card_list, card_list_blit, target_positions):
        self.card_back_deck = card_back_deck
        self.card_list = card_list
        self.card_list_blit = card_list_blit
        self.target_positions = target_positions
        self.card_rects = []
        self.flipped_cards = [False] * len(card_list)  # Track flipped cards by making a list of booleans according to the length of card_list

    def get_card_rect(self):
        # Clear the card_rects list so that it won't just keep on adding, creating an index error
        self.card_rects.clear()
        # Get the card_rects list
        for i, rect in enumerate(self.card_list_blit):
            rect = screen.blit(self.card_back_deck, self.target_positions[i])  
            self.card_rects.append(rect)
        return self.card_rects
    
    def set_flipped_cards(self, i, flipped = True):
        self.flipped_cards[i] = flipped # True = flipped, False = not flipped

    def render_cards(self):
        for i in range(len(self.card_list)):
            if self.flipped_cards[i]:
                screen.blit(self.card_list_blit[i], self.target_positions[i])  # Draw card faces
            else:
                screen.blit(self.card_back_deck, self.target_positions[i])  # Draw card backs



