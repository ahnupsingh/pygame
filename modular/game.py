from index import *
from bubbles import *
from player import *

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
                ball_radius1 = ball_radius1/2
                Bubble1.speed[1] = 50/ball_radius1
                #ball_radius2 = ball_radius2/2
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
        screen.blit(textSurface,(width/2-textSurface.get_width()/2,height/2 -textSurface.get_height()/2))


    # if ball_radius2 > 2:
    #     Bubble2.update(ball_radius2)

    #print "Bubble position: " + str(Bubble1.position)
    if(Bubble1.is_collided_with(player1)==1):
        a = 1
        #print "Collision"

    player1.update(player_pos,player_dir)
    pygame.display.flip()
    pygame.display.update()
