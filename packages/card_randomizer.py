import pygame
import random
pygame.init()

class Card:
    def __init__(self):
        self.cardList = ['queen_of_clubs.png', 'jack_of_diamonds.png', 'ace_of_spades.png', 'ace_of_hearts.png', '10_of_hearts.png', 
                        'ace_of_spades.png', 'ace_of_hearts.png', '10_of_hearts.png', 'jack_of_diamonds.png', 'queen_of_clubs.png']
        
        self.random_card_list = self.generate_random_card()
        
    def generate_random_card(self):
        randomlist = []
        for _ in range(len(self.cardList)):
            randomCard = random.choice(self.cardList)
            randomlist.append(randomCard)
            self.cardList.remove(randomCard)        
        return randomlist
    





