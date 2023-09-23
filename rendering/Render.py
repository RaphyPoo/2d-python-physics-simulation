import sys
import pygame
import pymunk
from rendering.Button import Button
from simulations.Simulation1 import Simulation1
from simulations.Simulation2 import Simulation2
from simulations.Simulation3 import Simulation3

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
      self.screen.fill((0, 0, 0))

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
                      Simulation1(self)
                  if SIMULATION_TWO_BUTTON.checkForInput(MENU_MOUSE_POS):
                      Simulation2(self)
                  if SIMULATION_THREE_BUTTON.checkForInput(MENU_MOUSE_POS):
                      Simulation3(self)
                  if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                      pygame.quit()
                      sys.exit()

          pygame.display.update()

    def pause_menu(self, is_paused):
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("PAUSED", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.width/2, 100))

        RESUME_BUTTON = Button(image=None, pos=(self.width/2, 250), 
                            text_input="Resume", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        MAIN_MENU_BUTTON = Button(image=None, pos=(self.width/2, 350), 
                            text_input="Main Menu", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        self.screen.blit(MENU_TEXT, MENU_RECT)

        for button in [RESUME_BUTTON, MAIN_MENU_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(self.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    is_paused[0] = False
                if MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.main_menu()

        pygame.display.update()