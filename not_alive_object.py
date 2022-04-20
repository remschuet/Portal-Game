from tkinter import *
from PIL import Image, ImageTk
from environment import Environment
from physical_object import PhysicalObject


class SceneObject(PhysicalObject):

    def __init__(self, name: str, canvas: Canvas, environment: Environment,
                 position_x, position_y, height: int, length: int, pv: int):
        super().__init__(name, position_x, position_y, height, length, pv)
        self.canvas = canvas
        self.environment = environment

        prefix = str.lower(self.name)

        object_image = Image.open("assets\\" + prefix + "_object.png")
        resized_image = object_image.resize((80, 80), Image.ANTIALIAS)
        self.object_idle = ImageTk.PhotoImage(resized_image)
        self.player_image = self.canvas.create_image(self.position_x, self.position_y,
                                                     anchor=NW, image=self.object_idle)

        self.environment.set_position_player(self.name, self.position_x, self.position_y)

    def print_name_position(self):
        print(f"{self.name} ({self.position_x, self.position_y})")
