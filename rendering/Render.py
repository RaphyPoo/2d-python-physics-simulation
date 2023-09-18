import sys
import pygame
from physics.Physics import Physics


class Render:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))  # creating the display surface
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.Physics = Physics()
        pygame.init()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                # create_apple(space, event.pos)
                # apples.append(create_apple(space, event.pos))
        self.screen.fill((0, 0, 0))
        space.step(1 / 50)
        pygame.display.update()
        clock.tick(120)

    def draw_static_ball(self, balls):
        for ball in balls:
            pos_x = int(ball.body.position.x)
            pos_y = int(ball.body.position.y)
            pygame.draw.circle(self.screen, (255, 255, 255), (pos_x, pos_y), 50)

    def draw_apples(self, apples):
        for apple in apples:
            pos_x = int(apple.body.position.x)
            pos_y = int(apple.body.position.y)
            pygame.draw.circle(self.screen, (255, 255, 255), (pos_x, pos_y), 80)
