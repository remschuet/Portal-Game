import random
from tkinter import *

from PIL import Image, ImageTk


class Player:
    def __init__(self, name, canvas: Canvas, root):
        self.name = name
        self.speed = 10
        self.canvas = canvas
        self.root = root

        self.position_x = 100
        self.position_y = 100

        self.current_direction = 0
        self.current_steps = 0
        self.can_move_in_canvas = bool

        if self.name == "Jack":
            player_image = Image.open("player_idle.jpg")
            resized_image = player_image.resize((80, 70), Image.ANTIALIAS)
            self.player_idle = ImageTk.PhotoImage(resized_image)
            self.player_image = canvas.create_image(100, 100, anchor=NW, image=self.player_idle)
            print("(", self.position_x, self.position_y, ")")

            player_image_left = Image.open("player_left.jpg")
            resized_image_left = player_image_left.resize((80, 70), Image.ANTIALIAS)
            self.player_left = ImageTk.PhotoImage(resized_image_left)

            player_image_right = Image.open("player_right.jpg")
            resized_image_right = player_image_right.resize((80, 70), Image.ANTIALIAS)
            self.player_right = ImageTk.PhotoImage(resized_image_right)

            player_image_up = Image.open("player_up.jpg")
            resized_image_up = player_image_up.resize((80, 70), Image.ANTIALIAS)
            self.player_up = ImageTk.PhotoImage(resized_image_up)

        if self.name == "enemy":
            player_image = Image.open("enemy_idle.jpg")
            resized_image = player_image.resize((80, 70), Image.ANTIALIAS)
            self.player_idle = ImageTk.PhotoImage(resized_image)
            self.player_image = canvas.create_image(100, 100, anchor=NW, image=self.player_idle)

            player_image_left = Image.open("enemy_left.jpg")
            resized_image_left = player_image_left.resize((80, 70), Image.ANTIALIAS)
            self.player_left = ImageTk.PhotoImage(resized_image_left)

            player_image_right = Image.open("enemy.right.jpg")
            resized_image_right = player_image_right.resize((80, 70), Image.ANTIALIAS)
            self.player_right = ImageTk.PhotoImage(resized_image_right)

            player_image_up = Image.open("enemy_up.jpg")
            resized_image_up = player_image_up.resize((80, 70), Image.ANTIALIAS)
            self.player_up = ImageTk.PhotoImage(resized_image_up)

    def pressing(self, event):
        # Just for the enemy
        if event.char == "a": self.move_left(event)
        if event.char == "d": self.move_right(event)
        if event.char == "w": self.move_up(event)
        if event.char == "s": self.move_down(event)

    def random_move_direction(self):
        if self.current_steps == 0:
            random.seed()       # reinitialise le module random
            self.current_direction = random.randint(1, 4)
            self.current_steps = random.randint(1, 8)
        else:
            self.current_steps -= 1
        self.random_move_length(direction=self.current_direction)

    def random_move_length(self, direction: int):
        if direction == 1: self.move_left(None)
        if direction == 2: self.move_right(None)
        if direction == 3: self.move_up(None)
        if direction == 4: self.move_down(None)

        # self.root.after(500, self.random_move_direction)

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

    def new_position(self, move_direction):
        if move_direction == "left":
            new = self.position_x - self.speed
            self.position_x = new
        if move_direction == "right":
            new = self.position_x + self.speed
            self.position_x = new
        if move_direction == "up":
            new = self.position_y - self.speed
            self.position_y = new
        if move_direction == "down":
            new = self.position_y + self.speed
            self.position_y = new
        print("(", self.name,":",self.position_x, self.position_y, ")")

    def move_in_canvas(self, direction):
        if self.position_x > 200 and direction == "right":
            self.can_move_in_canvas = False
        elif self.position_x < 0 and direction == "left":                   # Why elif and not if ??
            self.can_move_in_canvas = False
        elif self.position_y < 0 and direction == "up":
            self.can_move_in_canvas = False
        elif self.position_y > 200 and direction == "down":
            self.can_move_in_canvas = False
        else:
            self.can_move_in_canvas = True

    def move_left(self, event):
        self.move_in_canvas("left")
        if self.can_move_in_canvas:
            self.canvas.move(self.player_image, -self.speed, 0)
            self.update_image("left")
            self.new_position("left")

    def move_right(self, event):
        self.move_in_canvas("right")
        if self.can_move_in_canvas:
            self.can_move_in_canvas = False
            self.canvas.move(self.player_image, self.speed, 0)
            self.update_image("right")
            self.new_position("right")

    def move_up(self, event):
        self.move_in_canvas("up")
        if self.can_move_in_canvas:
            self.canvas.move(self.player_image, 0, -self.speed)
            self.update_image("up")
            self.new_position("up")

    def move_down(self, event):
        self.move_in_canvas("down")
        if self.can_move_in_canvas:
            self.canvas.move(self.player_image, 0, self.speed)
            self.update_image("down")
            self.new_position("down")



