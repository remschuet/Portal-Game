class PhysicalObject:
    def __init__(self, name, position_x, position_y, height: int, length: int, pv: int):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.length = length
        self.pv = pv

        self.physical_object_list = []                           # Pourquoi ils ne sont pas tous ajouté à chaque fois ?
        self.physical_object_list.append(self.name)
        print(self.physical_object_list)

    def death(self, name):
        # Need to retrieve the player
        print(f"{name} need to died")
        # self.pv = 0
