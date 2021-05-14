# snake game in python

import pygame, sys, random, math, datetime

dim_x = 240
dim_y = 240

w = 1

# check for initialising error
check_error = pygame.init()
if check_error[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_error[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized")

# Play Surface
playSurface = pygame.display.set_mode(((dim_x+10), (dim_y+10)))
pygame.display.set_caption('Snakey')
#time.sleep(5)

# Colors
red = pygame.Color(255,0,0)#gameOver
green = pygame.Color(0,255,0)#Snake
black = pygame.Color(0,0,0)#Score
gray = pygame.Color(128,128,128)#background
brown = pygame.Color(162,42,42)#food

# FPS Controller
fpsController = pygame.time.Clock()

# Important Variables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]] #,[70,50],[60,50],[50,50],[40,50],[30,50],[20,50]

foodPos = [random.randrange(1,dim_x/10)*10, random.randrange(1,dim_y/10)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0

#Game Over Function
def gameOver():
    if w and (score > 250) :
        e = datetime.datetime.now()
        file = open(r"C:\Users\admin\Documents\python\highscore.txt", "a")
        file.write("%s" % e + " Score: " + str(score) +'\n') 
        file.close   
    myFont = pygame.font.SysFont('monaco', dim_x/10)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (dim_x/2,15)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# score function
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice ==1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (dim_x/2, dim_y/2)    

    playSurface.blit(Ssurf, Srect)

#Main Logic Of Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # snake bodyh mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score+=10
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, dim_x/10) * 10, random.randrange(1, dim_y/10) * 10]
    foodSpawn = True

    playSurface.fill(gray)
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green,pygame.Rect(pos[0], pos[1],10,10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > dim_x :
        snakePos[0] = 0
    elif snakePos[0] < 0:
        snakePos[0] = dim_x
    if snakePos[1] > dim_y :
        snakePos[1] = 0
    elif snakePos[1] < 0:
        snakePos[1] = dim_y

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    showScore()
    pygame.display.flip()
    if score < 100:
        fpsController.tick(8)
    elif score >=100 :
        fpsController.tick(math.log(score//10) + 7)
    