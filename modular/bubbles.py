from index import *
class Bubble:
    def __init__(self,x_pos,radius,color):
        self.radius = int(radius)
        self.speed = [1,110/self.radius]
        self.position = [x_pos, 40 + self.radius]
        self.color = color
        self.surface = pygame.Surface([2 * self.radius,2 * self.radius], pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
        #self.surface.fill(red)

    def update(self,radius):
        pos_x = self.position[0]
        pos_y = self.position[1]
        ballrect = pygame.draw.circle(screen,self.color,[int(pos_x),int(pos_y)],radius)
        #ballrect = pygame.draw.circle(self.surface,self.color,(0,0),radius)
        self.surface.get_rect().move(self.position)
        screen.blit(self.surface,ballrect)

        #print str(self.position[0]) + " " + str(self.position[1])
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        if self.position[0] < 0 + radius or self.position[0] > width-radius:
            self.speed[0] *= -1

        if self.position[1] < 0 + radius or self.position[1] > height-radius:
            self.speed[1] *= -1

    def split(self):
        split_ball1 = Bubble(self.position[0],int(self.radius/2),self.color)
        split_ball2 = Bubble(self.position[0]+self.radius,self.radius/2,self.color)

        split_ball1.update(int(self.radius/2))
        split_ball2.update(int(self.radius/2))

    def is_collided_with(self, Player):
        #print str(self.surface.get_rect())
        collided = self.surface.get_rect().colliderect(Player.rect)
        return collided

    def __del__(self):
        del self
        print "Bubble Destructed"
