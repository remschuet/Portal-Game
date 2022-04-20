class PhysicalObject:
    def __init__(self, name, position_x, position_y, height: int, length: int, pv: int):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.length = length
        self.pv = pv

    def death(self):
        self.pv = 0
