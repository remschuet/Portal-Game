import pygame


class Songs:
    def __init__(self):
        pygame.mixer.init()
        self.play_music_game()

    def play_music_game(self):
        pygame.mixer.music.load("game_song.mp3")
        pygame.mixer.music.play(loops=0)

    def play_music_contact(self):
        # Play music when enemy touch
        None
