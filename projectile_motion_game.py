from pygame.locals import *
from math import *
import pygame
from projectile_motion.player import Player
from GUI.main_ui import MainUI

START_V = 100
START_ANG = 45


class ProjectileMotionGame:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("Calibri", 20)
        self.clock = pygame.time.Clock()
        self.res = (1280, 720)
        self.fps_count = 60
        self.screen = pygame.display.set_mode(self.res, 0, 32)
        pygame.display.set_caption('Projectile motion simulator')
        self.gui = MainUI(self.screen)

        self.sprites = {
            'background': {
                'x_y': (0, 0),
                'img': pygame.image.load('assets/background.png')
            },
            'hoop': {
                'x_y': (950, 140),
                'img': pygame.image.load('assets/hoop.png')
            },
            'player': {
                'x_y': (30, 220),
                'img': pygame.image.load('assets/player.png')
            },
            'ball': {
                'x_y': (150, 240),
                'img': pygame.image.load('assets/ball_60.png')
            }
        }

        self.player = Player(self.fps_count, self.clock, self.screen, self.sprites)
        self.shot_data = shot_data = {
            'final_velocity': 0,
            'v_x': 0,
            'v_y': 0,
            'x_max': 0,
            'y_max': 0,
            't': 0
        }

    def draw_sprites(self):
        for sprite in self.sprites:
            current_sprite = self.sprites.get(sprite)
            self.screen.blit(current_sprite.get('img'), current_sprite.get('x_y'))


    def draw_gui(self):
        self.clock.tick(self.fps_count)
        self.gui.update()
        pygame.display.flip()

    def draw_text(self):
        text_v_f = self.font.render(f"Velocidad final: {self.shot_data.get('final_velocity'):.3f}",
                                    True,
                                    pygame.Color('white'))
        text_v_f_x_y = (800, 30)

        text_v_x = self.font.render(f"Velocidad en eje x: {self.shot_data.get('v_x'):.3f}",
                                    True,
                                    pygame.Color('white'))
        text_v_x_x_y = (800, 50)

        text_v_y = self.font.render(f"Velocidad en eje y: {self.shot_data.get('v_y'):.3f}",
                                    True,
                                    pygame.Color('white'))
        text_v_y_x_y = (800, 70)

        text_d = self.font.render(f"Distancia recorrida: {self.shot_data.get('x_max'):.3f}",
                                  True,
                                  pygame.Color('white'))
        text_d_x_y = (800, 90)

        text_h = self.font.render(f"Altura: {self.shot_data.get('y_max'):.3f}",
                                  True,
                                  pygame.Color('white'))
        text_h_x_y = (800, 110)

        text_t = self.font.render(f"Tiempo: {self.shot_data.get('t'):.3f}",
                                  True,
                                  pygame.Color('white'))
        text_t_x_y = (800, 130)

        self.screen.blit(text_v_f, text_v_f_x_y)
        self.screen.blit(text_v_x, text_v_x_x_y)
        self.screen.blit(text_v_y, text_v_y_x_y)
        self.screen.blit(text_d, text_d_x_y)
        self.screen.blit(text_h, text_h_x_y)
        self.screen.blit(text_t, text_t_x_y)
        pygame.display.flip()

    def event_loop(self):
        angle = START_ANG
        velocity = START_V

        for event in pygame.event.get():
            self.gui.check_events(event)
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if self.gui.textboxes['angle'].text:
                    angle = float(self.gui.textboxes['angle'].text)
                if self.gui.textboxes['v_0'].text:
                    velocity = float(self.gui.textboxes['v_0'].text)
                v_0 = (velocity * cos(radians(angle)), -velocity * sin(radians(angle)))
                self.shot_data = self.player.shoot(v_0, self.sprites.get('ball').get('x_y'))
                self.draw_text()


if __name__ == '__main__':
    projectile_motion_game = ProjectileMotionGame()
    while True:
        projectile_motion_game.draw_sprites()
        projectile_motion_game.draw_gui()
        projectile_motion_game.draw_text()
        projectile_motion_game.event_loop()
