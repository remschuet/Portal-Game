
class SceneObject:
    def __init__(self, name: str, position_x, position_y):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y

    def print_name_position(self):
        print(f"{self.name} ({self.position_x, self.position_y})")


"""
     Afficher l'image en fonction de son nom
"""