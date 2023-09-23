import pymunk


class Physics:
    def __init__(self, gravity_x, gravity_y):
        self.space = pymunk.Space()
        self.space.gravity = (gravity_x, gravity_y)
