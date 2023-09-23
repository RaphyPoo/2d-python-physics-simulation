import pymunk
import pygame

class Circle:
    def __init__(self, pos, elasticity, body_type, mass, radius, physics, render):
        self.pos = pos
        self.elasticity = elasticity
        self.body_type = body_type
        self.radius = radius
        self.physics = physics
        self.render = render

        self.body = pymunk.Body(mass, 100, body_type=self.body_type)
        self.body.position = self.pos
        shape = pymunk.Circle(self.body, self.radius)
        shape.elasticity = self.elasticity
        self.physics.space.add(self.body, shape)
    
    def draw(self):
        pos_x = int(self.body.position.x)
        pos_y = int(self.body.position.y)
        pygame.draw.circle(self.render.screen, (255, 255, 255), (pos_x, pos_y), self.radius)

    