import sys
import pygame
import pymunk
from physics.Physics import Physics
from objects.Circle import Circle
from objects.Line import Line

class Simulation1: 
    def __init__(self, render):
        is_paused = [False]
        self.render = render
        self.screen = render.screen
        self.width = render.width
        self.height = render.height
        self.clock = render.clock

        physics = Physics(0, 100)
        self.screen.fill((0, 0, 0))
        lines = []
        circles = []
        lines.append(Line((self.width/2, self.height), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics, self))
        lines.append(Line((self.width/2, self.height), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics, self))

        circles.append(Circle((self.width/2 - 10, self.height/2), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics, self))

        while True:
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

            physics.space.step(1 / 50)
            for line in lines:
                line.draw()
            for circle in circles:
                circle.draw()

            if is_paused[0] == True:
                self.render.pause_menu(is_paused)
            pygame.display.update()
            self.clock.tick(120)