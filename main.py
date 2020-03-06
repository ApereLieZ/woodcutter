import pygame


import sys

sys.path.append('levels')

from levels import *

 
pygame.init()
pygame.display.set_caption('Дровосек 2')
from Player import Player
from platforms import Platform

#SOUND


SIZE = [640, 480]
#Window create
window = pygame.display.set_mode(SIZE)
#game win
screen = pygame.Surface(SIZE)


# create hero
hero = Player(55,55)
left = right = up =False


#Create level

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platforms= []


x=0
y=0
for row in level:
	for col in row:
		if col =='-':
			block = Platform(x, y,'sprites/platform/block.png')
			sprite_group.add(block)
			platforms.append(block)
		elif col =='*':
			pl = Platform(x, y,'sprites/platform/glass.jpg')
			sprite_group.add(pl)
			platforms.append(pl)
			pl.collideV = False
		elif col =='@':
			actblock = Platform(x, y,'sprites/platform/act.png')
			sprite_group.add(actblock)
			platforms.append(actblock)
			actblock.actionB = True
		elif col =='$':
			coin =Platform(x, y,'sprites/platform/coin.png')
			sprite_group.add(coin)
			platforms.append(coin)
			coin.isItem = True
			coin.collideV = False
		elif col =='#':
			spike =Platform(x, y,'sprites/platform/spike.png')
			sprite_group.add(spike)
			platforms.append(spike)
			spike.atack = True
		x += 40
	y += 40
	x =  0

#Camera
class Camera:
	def __init__(self, camera_func, width ,height ):
		self.camera_func = camera_func
		self.state = pygame.Rect(0,0,width,height)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
	l = -target_rect.x + SIZE[0]/2
	t = -target_rect.y + SIZE[1]/2
	w,h = camera.width, camera.height

	l = min(0,l)
	l = max(-(camera.width-SIZE[0]), l)
	t = max(-(camera.height-SIZE[1]), t)
	t = min(0,t)

	return pygame.Rect(l,t,w,h)
total_level_width = len(level[0])*40
total_level_height = len(level) *40

camera = Camera(camera_func, total_level_width, total_level_height)


done = True

timer = pygame.time.Clock()

while done:
	for e in pygame.event.get():
		if e.type ==pygame.QUIT:
			done = False

		#KEY Option
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_LEFT:
				left = True

			if e.key == pygame.K_RIGHT:
				right = True
			if e.key == pygame.K_UP:
				up = True

		if e.type == pygame.KEYUP:
			if e.key == pygame.K_LEFT:
				left = False
			if e.key == pygame.K_RIGHT:
				right = False
			if e.key == pygame.K_UP:
				up = False

	#FILL SCREEN
	screen.fill((0, 0 , 0))

	#ADD HERO
	hero.update(left, right,up, platforms)
	camera.update(hero)
	for e in sprite_group:
		screen.blit(e.image, camera.apply(e))
		
	#sprite_group.draw(screen)

	pygame.draw.rect(screen, hero.BarColor, (20, 20, hero.hp,20))
	if hero.hp < 0:
		done = False
	#Display
	window.blit(screen ,(0, 0))
	#UPDATE
	pygame.display.flip()

	timer.tick(60)