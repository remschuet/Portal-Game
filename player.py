from tkinter import *

from PIL import Image, ImageTk

from environment import Environment
from physical_object import PhysicalObject


class Player(PhysicalObject):
    def __init__(self, name, canvas: Canvas, environment: Environment,
                 position_x: int, position_y: int, height: int, length: int, pv: int):
        super().__init__(name, position_x, position_y, height, length, pv)
        self.speed = 10
        self.canvas = canvas

        self.current_direction = 0
        self.current_steps = 0
        self.environment = environment

        prefix = str.lower(self.name)
        player_image = Image.open("assets\\" + prefix + "_idle.jpg")
        resized_image = player_image.resize((80, 80), Image.ANTIALIAS)
        self.player_idle = ImageTk.PhotoImage(resized_image)
        self.player_image = self.canvas.create_image(self.position_x, self.position_y,
                                                     anchor=NW, image=self.player_idle)
        print("(", self.position_x, self.position_y, ")")

        player_image_left = Image.open("assets\\" + prefix + "_left.jpg")
        resized_image_left = player_image_left.resize((80, 80), Image.ANTIALIAS)
        self.player_left = ImageTk.PhotoImage(resized_image_left)

        player_image_right = Image.open("assets\\" + prefix + "_right.jpg")
        resized_image_right = player_image_right.resize((80, 80), Image.ANTIALIAS)
        self.player_right = ImageTk.PhotoImage(resized_image_right)

        player_image_up = Image.open("assets\\" + prefix + "_up.jpg")
        resized_image_up = player_image_up.resize((80, 80), Image.ANTIALIAS)
        self.player_up = ImageTk.PhotoImage(resized_image_up)

        self.environment.set_position_player(self.name, self.position_x, self.position_y)

    def print_position_x_y(self, _):
        print("(", self.name, ":", self.position_x, self.position_y, ")")

    def set_speed(self, speed):
        self.speed = speed

    def update_image(self, direction):
        if direction == "left":
            self.canvas.itemconfig(self.player_image, image=self.player_left)
        if direction == "right":
            self.canvas.itemconfig(self.player_image, image=self.player_right)
        if direction == "down":
            self.canvas.itemconfig(self.player_image, image=self.player_idle)
        if direction == "up":
            self.canvas.itemconfig(self.player_image, image=self.player_up)

    def move(self, direction: str) -> bool:
        enable_move = False
        if self.environment.can_move(self.name, self.position_x, self.position_y, direction, self.speed):
            # update player position
            (self.position_x, self.position_y) = self.environment.get_next_position(self.name,
                                                                                    self.position_x,
                                                                                    self.position_y, direction,
                                                                                    self.speed)
            # update current player position in environnement
            self.environment.set_position_player(self.name, self.position_x, self.position_y)
            enable_move = True

            # Ne comprends pas si c'est utile
            # item = self.environment.is_collision_detected(self.name, self.position_x, self.position_y)
            print(f" {self.name} move to {self.position_x} {self.position_y}!")

        else:
            print(f"{self.name} cannot move")
            if not isinstance(self, Player):
                print(f"{self.name} ne peut pas bouger!")
        return enable_move

    def death(self):
        self.pv = 0

    def move_right(self, _):
        if self.move("right"):
            self.update_image("right")
            self.canvas.move(self.player_image, self.speed, 0)

    def move_up(self, _):
        if self.move("up"):
            self.update_image("up")
            self.canvas.move(self.player_image, 0, -self.speed)

    def move_down(self, _):
        if self.move("down"):
            self.update_image("down")
            self.canvas.move(self.player_image, 0, self.speed)

    def move_left(self, _):
        if self.move("left"):
            self.update_image("left")
            self.canvas.move(self.player_image, -self.speed, 0)
