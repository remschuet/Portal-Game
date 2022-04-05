from tkinter import *

from container_canvas import ContainerCanvas

root = Tk()
# root.attributes("-fullscreen", True)
root.geometry("800x500")

management_map = ContainerCanvas(root)


root.mainloop()


"""
FAIT Timer dans le canvas
FAIT Point de vie
FAIT Vérifie le nbr de point de vie
     Refactor container_canvas
     Menu option
     Son
     system de level sur une certaine place 
"""