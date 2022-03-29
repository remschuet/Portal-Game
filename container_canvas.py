from tkinter import *
from PIL import Image, ImageTk


class ContainerCanvas:
    def __init__(self, root):
        self.root = root

        self.map_canvas_level_01 = True
        self.map_canvas_main_menu = False

        container = Frame(self.root, bg="yellow")
        container.pack(expand=True, fill="both")

        self.map_canvas = Canvas(container)
        self.map_canvas.update()

        if self.map_canvas_level_01:

            background_image_png = Image.open("background.png")
            background_resized_image = background_image_png.resize((2000, 2000), Image.ANTIALIAS)
            self.background_image = ImageTk.PhotoImage(background_resized_image)

            self.map_canvas.configure(width=container.winfo_width(), height=container.winfo_height())
            self.map_canvas.pack(fill="both", expand=True)
            self.map_canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        elif self.map_canvas_main_menu:

            background_image_png = Image.open("menu.png")
            background_resized_image = background_image_png.resize((1000, 1000), Image.ANTIALIAS)
            self.background_image = ImageTk.PhotoImage(background_resized_image)

            self.map_canvas.configure(width=container.winfo_width(), height=container.winfo_height())
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

        return self.map_canvas_main_menu, self.map_canvas_level_01


