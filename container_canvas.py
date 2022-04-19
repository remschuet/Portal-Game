from tkinter import *
from PIL import Image, ImageTk
from player import Player
from not_alive_object import SceneObject
from environment import Environment
from enemy import Enemy
from songs_manager import Songs


class ContainerCanvas:
    def __init__(self, root):
        self.root = root

        self.container = Frame(self.root, bg="yellow")
        self.container.pack(expand=True, fill="both")

        self.environment = None

        self.jack = None
        self.enemy = None
        self.box = None
        self.tnt_box = None

        self.map_canvas = None
        self.background_image_game = None
        self.background_image_menu = None
        self.start_button_img = None
        self.option_button_img = None
        self.background_image_option = None
        self.option_option_button_img = None
        self.music_option_button_img = None

        self.songs_manager = Songs()
        self.enable_canvas("menu")

    def enable_canvas(self, canvas_name: str):
        if self.map_canvas:
            self.map_canvas.forget()

        if canvas_name == "menu":
            self.load_canvas_menu()
        elif canvas_name == "option":
            self.load_canvas_option()
        elif canvas_name == "level01":
            self.load_canvas_level01()
        elif canvas_name == "level02":
            self.load_canvas_level02()

    def load_canvas_menu(self):
        self.map_canvas = Canvas(self.container)
        self.map_canvas.update()
        self.image_manager()
        self.songs_manager.play_music_menu()

        self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
        self.map_canvas.pack(fill="both", expand=True)
        self.map_canvas.create_image(-100, 0, image=self.background_image_menu, anchor="nw")

        start_button = Button(self.map_canvas, image=self.start_button_img, borderwidth=0,
                              command=lambda:
                              [start_button.destroy(), option_button.destroy(), self.start_level01()])
        start_button.place(x=340, y=160)

        option_button = Button(self.map_canvas, image=self.option_button_img, borderwidth=0,
                               command=lambda:
                               [start_button.destroy(), option_button.destroy(), self.start_option()])
        option_button.pack(side=BOTTOM, pady=180)

    def load_canvas_option(self):
        print("canvas option")

        self.map_canvas = Canvas(self.container)
        self.map_canvas.update()

        self.image_manager()
        self.songs_manager.play_music_menu()

        self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
        self.map_canvas.pack(fill="both", expand=True)
        self.map_canvas.create_image(-100, 0, image=self.background_image_option, anchor="nw")

        return_button = Button(self.map_canvas, image=self.option_option_button_img, borderwidth=0,
                               command=lambda:
                               [return_button.destroy(), music_button.destroy(), self.start_menu()])
        return_button.place(x=340, y=160)

        music_button = Button(self.map_canvas, image=self.music_option_button_img, borderwidth=0,
                              command=lambda:
                              [self.songs_manager.cancel_music()])
        music_button.pack(side=BOTTOM, pady=180)

    def load_canvas_level01(self):
        self.map_canvas = Canvas(self.container)
        self.map_canvas.update()

        self.image_manager()

        self.songs_manager.stop_music()
        self.songs_manager.play_music_game()

        self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
        self.map_canvas.pack(fill="both", expand=True)
        self.map_canvas.create_image(0, 0, image=self.background_image_game, anchor="nw")

        self.create_players()

        self.main_timer_level01(1)
        self.update_timer(1)

    def load_canvas_level02(self):
        self.map_canvas = Canvas(self.container)
        self.map_canvas.update()

        self.image_manager()

        self.songs_manager.stop_music()
        self.songs_manager.play_music_game()

        self.map_canvas.configure(width=self.container.winfo_width(), height=self.container.winfo_height())
        self.map_canvas.pack(fill="both", expand=True)
        self.map_canvas.create_image(0, 0, image=self.background_image_game, anchor="nw")

        self.create_players()

        self.main_timer_level01(1)
        self.update_timer(1)

    def create_players(self):
        self.environment = Environment()

        self.jack = Player("Jack", self.map_canvas, self.environment,
                           position_x=150, position_y=150, pv=10, height=60, length=70)

        self.enemy = Enemy("enemy", self.map_canvas, self.environment,
                           position_x=70, position_y=70, pv=10, height=60, length=70)
        self.root.bind("1", self.enemy.print_position_x_y)
        self.box = SceneObject("box", self.map_canvas, self.environment,
                               position_x=300, position_y=300, height=60, length=70)
        self.tnt_box = SceneObject("box_tnt", self.map_canvas, self.environment,
                                   position_x=400, position_y=350, height=60, length=70)

        self.root.bind("2", self.jack.print_position_x_y)

        self.root.bind("<Left>", self.jack.move_left)
        self.root.bind("<Right>", self.jack.move_right)
        self.root.bind("<Up>", self.jack.move_up)
        self.root.bind("<Down>", self.jack.move_down)

    def image_manager(self):
        background_image_png = Image.open("assets/background.png")
        background_resized_menu = background_image_png.resize((2000, 2000), Image.ANTIALIAS)
        self.background_image_game = ImageTk.PhotoImage(background_resized_menu)

        background_image_menu = Image.open("assets/menu.png")
        background_resized_menu = background_image_menu.resize((1000, 1000), Image.ANTIALIAS)
        self.background_image_menu = ImageTk.PhotoImage(background_resized_menu)

        start_image_menu = Image.open("assets/button_start_menu.png")
        menu_resized_image = start_image_menu.resize((120, 70), Image.ANTIALIAS)
        self.start_button_img = ImageTk.PhotoImage(menu_resized_image)

        option_image_menu = Image.open("assets/button_option_menu.png")
        menu_option_resized_image = option_image_menu.resize((120, 70), Image.ANTIALIAS)
        self.option_button_img = ImageTk.PhotoImage(menu_option_resized_image)

        option_image_option = Image.open("assets/button_return_option.png")
        option_option_resized_image = option_image_option.resize((120, 70), Image.ANTIALIAS)
        self.option_option_button_img = ImageTk.PhotoImage(option_option_resized_image)

        music_image_option = Image.open("assets/button_option_music.png")
        music_option_resized_image = music_image_option.resize((120, 70), Image.ANTIALIAS)
        self.music_option_button_img = ImageTk.PhotoImage(music_option_resized_image)

        background_image_option = Image.open("assets/option.png")
        background_resized_option = background_image_option.resize((1000, 1000), Image.ANTIALIAS)
        self.background_image_option = ImageTk.PhotoImage(background_resized_option)

    def main_timer_level01(self, count):
        if self.jack.pv <= 0 or (self.enemy and self.enemy.pv <= 0):
            self.songs_manager.play_music_contact()
            self.start_menu()
        else:
            self.root.after(25000, self.main_timer_level01, count + 0.25)

        if count - int(count) == 0:
            print("timer :", count)

    def update_timer(self, count: int):
        if count >= 0:
            print(count)
        else:
            self.enemy.random_move_direction()
        self.root.after(1000, self.update_timer, count - 1)

    def start_menu(self):
        self.enable_canvas("menu")

    def start_option(self):
        self.enable_canvas("option")

    def start_level01(self):
        self.enable_canvas("level01")

    def start_level_02(self):
        self.enable_canvas("level02")
