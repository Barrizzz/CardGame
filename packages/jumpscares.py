import random
import pygame
pygame.init()

class Jumpscares:
    def __init__(self):
        self.jumpscare_list = ['jason.png', 'mikel.jpg']
        self.jumpscare_sounds = ['ascending_jumpscare.mp3', 'ah_hell_nah.mp3', 'plankton_funny.mp3']

        self.jumpscares = [pygame.image.load(f"sprites/{img}") for img in self.jumpscare_list]
        self.jumpscares = [pygame.transform.scale(img, (1000, 600)) for img in self.jumpscares]
        self.sounds = [pygame.mixer.Sound(f"sounds/{sound}") for sound in self.jumpscare_sounds]

    def display_jumpscare(self, screen):
        screen.blit(random.choice(self.jumpscares), (0, 0))
        self.play_jumpscare_sound(random.randint(0, len(self.jumpscare_sounds) - 1))
        pygame.display.flip()

    def play_jumpscare_sound(self, index):
        self.sounds[index].play()
        self.sounds[index].set_volume(self.volume)

    def stop_all_sounds(self):
        for sound in self.sounds:
            sound.stop()
