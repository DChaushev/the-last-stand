import pygame, glob
from pygame.locals import *
import enumerations
from enumerations import *
import random
from random import randint


l_run_ani = glob.glob("zombie sprite/walk/z-walk-left*.png")
l_dead_ani = glob.glob("zombie sprite/dead/z-dead-left*.png")

l_run_ani.sort()
l_dead_ani.sort()

R_ANIMATION_RUN = []
R_ANIMATION_DEAD = []
L_ANIMATION_RUN = []
L_ANIMATION_DEAD = []

for i in range(0, len(l_run_ani)):
    R_ANIMATION_RUN.append(pygame.transform.flip(pygame.image.load(l_run_ani[i]), True, False))
    L_ANIMATION_RUN.append(pygame.image.load(l_run_ani[i]))

for i in range(0, len(l_dead_ani)):
    R_ANIMATION_DEAD.append(pygame.transform.flip(pygame.image.load(l_dead_ani[i]), True, False))
    L_ANIMATION_DEAD.append(pygame.image.load(l_dead_ani[i]))


class Zombie:

    def __init__(self):
        self.is_alive = True
        self.health = 15
        yy = randint(-20, 800)
        lx = randint(-300, -50)
        rx = randint(1074, 1324)
        if yy < 0 or yy > 768:
            xx = randint(0, 1024)
            self.x = xx
        else:
            self.x = random.choice([rx, lx])
        self.y = yy
        self.facing = RIGHT
        self.animation_position_run = 0
        self.animation_position_max = len(l_run_ani) - 1
        self.animation_dead_position = 0
        self.animation_dead_max = len(l_dead_ani) - 1
        self.surface = R_ANIMATION_RUN[self.animation_position_run]
        self.speed = 1

    def update(self, x, y, player_width, player_height):

        zombie_width = self.surface.get_width()
        zombie_height = self.surface.get_height()

        if self.is_alive:
            if self.x + int(zombie_width/2) < x + int(player_width/2):
                self.x += self.speed
                self.surface = R_ANIMATION_RUN[self.animation_position_run]
            else:
                self.x -= self.speed
                self.surface = L_ANIMATION_RUN[self.animation_position_run]
            if self.y + int(zombie_height/2) < y + int(player_height/2):
                self.y += self.speed
            else:
                self.y -= self.speed

            if self.animation_position_run == self.animation_position_max:
                    self.animation_position_run = 0
            else:
                self.animation_position_run += 1

        else:
            if self.x < x + int(player_width/2):
                self.surface = R_ANIMATION_DEAD[self.animation_dead_position]
            else:
                self.surface = L_ANIMATION_DEAD[self.animation_dead_position]

            if self.animation_dead_position == self.animation_dead_max:
                pass
            else:
                self.animation_dead_position += 1


        if self.x + int(zombie_width/2) > x and self.x + int(zombie_width/2) < x + player_width and self.y + int(zombie_height/2) > y and self.y + int(zombie_height/2) < y + player_height:
            return 1

        return 0