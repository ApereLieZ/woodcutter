import pygame


walkSound = pygame.mixer.Sound('sound/walk.ogg')
jumpSound = pygame.mixer.Sound('sound/jump1.ogg')
coinSound = pygame.mixer.Sound('sound/coin.ogg')

pygame.mixer.music.load('sound/theme.mp3')
pygame.mixer.music.play(-1)

walkSound.set_volume(0.5)
jumpSound.set_volume(0.05)
coinSound.set_volume(0.5)