import random
from tkinter import Canvas

from environment import Environment
from player import Player


class Enemy(Player):
    def __init__(self, name, canvas: Canvas, environment: Environment, position_x: int, position_y: int, pv: int):
        super().__init__(name, canvas, environment, position_x, position_y, pv)

    def random_move_direction(self):
        if self.current_steps == 0:
            random.seed()  # reinitialise le module random
            self.current_direction = random.randint(1, 4)
            self.current_steps = random.randint(1, 8)
        else:
            self.current_steps -= 1
        self.random_move_length(direction=self.current_direction)

    def random_move_length(self, direction: int):
        if direction == 1:
            self.move_left(None)
        if direction == 2:
            self.move_right(None)
        if direction == 3:
            self.move_up(None)
        if direction == 4:
            self.move_down(None)
