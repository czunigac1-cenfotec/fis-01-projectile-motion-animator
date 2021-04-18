from pygame.locals import *
import pygame


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.res = [640, 480]
        self.FPS = 50
        self.screen = pygame.display.set_mode(self.res)

        self.font = pygame.font.SysFont("Calibri", 16)

        #ToDo: Create main_gui instance


    def start(self):
        raise NotImplementedError

    def draw_gui(self):
        raise NotImplementedError

    def event_loop(self):
        for event in pygame.event.get():
            #self.GUI.check_events(event)
            if event.type == QUIT:
                self.running = 0
                pygame.quit()