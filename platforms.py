from pygame.sprite import Sprite
from pygame.image import load
from sound import coinSound


class Platform(Sprite):

	def __init__(self, x , y, src):
		Sprite.__init__(self)
		self.src =src
		self.image = load(self.src)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.collideV = True
		self.actionB = False
		self.isItem = False
		self.atack = False
		self.targetSound = False

	def actionActive(self,src,x,y):
		Sprite.__init__(self)
		self.src = src
		self.image = load(self.src)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.actionB = False

	def CollectItem(self):
		coinSound.play()
		self.rect = self.image.get_rect()
		print("coin")

	def SpawnCoin(self, src, x,y):
		self.src = src
		self.image = load(self.src)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - 40
		self.isItem = True





	


	


