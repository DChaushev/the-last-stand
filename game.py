import pygame, sys, time, random, glob
from pygame.locals import *
from random import randint

FPS = 30
TERRAINCOLOR = (10, 127, 2)

import Hero
from Hero import *
import enumerations
from enumerations import *
import Zombie
from Zombie import *
from menu import *

def fire(player, zombies):
    if player.facing == RIGHT:
        zombies = [z for z in zombies if z.x > player.x]
        zombies.sort(key= lambda z: z.x)
        for z in zombies:
            if player.y + 21 >= z.y and player.y + 21 <= z.y + z.surface.get_height():
                z.health -= player.power
                if z.health <= 0:
                    z.is_alive = False
                    player.score += 5
                return

    elif player.facing == LEFT:
        zombies = [z for z in zombies if z.x < player.x]
        zombies.sort(key= lambda z: z.x, reverse = True)
        for z in zombies:
            if player.y + 21 >= z.y and player.y + 21 <= z.y + z.surface.get_height():
                z.health -= player.power
                if z.health <= 0:
                    z.is_alive = False
                    player.score += 5
                return


def gameOver():
    font = pygame.font.Font(None, 30)
    text = font.render("Game Over", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_x = DISPLAYSURF.get_width() / 2 - text_rect.width / 2
    text_y = DISPLAYSURF.get_height() / 2 - text_rect.height / 2
    DISPLAYSURF.blit(text, [text_x, text_y])


def gameplay():

    zombie_count = 10
    player = Hero()
    zombies = []
    for i in range(zombie_count):
        zombie = Zombie()
        zombies.append(zombie)

    scoreIncrementTimer = 0
    lastFrameTicks = pygame.time.get_ticks()

    while 1:

        DISPLAYSURF.fill(TERRAINCOLOR)
        DISPLAYSURF.blit(player.surface, (player.x, player.y))

        gamefont = pygame.font.Font(None, 30)
        scoretext = gamefont.render('Score: ' + str(player.score), 2, [0, 0, 0])
        boxsize = scoretext.get_rect()
        scoreXpos = 900

        DISPLAYSURF.blit(scoretext, (scoreXpos, 20))

        if player.is_alive:

            if not zombies:
                zombie_count += 5
                for i in range(zombie_count):
                    zombie = Zombie()
                    zombies.append(zombie)

            zombies = [z for z in zombies if z.animation_dead_position < z.animation_dead_max]
            for z in zombies:
                DISPLAYSURF.blit(z.surface, (z.x, z.y))
                box = pygame.Rect(z.x, z.y, (z.health*z.surface.get_width())/10, -5)
                pygame.draw.rect(DISPLAYSURF, (255, 0, 0), box, 0)

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
                    fire(player, zombies)
                elif event.key == K_ESCAPE:
                    return
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

        player.update()

        for z in zombies:
            dead = z.update(player.x, player.y)
            if dead:
                player.is_alive = False

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        thisFrameTicks = pygame.time.get_ticks()
        ticksSinceLastFrame = thisFrameTicks - lastFrameTicks
        lastFrameTicks = thisFrameTicks

        scoreIncrementTimer = scoreIncrementTimer + ticksSinceLastFrame
        if scoreIncrementTimer > 1000:
            player.score += 1
            scoreIncrementTimer = 0



def main():

    global FPSCLOCK, DISPLAYSURF, zombie_count

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('The Last Stand')


    menu = RotatingMenu(x=320, y=240, radius=220, arc=pi, defaultAngle=pi/2.0)
    menu.addItem(MenuItem("New Game"))
    menu.addItem(MenuItem("High Scores"))
    menu.addItem(MenuItem("Exit"))
    menu.selectItem(0)

    while True:
        show_menu(menu)



def show_menu(menu):

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                menu.selectItem(menu.selectedItemNumber + 1)
            if event.key == pygame.K_RIGHT:
                menu.selectItem(menu.selectedItemNumber - 1)
            if event.key == pygame.K_KP_ENTER:
                print(menu.selectedItemNumber)
                if menu.selectedItemNumber == 2:
                    pygame.quit()
                    sys.exit()
                elif menu.selectedItemNumber == 0:
                    gameplay()

    menu.update()

    #Draw stuff
    DISPLAYSURF.fill((0,0,0))
    menu.draw(DISPLAYSURF)
    pygame.display.flip()

if __name__ == '__main__':
    main()

