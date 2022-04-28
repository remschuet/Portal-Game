from tkinter import *
from container_canvas import ContainerCanvas


root = Tk()
# root.attributes("-fullscreen", True)
root.geometry("800x500")

management_map = ContainerCanvas(root)


root.mainloop()


"""
À Faire
     Ennemi qui ne bloque pas contre un coin
     
     Créer une class qui s occupe de la création des images
     Créer une classe qui s occupe des l initialisation des joueurs et items
    
     Length et width inutile, ils sont écrasés par des valeurs dans environnement.

FAIT
    27 avril 
    FAIT système de niveau dans init_object
    FAIT Créer init_object et créer les objects par cette classe   
    FAIT Environnement s occupe de dire à physical object de décrémenter les point de vies
    Avant
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