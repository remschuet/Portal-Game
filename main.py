from tkinter import *

from PIL import Image, ImageTk

from environment import Environment
from player import Player


def update_timer(count: int):
    if count >= 0:
        print(count)
    else:
        enemy.random_move_direction()
    root.after(1000, update_timer, count - 1)


root = Tk()

# root.attributes("-fullscreen", True)
root.geometry("800x500")

background_image_png = Image.open("background.png")

background_resized_image = background_image_png.resize((2000, 2000), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(background_resized_image)

container = Frame(root, bg="yellow")
container.pack(expand=True, fill="both")
map = Canvas(container)
map.update()

map.configure(width=container.winfo_width(), height=container.winfo_height())
map.pack(fill="both", expand=True)
map.create_image(0, 0, image=background_image, anchor="nw")

environment = Environment(map)
jack = Player("Jack", map, environment, position_x=150, position_y=150)
enemy = Player("enemy", map, environment, position_x=70, position_y=70)


root.bind("1", enemy.print_position_x_y)
root.bind("2", jack.print_position_x_y)

root.bind("<Left>", jack.move_left)
root.bind("<Right>", jack.move_right)
root.bind("<Up>", jack.move_up)
root.bind("<Down>", jack.move_down)

update_timer(1)

root.mainloop()
