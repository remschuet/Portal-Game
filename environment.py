from tkinter import Canvas


class Environment:
    def __init__(self, fight_map: Canvas):

        self.length = 70        # longueur
        self.height = 60        # hauteur

        self.players = {}

    def set_position_player(self, name, position_x, position_y):
        self.players[name] = (position_x, position_y)
        print(f" Player {name} now at x={position_x} y={position_y} )")

    def can_move(self, position_x: int, position_y: int, direction: str, speed: int):
        return (position_x, position_y) != self.get_next_position(
            position_x, position_y, direction, speed)

    def get_next_position(self, position_x: int, position_y: int, direction: str, speed: int) \
            -> (int, int):
        if position_x < 710 and direction == "right":
            position_x += speed
            if position_x > 710:
                position_x = 710
        elif position_x > 0 and direction == "left":
            position_x -= speed
            if position_x < 0:
                position_x = 0
        elif position_y > 0 and direction == "up":
            position_y -= speed
            if position_y < 0:
                position_y = 0
        elif position_y < 420 and direction == "down":
            position_y += speed
            if position_y > 420:
                position_y = 420
        return position_x, position_y

    def is_collision_detected(self, name: str, position_x: int, position_y: int):
        for player_name, (x, y) in self.players.items():
            if name != player_name:
                if position_x + self.height >= x and \
                        position_x <= x + self.height and \
                        position_y + self.length >= y and \
                        position_y <= y + self.length:
                    print(f" {name} en collision avec  {player_name}")
                    return True
        return False
