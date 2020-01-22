import pygame as pg
import sys
from pygame.locals import *

pg.init()

win = pg.display.set_mode((1200,800))

pg.display.set_caption("Schlag den Dietron")

walkRight = [pg.image.load(os.path.join("pics", "CharakterA_R_1.png"), pg.image.load(os.path.join("pics", "CharakterA_R_2.png"), pg.image.load(os.path.join("pics", "CharakterA_R_3.png"), pg.image.load(os.path.join("pics", "CharakterA_R_4.png"), pg.image.load(os.path.join("pics", "CharakterA_R_5.png"), pg.image.load(os.path.join("pics", "CharakterA_R_6.png"), pg.image.load(os.path.join("pics", "CharakterA_R_7.png"), pg.image.load(os.path.join("pics", "CharakterA_R_8.png"), pg.image.load(os.path.join("pics", "CharakterA_R_9.png")]
walkLeft = [pg.image.load(os.path.join("pics", "CharakterA_L_1.png"), pg.image.load(os.path.join("pics", "CharakterA_L_2.png"), pg.image.load(os.path.join("pics", "CharakterA_L_3.png"), pg.image.load(os.path.join("pics", "CharakterA_L_4.png"), pg.image.load(os.path.join("pics", "CharakterA_L_5.png"), pg.image.load(os.path.join("pics", "CharakterA_L_6.png"), pg.image.load(os.path.join("pics", "CharakterA_L_7.png"), pg.image.load(os.path.join("pics", "CharakterA_L_8.png"), pg.image.load(os.path.join("pics", "CharakterA_L_9.png")]
char = pg.image.load(os.path.join("pics", "CharakterA_char.png")
ducking = pg.image.load(os.path.join("pics", "Charakter_A_ducking.png")
screenWidth = 1200
bg = pg.image.load("bg.png")

clock = pg.time.Clock()


#player
>>>>>>> deemachtmit
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
        

win.blit(bg, (0,0))


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0,0))


    if dieter.walkCount + 1 >= 25:
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

#mainloop
dieter = player(300, 700, 64, 64)
run = True
while run:
    
    clock.tick(25)

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
            dieter.right = False
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



 

    
pg.quit()
