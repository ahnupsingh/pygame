from index import *
# Player Class
class player:
    def __init__(self):
        self.x = 200
        self.y = 350
        self.speed = 7
        self.ani_speed = self.speed
        self.ani = glob.glob("walk/rsz_image*.jpg")
        #print self.ani
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani)-1
        self.img = pygame.image.load(self.ani[0])
        self.rect = self.img.get_rect()
        self.update(0,0)

    def update(self,player_pos,player_dir):
        if player_pos !=  0:
            self.ani_speed -= 1
            self.x +=player_pos
            if self.ani_speed == 0:
                if player_dir == 1:
                    self.img = pygame.image.load(self.ani[self.ani_pos])
                elif player_dir == 0:
                    self.img = pygame.transform.flip(pygame.image.load(self.ani[self.ani_pos]),True,False)
                self.ani_speed = self.speed
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1
            screen.blit(self.img,(self.x,self.y))
        else:
            img = pygame.image.load(self.ani[2])
            if player_dir == 1:
                screen.blit(img,(self.x,self.y))
            elif player_dir == 0:
                screen.blit(pygame.transform.flip(img,True,False),(self.x,self.y))
    # Destructor
    def __del__(self):
        del self
        print "Player Destructed"
