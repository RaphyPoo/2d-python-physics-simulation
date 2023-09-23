import pymunk 
import pygame

class Line:
    def __init__(self, pos_1, pos_2, elasticity, body_type, mass, width, physics, render):
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.elasticity = elasticity
        self.body_type = body_type
        self.width = width
        self.physics = physics
        self.render = render

        self.body = pymunk.Body(mass, 100, body_type=self.body_type)
        shape = pymunk.Segment(self.body, pos_1, pos_2, 5)
        shape.elasticity = self.elasticity
        self.add_to_space(shape)

    def draw(self):
        pygame.draw.line(self.render.screen, (255, 255, 255), self.pos_1, self.pos_2, self.width)

    def add_to_space(self, shape):
        self.physics.space.add(self.body, shape)