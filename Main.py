import pygame
import random
import sys
import math
pygame.init()
'''
When the game starts, you need to move to the right or left after that it will
become random after 
'''
pygame.font.init()
points=0
# The images of the charcters
pla = pygame.image.load('Images/jogging.png')
bu = pygame.image.load('Images/panda-bear.png')
ep=pygame.image.load('Images/hunter.png')
rk=pygame.image.load('Images/right-arrow-button.png')
lk = pygame.image.load('Images/left-arrow-button.png')
#Colors
black = (0,0,0)
white = (255,255,255)
blue = (0,0,205)
red = (255,0,0)
green= (0,128,0)
yellow = (255,255,0)
# screen and players/points/enemy
width = 800
height = 600
player_pos=[360,530]
all_pos=[160,360,559]
Panda = [560,0]
bird = [380,0]
p_size = 60
p_length = 60
bi_length = 5
bi_size = 5
px=Panda[0]
py=Panda[1]
enemy_pos=[360,0]
en_size = 60
en_length = 60
player_size=60
player_length = 60
x = player_pos[0]
y = player_pos[1]
xx = enemy_pos[0]
yy= enemy_pos[1]
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
game_over = False
# detect Collsion
def collsion(player_pos,enemy_pos):
    x = player_pos[0]
    y = player_pos[1]
    xx = enemy_pos[0]
    yy= enemy_pos[1]
    if (xx >= x and xx<(x+player_size)) or (x>=xx and x<(xx+en_size)):
        if ((yy>=y and yy<(y+player_size)) or (y>=yy) and y<(yy+en_size)):
            return True
    return False
#Detect Collsion/Points
def pos(player_pos,Panda):
    x = player_pos[0]
    y = player_pos[1]
    px=Panda[0]
    py=Panda[1]
    points=0
    distance = math.sqrt((math.pow(px-x,2))+(math.pow(py-y,2)))
    if distance <10:
        return True
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x>160:
                x-=200
            elif event.key == pygame.K_RIGHT and x<560:
                x+=200
        player_pos = [x,y]
#The drawings on the Screen
    pygame.Surface.fill(screen,black)
    pygame.draw.polygon(screen,green,[(0,600),(0,0),(100,0),(100,600)])
    pygame.draw.polygon(screen,green,[(800,600),(800,0),(700,0),(700,600)])
    pygame.draw.line(screen,white,(700,0),(700,800))
    pygame.draw.line(screen,white,(100,0),(100,800))
    pygame.draw.line(screen,yellow,(500,0),(500,800))
    pygame.draw.line(screen,yellow,(300,0),(300,800))
    pygame.draw.rect(screen,green,(enemy_pos[0],enemy_pos[1],en_size,en_length))
    pygame.draw.rect(screen,blue,(Panda[0],Panda[1],p_size,p_length))
    pygame.draw.rect(screen,red,(x,y,player_size,player_size))
    myfont= pygame.font.SysFont("timesnewroman",25)
    textsurface = myfont.render("Points:"+str(points), False,red)
    left = myfont.render("Move Left",False,red)
    right = myfont.render('Move Right', False, blue)
    Task = myfont.render("Save The Pandas",False,yellow)
    screen.blit(Task,(0,300))
    screen.blit(rk,(0,60))
    screen.blit(right,(0,110))
    screen.blit(left,(0,230))
    screen.blit(lk,(0,180))
    screen.blit(pla,(player_pos[0],player_pos[1]))
    screen.blit(bu,(Panda[0],Panda[1]))
    screen.blit(ep,(enemy_pos[0],enemy_pos[1]))
    screen.blit(textsurface,(0,0))

#Movement of the Points
    if Panda[1]>=0 and Panda[1]<height:
        Panda[1]+=10
    else:
        Panda[0]=random.choice(all_pos)
        Panda[1]=0
#Movement of the Enemy
    if enemy_pos[1]>=0 and enemy_pos[1]<height:
        enemy_pos[1]+=30
    else:
        enemy_pos[0]= random.choice(all_pos)
        enemy_pos[1]=20
#Stage 2
    if points == 10:
        enemy_pos[1]+=25
#Game Over
    if collsion(player_pos,enemy_pos):
        game_over= True
#Points/Reset of the Panda
    if pos(player_pos,Panda):
        Panda[1]=0
        Panda[0]=random.choice(all_pos)
        points +=1

    clock.tick(10)
    pygame.display.update()

