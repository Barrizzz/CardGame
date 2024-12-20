import pygame
import random
pygame.init()

class Music:
    def __init__(self, volume):
        # Volume
        self.volume = volume

        # This is for sounds and jumpscares
        self.main_music = pygame.mixer.Sound("sounds/happy_quiz.mp3")
        self.let_it_snow = pygame.mixer.Sound("sounds/let_it_snow.mp3")
        self.thick_of_it = pygame.mixer.Sound("sounds/ThickOfIt_Jazz.mp3")

        self.main_music_list = [self.main_music, self.let_it_snow, self.thick_of_it]

        self.weird_music = pygame.mixer.Sound("sounds/weird_song.mp3")

        self.countdown_25sec = pygame.mixer.Sound("sounds/25_second_countdwn.mp3")
        self.countdown_20sec = pygame.mixer.Sound("sounds/20_second_countdwn.mp3")
        self.countdown_10sec = pygame.mixer.Sound("sounds/10_second_countdwn.mp3")
        self.countdown_5sec = pygame.mixer.Sound("sounds/5_second_countdwn.mp3")
        self.countdown_music = [self.countdown_25sec, self.countdown_20sec, self.countdown_10sec, self.countdown_5sec]

        self.main_music = None
        self.current_countdown_sound = None
    
    def play_main_music(self):
        self.main_music = random.choice(self.main_music_list)
        self.main_music.play(-1)
        # Set the volume of some music to be louder
        if self.main_music == self.thick_of_it:
            self.main_music.set_volume(self.volume + 0.4) # I am sorry for the magic numbers here, since the volume of the sounds in the file are not consistent :(
        else:
            self.main_music.set_volume(self.volume + 0.2)
    
    def play_weird_music(self):
        self.weird_music.play(-1)
        self.weird_music.set_volume(self.volume + 0.2)
    
    def stop_all_music(self):
        for music in self.main_music_list:
            music.stop()
        self.weird_music.stop()
    
    def stop_all_coundown_music(self):
        for music in self.countdown_music:
            music.stop()

    def countdown_sounds(self, time):
        self.stop_all_music()
        countdown_music = getattr(self, f'countdown_{time}sec') # Getting the attribute of the countdown sound (Ex. self.countdown_25sec = pygame.mixer.Sound("sounds/25_second_countdwn.mp3"))
        if self.current_countdown_sound != countdown_music: # If the current countdown sound is not the same as the one we want to play (this is to prevent the same sound from overlaying)
            if self.current_countdown_sound: # If there exist a current countdown sound, stop it (this ensures that it only stops once)
                self.current_countdown_sound.stop()
            countdown_music.play(loops = -1) # Play the new countdown sound
            countdown_music.set_volume(self.volume + 0.3)
            self.current_countdown_sound = countdown_music