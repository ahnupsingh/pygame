from index import *
from bubbles import *
from player import *
from chain import *

#   instance of Bubbles
radiuses = [20,30,40,50]
x_position = [65,130,195,280,345,410,475,540,580]
#   Bubble 1
Bubble1 = Bubble(random.choice(x_position),random.choice(radiuses),random.choice(colors))

#instance of player
player1 = Player()
playerLife = 3

#instance of Chain
chain = Chain(player1)

spriteAll = pygame.sprite.Group()
spriteAll.add(player1)
spriteAll.add(Bubble1)
spriteAll.add(chain)

bubbleSprite = pygame.sprite.Group()
bubbleSprite.add(Bubble1)
hits = 0

done = False
while not done:
    screen.fill(Back_color)
    spriteAll.draw(screen)
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            done = True
            sys.exit()


    collided_bubble = pygame.sprite.spritecollide(chain,bubbleSprite,False)
    for bubble in collided_bubble:
        if chain in spriteAll:
            spriteAll.remove(bubble)
            bubble.diameter = bubble.diameter / 2
            bubble.position[0] = bubble.position[0] + 100 * bubble.speed[0]
            bubble.image = pygame.Surface([bubble.diameter,bubble.diameter])
            next_bubble = Bubble(bubble.position[0] - 100 * bubble.speed[0],bubble.diameter/2,bubble.color)
            next_bubble.speed[0] = -1 * bubble.speed[0]
            bubbleSprite.add(next_bubble)
            spriteAll.add(next_bubble)
            spriteAll.add(bubble)

    if pygame.sprite.spritecollide(player1,bubbleSprite,False):
        playerLife -= 1
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    textSurface = myfont.render('Player Life: ' + str(playerLife), False, (0,0,0))
    screen.blit(textSurface,(500,10))

    if len(bubbleSprite) <= 0:
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textSurface = myfont.render('Congrats!!!',False,(0,1,0))
        screen.blit(textSurface,(width/2-textSurface.get_width()/2,height/2 -textSurface.get_height()/2))

    for bubbles in bubbleSprite:
        bubbles.update()
    player1.update()
    chain.update(player1.x + player1.width/2, spriteAll)
    pygame.display.flip()
    pygame.display.update()
