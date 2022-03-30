from tkinter import *
from PIL import Image, ImageTk
from player import Player
from environment import Environment
from enemy import Enemy


class ContainerCanvas:
    def __init__(self, root):
        self.root = root

        self.map_canvas_level_01 = False
        self.map_canvas_main_menu = True

        self.container = Frame(self.root, bg="yellow")
        self.container.pack(expand=True, fill="both")

        self.map_canvas = Canvas(self.container)
        self.map_canvas.update()

        self.verify_which_canvas()

    def verify_which_canvas(self):
        if self.map_canvas_level_01:
            print("bob")

            environment = Environment(self.map_canvas)
            jack = Player("Jack", self.map_canvas, environment, position_x=150, position_y=150)
            enemy = Enemy("enemy", self.map_canvas, environment, position_x=70, position_y=70)

            self.root.bind("1", enemy.print_position_x_y)
            self.root.bind("2", jack.print_position_x_y)

            self.root.bind("<Left>", jack.move_left)
            self.root.bind("<Right>", jack.move_right)
            self.root.bind("<Up>", jack.move_up)
            self.root.bind("<Down>", jack.move_down)

            background_image_png = Image.open("background.png")
            background_resized_image = background_image_png.resize((2000, 2000), Image.ANTIALIAS)
            self.background_image = ImageTk.PhotoImage(background_resized_image)

            self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
            self.map_canvas.pack(fill="both", expand=True)
            self.map_canvas.create_image(0, 0, image=self.background_image, anchor="nw")

            self.start_button.destroy()

        elif self.map_canvas_main_menu:

            background_image_png = Image.open("menu.png")
            background_resized_image = background_image_png.resize((1000, 1000), Image.ANTIALIAS)
            self.background_image = ImageTk.PhotoImage(background_resized_image)

            self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
            self.map_canvas.pack(fill="both", expand=True)
            self.map_canvas.create_image(-100, 0, image=self.background_image, anchor="nw")

            background_image_menu = Image.open("button_start_menu.png")
            menu_resized_image = background_image_menu.resize((120, 70), Image.ANTIALIAS)
            self.start_button_img = ImageTk.PhotoImage(menu_resized_image)

            self.start_button = Button(self.map_canvas, image=self.start_button_img, borderwidth=0,
                                       command=lambda: self.press_start())
            self.start_button.place(x=340, y=160)

    def get_map_canvas(self):
        return self.map_canvas

    def get_bool_map_canvas(self):
        return self.map_canvas_level_01, self.map_canvas_main_menu

    def press_start(self):
        self.map_canvas_main_menu = False
        self.map_canvas_level_01 = True
        print("Press Start !")
        self.verify_which_canvas()

        return self.map_canvas_main_menu, self.map_canvas_level_01
