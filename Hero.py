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
        self.shooting = False
        self.score = 0

    def update(self):
        if self.is_alive:
            if self.move_left and self.x > 0:
                self.x -= self.speed
                self.facing = LEFT
                self.surface = L_ANIMATION_RUN[self.animation_position_run]
            if self.move_right and self.x + self.surface.get_width() < WINDOW_WIDTH:
                self.x += self.speed
                self.facing = RIGHT
                self.surface = R_ANIMATION_RUN[self.animation_position_run]
            if self.move_down and self.y < WINDOW_HEIGHT - self.surface.get_height():
                self.y += self.speed
                if self.facing == LEFT:
                   self.surface = L_ANIMATION_RUN[self.animation_position_run]
                elif self.facing == RIGHT:
                    self.surface = R_ANIMATION_RUN[self.animation_position_run]
            if self.move_up and self.y > 0:
                self.y -= self.speed
                if self.facing == LEFT:
                   self.surface = L_ANIMATION_RUN[self.animation_position_run]
                elif self.facing == RIGHT:
                    self.surface = R_ANIMATION_RUN[self.animation_position_run]

            if self.shooting:
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
            elif self.animation_position_dead < self.animation_dead_max:
                self.animation_position_dead += 1


    """
    I am very proud of this function.
    When the player fires, depending on the side he is facing, we check only for hit on that side.
    The zombies are sorted by the distance to the player and we are always hitting the closest one.

    ANSWER TO THE QUESTION WHY THERE IS NO SHOOTIN DOWN:
        -because I were't able to find good spritesheets :D
    """

    def fire(self, zombies):
        if self.facing == RIGHT:
            zombies = [z for z in zombies if z.x > self.x]
            zombies.sort(key= lambda z: z.x)
            for z in zombies:
                if self.y + 21 >= z.y and self.y + 21 <= z.y + z.surface.get_height():
                    z.health -= self.power
                    if z.health <= 0:
                        z.is_alive = False
                        self.score += 5
                    return

        elif self.facing == LEFT:
            zombies = [z for z in zombies if z.x < self.x]
            zombies.sort(key= lambda z: z.x, reverse = True)
            for z in zombies:
                if self.y + 21 >= z.y and self.y + 21 <= z.y + z.surface.get_height():
                    z.health -= self.power
                    if z.health <= 0:
                        z.is_alive = False
                        self.score += 5
                    return