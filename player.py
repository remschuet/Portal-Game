from tkinter import *

from PIL import Image, ImageTk

from environment import Environment


class Player:
    def __init__(self, name, canvas: Canvas, environment: Environment, position_x: int, position_y: int):
        self.name = name
        self.speed = 10
        self.canvas = canvas
        self.environment = environment

        self.position_x = position_x
        self.position_y = position_y

        self.current_direction = 0
        self.current_steps = 0

        self.environment.set_position_player(self.name, self.position_x, self.position_y)

        prefix = str.lower(self.name)
        player_image = Image.open(prefix + "_idle.jpg")
        resized_image = player_image.resize((80, 70), Image.ANTIALIAS)
        self.player_idle = ImageTk.PhotoImage(resized_image)
        self.player_image = canvas.create_image(self.position_x, self.position_y,
                                                anchor=NW, image=self.player_idle)
        print("(", self.position_x, self.position_y, ")")

        player_image_left = Image.open(prefix + "_left.jpg")
        resized_image_left = player_image_left.resize((80, 70), Image.ANTIALIAS)
        self.player_left = ImageTk.PhotoImage(resized_image_left)

        player_image_right = Image.open(prefix + "_right.jpg")
        resized_image_right = player_image_right.resize((80, 70), Image.ANTIALIAS)
        self.player_right = ImageTk.PhotoImage(resized_image_right)

        player_image_up = Image.open(prefix + "_up.jpg")
        resized_image_up = player_image_up.resize((80, 70), Image.ANTIALIAS)
        self.player_up = ImageTk.PhotoImage(resized_image_up)

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

        if self.environment.can_move(self.position_x, self.position_y, direction, self.speed):
            (self.position_x, self.position_y) = self.environment.get_next_position(
                self.position_x, self.position_y, direction, self.speed)
            self.update_image(direction)
            enable_move = True

            # Position in dictionary for every player
            self.environment.is_collision_detected(self.name, self.position_x, self.position_y)
            self.environment.set_position_player(self.name, self.position_x, self.position_y)

        else:
            print(f"{self.name} cannot move")
        return enable_move

    def move_right(self, _):
        if self.move("right"):
            self.canvas.move(self.player_image, self.speed, 0)

    def move_up(self, _):
        if self.move("up"):
            self.canvas.move(self.player_image, 0, -self.speed)

    def move_down(self, _):
        if self.move("down"):
            self.canvas.move(self.player_image, 0, self.speed)

    def move_left(self, _):
        if self.move("left"):
            self.canvas.move(self.player_image, -self.speed, 0)
