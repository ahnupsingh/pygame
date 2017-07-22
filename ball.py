import sys, pygame
from pygame.locals import *
pygame.init()

size = width,height = 640,480
speed = [1,4]
black = 0,0,0
white = 255,255,255
blue = 0,0,255


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

ball = pygame.image.load("redBall.png")
print(type(ball))
ballrect = ball.get_rect()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            ballrect.width = ballrect.width/2
            ball = pygame.transform.scale(ball, (ballrect.width,ballrect.width))
            bound = ball.get_clip()
            bound.move(200,200)
            screen.blit(ball,bound)


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
        print speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        print ballrect.bottom
        print ballrect.top
        speed[1] = -speed[1]


    screen.fill(white)
    screen.blit(ball,ballrect)
    pygame.display.flip()
    fpsClock.tick(FPS)
