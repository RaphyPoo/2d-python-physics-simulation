import pymunk


def create_circle(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape


def create_static_circle(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape


class Physics:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.step(1 / 50)
        self.space.gravity = (0, 20)
