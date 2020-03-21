import pygame

import sys

sys.path.append('levels')

from levels import *

 
pygame.init()
pygame.display.set_caption('Дровосек 2')
from Player import Player
from platforms import Platform

#SOUND


SIZE = [700, 600]
#Window create
window = pygame.display.set_mode(SIZE)
#game win
screen = pygame.Surface(SIZE)
#SAVEFILE
SAVES = open("saves.txt", 'r' )
fileS = SAVES.readlines()
xS = int(fileS[0])
yS = int(fileS[1])
iS = int(fileS[4])
SAVES.close()

bg = ["sprites/bg/bg1.png","sprites/bg/bg2.png"]



# create hero
hero = Player(xS,yS)
left = right = up =False


#Create level

sprite_group = pygame.sprite.Group()
platforms= []


x=0
y=0
def CreateLevel(x,y,i):
	window.fill((0, 0 , 0))
	x = 0
	y = 0
	for row in levels[i]:
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
				coin.isCoin = True
				coin.collideV = False
			elif col =='#':
				spike =Platform(x, y,'sprites/platform/spike.png')
				sprite_group.add(spike)
				platforms.append(spike)
				spike.atack = True
			elif col == "H":
				heart = Platform(x, y,'sprites/platform/hurt.png')
				sprite_group.add(heart)
				platforms.append(heart)
				heart.isHeart = True
				heart.isItem = True
				heart.collideV = False
			elif col =='S':
				save =Platform(x, y,'sprites/platform/save.png')
				sprite_group.add(save)
				platforms.append(save)
				save.isSave = True
				save.collideV = False
				save.isItem = True
			elif col == "+":
				poution = Platform(x, y,'sprites/platform/poution.png')
				sprite_group.add(poution)
				platforms.append(poution)
				poution.isPoution = True
				poution.isItem = True
				poution.collideV = False
			elif col == "→":
				NextLevelBlock = Platform(x, y,'sprites/platform/wood.png')
				sprite_group.add(NextLevelBlock)
				platforms.append(NextLevelBlock)
				NextLevelBlock.isWin = True
				NextLevelBlock.collideV = False
				NextLevelBlock.isItem = True
			x += 40
		y += 40
		x =  0

CreateLevel(x,y,iS)
sprite_group.add(hero)

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
total_level_width = len(levels[iS][0])*40
total_level_height = len(levels[iS]) *40

camera = Camera(camera_func, total_level_width, total_level_height)
# Fonts
pygame.font.init()
infFont = pygame.font.Font(None,32)

background_image=pygame.image.load(bg[iS]).convert()

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
	screen.blit(background_image, [1-hero.rect.x*0.1,0])
	#ADD HERO
	hero.update(left, right,up, platforms)
	camera.update(hero)
	for e in sprite_group:
		screen.blit(e.image, camera.apply(e))
		
	#sprite_group.draw(screen)
	screen.blit(infFont.render(u"Life: %s" % hero.life,1,(200,200,200)), (SIZE[0]-90,20 ))
	screen.blit(infFont.render(u"Coin: %s" % hero.coin,1,(200,200,200)), (SIZE[0]-90,SIZE[1]-50 ))

	pygame.draw.rect(screen, hero.BarColor, (20, 20, hero.hp,20))
	if hero.hp <0 and hero.life <=0:
		done = False
	if hero.hp < 0:
		SAVES = open("saves.txt", 'r' )
		fileS = SAVES.readlines()
		xS = int(fileS[0])
		yS = int(fileS[1])
		iS = int(fileS[4])
		SAVES.close()
		hero.life -= 1
		hero.rect.x = xS
		hero.rect.y = yS
		hero.hp = 100
	if hero.nextLVL == True:
		SAVES = open("saves.txt", 'r' )
		fileS = SAVES.readlines()
		
		iS = int(fileS[4])
		SAVES.close()
		for e in sprite_group:
			e.kill()
		
		SAVES1 = open("saves.txt", 'w' )
		SAVES1.write(str(56)+ '\n' + str(56) + '\n' + str(hero.coin) + '\n' + str(hero.life) +'\n' +str(hero.iS))
		SAVES1.close()
		platforms= []
		hero.rect.x = 56
		hero.rect.y = 56
		background_image=pygame.image.load(bg[iS]).convert()
		CreateLevel(x,y,iS)
		sprite_group.add(hero)
		hero.nextLVL = False

		

	
	#Display
	window.blit(screen ,(0, 0))
	#UPDATE
	pygame.display.flip()

	timer.tick(60)