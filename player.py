import random
from tkinter import *

from PIL import Image, ImageTk


class Player:
    def __init__(self, name, canvas: Canvas, root):
        self.name = name
        self.speed = 10
        self.canvas = canvas
        self.root = root

        if self.name == "Jack":
            player_image = Image.open("player_idle.jpg")
            resized_image = player_image.resize((80, 70), Image.ANTIALIAS)
            self.player_idle = ImageTk.PhotoImage(resized_image)
            self.player_image = canvas.create_image(100, 100, anchor=NW, image=self.player_idle)

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
            self.player_image = canvas.create_image(200, 200, anchor=NW, image=self.player_idle)

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

    def random_move(self):
        print("Move left")
        self.move_left(None)
        self.root.after(1000, self.random_move)

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

    def move_left(self, event):
        self.canvas.move(self.player_image, -self.speed, 0)
        self.update_image("left")

    def move_right(self, event):
        self.canvas.move(self.player_image, self.speed, 0)
        self.update_image("right")

    def move_up(self, event):
        self.canvas.move(self.player_image, 0, -self.speed)
        self.update_image("up")

    def move_down(self, event):
        self.canvas.move(self.player_image, 0, self.speed)
        self.update_image("down")

