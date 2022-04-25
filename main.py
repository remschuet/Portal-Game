from tkinter import *
from container_canvas import ContainerCanvas


root = Tk()
# root.attributes("-fullscreen", True)
root.geometry("800x500")

management_map = ContainerCanvas(root)


root.mainloop()


"""
PAPA
     Environnement ligne 86
     Physical Object ligne 10

À Faire
     Environnement s occupe de dire à physical object de decremanter les point de vies

     Ennemi qui ne bloque pas contre un coin
     
     Créer une class qui s occupe de la création des images
     Créer une classe qui s occupe des l initialisation des joueurs et items
    
     Length et width inutile, ils sont écrasés par des valeurs dans environnement.

FAIT      
    FAIT Mettre dans chacun des class player et not alive object la ligne de code
    FAIT Vérifier sur qui est le contact dans Environment
    FAIT Modifier X Y pour la même valeur image et box collider    
    FAIT Collision 
    FAIT Son
    FAIT Timer dans le canvas
    FAIT Point de vie
    FAIT Vérifie le nbr de point de vie
    FAIT Refactor container_canvas
    FAIT Menu option
     
"""