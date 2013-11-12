import sys, pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
width, height = 400, 600
windowSurfaceObj = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pygame Cheat Sheet')

redColor = pygame.Color(255, 0, 0)
blueColor = pygame.Color(0,0,255)
mousex, mousey = 0, 0
x,y = 1,1
speed = 1
xdir,ydir = 1,1
while True:
    windowSurfaceObj.fill(redColor)
    if speed < 1:
        speed = 1
    #yeah right!
    if x + speed*xdir < 0 :
        x = 0
        xdir *= -1
    elif x + speed*xdir > width - 50:
        x = width - 50
        xdir *= -1
    elif y <= mousey and y + 50 >= mousey and abs((x+speed*xdir - mousex)) == speed-1 + 5:
        x = mousex + 5
        xdir *= -1
    elif y <= mousey and y + 50 >= mousey and abs((x + 50 + speed*xdir - mousex)) == speed-1 + 5:
        x = mousex - 50 - 5
        xdir *= -1
    else:
        x += speed*xdir
    if y + speed*ydir < 0:
        y = 0
        ydir *= -1
    elif x <= mousex and x + 50 >= mousex and abs((y + speed*ydir - mousey)) == speed-1 + 5:
        y = mousey + 5
        ydir *= -1
    elif x <= mousex and x + 50 >= mousex and abs((y + 50+ speed*ydir - mousey)) == speed-1 + 5:
        y = mousey - 50 - 5
        ydir *= -1
    elif y+speed*ydir > height - 50:
        y = height - 50
        ydir *= -1
    else:
        y += speed*ydir
    #THIS IS A GITHUB TEST
    pygame.draw.rect(windowSurfaceObj, blueColor, (x, y, 50,50))
    pygame.draw.rect(windowSurfaceObj, blueColor, (mousex - 5, mousey - 5, 10, 10))
    for event in pygame.event.get():
        #print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_LEFT:
                mousex -= 10
            if event.key == K_UP:
                mousey -= 10
            if event.key == K_RIGHT:
                mousex += 10
            if event.key == K_DOWN:
                mousey += 10
            if event.key == K_a:
                speed += 1
            if event.key == K_s:
                speed -= 1
            if event.key == K_r:
                speed = 5
    pygame.display.update()
    fpsClock.tick()
