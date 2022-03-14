from tkinter import *
from player import Player

root = Tk()

# root.attributes("-fullscreen", True)
root.geometry("800x500")

container = Frame(root, bg="yellow")
container.pack(expand=True, fill="both")
map = Canvas(container)
map.update()
map.configure(width=container.winfo_width(), height=container.winfo_height(), bg="white")
map.pack(fill="both", expand=True)

jack = Player("Jack", map)
enemy = Player("enemy", map)

root.bind("<Key>", enemy.pressing)

root.bind("<Left>", jack.move_left)
root.bind("<Right>", jack.move_right)
root.bind("<Up>", jack.move_up)
root.bind("<Down>", jack.move_down)

root.mainloop()
