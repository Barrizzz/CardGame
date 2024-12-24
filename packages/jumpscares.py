import random
import pygame
pygame.init()

class Jumpscares:
    def __init__(self, volume):
        self.volume = volume
        self.jumpscare_list = ['jason.png', 'mikel.jpg', 'cardface/tal_card.png', 'cardface/mikel_card.png']
        self.jumpscare_sounds = ['ah_hell_nah.mp3', 'ascending_jumpscare.mp3']
        
        self.death_screen_sound = 'plankton_funny.mp3'
        self.plankton_funny = pygame.mixer.Sound(f"sounds/{self.death_screen_sound}")

        self.jumpscares = [pygame.transform.scale(pygame.image.load(f"sprites/{img}"), (1000, 600)) for img in self.jumpscare_list]
        self.sounds = [pygame.mixer.Sound(f"sounds/{sound}") for sound in self.jumpscare_sounds]

        self.current_jumpscare = None
        self.current_sound = None
        self.current_sound_name = None

    def display_jumpscare(self, screen):
        index_jumpscare = random.randint(0, len(self.jumpscare_list) - 1) # Randomize the jumpscare image
        index_sound = random.randint(0, len(self.jumpscare_sounds) - 1) # Randomize the jumpscare sound
        
        if self.current_jumpscare is None: # If there is no current jumpscare, set the current jumpscare and sound (this ensures that the code only runs once)
            self.current_jumpscare = self.jumpscares[index_jumpscare]
            self.current_sound = self.sounds[index_sound]
            self.current_sound_name = self.jumpscare_sounds[index_sound]
            self.current_sound.play()

            if self.current_sound_name == 'ah_hell_nah.mp3':
                self.current_sound.set_volume(self.volume + 1)  # Make the volume bigger for this specific sound since it is quiet
            else:
                self.current_sound.set_volume(self.volume) # For the rest use the volume in the main.py
        return screen.blit(self.current_jumpscare, (0, 0))

    def reset_jumpscare(self):
        if self.current_sound: # If self.current_sound exists, stop it
            self.current_sound.stop()
        # Reset the variables
        self.current_jumpscare = None
        self.current_sound = None
        self.current_sound_name = None

    def get_death_screen(self):
        index = random.randint(0, len(self.jumpscare_list) - 1) # Randomize the death screen
        death_screen = self.jumpscares[index]
        return death_screen
    
    def play_death_screen_sound(self):
        self.plankton_funny.play()

    def stop_jumpscare_sounds(self):
        for sound in self.sounds:
            sound.stop()
        self.plankton_funny.stop()
