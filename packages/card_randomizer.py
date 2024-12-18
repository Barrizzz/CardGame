import pygame
import random
pygame.init()

class Cardrandomizer:
    def __init__(self):
        self.suits = ["hearts", "diamonds", "clubs", "spades"]
        self.ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        self.__cardList = ["sal_card", "tal_card", "mikel_card", "bar_card"]
        for suit in self.suits: # Loop through the suits
            for rank in self.ranks: # Loop through the ranks
                self.__cardList.append(f"{rank}_of_{suit}") # Append the name of the {rank}_of_{suit} to the cardList, since the name of the files are in this format

        random.shuffle(self.__cardList)
        
        self.__random_card_list = []
        self.__random_card_list_blit = []

    def generate_random_cards(self):
        randomlist = []
        for _ in range(6):
            randomCard = random.choice(self.__cardList)
            randomlist.append(randomCard)
            self.__cardList.remove(randomCard)
        randomlist += randomlist # Duplicate the list (since we need pairs)
        random.shuffle(randomlist) # Shuffles the list
        return randomlist
    
    def create_random_cards(self):
        # Generate a new random card list
        self.__random_card_list = self.generate_random_cards() # This is very important for knowing which cards match, since it is just the name of the card (ex. 2_of_diamonds)
        
        # Create a list of card images for blitting
        for card_name in self.__random_card_list:
            card_image_path = "sprites/cardface/" + card_name + ".png"
            card_image = pygame.image.load(card_image_path)
            card_image = pygame.transform.scale(card_image, (100, 150))
            self.__random_card_list_blit.append(card_image) # This is the list of card images that will be blitted on the screen (not the name of the card!)
        #print(self.random_card_list_blit)
        #print(self.random_card_list)
    
    def get_random_card_list(self):
        return self.__random_card_list
    
    def get_random_card_list_blit(self):
        return self.__random_card_list_blit

#test = Cardrandomizer()
#test.create_random_cards()
#print(test.get_random_card_list())







