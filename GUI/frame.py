import pygame
from pygame.locals import *
import sys


class Frame(object):
    ''' Frame class, holds widgets and updates them also'''
    def __init__(self, screen, size, pos):

        self.screen = screen
        self.size = size
        self.pos = pos
        
        
        self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)


        self.widgets = []



    def update(self):
        self.screen.blit(self.image, (self.rect))

        for w in self.widgets:
            w.update()
            w.draw(self.image)

    def off(self, rect):
        rect.x = rect.x + self.rect.x
        rect.y = rect.y + self.rect.y        
        return rect

    def check_events(self, event):
        for w in self.widgets:
            w.check_events(event)