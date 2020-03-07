import pygame


walkSound = pygame.mixer.Sound('sound/walk.ogg')
jumpSound = pygame.mixer.Sound('sound/jump1.ogg')
coinSound = pygame.mixer.Sound('sound/coin.ogg')
hurtSound = pygame.mixer.Sound('sound/hurt.ogg')
actionBlockSound = pygame.mixer.Sound('sound/actionBlockSound.ogg')
heartSound = pygame.mixer.Sound('sound/heart.ogg')
poutionSound = pygame.mixer.Sound('sound/poution.ogg')

pygame.mixer.music.load('sound/theme.mp3')
pygame.mixer.music.play(-1)

walkSound.set_volume(0.5)
jumpSound.set_volume(0.05)
coinSound.set_volume(0.5)
hurtSound.set_volume(0.5)
actionBlockSound.set_volume(0.5)
heartSound.set_volume(0.5)
poutionSound.set_volume(1)