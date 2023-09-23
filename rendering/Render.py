import sys
import pygame
import pymunk
from rendering.Button import Button
from physics.Physics import Physics
from objects.Circle import Circle
from objects.Line import Line


def get_font(size):
    return pygame.font.Font("assets/Font.ttf", size)

class Render:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 900))
        self.clock = pygame.time.Clock()
        self.Physics = Physics()
        pygame.display.set_caption("Physics Simulations")

    def main_menu(self):
      while True:
          pygame.display.set_caption("Physics Simulations")
          MENU_MOUSE_POS = pygame.mouse.get_pos()

          MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
          MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

          PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                              text_input="Simulation 1", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
          QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                              text_input="Quit", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

          self.screen.blit(MENU_TEXT, MENU_RECT)

          for button in [PLAY_BUTTON, QUIT_BUTTON]:
              button.changeColor(MENU_MOUSE_POS)
              button.update(self.screen)
          
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              if event.type == pygame.MOUSEBUTTONDOWN:
                  if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                      self.Simulation1()
                  if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                      pygame.quit()
                      sys.exit()

          pygame.display.update()

    def Simulation1(self):
        circles = []
        lines = []
        lines.append(Line((0, 800), (1280, 800), 1.0, pymunk.Body.STATIC, 10, 5, self.Physics, self))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    circles.append(Circle(event.pos, 1.0, pymunk.Body.DYNAMIC, 10, 50, self.Physics, self))

            self.screen.fill((0, 0, 0))
            self.Physics.space.step(1 / 50)
            for line in lines:
                line.draw()
            for circle in circles:
                circle.draw()
            pygame.display.update()
            self.clock.tick(120)

