import sys, pygame
from pygame.locals import *
pygame.init()

size = width,height = 640,480
speed = [20,20]
black = 0,0,0
white = 255,255,255
blue = 0,0,255
radius = 20
position = [20,20]


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(size)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            radius = radius/2
            pygame.draw.circle(screen,blue,[20,20],radius)

    screen.fill(white)
    ballrect = pygame.draw.circle(screen,blue,speed,radius)
    print speed[0]
    if ballrect.left < 0:
        while(ballrect.right < width):
            speed[0] += 1
    elif ballrect.right > width:
        while(ballrect.left > 0):
            speed[0] -= 1

    if ballrect.top < 0:
        while(ballrect.bottom < height):
            speed[1] += 4
    elif ballrect.bottom > height:
        while(ballrect.top > 0):
            speed[1] += 4

    pygame.display.flip()
    fpsClock.tick(FPS)
