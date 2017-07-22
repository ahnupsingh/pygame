import pygame, sys, glob
from pygame import *

h = 800
w = 800

screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

class player:
    def __init__(self):
        self.x = 200
        self.y = 0
        self.speed = 10
        self.ani_speed = self.speed
        self.ani = glob.glob("walk/image*.jpg")
        print self.ani
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani)-1
        self.img = pygame.image.load(self.ani[0])
        self.update(0)

    def update(self,player_pos):
        #pygame.display.flip()
        if player_pos !=  0:
            self.ani_speed -= 1
            self.x +=player_pos
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed = self.speed
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1
            screen.blit(self.img,(self.x,self.y))

player1 = player()
player_pos = 0


while 1:
    screen.fill((255,255,255))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            player_pos = 1
        elif event.type == KEYUP and event.key == K_RIGHT:
            player_pos = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            player_pos = -1
        elif event.type == KEYUP and event.key == K_LEFT:
            player_pos = 0
    player1.update(player_pos)
    pygame.display.update()
