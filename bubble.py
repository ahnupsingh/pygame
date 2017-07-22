import sys, pygame, glob, random
from pygame.locals import *
pygame.init()

# Game Screen Dimension
size = width,height = 640,480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BUBBLE TROUBLE')

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
        print self.position[0]
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


#   instance of Bubbles
radiuses = [10,10,30,40,50]
x_position = [65,130,195,280,345,410,475,540,580]
#   Bubble 1
ball_radius1 = random.choice(radiuses)
Bubble1 = Bubble(random.choice(x_position),ball_radius1,blue)


# #   Bubble 2
# ball_radius2 = random.choice(radius)
# print "Ball 2 radius - " + str(ball_radius2)
# Bubble2 = Bubble(random.choice(x_position),random.choice(radius),green)

#instance of player
player1 = player()
player_pos = 0
player_dir = 0
count = 0

done = False
a = 0
while not done:
    screen.fill(white)
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            done = True
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            line_x = player1.x + player1.rect.width/2
            pygame.draw.line(screen,blue,(line_x,0),(line_x,height))
            if (line_x in range(Bubble1.position[0]-Bubble1.radius,Bubble1.position[0]+Bubble1.radius)):
                #ball_radius1 = ball_radius1/2
                #ball_radius2 = ball_radius2/2
                a = 1
                count += 1
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            player_pos = 1
            player_dir = 1
        elif event.type == KEYUP and event.key == K_RIGHT:
            player_pos = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            player_pos = -1
            player_dir = 0
        elif event.type == KEYUP and event.key == K_LEFT:
            player_pos = 0

    if a==1:
        Bubble1.__del__()
        Bubble1.split()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    textSurface = myfont.render('Hits: ' + str(count), False, (0,0,0))
    screen.blit(textSurface,(500,10))
    # Control of Bubbles
    #print "Ball 1 radius - " + str(ball_radius1)
    #print "Ball 2 radius - " + str(ball_radius2)
    if ball_radius1 > 2:
        Bubble1.update(ball_radius1)
    else:
        textSurface = myfont.render('Congrats!!!',False,(0,1,0))
        screen.blit(textSurface,(width/2-11,height/2))


    # if ball_radius2 > 2:
    #     Bubble2.update(ball_radius2)

    #print "Bubble position: " + str(Bubble1.position)
    if(Bubble1.is_collided_with(player1)==1):
        a = 1
        #print "Collision"

    player1.update(player_pos,player_dir)
    pygame.display.flip()
    pygame.display.update()
