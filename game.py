import pygame, sys, time
from pygame.locals import *

FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
PLAYERX = int(WINWIDTH/2)
PLAYERY = int(WINHEIGHT/2)
PISTOL = 'pistol'
MACHINEGUN = 'machine_gun'
TERRAINCOLOR = (10, 127, 2)
RIGHT = 'right'
LEFT = 'left'
SPEED = 2

class Hero:
	def __init__(self):
		self.isAlive = True
		self.level = 1
		self.gun = PISTOL
		self.facing = RIGHT
		self.x = PLAYERX
		self.y = PLAYERY


def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, TREEIMAGE, R_TROOPER_IDLE, L_TROOPER_IDLE
	player = Hero()

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	pygame.display.set_caption('The Last Stand')

	L_TROOPER_RUN_1 = pygame.image.load('soldier sprite/soldier_run2.gif')
	R_TROOPER_RUN_1 = pygame.transform.flip(L_TROOPER_RUN_1, True, False)

	L_TROOPER_RUN_2 = pygame.image.load('soldier sprite/soldier_run2_2.gif')
	R_TROOPER_RUN_2 = pygame.transform.flip(L_TROOPER_RUN_1, True, False)

	L_TROOPER_IDLE = pygame.image.load('soldier sprite/soldier_idle.gif')
	R_TROOPER_IDLE = pygame.transform.flip(L_TROOPER_IDLE, True, False)

	player.surface = L_TROOPER_IDLE

	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False

	while True:

		DISPLAYSURF.fill(TERRAINCOLOR)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key in (K_UP, K_w):
					moveDown = False
					moveUp = True
				elif event.key in (K_DOWN, K_s):
					moveUp = False
					moveDown = True
				elif event.key in (K_LEFT, K_a):
					moveRight = False
					moveLeft = True
					if player.facing == RIGHT:
						player.surface = R_TROOPER_IDLE
						player.facing = LEFT
				elif event.key in (K_RIGHT, K_d):
					moveLeft = False
					moveRight = True
					if player.facing == LEFT:
						player.surface = L_TROOPER_IDLE
						player.facing = RIGHT

			elif event.type == KEYUP:
				if event.key in (K_UP, K_w):
					moveUp = False
				elif event.key in (K_DOWN, K_s):
					moveDown = False
				elif event.key in (K_RIGHT, K_d):
					moveRight = False
				elif event.key in (K_LEFT, K_a):
					moveLeft = False

		if moveLeft:
			player.x -= SPEED
		if moveRight:
			player.x += SPEED
		if moveUp:
			player.y -= SPEED
		if moveDown:
			player.y += SPEED

		DISPLAYSURF.blit(player.surface, (player.x, player.y))


		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()