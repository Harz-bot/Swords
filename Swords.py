import pygame as pg
import sys
from pygame.locals import *

frames = 25


pg.init()

win = pg.display.set_mode((1200,800))

pg.display.set_caption("Schlag den Dietron")

walkRight = [pg.image.load("CharackterA_R_1.png"), pg.image.load("CharackterA_R_2.png"), pg.image.load("CharackterA_R_3.png"), pg.image.load("CharackterA_R_4.png"), pg.image.load("CharackterA_R_5.png"), pg.image.load("CharackterA_R_6.png"), pg.image.load("CharackterA_R_7.png"), pg.image.load("CharackterA_R_8.png"), pg.image.load("CharackterA_R_9.png")]
walkLeft = [pg.image.load("CharackterA_L_1.png"), pg.image.load("CharackterA_L_2.png"), pg.image.load("CharackterA_L_3.png"), pg.image.load("CharackterA_L_4.png"), pg.image.load("CharackterA_L_5.png"), pg.image.load("CharackterA_L_6.png"), pg.image.load("CharackterA_L_7.png"), pg.image.load("CharackterA_L_8.png"), pg.image.load("CharackterA_L_9.png")]
char = pg.image.load("CharakterA_char.png")
ducking = pg.image.load("Charakter_A_ducking.png")
screenWidth = 1200
tframe = pg.time.Clock()


# Hintergrund laden
#######################################

# und mit dem ersten Bild anfangen

bg = [pg.image.load("bg_1.png"), pg.image.load("bg_2.png"), pg.image.load("bg_3.png")]
background = True
bgframe = 1

# Zeitintervall: Hintergrund-Animation
bgtick = USEREVENT + 1
pg.time.set_timer(bgtick, 500)




class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self. vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.ducking = False
        self.walkCount = 0
        


# FrameUpdate
def redrawGameWindow():
    global walkCount

    
    win.blit(bg[bgframe-1], (0,0))

    if dieter.walkCount + 1 >= frames:
        dieter.walkCount = 0

    if dieter.left:
        win.blit(walkLeft[dieter.walkCount//3], (dieter.x,dieter.y))
        dieter.walkCount += 1
    elif dieter.right:
        win.blit(walkRight[dieter.walkCount//3], (dieter.x,dieter.y))
        dieter.walkCount += 1
    elif dieter.ducking:
        win.blit(ducking, (dieter.x, dieter.y))
    else:
        win.blit(char, (dieter.x,dieter.y))



    pg.display.update()

    
    
#Erfasse Bewegung pro Frame

dieter = player(300, 700, 64, 64)
run = True
tick = pg.time.get_ticks()
while run:
    text = (
    "bgframe: %s tframeGetTime %s  tframeRawTime %s tframeFPS %s gettick %s"
    % (bgframe, tframe.get_time(), tframe.get_rawtime(), tframe.get_fps(), pg.time.get_ticks())
    )
    # print(text)
    
    
    
    
    # Hintergrund-Animation
    if pg.event.get(bgtick):
        bgframe += 1
        if bgframe > 3:
            bgframe = 1
        
        
        


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and dieter.x > dieter.vel:
        dieter.x -= dieter.vel
        dieter.left = True
        dieter.rigt = False
        dieter.ducking = False
    elif keys[pg.K_RIGHT] and dieter.x < screenWidth - dieter.width - dieter.vel:
        dieter.x += dieter.vel
        dieter.right = True
        dieter.left = False
        dieter.ducking = False
    elif keys[pg.K_DOWN]:
        dieter.right = False
        dieter.left = False
        dieter.ducking = True
    elif keys[pg.K_ESCAPE]:
        run = False
    else:
        dieter.right = False
        dieter.left = False
        
        dieter.walkCount = 0
   
    
    if not (dieter.isJump):
        if keys[pg.K_UP]:
            dieter.isJump = True
            if keys[pg.K_RIGHT] :
                dieter.right = True
                if dieter.x == 1130:
                    dieter.right = False
            else :
                dieter.right = False
            if keys[pg.K_LEFT]:
                dieter.left = True
                if dieter.x == 10:
                    dieter.left = False
            else :
                dieter.left = False
            dieter.ducking = False
            dieter.walkCount = 0
        
    else:
        if dieter.jumpCount >= -10:
            neg = 1
            if dieter.jumpCount < 0:
                neg = -1
            dieter.y -= (dieter.jumpCount ** 2) * 0.3 * neg
            dieter.jumpCount -= 1
        else:        
            dieter.isJump = False
            dieter.jumpCount = 10
            
    redrawGameWindow()
    
    tframe.tick(frames)
    tick = pg.time.get_ticks()

    print("X: %s  Y: %s" % (dieter.x, dieter.y))

 

    
pg.quit()
