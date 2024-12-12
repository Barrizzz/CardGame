import pygame
import random
pygame.init()

class Cardrandomizer:
    def __init__(self, random_card_list, random_card_list_blit):
        self.suits = ["hearts", "diamonds", "clubs", "spades"]
        self.ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        self.cardList = [f"{rank}_of_{suit}" for suit in self.suits for rank in self.ranks] + ["sal_card", "tal_card", "mikel_card", "bar_card"]
        random.shuffle(self.cardList)
        
        self.random_card_list = random_card_list
        self.random_card_list_blit = random_card_list_blit
        
    def generate_random_card(self):
        randomlist = []
        for _ in range(6):
            randomCard = random.choice(self.cardList)
            randomlist.append(randomCard)
            self.cardList.remove(randomCard)
        randomlist += randomlist
        random.shuffle(randomlist)
        return randomlist
    
    def create_random_cards(self):
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

test = Cardrandomizer('1', '2')
print(test.generate_random_card())







