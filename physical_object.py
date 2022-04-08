from environment import Environment


class PhysicalObject:
    def __init__(self, name, position_x, position_y, environment: Environment, height: int, length: int):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.environment = environment
        self.height = height
        self.length = length

        self.environment.set_position_player(self.name, self.position_x, self.position_y)
