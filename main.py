from tkinter import *
from player import Player
from PIL import Image, ImageTk


def update_timer(count: int):
    if count >= 0:
        root.after(1000, update_timer, count - 1)
        print(count)
    else:
        enemy.random_move_direction()


def get_specific_position():                        # not optimal
    position_enemy = enemy.get_position_x_y(None)
    print("Position of enemy", position_enemy)
    position_jack = jack.get_position_x_y(None)
    print("Position of jack", position_jack)


root = Tk()

# root.attributes("-fullscreen", True)
root.geometry("800x500")
background_image = PhotoImage(file="background.png")


container = Frame(root, bg="yellow")
container.pack(expand=True, fill="both")
map = Canvas(container)
map.update()


map.configure(width=container.winfo_width(), height=container.winfo_height())
map.pack(fill="both", expand=True)

jack = Player("Jack", map, root, position_x=150, position_y=150)
enemy = Player("enemy", map, root, position_x=70, position_y=70)

get_specific_position()  # Take the position of player and enemy

root.bind("1", enemy.print_position_x_y)
root.bind("2", jack.print_position_x_y)

root.bind("<Left>", jack.move_left)
root.bind("<Right>", jack.move_right)
root.bind("<Up>", jack.move_up)
root.bind("<Down>", jack.move_down)

update_timer(1)

root.mainloop()
