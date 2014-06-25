import pygame, glob
from pygame.locals import *
import enumerations
from enumerations import *

L_TROOPER_STAND = pygame.image.load('soldier sprite/stand_left.png')
R_TROOPER_STAND = pygame.transform.flip(L_TROOPER_STAND, True, False)

r_run_ani = glob.glob("soldier sprite/run/tmp-*.gif")
r_dead_ani = glob.glob("soldier sprite/die/tmp-*.gif")

r_run_ani.sort()
r_dead_ani.sort()

R_ANIMATION_RUN = []
R_ANIMATION_DEAD = []
L_ANIMATION_RUN = []
L_ANIMATION_DEAD = []

for i in range(0, len(r_run_ani)):
    L_ANIMATION_RUN.append(pygame.transform.flip(pygame.image.load(r_run_ani[i]), True, False))
    R_ANIMATION_RUN.append(pygame.image.load(r_run_ani[i]))

for i in range(0, len(r_dead_ani)):
    L_ANIMATION_DEAD.append(pygame.transform.flip(pygame.image.load(r_dead_ani[i]), True, False))
    R_ANIMATION_DEAD.append(pygame.image.load(r_dead_ani[i]))

class Hero:

    def __init__(self):
        self.is_alive = True
        self.power = 5
        self.facing = RIGHT
        self.x = int(WINDOW_WIDTH/2)
        self.y = int(WINDOW_HEIGHT/2)
        self.surface = R_TROOPER_STAND
        self.animation_position_dead = 0
        self.animation_position_run = 0
        self.animation_max = len(R_ANIMATION_RUN) - 1
        self.animation_dead_max = len(R_ANIMATION_DEAD) - 1
        self.speed = 2
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.fire = False

    def update(self):
        if self.is_alive:
            if self.move_left:
                self.x -= self.speed
                self.facing = LEFT
                self.surface = L_ANIMATION_RUN[self.animation_position_run]
            if self.move_right:
                self.x += self.speed
                self.facing = RIGHT
                self.surface = R_ANIMATION_RUN[self.animation_position_run]
            if self.move_down:
                self.y += self.speed
                if self.facing == LEFT:
                   self.surface = L_ANIMATION_RUN[self.animation_position_run]
                elif self.facing == RIGHT:
                    self.surface = R_ANIMATION_RUN[self.animation_position_run]
            if self.move_up:
                self.y -= self.speed
                if self.facing == LEFT:
                   self.surface = L_ANIMATION_RUN[self.animation_position_run]
                elif self.facing == RIGHT:
                    self.surface = R_ANIMATION_RUN[self.animation_position_run]

            if self.fire:
                if self.facing == LEFT:
                    self.surface = pygame.image.load('soldier sprite/shoot_left.png')
                elif self.facing == RIGHT:
                    self.surface = pygame.transform.flip(pygame.image.load('soldier sprite/shoot_left.png'), True, False)

            elif not self.move_left and not self.move_right and not self.move_up and not self.move_down:
                if self.facing == RIGHT:
                    self.surface = R_TROOPER_STAND
                elif self.facing == LEFT:
                    self.surface = L_TROOPER_STAND

            if self.animation_position_run == self.animation_max:
                self.animation_position_run = 0
            else:
                self.animation_position_run += 1

        else:
            if self.facing == RIGHT:
                self.surface = R_ANIMATION_DEAD[self.animation_position_dead]
            else:
                self.surface = L_ANIMATION_DEAD[self.animation_position_dead]

            if self.animation_position_dead == self.animation_dead_max:
                pass
            else:
                self.animation_position_dead += 1
