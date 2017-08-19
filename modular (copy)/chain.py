import pygame
from index import *

blue = [0,0,255]
class Chain(pygame.sprite.Sprite):
    """docstring for Chain."""
    def __init__(self,player):
        super(Chain, self).__init__()
        self.image = pygame.Surface([2,player.y])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.y = 0

    def update(self,pos_x,spriteAll):
        self.rect.x = pos_x - self.image.get_width()/2
        print self.image.get_width()
        print self.rect.y
        # self.rect.y = self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            spriteAll.add(self)
        else:
            spriteAll.remove(self)
