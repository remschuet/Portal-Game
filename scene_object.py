from tkinter import *
from PIL import Image, ImageTk
from collision_manager import Environment


class SceneObject:
    def __init__(self, name: str, canvas: Canvas, environment: Environment, position_x, position_y):
        self.name = name
        self.canvas = canvas
        self.environment = environment
        self.position_x = position_x
        self.position_y = position_y

        prefix = str.lower(self.name)

        object_image = Image.open(prefix + "_object.png")
        resized_image = object_image.resize((50, 40), Image.ANTIALIAS)
        self.object_idle = ImageTk.PhotoImage(resized_image)
        self.player_image = self.canvas.create_image(self.position_x, self.position_y,
                                                     anchor=NW, image=self.object_idle)

    def print_name_position(self):
        print(f"{self.name} ({self.position_x, self.position_y})")


"""
FAIT Afficher l' image en fonction de son nom
"""