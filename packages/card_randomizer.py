import pygame
import random
pygame.init()

class Cardrandomize:
    def __init__(self):
        self.cardList = ['queen_of_clubs', 'jack_of_diamonds', '7_of_diamonds', 'ace_of_spades', 'ace_of_hearts', '10_of_hearts', 
                        'ace_of_spades', 'ace_of_hearts', '10_of_hearts', 'jack_of_diamonds', 'queen_of_clubs',
                        '7_of_diamonds'
                        ]
        
        self.random_card_list = self.generate_random_card()
        
    def generate_random_card(self):
        randomlist = []
        for _ in range(len(self.cardList)):
            randomCard = random.choice(self.cardList)
            randomlist.append(randomCard)
            self.cardList.remove(randomCard)        
        return randomlist
    





