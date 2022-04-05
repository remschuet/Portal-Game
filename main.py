from tkinter import *
from songs_manager import Songs
from container_canvas import ContainerCanvas


root = Tk()
# root.attributes("-fullscreen", True)
root.geometry("800x500")

management_map = ContainerCanvas(root)
songs_manager = Songs()


root.mainloop()


"""
FAIT Timer dans le canvas
FAIT Point de vie
FAIT Vérifie le nbr de point de vie
FAIT Refactor container_canvas
     Menu option
     Ennemi qui ne bloque pas contre un coin
     Son
     system de level sur une certaine place 
"""