import pymunk


class Physics:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 20)

    def create_circle(self, pos):
        body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
        body.position = pos
        shape = pymunk.Circle(body, 50)
        self.space.add(body, shape)
        return shape

    def create_static_circle(self, pos):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Circle(body, 50)
        self.space.add(body, shape)
        return shape
