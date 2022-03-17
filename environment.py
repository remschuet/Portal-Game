from tkinter import Canvas


class Environment:
    def __init__(self, fight_map: Canvas):
        self.fight_map = fight_map
        self.jack_position_x = int
        self.jack_position_y = int
        self.enemy_position_x = int
        self.enemy_position_y = int

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

    def get_postion_all_Player(self, name, position_x, position_y):
        # print(f" the postion of {name}  is x={position_x} y={position_y}")
        if name == "Jack":
            self.jack_position_x = position_x
            self.jack_position_y = position_y

        elif name == "enemy":
            self.enemy_position_x = position_x
            self.enemy_position_y = position_y

        all_top_jack_position_x = [self.jack_position_x, (self.jack_position_x + 10), (self.jack_position_x + 20),
                                   (self.jack_position_x + 30), (self.jack_position_x + 40),
                                   (self.jack_position_x + 50), (self.jack_position_x + 60),
                                   (self.jack_position_x + 70), (self.jack_position_x + 80)]
        print(f" the position top x jack is : {all_top_jack_position_x[:]}")

        all_top_enemy_position_x = [self.enemy_position_x, (self.enemy_position_x + 10), (self.enemy_position_x + 20),
                                    (self.enemy_position_x + 30), (self.enemy_position_x + 40),
                                    (self.enemy_position_x + 50), (self.enemy_position_x + 60),
                                    (self.enemy_position_x + 70), (self.enemy_position_x + 80)]
        print(f" the position top x jack is : {all_top_enemy_position_x[:]}")

        # if all_top_jack_position_x == all_top_enemy_position_x:
        #     print("Même position !")