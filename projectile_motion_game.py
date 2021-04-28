from pygame.locals import *
from math import *
import pygame
from projectile_motion.player import Player

START_V = 100
START_ANG = 45

class ProjectileMotionGame:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.res = (1280, 720)
        self.fps_count = 60
        self.screen = pygame.display.set_mode(self.res, 0, 32)
        pygame.display.set_caption('Projectile motion simulator')

        self.font = pygame.font.SysFont("Calibri", 16)

        self.player_x_y = (-5, 450)
        self.ball_x_y = (22, 478)
        self.player = None
        self.start()

        #ToDo: Create main_gui instance

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def start(self):
        #background_img = pygame.image.load('assets/potw1703a.jpg')
        #player_img = pygame.image.load('assets/player.png')
        ball_img = pygame.image.load('assets/ball.png')

        #player_img = pygame.transform.rotate(player_img, -15)
        #player_mov_img = self.rot_center(player_img, shooting_angle)

        #self.screen.blit(background_img, (0, 0))
        #self.screen.blit(player_mov_img, player_x_y)
        self.screen.blit(ball_img, self.ball_x_y)

        self.player = Player(self.fps_count, self.clock, self.screen, ball_img)


    def draw_gui(self):
        raise NotImplementedError

    def event_loop(self):
        angle = START_ANG
        velocity = START_V

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    v_0 = (velocity * cos(radians(angle)), -velocity * sin(radians(angle)))
                    print(self.player.shoot(v_0,(22,478)))

        keystate = pygame.key.get_pressed()

        #TODO: Replace ang defnition from textboxes.text

        if keystate[K_LEFT]:  # rotate conterclockwise
            angle += 2
            if angle > 90:
                angle = 90
            #cannonMovImg = self.rot_center(cannonImg, ang)

        if keystate[K_RIGHT]:  # rotate clockwise
            angle -= 2
            if angle < 0:
                ang = 0
            #cannonMovImg = rot_center(cannonImg, ang)
        pygame.display.flip()


if __name__ == '__main__':
    projectile_motion_game = ProjectileMotionGame()
    while True:
        projectile_motion_game.event_loop()

