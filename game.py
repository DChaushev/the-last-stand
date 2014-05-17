import pygame, sys, time, random
from pygame.locals import *
from random import randint

FPS = 30
WINWIDTH = 1024
WINHEIGHT = 768
PLAYERX = int(WINWIDTH/2)
PLAYERY = int(WINHEIGHT/2)
PISTOL = 'pistol'
MACHINEGUN = 'machine_gun'
TERRAINCOLOR = (10, 127, 2)
RIGHT = 'right'
LEFT = 'left'
SPEED = 2
ZOMBIESPEED = 1

class Hero:
	def __init__(self):
		self.isAlive = True
		self.level = 1
		self.gun = PISTOL
		self.facing = RIGHT
		self.x = PLAYERX
		self.y = PLAYERY


class Zombie:
	def __init__(self):
		self.isAlive = True
		self.health = 100
		self.facing = RIGHT
		self.x = random.choice([100, 1000])
		self.y = randint(10, 750)



def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, TREEIMAGE, R_TROOPER_IDLE, L_TROOPER_IDLE, R_ZOMBIE_WALK, L_ZOMBIE_WALK, zombies, L_TROOPER_WEAPON, R_TROOPER_WEAPON


	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	pygame.display.set_caption('The Last Stand')


	## ---Surfaces--------------------------------------------------------

	L_TROOPER_RUN_1 = pygame.image.load('soldier sprite/soldier_run2.gif')
	R_TROOPER_RUN_1 = pygame.transform.flip(L_TROOPER_RUN_1, True, False)

	L_TROOPER_RUN_2 = pygame.image.load('soldier sprite/soldier_run2_2.gif')
	R_TROOPER_RUN_2 = pygame.transform.flip(L_TROOPER_RUN_1, True, False)

	L_TROOPER_IDLE = pygame.image.load('soldier sprite/soldier_idle.gif')
	R_TROOPER_IDLE = pygame.transform.flip(L_TROOPER_IDLE, True, False)


	R_ZOMBIE_WALK = pygame.image.load('zombie sprite/zombie_walk_right.gif')
	L_ZOMBIE_WALK = pygame.transform.flip(R_ZOMBIE_WALK, True, False)

	L_TROOPER_WEAPON = pygame.image.load('soldier sprite/soldier_shoot.gif')
	R_TROOPER_WEAPON = pygame.transform.flip(L_TROOPER_WEAPON, True, False)


	##-------------------------------------------------------------------

	player = Hero()
	zombies = []
	for i in range(10):
		zombie = Zombie()
		zombie.surface = R_ZOMBIE_WALK
		zombies.append(zombie)

	for i in zombies:
		print("({0}, {1})".format(i.x, i.y))

	player.surface = R_TROOPER_WEAPON
	

	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False
	fire = False

	while True:

		DISPLAYSURF.fill(TERRAINCOLOR)

		if player.facing == RIGHT:
			player.surface = R_TROOPER_WEAPON
		elif player.facing == LEFT:
			player.surface = L_TROOPER_WEAPON

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
						player.surface = L_TROOPER_WEAPON
						player.facing = LEFT
				elif event.key in (K_RIGHT, K_d):
					moveLeft = False
					moveRight = True
					if player.facing == LEFT:
						player.surface = R_TROOPER_WEAPON
						player.facing = RIGHT
				elif event.key == K_SPACE:
					fire = True

			elif event.type == KEYUP:
				if event.key in (K_UP, K_w):
					moveUp = False
				elif event.key in (K_DOWN, K_s):
					moveDown = False
				elif event.key in (K_RIGHT, K_d):
					moveRight = False
				elif event.key in (K_LEFT, K_a):
					moveLeft = False
				elif event.key == K_SPACE:
					fire = False

		if player.isAlive:
			if moveLeft:
				player.x -= SPEED
			if moveRight:
				player.x += SPEED
			if moveUp:
				player.y -= SPEED
			if moveDown:
				player.y += SPEED
			if fire:
				fireWeapon(player, zombies)
		else:
			player.surface = pygame.image.load('soldier sprite/soldier_dead.gif')


		zombieMove(zombies, player)

		
		for zombie in zombies:
			DISPLAYSURF.blit(zombie.surface, (zombie.x, zombie.y))
		DISPLAYSURF.blit(player.surface, (player.x, player.y))


		pygame.display.update()
		FPSCLOCK.tick(FPS)

def zombieMove(zombies, player):
	for zombie in zombies:
		if(zombie.isAlive):
			if zombie.x < player.x:
				zombie.x += ZOMBIESPEED;
				zombie.surface = R_ZOMBIE_WALK
			elif zombie.x > player.x:
				zombie.x -= ZOMBIESPEED
				zombie.surface = L_ZOMBIE_WALK
			if zombie.y < player.y:
				zombie.y += ZOMBIESPEED
			elif zombie.y > player.y:
				zombie.y -= ZOMBIESPEED
			if zombie.x == player.x and zombie.y == player.y:
				player.isAlive = False

def fireWeapon(player, zombies):
	for zombie in zombies:
		if player.facing == LEFT:
			player.surface = pygame.image.load('soldier sprite/soldier_shoot_left.gif')
			if zombie.x < player.x:
				if zombie.y <= player.y + 64/2 and zombie.y >= player.y:
					zombie.isAlive = False
					zombie.surface = pygame.image.load('zombie sprite/zombie_dead.gif')
					return
		if player.facing == RIGHT:
			player.surface = pygame.transform.flip(pygame.image.load('soldier sprite/soldier_shoot_left.gif'), True, False)
			if zombie.x > player.x:
				if zombie.y <= player.y + 64/2 and zombie.y >= player.y:
					zombie.isAlive = False
					zombie.surface = pygame.image.load('zombie sprite/zombie_dead.gif')
					return



if __name__ == '__main__':
	main()