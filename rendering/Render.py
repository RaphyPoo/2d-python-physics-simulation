import sys
import pygame
from physics.Physics import Physics


class Render:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.Physics = Physics()
        pygame.display.set_caption("Physics Simulations")

    def run(self):
        circles = []
        isPlaying = True
        while isPlaying:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    circles.append(self.Physics.create_circle(event.pos))

            self.screen.fill((0, 0, 0))
            self.Physics.space.step(1 / 50)
            self.draw_circles(circles)
            pygame.display.update()
            self.clock.tick(120)

    def draw_static_ball(self, balls):
        for ball in balls:
            pos_x = int(ball.body.position.x)
            pos_y = int(ball.body.position.y)
            pygame.draw.circle(self.screen, (255, 255, 255), (pos_x, pos_y), balls.radius)

    def draw_circles(self, circles):
        for circle in circles:
            pos_x = int(circle.body.position.x)
            pos_y = int(circle.body.position.y)
            pygame.draw.circle(self.screen, (255, 255, 255), (pos_x, pos_y), circle.radius)
