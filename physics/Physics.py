import pymunk


class Physics:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 20)
