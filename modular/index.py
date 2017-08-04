import sys, pygame, glob, random
from pygame.locals import *
pygame.init()

# Game Screen Dimension
size = width,height = 640,480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BUBBLE TROUBLE')

#pygame.mouse.set_visible(True)
# Color Definition
black = 0,0,0
white = 255,255,255
blue = 0,0,255
green = 0,255,0
red = 255,0,0

# Frame per second
FPS = 60
fpsClock = pygame.time.Clock()

# Background Music Play
# pygame.mixer.music.load('abc.mp3')
# pygame.mixer.music.play(-1, 0.0)
