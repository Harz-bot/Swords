import pygame as pg

pg.init()

win = pg.display.set_mode((1200,800))

pg.display.set_caption("NIDHOG")

walkRight = [pg.image.load("CharackterA_R_1.png"), pg.image.load("CharackterA_R_2.png"), pg.image.load("CharackterA_R_3.png"), pg.image.load("CharackterA_R_4.png"), pg.image.load("CharackterA_R_5.png"), pg.image.load("CharackterA_R_6.png"), pg.image.load("CharackterA_R_7.png"), pg.image.load("CharackterA_R_8.png"), pg.image.load("CharackterA_R_9.png")]
walkLeft = [pg.image.load("CharackterA_L_1.png"), pg.image.load("CharackterA_L_2.png"), pg.image.load("CharackterA_L_3.png"), pg.image.load("CharackterA_L_4.png"), pg.image.load("CharackterA_L_5.png"), pg.image.load("CharackterA_L_6.png"), pg.image.load("CharackterA_L_7.png"), pg.image.load("CharackterA_L_8.png"), pg.image.load("CharackterA_L_9.png")]
char = pg.image.load("CharakterA_char.png")
screenWidth = 1200

clock = pg.time.Clock()

x = 50
y = 700
width = 40
height = 60
vel = 10

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.fill((255,0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
        

    pg.display.update()


run = True
while run:
    clock.tick(27)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
        left = True
        rigt = False
    elif keys[pg.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
   
    
    if not (isJump):
       
        if keys[pg.K_UP]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.3 * neg
            jumpCount -= 1
        else:        
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()



 

    
pg.quit()
