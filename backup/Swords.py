import pygame as pg
import sys
from pygame.locals import *

frames = 25

speeeeed = 40

sprungHoehe = 10

bildBreite = 1200
bildHoehe = 800


player1_startX = 400
player1_startY = 700


pg.init()



win = pg.display.set_mode((bildBreite, bildHoehe))

pg.display.set_caption("Schlag den Dietron")


walkRight = [pg.image.load("CharackterA_R_1.png"), pg.image.load("CharackterA_R_2.png"), pg.image.load("CharackterA_R_3.png"), pg.image.load("CharackterA_R_4.png"), pg.image.load("CharackterA_R_5.png"), pg.image.load("CharackterA_R_6.png"), pg.image.load("CharackterA_R_7.png"), pg.image.load("CharackterA_R_8.png"), pg.image.load("CharackterA_R_9.png")]
walkLeft = [pg.image.load("CharackterA_L_1.png"), pg.image.load("CharackterA_L_2.png"), pg.image.load("CharackterA_L_3.png"), pg.image.load("CharackterA_L_4.png"), pg.image.load("CharackterA_L_5.png"), pg.image.load("CharackterA_L_6.png"), pg.image.load("CharackterA_L_7.png"), pg.image.load("CharackterA_L_8.png"), pg.image.load("CharackterA_L_9.png")]
char = pg.image.load("CharakterA_char.png")
ducking = pg.image.load("Charakter_A_ducking.png")
tframe = pg.time.Clock()


player_breite = char.get_rect().size[0]
player_hoehe = char.get_rect().size[1]


player_mitte = player_breite/2
print("PM %s" % player_mitte)
rand_links = 0
rand_rechts = bildBreite - player_breite

print("RL %s" % rand_links)
print("RR %s" % rand_rechts)


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
        self.speed = speeeeed
        self.isJump = False
        self.sprungMeter = sprungHoehe
        self.left = False
        self.right = False
        self.ducking = False
        self.bewegung = 0
        


# FrameUpdate
def updateBild():

    global bewegung

            
    win.blit(bg[bgframe-1], (0,0))

    if dieter.bewegung + 1 >= frames:
        dieter.bewegung = 0

    if dieter.left:
        win.blit(walkLeft[dieter.bewegung//3], (dieter.x,dieter.y))
        dieter.bewegung += 1
    elif dieter.right:
        win.blit(walkRight[dieter.bewegung//3], (dieter.x,dieter.y))
        dieter.bewegung += 1
    elif dieter.ducking:
        win.blit(ducking, (dieter.x, dieter.y))
    else:
        win.blit(char, (dieter.x,dieter.y))


    tframe.tick(frames)

    pg.display.update()
    

    
    
#Erfasse Bewegung pro Frame

run = True
tick = pg.time.get_ticks()

dieter = player(player1_startX, player1_startY, player_breite, player_hoehe)

while run:


    # Hintergrund-Animation

    if pg.event.get(bgtick):
        bgframe += 1
        if bgframe > 3:
            bgframe = 1
        

    dieter.left = False
    dieter.right = False
    dieter.ducking = False

    keys = pg.key.get_pressed()
    
        
        
    if keys[pg.K_UP]:
        dieter.isJump = True
        
    if keys[pg.K_LEFT]: #geändert
        if (dieter.x-dieter.speed ) >= rand_links :
            dieter.x -= dieter.speed
            dieter.left = True
        else :
            dieter.x = rand_links
    elif keys[pg.K_RIGHT] :
        if dieter.x+dieter.speed <= rand_rechts :
            dieter.x += dieter.speed
            dieter.right = True
        else :
            dieter.x = rand_rechts
    elif keys[pg.K_DOWN]:
        dieter.ducking = True
    
    elif keys[pg.K_ESCAPE]:
        run = False
    else :
        dieter.bewegung = 0

    
    
    
    if dieter.isJump:
    
        # Aus dem Rand springen VERBOTEN!!
        if dieter.right :
            if dieter.x >= rand_rechts:
                dieter.right = False
        
        elif dieter.left :
            if dieter.x <= rand_links:
                dieter.left = False
        
        
        
        # Sprung "Animation"
        
        if dieter.sprungMeter  >= -sprungHoehe:
            neg = 1
            if dieter.sprungMeter  < 0:
                neg = -1
            dieter.y -= (dieter.sprungMeter  ** 2)  * neg
            dieter.sprungMeter  -= 1
        else:        
            dieter.isJump = False
            dieter.sprungMeter  = sprungHoehe
            
    
    print("DX %s   ---   DY %s" % ( dieter.x, dieter.y) )
        
           
    #Quit den shit mit ix
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
 
    updateBild()
    
