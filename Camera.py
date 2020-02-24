import pygame

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
