import pygame
from math import *


class Player:
    def __init__(self, fps_count, fps_clock, screen, ball_img):
        self.fps_count = fps_count  # frames per second setting
        self.fps_clock = fps_clock
        self.screen = screen
        self.ball_img = ball_img

    def shoot(self, v_0, ball_0):
        final_values = {
            'final_velocity': 0,
            'v_x': 0,
            'v_y': 0,
            'x_max': 0,
            'y_max': 0,
            't': 0
        }
        t = 0

        ball_travelling = True

        while ball_travelling:
            dt = self.fps_clock.tick(self.fps_count)
            t = t + dt / 250.0
            a = (0.0, 10.0)
            v = (v_0[0] + a[0] * t, v_0[1] + a[1] * t)
            s_0 = ball_0
            s = (s_0[0] + v_0[0] * t + a[0] * t * t / 2, s_0[1] + v_0[1] * t + a[1] * t * t / 2)
            self.screen.blit(self.ball_img, s)
            pygame.display.flip()
            # TODO: Change this coordinate to the actual floor of the simulator
            if s[1] >= 486:
                final_values['final_velocity'] = sqrt(v[0]*v[0] + v[1]*v[1])
                final_values['v_x'] = v[0]
                final_values['v_y'] = v[1]
                final_values['x_max'] = s[0]
                final_values['y_max'] = s[1]
                final_values['t'] = t
                ball_travelling = False

        return final_values
