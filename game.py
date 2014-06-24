import pygame, sys, time, random, glob
from pygame.locals import *
from random import randint

FPS = 30
# WINWIDTH = 1024
# WINHEIGHT = 768
# PLAYERX = int(WINWIDTH / 2)
# PLAYERY = int(WINHEIGHT / 2)
PISTOL = 'pistol'
MACHINEGUN = 'machine_gun'
TERRAINCOLOR = (10, 127, 2)
RIGHT = 'right'
LEFT = 'left'
SPEED = 2
ZOMBIESPEED = 1


# class Hero:
#     def __init__(self):
#         self.isAlive = True
#         self.facing = RIGHT
#         self.x = PLAYERX
#         self.y = PLAYERY
#         self.surface = R_TROOPER_WEAPON
#         self.ani_speed_init = 10
#         self.ani_speed = self.ani_speed_init
#         self.ani = glob.glob("soldier sprite/run/tmp-*.gif")
#         self.ani_dead = glob.glob("soldier sprite/die/tmp-*.gif")
#         self.ani.sort()
#         self.ani_dead.sort()
#         self.ani_pos_dead = 0
#         self.ani_pos = 0
#         self.ani_max = len(self.ani) - 1
#         self.ani_max_dead = len(self.ani_dead) - 1
#         self.width = self.surface.get_width()
#         self.height = self.surface.get_height()
#         print(self.width)
#         print(self.height)
#         self.rect = pygame.Rect(self.x, self.y, self.x + self.width, self.y + self.height)
#         print(self.rect)
#         self.update([])
#
#     def update(self, zombies):
#         if self.isAlive:
#             if moveLeft:
#                 self.x -= SPEED
#                 self.surface = L_TROOPER_WEAPON
#                 self.facing = LEFT
#                 self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
#             if moveRight:
#                 self.x += SPEED
#                 self.facing = RIGHT
#                 self.surface = pygame.image.load(self.ani[self.ani_pos])
#             if moveUp:
#                 self.y -= SPEED
#                 if self.facing == LEFT:
#                     self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
#                 else:
#                     self.surface = pygame.image.load(self.ani[self.ani_pos])
#             if moveDown:
#                 self.y += SPEED
#                 if self.facing == LEFT:
#                     self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
#                 else:
#                     self.surface = pygame.image.load(self.ani[self.ani_pos])
#             if fire:
#                 self.fireWeapon(zombies)
#             if self.ani_pos == self.ani_max:
#                 self.ani_pos = 0
#             else:
#                 self.ani_pos += 1
#
#             self.rect = pygame.Rect(self.x, self.y, self.x + self.width, self.y + self.height)
#             if pygame.Rect.colliderect(self.rect, tree_rect):
#                 print("collide withe tree")
#
#         elif self.isAlive == False:
#             if self.facing == RIGHT:
#                 self.surface = pygame.image.load(self.ani_dead[self.ani_pos_dead])
#             else:
#                 self.surface = pygame.transform.flip(pygame.image.load(self.ani_dead[self.ani_pos_dead]), True, False)
#             if self.ani_pos_dead == self.ani_max_dead:
#                 pass
#             else:
#                 self.ani_pos_dead += 1
#
#         else:
#             self.surface = pygame.image.load('soldier sprite/soldier_dead.gif')
#
#         DISPLAYSURF.blit(self.surface, (self.x, self.y))
#
#
#     def fireWeapon(self, zombies):
#         for zombie in zombies:
#             if type(zombie) == type(Zombie()):
#                 if self.facing == LEFT:
#                     self.surface = pygame.image.load('soldier sprite/shoot_left.png')
#                     if zombie.x < self.x:
#                         if zombie.y <= self.y + 64 / 2 and zombie.y >= self.y:
#                             zombie.isAlive = False
#                             return
#                 if self.facing == RIGHT:
#                     self.surface = pygame.transform.flip(pygame.image.load('soldier sprite/shoot_left.png'), True,
#                                                          False)
#                     if zombie.x > self.x and zombie.x:
#                         if zombie.y <= self.y + 64 / 2 and zombie.y >= self.y:
#                             zombie.health -= 5
#                             print(zombie.health)
#                             if zombie.health <= 0:
#                                 zombie.isAlive = False
#                             return
#
#             elif type(zombie == type(Butcher())):
#                 if self.facing == LEFT:
#                     self.surface = pygame.image.load('soldier sprite/shoot_left.png')
#                     if zombie.x < self.x:
#                         if zombie.y <= self.y + int(pygame.Surface.get_height(zombie.surface)) and zombie.y + int(
#                                 pygame.Surface.get_height(zombie.surface)) >= self.y:
#                             zombie.health -= 0.2
#                             zombie.surface = pygame.image.load('zombie sprite/Butcher_hit_right.png')
#                             print(zombie.health)
#                             if zombie.health <= 0:
#                                 zombie.isAlive = False
#                             return
#                 if self.facing == RIGHT:
#                     self.surface = pygame.transform.flip(pygame.image.load('soldier sprite/shoot_left.png'), True,
#                                                          False)
#                     if zombie.x > self.x and zombie.x:
#                         if zombie.y <= self.y + int(pygame.Surface.get_height(zombie.surface)) and zombie.y + int(
#                                 pygame.Surface.get_height(zombie.surface)) >= self.y:
#                             zombie.health -= 0.2
#                             zombie.surface = pygame.transform.flip(
#                                 pygame.image.load('zombie sprite/Butcher_hit_right.png'), True, False)
#                             print(zombie.health)
#                             if zombie.health <= 0:
#                                 zombie.isAlive = False
#                             return
#
#
# class Zombie:
#     def __init__(self):
#         self.isAlive = True
#         self.health = 5
#         self.facing = RIGHT
#         self.x = random.choice([100, 1000])
#         self.y = randint(10, 750)
#         self.ani_speed_init = 10
#         self.ani_speed = self.ani_speed_init
#         self.ani = glob.glob("zombie sprite/walk/z-walk-left*.png")
#         self.ani_dead = glob.glob("zombie sprite/dead/z-dead-left*.png")
#         self.ani_dead.sort()
#         self.ani.sort()
#         self.ani_pos = 0;
#         self.ani_pos_dead = 0;
#         self.ani_max = len(self.ani) - 1
#         self.ani_max_dead = len(self.ani_dead) - 1
#         self.surface =  pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
#         self.width = self.surface.get_width()
#         self.height = self.surface.get_height()
#         self.rect = pygame.Rect(self.x, self.y, self.x + self.width, self.y + self.height)
#
#
#     def update(self, player, zombies):
#
#         if (self.isAlive):
#             if self.x < player.x:
#                 self.x += ZOMBIESPEED;
#                 self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
#             elif self.x > player.x:
#                 self.x -= ZOMBIESPEED
#                 self.surface = pygame.image.load(self.ani[self.ani_pos])
#             if self.y < player.y:
#                 self.y += ZOMBIESPEED
#             elif self.y > player.y:
#                 self.y -= ZOMBIESPEED
#             if self.x == player.x and self.y == player.y:
#                 player.isAlive = False
#             if self.ani_pos == self.ani_max:
#                 self.ani_pos = 0
#             else:
#                 self.ani_pos += 1
#
#
#         else:
#             if self.x < player.x:
#                 self.surface = pygame.transform.flip(pygame.image.load(self.ani_dead[self.ani_pos_dead]), True, False)
#             elif self.x > player.x:
#                 self.surface = pygame.image.load(self.ani_dead[self.ani_pos_dead])
#             if self.ani_pos_dead == self.ani_max_dead:
#                 pass
#             else:
#                 self.ani_pos_dead += 1
#
#         self.rect = pygame.Rect(self.x, self.y, self.x + self.width, self.y + self.height)
#
#
#
#
#
#     def draw(self):
#         DISPLAYSURF.blit(self.surface, (self.x, self.y))
#
#
# class Butcher:
#
#     def __init__(self):
#         self.isAlive = True
#         self.health = 100
#         self.speed = 1
#         self.facing = RIGHT
#         self.x = random.choice([-50, 0])
#         self.y = randint(10, 750)
#         self.surface = pygame.image.load('zombie sprite/butcher_right.gif')
#
#
#     def update(self, player):
#         if self.isAlive:
#             if self.x + int(pygame.Surface.get_width(self.surface)) < player.x:
#                 self.x += self.speed
#                 self.facing = RIGHT
#             elif self.x > player.x + int(pygame.Surface.get_width(player.surface)):
#                 self.x -= self.speed
#                 self.facing = LEFT
#             if self.y + int(pygame.Surface.get_height(self.surface) / 2) < player.y:
#                 self.y += self.speed
#             elif self.y + int(pygame.Surface.get_height(self.surface) / 2) > player.y:
#                 self.y -= self.speed
#             if self.facing == RIGHT:
#                 if self.x + int(pygame.Surface.get_width(self.surface)) == player.x and self.y + int(
#                                 pygame.Surface.get_height(self.surface) / 2) == player.y:
#                     player.isAlive = False
#             if self.facing == LEFT:
#                 if self.x == player.x + int(pygame.Surface.get_width(player.surface)) and self.y + int(
#                                 pygame.Surface.get_height(self.surface) / 2) == player.y:
#                     player.isAlive = False
#
#         if self.facing == RIGHT:
#             self.surface = pygame.image.load('zombie sprite/butcher_right.gif')
#         elif self.facing == LEFT:
#             self.surface = pygame.transform.flip(pygame.image.load('zombie sprite/butcher_right.gif'), True, False)
#
#     def draw(self):
#         DISPLAYSURF.blit(self.surface, (self.x, self.y))
#
import Hero
from Hero import *
import enumerations
from enumerations import *


def main():
    global BG, tree_rect, FPSCLOCK, DISPLAYSURF, BASICFONT, TREEIMAGE, R_TROOPER_IDLE, L_TROOPER_IDLE, R_ZOMBIE_WALK, L_ZOMBIE_WALK, zombies, L_TROOPER_WEAPON, R_TROOPER_WEAPON, moveLeft, moveRight, moveUp, moveDown, fire

    # moveLeft = False
    # moveRight = False
    # moveUp = False
    # moveDown = False
    # fire = False
    # zombie_number = 10
    # zombies_left = False
    # wave = 1

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('The Last Stand')


    player = Hero()
    # zombies = []
    # for i in range(zombie_number):
    #     zombie = Zombie()
    #     zombies.append(zombie)




    while True:

        DISPLAYSURF.fill(TERRAINCOLOR)
        DISPLAYSURF.blit(player.surface, (player.x, player.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    player.move_down = False
                    player.move_up = True
                elif event.key in (K_DOWN, K_s):
                    player.move_up = False
                    player.move_down = True
                elif event.key in (K_LEFT, K_a):
                    player.move_right = False
                    player.move_left = True
                elif event.key in (K_RIGHT, K_d):
                    player.move_left = False
                    player.move_right = True
                elif event.key == K_SPACE:
                    player.fire = True
            elif event.type == KEYUP:
                if event.key in (K_UP, K_w):
                    player.move_up = False
                elif event.key in (K_DOWN, K_s):
                    player.move_down = False
                elif event.key in (K_RIGHT, K_d):
                    player.move_right = False
                elif event.key in (K_LEFT, K_a):
                    player.move_left = False
                elif event.key == K_SPACE:
                    player.fire = False

        # zombiesLeft = False
        # for zombie in zombies:
        #     zombie.update(player, zombies)
        #     zombie.draw()
        #     if zombie.isAlive:
        #         zombiesLeft = True


        #if zombiesLeft == False:
        #	BG = pygame.image.load('terrain/19_open.jpg')
        # 	del zombies[:]
        #	if wave == 1:
        #		zombies.append(Butcher())
        #		wave+=1
        # 	zombie_number += 2
        # 	for i in range(zombie_number):
        # 		zombies.append(Zombie())


        player.update()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()