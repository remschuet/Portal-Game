from tkinter import *
from container_canvas import ContainerCanvas


root = Tk()
# root.attributes("-fullscreen", True)
root.geometry("800x500")

management_map = ContainerCanvas(root)


root.mainloop()


"""
     Ennemi qui ne bloque pas contre un coin
     Vérifier sur qui est le contact dans Environment
     
     Modifier X Y pour la même valeur
     Créer une class qui s occupe de la création des images
    
    
FAIT Collision 
FAIT Son
FAIT Timer dans le canvas
FAIT Point de vie
FAIT Vérifie le nbr de point de vie
FAIT Refactor container_canvas
FAIT Menu option
     
"""