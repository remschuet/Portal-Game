import pygame


class Songs:

    def __init__(self):
        pygame.mixer.init()
        self.music_enable = True

    def stop_music(self):
        if self.music_enable:
            pygame.mixer.music.stop()

    def cancel_music(self):
        if self.music_enable:
            self.stop_music()
            self.music_enable = False
        else:
            self.music_enable = True

    def play_music_menu(self):
        if self.music_enable:
            pygame.mixer.music.load("assets/sound/game_song.mp3")
            pygame.mixer.music.play(loops=0)

    def play_music_game(self):
        if self.music_enable:
            pygame.mixer.music.load("assets/sound/game_song.mp3")
            pygame.mixer.music.play(loops=0)

    def play_music_contact(self):
        if self.music_enable:
            pygame.mixer.music.load("assets/sound/game_over.wav")
            pygame.mixer.music.play(loops=0)

    def play_music_switch_level(self):
        if self.music_enable:
            pygame.mixer.music.load("assets/sound/switch_level.wav")
            pygame.mixer.music.play(loops=0)
