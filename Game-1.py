#All images file path should be changed else it wont work
#Images are uploaded under Images folder under main
#Report if any bugs found
import pygame
import math
from pygame.locals import*
import sys
import os
import random
#1initialising game
pygame.init()
width,height=640,480
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Iron Man VS Thanos Avengers 4 endgame")
#2setting gameplay modes
keys =[False,False,False,False]
playerpos=[100,100]
#setting weapon system
acc=[0,0]
fires=[]
#setting enemy system
badtimer=100
badtimer1=0
enemies=[[640,100]]
healthvalue= 194
#3loading images
player= os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\IITB2.jpg")
player1=pygame.image.load(player)
enemy= os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\\thanos.jpg")
enemy1= pygame.image.load(enemy)
enemy2=enemy1
#showing health of defendant
health= os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\\images1.jpg")
health1=pygame.image.load(health)
#showing game over display
gover= os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\\RON1.jpg")
gover1=pygame.image.load(gover)
ywin=os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\\Ron2.jpg")
ywin1=pygame.image.load(ywin)
#loading weapons
fire1= os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\\adv.jpg")
fire= pygame.image.load(fire1)
#4background
grass= os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\download1.jpg")
grass1= pygame.image.load(grass)
building= os.path.join("C:\\Users\Shreesh Kulkarni\Desktop\jeeadv1.jpg")
building1= pygame.image.load(building)
#5using loops
run=1
excode=0
while run:
    badtimer-=1
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    #drawing on screen with required size
    for x in range(100):
        for y in range(200):
            screen.blit(grass1,(x*100,y*100))
    screen.blit(building1,(0,30))
    screen.blit(building1,(0,135))
    screen.blit(building1,(0,240))
    screen.blit(building1,(0,345))

    #for rotating character
    position=pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    #converting into radians
    playerrot = pygame.transform.rotate(player1, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)
    #drawing enemies
    if badtimer == 0:
        enemies.append([640, random.randint(50, 430)])
        badtimer = 100 - (badtimer1 *2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    # for loop:for monitoring the x position of the enemy if it is offscreen deletes the enemy
    for i in enemies:
        if i[0] < -64:
            enemies.pop(index)
        i[0] -= 7
        #attacking bases and reducing health
        badrect = pygame.Rect(enemy2.get_rect())
        badrect.top = i[1]
        badrect.left = i[0]
        if badrect.left < 64:
            healthvalue -= random.randint(5, 20)
            enemies.pop(index)
        #checking for firing the bullets and colliding with enemies and thus killing them
        index1=0
        for i in fires:
            brect=pygame.Rect(fire.get_rect())
            brect.left=i[1]
            brect.top=i[2]
            if badrect.colliderect(brect):
                acc[0]+=1
                enemies.pop(index)
                fires.pop(index1)
            index1+=1
        index += 1

    #draws all enemies on screen
    for i in enemies:
        screen.blit(enemy2, i)
    #drawing weapons
    for i in fires:
        index=0
        #speed of weapons
        velx=math.cos(i[0])*100
        vely=math.sin(i[0])*100
        i[1]+=velx
        i[2]+=vely
        #checking if weapon goes out of bounds if it goes delete the weapon
        if i[1]<-64 or i[1]>640 or i[2]<-64 or i[2]>480:
            fires.pop(index)
        index+=1
        for j in fires:
            fire2= pygame.transform.rotate(fire,360-j[0]*57.29)
            screen.blit(fire2,(j[1],j[2]))
    #showing timer clock etc
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((pygame.time.get_ticks())).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)
    #drawing health bar
    for i in range(healthvalue):
        screen.blit(health1,(i+8,8))

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
            #making player move
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key ==K_w:
                keys[0]=False
            elif event.key==K_a:
                keys[1]=False
            elif event.key==K_s:
                keys[2]=False
            elif event.key==K_d:
                keys[3]=False
        #appending weapons
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            fires.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

    #9 moving player
    if keys[0]:
        playerpos[1]-=10
    elif keys[2]:
        playerpos[1]+=10
    if keys[1]:
        playerpos[0]-=10
    elif keys[3]:
        playerpos[0]+=10
        #checking whether you win or lose
    if pygame.time.get_ticks()>=90000:
        run=0
        excode=1
    if healthvalue<=0:
        run=0
        excode=0
    if acc[0]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0
    #displaying whether you won or lost
    if excode==0:
        pygame.font.init()
        font=pygame.font.Font(None,24)
        text= font.render("Accuracy: "+str(accuracy)+"%",True,(255,0,0))
        textRect=text.get_rect()
        textRect.centerx=screen.get_rect().centerx
        textRect.centery=screen.get_rect().centery+24
        screen.blit(gover1,(0,0))
        screen.blit(text,textRect)
    else:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 24
        screen.blit(ywin1, (0, 0))
        screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        pygame.display.flip()















