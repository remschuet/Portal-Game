from not_alive_object import SceneObject


class InitObject:
    def __init__(self):
        self.map_canvas = None
        self.environment = None

        self.box01 = None

        self.box02 = None
        self.tnt_box = None
        self.portal_box = None

    def level_01(self, map_canvas, environment):
        self.map_canvas = map_canvas
        self.environment = environment

        print("InitObject on")
        self.box01 = SceneObject("box01", self.map_canvas, self.environment,
                                 position_x=300, position_y=300, pv=100, height=70, length=70, photo_name="box")

        self.box02 = SceneObject("box02", self.map_canvas, self.environment,
                                 position_x=400, position_y=100, pv=100, height=70, length=70, photo_name="box")

        self.tnt_box = SceneObject("box_tnt", self.map_canvas, self.environment,
                                   position_x=400, position_y=350, pv=100, height=70, length=70, photo_name="box_tnt")

        self.portal_box = SceneObject("box_portal", self.map_canvas, self.environment,
                                      position_x=600, position_y=410, pv=100, height=70, length=70, photo_name="box_portal")
