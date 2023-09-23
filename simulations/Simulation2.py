import sys
import pygame
import pymunk
from physics.Physics import Physics
from objects.Circle import Circle
from objects.Line import Line

class Simulation2: 
    def __init__(self, render):
        is_paused = [False]
        self.render = render
        self.screen = render.screen
        self.width = render.width
        self.height = render.height
        self.clock = render.clock

        physics_1 = Physics(0, 100)
        physics_2 = Physics(0, -100)
        physics_3 = Physics(100, 0)
        physics_4 = Physics(-100, 0)

        self.screen.fill((0, 0, 0))
        line_bottom_left = Line((self.width/2, self.height), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_1, self)
        line_bottom_right = Line((self.width/2, self.height), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_1, self)
        circle_1 = Circle((self.width/2 - 5, self.height/2), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_1, self)

        line_top_left = Line((self.width/2, 0), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_2, self)
        line_top_right = Line((self.width/2, 0), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_2, self)
        circle_2 = Circle((self.width/2 + 5, self.height/2), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_2, self)
        
        line_top_left_2 = Line((self.width/2, 0), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_3, self)
        line_bottom_left_2 = Line((self.width/2, self.height), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_3, self)
        circle_3 = Circle((self.width/2, self.height/2 + 5), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_3, self)

        line_top_right_2 = Line((self.width/2, 0), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_4, self)
        line_bottom_right_2 = Line((self.width/2, self.height), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_4, self)
        circle_4 = Circle((self.width/2, self.height/2 - 5), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_4, self)

        lines = [line_bottom_left, line_bottom_right, line_top_left, line_top_right]
        circles = [circle_1, circle_2, circle_3, circle_4]
        physics = [physics_1, physics_2, physics_3, physics_4]
        trails = []

        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                    if is_paused[0] == True:
                        is_paused[0] = False
                    else:
                        is_paused[0] = True

            for physic in physics:
                physic.space.step(1 / 50)        
            for line in lines:
                line.draw()
            for circle in circles:
                circle.draw()
                trails.append(circle.body.position)

            for trail in trails:
                pygame.draw.circle(self.screen, (255, 255, 255), trail, 2)

            if is_paused[0] == True:
                self.render.pause_menu(is_paused)

            pygame.display.update()
            self.clock.tick(120)