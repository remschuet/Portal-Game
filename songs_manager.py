import pygame


class Songs:
    def __init__(self):
        pygame.mixer.init()

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_music_menu(self):
        pygame.mixer.music.load("game_song.mp3")
        pygame.mixer.music.play(loops=0)

    def play_music_game(self):
        pygame.mixer.music.load("game_song.mp3")
        pygame.mixer.music.play(loops=0)

    def play_music_contact(self):
        pygame.mixer.music.load("game_over.wav")
        pygame.mixer.music.play(loops=0)

    def play_music_switch_level(self):
        pygame.mixer.music.load("switch_level.wav")
        pygame.mixer.music.play(loops=0)