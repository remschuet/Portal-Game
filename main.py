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
FAIT Refactor container_canvas
FAIT Menu option
     Ennemi qui ne bloque pas contre un coin
FAIT Son
     Vérifier sur qui est le contact dans Environment
     Faire une class image_manager
"""