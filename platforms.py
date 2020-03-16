from pygame.sprite import Sprite
from pygame.image import load


class Platform(Sprite):

	def __init__(self, x , y, src):
		Sprite.__init__(self)
		self.src =src
		self.image = load(self.src)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.collideV = True
		self.collideAbsolute = False
		self.actionB = False
		self.isItem = False
		self.isCoin = False
		self.atack = False
		self.targetSound = False
		self.isHeart = False
		self.isPoution = False
		self.isSave = False
		self.isWin = False

	def actionActive(self,src,x,y):
		Sprite.__init__(self)
		self.src = src
		self.image = load(self.src)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.actionB = False

	def CollectItem(self):
		self.rect = self.image.get_rect()
		print("item")

	def SpawnCoin(self, src, x,y):
		self.src = src
		self.image = load(self.src)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - 40
		self.isItem = True





	


	


