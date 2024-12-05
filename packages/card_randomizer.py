import pygame
import random
pygame.init()

class Cardrandomize:
    def __init__(self):
        self.cardList = ['queen_of_clubs', 'jack_of_diamonds', '7_of_diamonds', 'ace_of_spades', 'ace_of_hearts', '10_of_hearts', 
                        'ace_of_spades', 'ace_of_hearts', '10_of_hearts', 'jack_of_diamonds', 'queen_of_clubs',
                        '7_of_diamonds'
                        ]
        
        self.random_card_list = []
        self.random_card_list_blit = []
        
    def generate_random_card(self):
        randomlist = []
        for _ in range(len(self.cardList)):
            randomCard = random.choice(self.cardList)
            randomlist.append(randomCard)
            self.cardList.remove(randomCard)        
        return randomlist
    
    def create_random_cards(self):
        # Clear the lists before starting a new game
        self.random_card_list.clear()
        self.random_card_list_blit.clear() 

        # Generate a new random card list
        self.random_card_list = self.generate_random_card()

        # Create a list of card images for blitting
        for card_name in self.random_card_list:
            card_image_path = "sprites/cardface/" + card_name + ".png"
            card_image = pygame.image.load(card_image_path)
            card_image = pygame.transform.scale(card_image, (100, 150))
            self.random_card_list_blit.append(card_image)
        #print(self.random_card_list_blit)
        #print(self.random_card_list)

#test = Cardrandomize()
#test.create_random_cards()







