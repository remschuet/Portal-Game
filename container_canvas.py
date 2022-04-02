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
        self.map_canvas = None
        self.jack = None
        self.enemy = None

        self.enable_canvas("menu")

    def enable_canvas(self, canvas_name:str):
        if self.map_canvas:
            self.map_canvas.forget()

        if canvas_name == "level01":
            self.map_canvas = Canvas(self.container)
            self.map_canvas.update()

            environment = Environment(self.map_canvas)

            background_image_png = Image.open("background.png")
            background_resized_menu = background_image_png.resize((2000, 2000), Image.ANTIALIAS)
            self.background_image_game = ImageTk.PhotoImage(background_resized_menu)

            self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
            self.map_canvas.pack(fill="both", expand=True)
            self.map_canvas.create_image(0, 0, image=self.background_image_game, anchor="nw")


            self.jack = Player("Jack", self.map_canvas, environment, position_x=150, position_y=150)
            self.enemy = Enemy("enemy", self.map_canvas, environment, position_x=70, position_y=70)

            self.root.bind("1", self.enemy.print_position_x_y)
            self.root.bind("2", self.jack.print_position_x_y)

            self.root.bind("<Left>", self.jack.move_left)
            self.root.bind("<Right>", self.jack.move_right)
            self.root.bind("<Up>", self.jack.move_up)
            self.root.bind("<Down>", self.jack.move_down)

            self.update_timer(1)

        elif self.map_canvas_main_menu:

            self.map_canvas = Canvas(self.container)
            self.map_canvas.update()

            background_image_menu = Image.open("menu.png")
            background_resized_menu = background_image_menu.resize((1000, 1000), Image.ANTIALIAS)
            self.background_image_menu = ImageTk.PhotoImage(background_resized_menu)

            self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
            self.map_canvas.pack(fill="both", expand=True)
            self.map_canvas.create_image(-100, 0, image=self.background_image_menu, anchor="nw")

            start_image_menu = Image.open("button_start_menu.png")
            menu_resized_image = start_image_menu.resize((120, 70), Image.ANTIALIAS)
            self.start_button_img = ImageTk.PhotoImage(menu_resized_image)

            option_image_menu = Image.open("button_option_menu.png")
            menu_option_resized_image = option_image_menu.resize((120, 70), Image.ANTIALIAS)
            self.option_button_img = ImageTk.PhotoImage(menu_option_resized_image)

            start_button = Button(self.map_canvas, image=self.start_button_img, borderwidth=0,
                                  command=lambda: [start_button.destroy(), option_button.destroy(), self.start_level01()])
            start_button.place(x=340, y=160)

            option_button = Button(self.map_canvas, image=self.option_button_img, borderwidth=0, state=NORMAL,
                                   command=lambda: None)
            option_button.pack(side=BOTTOM, pady=180)

    def update_timer(self, count: int):
        if count >= 0:
             print(count)
        else:
            self.enemy.random_move_direction()
        self.root.after(1000, self.update_timer, count - 1)

    def get_map_canvas(self):
        return self.map_canvas

    def start_level01(self):
        self.enable_canvas("level01")