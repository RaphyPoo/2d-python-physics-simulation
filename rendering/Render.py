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
        self.width = 1000
        self.height = 1000
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Physics Simulations")

    def main_menu(self):
      while True:
          pygame.display.set_caption("Physics Simulations")
          MENU_MOUSE_POS = pygame.mouse.get_pos()

          MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
          MENU_RECT = MENU_TEXT.get_rect(center=(self.width/2, 100))

          SIMULATION_ONE_BUTTON = Button(image=None, pos=(self.width/2, 250), 
                              text_input="Simulation 1", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
          
          SIMULATION_TWO_BUTTON = Button(image=None, pos=(self.width/2, 350), 
                              text_input="Simulation 2", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

          SIMULATION_THREE_BUTTON = Button(image=None, pos=(self.width/2, 450), 
                              text_input="Simulation 3", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

          QUIT_BUTTON = Button(image=None, pos=(self.width/2, 550), 
                              text_input="Quit", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

          self.screen.blit(MENU_TEXT, MENU_RECT)

          for button in [SIMULATION_ONE_BUTTON, SIMULATION_TWO_BUTTON, SIMULATION_THREE_BUTTON, QUIT_BUTTON]:
              button.changeColor(MENU_MOUSE_POS)
              button.update(self.screen)
          
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              if event.type == pygame.MOUSEBUTTONDOWN:
                  if SIMULATION_ONE_BUTTON.checkForInput(MENU_MOUSE_POS):
                      self.Simulation1()
                  if SIMULATION_TWO_BUTTON.checkForInput(MENU_MOUSE_POS):
                      self.Simulation2()
                  if SIMULATION_THREE_BUTTON.checkForInput(MENU_MOUSE_POS):
                      self.Simulation3()
                  if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                      pygame.quit()
                      sys.exit()

          pygame.display.update()

    def Simulation1(self):
        physics = Physics(0, 100)
        self.screen.fill((0, 0, 0))
        circles = []
        lines = []
        lines.append(Line((self.width/2, self.height), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics, self))
        lines.append(Line((self.width/2, self.height), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics, self))

        circles.append(Circle((self.width/2 - 10, self.height/2), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics, self))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            physics.space.step(1 / 50)
            for line in lines:
                line.draw()
            for circle in circles:
                circle.draw()
            pygame.display.update()
            self.clock.tick(120)

    def Simulation2(self):
        physics_1 = Physics(0, 100)
        physics_2 = Physics(0, -100)
        physics_3 = Physics(100, 0)
        physics_4 = Physics(-100, 0)

        self.screen.fill((0, 0, 0))
        circles = []
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

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for physic in physics:
                physic.space.step(1 / 50)        
            for line in lines:
                line.draw()
            for circle in circles:
                circle.draw()

            pygame.display.update()
            self.clock.tick(120)

    def Simulation3(self):
        physics_1 = Physics(0, 100)
        physics_2 = Physics(0, -100)
        physics_3 = Physics(100, 0)
        physics_4 = Physics(-100, 0)

        self.screen.fill((0, 0, 0))
        circles = []
        line_bottom_left = Line((self.width/2, self.height), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_1, self)
        line_bottom_right = Line((self.width/2, self.height), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_1, self)
        circle_1 = Circle((self.width/2 - self.width/4, self.height/2), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_1, self)

        line_top_left = Line((self.width/2, 0), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_2, self)
        line_top_right = Line((self.width/2, 0), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_2, self)
        circle_2 = Circle((self.width/2 + self.width/4, self.height/2), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_2, self)
        
        line_top_left_2 = Line((self.width/2, 0), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_3, self)
        line_bottom_left_2 = Line((self.width/2, self.height), (self.width, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_3, self)
        circle_3 = Circle((self.width/2, self.height/2 + self.width/4), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_3, self)

        line_top_right_2 = Line((self.width/2, 0), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_4, self)
        line_bottom_right_2 = Line((self.width/2, self.height), (0, self.height/2), 1.0, pymunk.Body.STATIC, 10, 5, physics_4, self)
        circle_4 = Circle((self.width/2, self.height/2 - self.width/4), 1.0, pymunk.Body.DYNAMIC, 100, 2, physics_4, self)

        lines = [line_bottom_left, line_bottom_right, line_top_left, line_top_right]
        circles = [circle_1, circle_2, circle_3, circle_4]
        physics = [physics_1, physics_2, physics_3, physics_4]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for physic in physics:
                physic.space.step(1 / 50)        
            for line in lines:
                line.draw()
            for circle in circles:
                circle.draw()

            pygame.display.update()
            self.clock.tick(120)

            
