from physical_object import PhysicalObject


class Environment:
    def __init__(self):

        self.length = 80  # longueur
        self.height = 80  # hauteur
        self.object_name = None

        self.key_found = False
        # Pas du tout efficace
        self.jack_pv = 10

        self.physicals_objects_list = {}
        print(type(self.physicals_objects_list))

    def set_position_player(self, name, position_x, position_y):
        self.physicals_objects_list[name] = (position_x, position_y)
        print(f" Player {name} now at x={position_x} y={position_y} )")

    def can_move(self, name: str, position_x: int, position_y: int, direction: str, speed: int):
        return (position_x, position_y) != self.get_next_position(
            name, position_x, position_y, direction, speed)

    def get_next_theorical_position(self, position_x: int, position_y: int, direction: str, speed: int) \
            -> (int, int):
        if direction == "right":
            position_x += speed
        elif direction == "left":
            position_x -= speed
        elif direction == "up":
            position_y -= speed
        elif direction == "down":
            position_y += speed
        return position_x, position_y

    def get_next_position(self, name: str, position_x: int, position_y: int, direction: str, speed: int) \
            -> (int, int):
        futur_x, futur_y = self.get_next_theorical_position(position_x, position_y, direction, speed)
        if futur_x > 710:
            futur_x = 710
        elif futur_x < 0:
            futur_x = 0
        elif futur_y < 0:
            futur_y = 0
        elif futur_y > 420:
            futur_y = 420
        return self.get_next_position_against_items(name, futur_x, futur_y, direction)

    def get_next_position_against_items(self, name: str, position_x: int, position_y: int, direction: str) -> (int, int):
        item = self.is_collision_detected(name, position_x, position_y)
        if item:
            item_x, item_y = self.physicals_objects_list[item]
            shift = 1
            if direction == "right":
                position_x = item_x - (self.height + shift)
            elif direction == "left":
                position_x = item_x + (self.height + shift)
            elif direction == "up":
                position_y = item_y + (self.length + shift)
            elif direction == "down":
                position_y = item_y - (self.length + shift)
        return position_x, position_y

    def is_collision_detected(self, name: str, position_x: int, position_y: int) -> str:
        """
        Detect avec quel objet on est en collision sinon retourne None
        """
        for self.object_name, (x, y) in self.physicals_objects_list.items():
            if name != self.object_name:
                if position_x + self.height >= x and \
                        position_x <= x + self.height and \
                        position_y + self.length >= y and \
                        position_y <= y + self.length:
                    # Return name of the object in collision not the player
                    self.action_after_collision()
                    return self.object_name
        return None

    def action_after_collision(self):
        if self.object_name == "box_tnt":
            self.jack_pv = 0
        elif self.object_name == "box_portal":
            self.key_found = True
