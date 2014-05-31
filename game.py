import pygame, sys, time, random, glob
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
		self.facing = RIGHT
		self.x = PLAYERX
		self.y = PLAYERY
		self.surface = R_TROOPER_WEAPON
		self.ani_speed_init = 10
		self.ani_speed = self.ani_speed_init
		self.ani = glob.glob("soldier sprite/run/tmp-*.gif")
		self.ani.sort()
		self.ani_pos = 0;
		self.ani_max = len(self.ani) - 1
		self.update([])

	def update(self, zombies):
		if self.isAlive:
			if moveLeft:
				self.x -= SPEED
				self.surface = L_TROOPER_WEAPON
				self.facing = LEFT
				self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
			if moveRight:
				self.x += SPEED
				self.facing = RIGHT
				self.surface = pygame.image.load(self.ani[self.ani_pos])
			if moveUp:
				self.y -= SPEED
				if self.facing == LEFT:
					self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
				else:
					self.surface = pygame.image.load(self.ani[self.ani_pos])
			if moveDown:
				self.y += SPEED
				if self.facing == LEFT:
					self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
				else:
					self.surface = pygame.image.load(self.ani[self.ani_pos])
			if fire:
				self.fireWeapon(zombies)
			if self.ani_pos == self.ani_max:
				self.ani_pos = 0
			else:
				self.ani_pos += 1

		else:
			self.surface = pygame.image.load('soldier sprite/soldier_dead.gif')

		DISPLAYSURF.blit(self.surface, (self.x, self.y))


	def fireWeapon(self, zombies):
		for zombie in zombies:
			if self.facing == LEFT:
				self.surface = pygame.image.load('soldier sprite/shoot_left.png')
				if zombie.x < self.x:
					if zombie.y <= self.y + 64/2 and zombie.y >= self.y:
						zombie.isAlive = False
						zombie.surface = pygame.image.load('zombie sprite/zombie_dead.gif')
						return
			if self.facing == RIGHT:
				self.surface = pygame.transform.flip(pygame.image.load('soldier sprite/shoot_left.png'), True, False)
				if zombie.x > self.x:
					if zombie.y <= self.y + 64/2 and zombie.y >= self.y:
						zombie.isAlive = False
						zombie.surface = pygame.image.load('zombie sprite/zombie_dead.gif')
						return

class Zombie:
	def __init__(self):
		self.isAlive = True
		self.health = 100
		self.facing = RIGHT
		self.x = random.choice([100, 1000])
		self.y = randint(10, 750)
		self.ani_speed_init = 10
		self.ani_speed = self.ani_speed_init
		self.ani = glob.glob("zombie sprite/walk/z-walk-left*.png")
		self.ani_dead = glob.glob("zombie sprite/dead/z-dead-left*.png")
		self.ani_dead.sort()
		self.ani.sort()
		self.ani_pos = 0;
		self.ani_pos_dead = 0;
		self.ani_max = len(self.ani) - 1
		self.ani_max_dead = len(self.ani_dead) - 1

	def update(self, player):
		
		if(self.isAlive):
			if self.x < player.x:
				self.x += ZOMBIESPEED;
				self.surface = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]), True, False)
			elif self.x > player.x:
				self.x -= ZOMBIESPEED
				self.surface = pygame.image.load(self.ani[self.ani_pos])
			if self.y < player.y:
				self.y += ZOMBIESPEED
			elif self.y > player.y:
				self.y -= ZOMBIESPEED
			if self.x == player.x and self.y == player.y:
				player.isAlive = False
			if self.ani_pos == self.ani_max:
				self.ani_pos = 0
			else:
		
				self.ani_pos += 1
		else:
			if self.x < player.x:
				self.surface = pygame.transform.flip(pygame.image.load(self.ani_dead[self.ani_pos_dead]), True, False)
			elif self.x > player.x:
				self.surface = pygame.image.load(self.ani_dead[self.ani_pos_dead])
			if self.ani_pos_dead == self.ani_max_dead:
				pass
			else:
				self.ani_pos_dead += 1

		DISPLAYSURF.blit(self.surface, (self.x, self.y))

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, TREEIMAGE, R_TROOPER_IDLE, L_TROOPER_IDLE, R_ZOMBIE_WALK, L_ZOMBIE_WALK, zombies, L_TROOPER_WEAPON, R_TROOPER_WEAPON, moveLeft, moveRight, moveUp, moveDown, fire

	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False
	fire = False

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

	L_TROOPER_WEAPON = pygame.image.load('soldier sprite/stand_left.png')
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
				elif event.key in (K_RIGHT, K_d):
					moveLeft = False
					moveRight = True
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



		player.update(zombies)


		
		for zombie in zombies:
			zombie.update(player)

		pygame.display.update()
		FPSCLOCK.tick(FPS)


if __name__ == '__main__':
	main()