from index import *

class Bubble(pygame.sprite.Sprite):
    def __init__(self, x_pos,radius,color):
        super(Bubble, self).__init__()
        self.radius = int(radius)
        self.speed = [1,12 - self.radius/10]
        self.position = [x_pos, 40 + self.radius]
        self.color = color
        self.image = pygame.Surface([2 * self.radius,2 * self.radius])
        self.image.fill(Back_color)
        pygame.draw.circle(self.image,self.color,[self.radius,self.radius],self.radius)
        self.rect = self.image.get_rect()

    def update(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        if self.position[0] < 0 + self.radius or self.position[0] > width- self.radius:
            self.speed[0] *= -1

        if self.position[1] < 0 + self.radius or self.position[1] > height-self.radius:
            self.speed[1] *= -1

        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

        if self.radius < 4:
            self.kill()


    def __del__(self):
        del self
        print "Bubble Destructed"
