import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
FPS = 50


def game_menu():
    image_bg = pygame.image.load("background.jpg")
    image_bg = pygame.transform.scale(image_bg, (1000, 600))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill((0, 0, 0))
        screen.blit(image_bg, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

game_menu()
pygame.QUIT