from tkinter import *

# from enemy import Enemy
# from environment import Environment
# from player import Player
from container_canvas import ContainerCanvas

# def update_timer(count: int):
#     if count >= 0:
#         print(count)
#     else:
#         enemy.random_move_direction()
#     root.after(1000, update_timer, count - 1)


root = Tk()

# root.attributes("-fullscreen", True)
root.geometry("800x500")

management_map = ContainerCanvas(root)

map_canvas_level_01, map_canvas_main_menu = management_map.get_bool_map_canvas()

# if map_canvas_level_01:
#    useless
#    map_canvas = management_map.get_map_canvas()

#    environment = Environment(map_canvas)
#    jack = Player("Jack", map_canvas, environment, position_x=150, position_y=150)
#    enemy = Enemy("enemy", map_canvas, environment, position_x=70, position_y=70)

#    root.bind("1", enemy.print_position_x_y)
#    root.bind("2", jack.print_position_x_y)

#    root.bind("<Left>", jack.move_left)
#    root.bind("<Right>", jack.move_right)
#    root.bind("<Up>", jack.move_up)
#    root.bind("<Down>", jack.move_down)

#     update_timer(1)

# elif map_canvas_main_menu:
#     jack = None
#     enemy = None

root.mainloop()
