from cgi import maxlen
import pygame, sys, time, random, glob
from pygame.locals import *
from random import randint
import usrinput
import Hero
from Hero import *
import enumerations
from enumerations import *
import Zombie
from Zombie import *
from menu import *


FPS = 30
TERRAINCOLOR = (10, 127, 2)


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


def gameOver(player):
    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 30)
    text = font.render("Game Over", True, (0, 0, 0))
    text1 = font1.render("score: " + str(player.score), True, (0, 0, 0))
    text2 = font1.render("press space to continue", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_x = DISPLAYSURF.get_width() / 2 - text_rect.width / 2
    text_y = DISPLAYSURF.get_height() / 2 - text_rect.height / 2

    while 1:
        DISPLAYSURF.blit(text, [text_x, text_y])
        DISPLAYSURF.blit(text1, [text_x, text_y + 50])
        DISPLAYSURF.blit(text2, [text_x, text_y + 100])

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    write_score(player.score)
                    main()

        pygame.display.update()


def start_game():

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

        DISPLAYSURF.blit(scoretext, (900, 20))

        if player.animation_position_dead == player.animation_dead_max:
            gameOver(player)

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

            thisFrameTicks = pygame.time.get_ticks()
            ticksSinceLastFrame = thisFrameTicks - lastFrameTicks
            lastFrameTicks = thisFrameTicks

            scoreIncrementTimer = scoreIncrementTimer + ticksSinceLastFrame
            if scoreIncrementTimer > 1000:
                player.score += 1
                scoreIncrementTimer = 0

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
            #, player.surface.get_width(), player.surface.get_height()
            if dead:
                player.is_alive = False

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def get_scores():
    f = open('high-scores')
    lines = f.readlines()
    f.close()
    print(lines)
    return lines


def write_score(new_score):
    input_score = get_scores()
    if '\n' in input_score:
        input_score.remove('\n')
    score = []
    players = []
    for s in input_score:
        ss = s.rstrip('\n')
        score.append(ss)

    for s in score:
        splitted = s.split(' ')
        d = {'name': splitted[0], 'score': splitted[1]}
        players.append(d)
    players.sort(key=lambda k:k['score'], reverse=True)
    print(players)

    for i, p in enumerate(players):
        if new_score > int(p['score']):
            name = get_name()
            d = {'name': name, 'score': new_score}
            players.insert(i, d)
            break

    with open('high-scores', 'w') as f:
        i = 0
        for p in players:
            if i < 5:
                f.write(p['name'] + " " + str(p['score']) + "\n")
                i+=1
            if i == 5:
                break


def get_name():

    screen = pygame.display.set_mode((1024, 768))
    screen.fill((255,255,255))
    txtbox = usrinput.Input(maxlength = 10, color = (255, 0, 0), prompt='Enter Name: ')
    clock = pygame.time.Clock()

    while 1:
        clock.tick(FPS)

        events = pygame.event.get()
        # process other events
        for event in events:
            # close it x button si pressed
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                elif event.key == K_KP_ENTER:
                    return txtbox.value

        screen.fill((255,255,255))

        txtbox.update(events)
        txtbox.draw(screen)
        pygame.display.flip()

def show_scores():

    input_score = get_scores()
    if '\n' in input_score:
        input_score.remove('\n')
    score = []
    players = []
    for s in input_score:
        ss = s.rstrip('\n')
        score.append(ss)
    print(score)

    for s in score:
        splitted = s.split(' ')
        d = {'name': splitted[0], 'score': splitted[1]}
        players.append(d)
    players.sort(key=lambda k:int(k['score']), reverse=True)

    WHITE=(255,255,255)
    myfont = pygame.font.SysFont("monospace", 46)
    scorefont = pygame.font.Font(None, 20)


    while 1:

        DISPLAYSURF.fill((0, 0, 0))
        label = myfont.render("High Scores", 1, WHITE)
        DISPLAYSURF.blit(label, (350, 100))
        scorebox = pygame.draw.rect(DISPLAYSURF, WHITE, (250, 200, 500, 300))

        x = 270
        y = 220

        for i,p  in enumerate(players):
            text = str(i+1) + ". " + p['name'] + ": " + p['score']
            score = myfont.render(text, 1, (0,0,0))
            DISPLAYSURF.blit(score, (x, y))
            y += 50

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        pygame.display.update()


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
                if menu.selectedItemNumber == 2:
                    pygame.quit()
                    sys.exit()
                if menu.selectedItemNumber == 1:
                    show_scores()
                elif menu.selectedItemNumber == 0:
                    start_game()

    menu.update()

    #Draw stuff
    DISPLAYSURF.fill((0,0,0))
    menu.draw(DISPLAYSURF)
    pygame.display.flip()

def main():

    global FPSCLOCK, DISPLAYSURF

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


if __name__ == '__main__':
    main()

