import pygame as pg

pg.init()

win = pg.display.set_mode((1200,800))

pg.display.set_caption("NIDHOG")

screenWidth = 1200

x = 50
y = 700
width = 40
height = 60
vel = 10

isJump = False
jumpCount = 10
ducking = False


def redrawGameWindow():
    
    win.fill((0,0,0))
    Charakter = pg.draw.rect(win, (255 ,0 ,0), (x, y, width, height))
    pg.display.update()


run = True
while run:
    pg.time.delay(25)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
    if keys[pg.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if keys[pg.K_DOWN]:
        ducking = True
    if ducking is True:
        height = 30
        y+30
        
            
    
            
        
    
    if not (isJump):
       
        if keys[pg.K_UP]:
            isJump = True
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
