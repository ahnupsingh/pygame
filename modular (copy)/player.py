from index import *
# Player Class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('laser_missile.png')
        self.image = pygame.transform.scale(self.image,(50,70))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = (width - self.width)/2
        self.y = height - self.height
        self.speed = 2
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed

        if self.x < 0:
            self.x = 0
        if self.x > width - self.width:
            self.x = width - self.width

    # Destructor
    def __del__(self):
        del self
        print "Player Destructed"
