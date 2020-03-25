# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from pygame.image import load
from platforms import Platform
from sound import *

import pyganim

SoundPack = ['sound/theme.mp3', 'sound/hell.mp3']

green= [0,255,0]
yellow=[255,255,0]
red = [255,0,0]

MOVE_SPEED = 3
G = 0.4
JUMP_POWER = 9

SAVES = open("saves.txt", 'r' )
fileS = SAVES.readlines()
xS = int(fileS[0])
yS = int(fileS[1])
iS = int(fileS[4])
coinS = int(fileS[2])
lifeS = int(fileS[3])

SAVES.close()

moveR = True
moveV = 0

ANIMATION_DELAY = 0.15

ANIMATION_STAY_RIGHT  = [
"sprites/hero/stand_right0.png",
"sprites/hero/stand_right1.png",
"sprites/hero/stand_right2.png",
"sprites/hero/stand_right3.png",]

ANIMATION_STAY_LEFT  = [
"sprites/hero/stand_left0.png",
"sprites/hero/stand_left1.png",
"sprites/hero/stand_left2.png",
"sprites/hero/stand_left3.png",]

ANIMATION_LEFT = [
"sprites/hero/walk_left0.png",
"sprites/hero/walk_left1.png",
"sprites/hero/walk_left2.png",
"sprites/hero/walk_left3.png",
"sprites/hero/walk_left4.png",
"sprites/hero/walk_left5.png",
]

ANIMATION_RIGHT = [
"sprites/hero/walk_right0.png",
"sprites/hero/walk_right1.png",
"sprites/hero/walk_right2.png",
"sprites/hero/walk_right3.png",
"sprites/hero/walk_right4.png",
"sprites/hero/walk_right5.png",
]


ANIMATION_JUMP_RIGHT = [
"sprites/hero/jump_right0.png",
"sprites/hero/jump_right1.png",
"sprites/hero/jump_right2.png",
"sprites/hero/jump_right3.png",
"sprites/hero/jump_right4.png",
"sprites/hero/jump_right5.png",
]

ANIMATION_JUMP_LEFT = [
"sprites/hero/jump_left0.png",
"sprites/hero/jump_left1.png",
"sprites/hero/jump_left2.png",
"sprites/hero/jump_left3.png",
"sprites/hero/jump_left4.png",
"sprites/hero/jump_left5.png",
]

ANIMATION_HURT_RIGHT = [
"sprites/hero/hurt_right0.png",
"sprites/hero/hurt_right1.png",
"sprites/hero/hurt_right2.png",
]

ANIMATION_HURT_LEFT = [
"sprites/hero/hurt_left0.png",
"sprites/hero/hurt_left1.png",
"sprites/hero/hurt_left2.png",
]


class Player(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = Surface((27, 32))
		self.xvel = 0
		self.yvel = 0
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.onGround = False
		self.image.set_colorkey((0,0,0))
		self.lookleft = True
		self.lookRight = False
		self.hp = 100
		self.BarColor = green
		self.hit = False
		self.life = lifeS
		self.coin = coinS
		self.nextLVL = False
		self.iS = iS
		
		def make_boltAnim(anim_list, delay):
			boltAnim = []
			for anim in anim_list:
				boltAnim.append((anim, delay))
			Anim = pyganim.PygAnimation(boltAnim)
			return Anim

		#Create Anim

		#Кирилл , я хз , но надо этот блок кода сделать покороче 

			#STAY
		self.boltAnimStayLeft = make_boltAnim(ANIMATION_STAY_LEFT, ANIMATION_DELAY)
		self.boltAnimStayLeft.play()

		self.boltAnimStayRight = make_boltAnim(ANIMATION_STAY_RIGHT, ANIMATION_DELAY)
		self.boltAnimStayRight.play()

			#Walk
		self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY)
		self.boltAnimLeft.play()

		self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY)
		self.boltAnimRight.play()

			#JUMP
		self.boltAnimJumpRight = make_boltAnim(ANIMATION_JUMP_RIGHT, ANIMATION_DELAY)
		self.boltAnimJumpRight.play()

		self.boltAnimJumpLeft = make_boltAnim(ANIMATION_JUMP_LEFT, ANIMATION_DELAY)
		self.boltAnimJumpLeft.play()

			#Hurt
		self.boltAnimHurtRight = make_boltAnim(ANIMATION_HURT_RIGHT, ANIMATION_DELAY)
		self.boltAnimHurtRight.play()

		self.boltAnimHurtLeft = make_boltAnim(ANIMATION_HURT_LEFT, ANIMATION_DELAY)
		self.boltAnimHurtLeft.play()


#Helth
	def helth_bar(self,player_helth):
		if player_helth > 75:
			self.BarColor = green
		elif player_helth > 50:
			self.BarColor = yellow
		elif player_helth < 50:
			self.BarColor = red

#HIT
	"""def hit(self):
			self.hp -=10
			self.yvel = -JUMP_POWER
			walkSound.stop()

			if self.lookleft:
				self.image.fill((0,0,0))
				self.boltAnimHurtLeft.blit(self.image, (0,0))
			else:
				self.image.fill((0,0,0))
				self.boltAnimHurtRight.blit(self.image, (-20,0))
	"""

	def update(self, left , right, up, platforms):
			
#hp
		self.helth_bar(self.hp)
#check look
		if left:
			self.lookleft = True
			self.lookRight = False
		elif right:
			self.lookleft = False
			self.lookRight = True
#JUMP
		if up and self.lookleft:
			self.image.fill((0,0,0))
			self.boltAnimJumpLeft.blit(self.image, (-15,0))
		elif up and self.lookRight:
			self.image.fill((0,0,0))
			self.boltAnimJumpRight.blit(self.image, (0,0))


		if left:
			self.xvel = -MOVE_SPEED
			if not up:
				self.image.fill((0,0,0))
				self.boltAnimLeft.blit(self.image, (0,0))
				walkSound.play()

				
		if right:
			self.xvel = MOVE_SPEED
			if not up:
				self.image.fill((0,0,0))
				self.boltAnimRight.blit(self.image, (0,0))
				walkSound.play()
			else:
				self.image.fill((0,0,0))
				self.boltAnimJumpRight.blit(self.image, (0,0))
		if up:
			walkSound.stop()
			jumpSound.play()
			
			if self.onGround:
				self.yvel = -JUMP_POWER
				
				
			
		if not(right or left):
			self.xvel = 0
			walkSound.stop()

			if not up and self.lookRight:
				self.image.fill((0,0,0))
				self.boltAnimStayRight.blit(self.image, (0,0))
			elif not up and self.lookleft:
				self.image.fill((0,0,0))
				self.boltAnimStayLeft.blit(self.image, (-20,0))


		if not(self.onGround):
			self.yvel += G

		self.onGround = False

		
		self.rect.x += self.xvel
		self.collide(self.xvel, 0, platforms)
		self.rect.y += self.yvel
		self.collide(0, self.yvel, platforms)

	def collide(self, xvel , yvel, platforms):

		for pl in platforms:


			if pl.isMoving:
				if pl.moveR:
					pl.rect.x +=1
					pl.moveV +=1
				elif not pl.moveR: 
					pl.rect.x -=1
					pl.moveV -=1
				if  pl.moveV >= 200:
					pl.moveR = False
				elif pl.moveV <= 0:
					pl.moveR = True


				

			#Коллизия платформ
			if collide_rect(self, pl) and not pl.collideAbsolute :

				if xvel > 0 and pl.collideV and not pl.isItem:
					self.rect.right = pl.rect.left

				if xvel < 0 and pl.collideV and not pl.isItem:
					self.rect.left = pl.rect.right
				if yvel > 0 and not pl.isItem:
					self.rect.bottom = pl.rect.top
					self.onGround = True
					self.yvel = 0
					'''
					if pl.isMoving and pl.moveR:
						self.rect.x -= 8
					elif pl.isMoving and not pl.moveR:
						self.rect.x -= 8
					'''

					if pl.atack:
						self.hp -=30
						self.yvel = -JUMP_POWER
						walkSound.stop()
						hurtSound.play()

						if self.lookleft:
							self.image.fill((0,0,0))
							self.boltAnimHurtLeft.blit(self.image, (0,0))
						else:
							self.image.fill((0,0,0))
							self.boltAnimHurtRight.blit(self.image, (-20,0))
				#Если убрать нижнее сравнение , то герой пубет прыгать сквозь препядствия , но приземляться на них
				if yvel < 0 and pl.collideV and not pl.isItem :
					self.rect.top = pl.rect.bottom
					self.yvel = 0
					#act block

#Крч, идея. Надо чтоб при исполнении условия , над этим блоком появлялась монетка
					if pl.actionB:
						xact = pl.rect.x
						yact = pl.rect.y
						pl.actionActive('sprites/platform/act1.png', xact,yact)
						walkSound.stop()
						actionBlockSound.play()
						#pl.SpawnCoin('sprites/platform/coin.png', xact, yact)
				#item
				if xvel > 0 and pl.collideV or xvel < 0 and pl.collideV or yvel > 0:
					

					if pl.isItem:
						walkSound.stop()
						if pl.isSave:
							SAVES1 = open("saves.txt", 'w' )
							SAVES1.write(str(pl.rect.x )+ '\n' + str(pl.rect.y) + '\n' + str(self.coin) + '\n' + str(self.life) +'\n' +str(self.iS))
							SAVES1.close()
							print("SEVED")
							pl.isSave = False
							pl.CollectItem()

						if pl.isWin:
							self.nextLVL =True
							self.iS = self.iS +1
							pygame.mixer.music.load(SoundPack[self.iS])
							pygame.mixer.music.play(-1)
							
							SAVES1 = open("saves.txt", 'w' )
							SAVES1.write(str(pl.rect.x )+ '\n' + str(pl.rect.y) + '\n' + str(self.coin) + '\n' + str(self.life) +'\n' +str(self.iS))
							SAVES1.close()
							
							pl.isWin = False
							pl.CollectItem()
							print("WIN")

						

						elif pl.isHeart:
							jumpSound.stop()
							walkSound.stop()
							heartSound.play()
							self.life +=1
							pl.CollectItem()

						elif pl.isCoin:
							jumpSound.stop()
							walkSound.stop()
							coinSound.play()
							self.coin +=1
							pl.CollectItem()
						elif pl.isPoution:
							self.hp =100
							jumpSound.stop()
							walkSound.stop()
							poutionSound.play()
							pl.CollectItem()
					








						


