import pygame as pg
import sys
from pygame.locals import *

spielerA = 2


frames = 25

speeeeed = 20

sprungHoehe = 10

bildBreite = 1200
bildHoehe = 800

start_Hoehe = 700





player1_startX = 400
B_player1_startX = 600




pg.init()


win = pg.display.set_mode((bildBreite, bildHoehe))

pg.display.set_caption("Schlag den Dietron")

# das Stanni-Bild von vorne
char = []

# Es gibt folgende Animationen
laufRechts = []
laufLinks = []
ducking = []


# looad player ONE Anis
laufRechts.append([pg.image.load("CharackterA_R_1.png"), pg.image.load("CharackterA_R_2.png"), pg.image.load("CharackterA_R_3.png"), pg.image.load("CharackterA_R_4.png"), pg.image.load("CharackterA_R_5.png"), pg.image.load("CharackterA_R_6.png"), pg.image.load("CharackterA_R_7.png"), pg.image.load("CharackterA_R_8.png"), pg.image.load("CharackterA_R_9.png")])
laufLinks.append([pg.image.load("CharackterA_L_1.png"), pg.image.load("CharackterA_L_2.png"), pg.image.load("CharackterA_L_3.png"), pg.image.load("CharackterA_L_4.png"), pg.image.load("CharackterA_L_5.png"), pg.image.load("CharackterA_L_6.png"), pg.image.load("CharackterA_L_7.png"), pg.image.load("CharackterA_L_8.png"), pg.image.load("CharackterA_L_9.png")])
char.append(pg.image.load("CharakterA_char.png"))
ducking.append(pg.image.load("Charakter_A_ducking.png"))

# looad player TWO Anis
laufRechts.append([pg.image.load("CharackterB_R_1.png"), pg.image.load("CharackterB_R_2.png"), pg.image.load("CharackterB_R_3.png"), pg.image.load("CharackterB_R_4.png"), pg.image.load("CharackterB_R_5.png"), pg.image.load("CharackterB_R_6.png"), pg.image.load("CharackterB_R_7.png"), pg.image.load("CharackterB_R_8.png"), pg.image.load("CharackterB_R_9.png")])
laufLinks.append([pg.image.load("CharackterB_L_1.png"), pg.image.load("CharackterB_L_2.png"), pg.image.load("CharackterB_L_3.png"), pg.image.load("CharackterB_L_4.png"), pg.image.load("CharackterB_L_5.png"), pg.image.load("CharackterB_L_6.png"), pg.image.load("CharackterB_L_7.png"), pg.image.load("CharackterB_L_8.png"), pg.image.load("CharackterB_L_9.png")])
char.append(pg.image.load("CharakterB_char.png"))
ducking.append(pg.image.load("Charakter_B_ducking.png"))








player_breite = pg.image.load("CharakterB_char.png").get_rect().size[0]
player_hoehe = pg.image.load("CharakterB_char.png").get_rect().size[1]

player_mitte = player_breite/2

rand_links = 0
rand_rechts = bildBreite - player_breite




tframe = pg.time.Clock()





# Hintergrund laden und mit dem ersten Bild anfangen

bg = pg.image.load("BG_IMG.png")
background = True
bgframe = 1

# Zeitintervall: Hintergrund-Animation ( angeblich 500 ms ) USEREVENT??? kp xD

bgtick = USEREVENT + 1
pg.time.set_timer(bgtick, 500)

        
# nur das charakter-gemale
def updateBewegung():

    
    
    # So viele Spieler zeichnen die es gibt (SpielerA)
    for curPL in range(spielerA):

        if player[curPL].bewegung + 1 >= frames:
            player[curPL].bewegung = 0

        if player[curPL].links:
            win.blit(laufLinks[curPL][player[curPL].bewegung//3], (player[curPL].x,player[curPL].y))
            player[curPL].bewegung += 1
        elif player[curPL].rechts:
            win.blit(laufRechts[curPL][player[curPL].bewegung//3], (player[curPL].x,player[curPL].y))
            player[curPL].bewegung += 1
        elif player[curPL].ducking:
            win.blit(ducking[curPL], (player[curPL].x, player[curPL].y))
        else:
            win.blit(char[curPL], (player[curPL].x,player[curPL].y))

        if player[curPL].bewegung + 1 >= frames:
            player[curPL].bewegung = 0

        if player[curPL].links:
            win.blit(laufLinks[curPL][player[curPL].bewegung//3], (player[curPL].x,player[curPL].y))
            player[curPL].bewegung += 1
        elif player[curPL].rechts:
            win.blit(laufRechts[curPL][player[curPL].bewegung//3], (player[curPL].x,player[curPL].y))
            player[curPL].bewegung += 1
        elif player[curPL].ducking:
            win.blit(ducking[curPL], (player[curPL].x, player[curPL].y))
        else:
            win.blit(char[curPL], (player[curPL].x,player[curPL].y))


    tframe.tick(frames)
            


class playerO(object):
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.speed = speeeeed
        self.sprungMeter = sprungHoehe
        self.springt = False
        self.links = False
        self.rechts = False
        self.ducking = False
        self.bewegung = 0
        
        

# Festgelegte keybindings
        
def getPlayerBinds(curPL) :

    escape = False
    
    keys = pg.key.get_pressed()
    
    
    if curPL == 0 :
        # Nur wenn man noch nicht gesprungen ist, kann man nochmal nach oben drücken
        if not player[0].springt:
            player[0].springt = keys[pg.K_UP]
        player[0].ducking = keys[pg.K_DOWN]
        player[0].links = keys[pg.K_LEFT]
        player[0].rechts = keys[pg.K_RIGHT]
    
    elif curPL == 1 :
        if not player[1].springt:
            player[1].springt = keys[pg.K_w]
        player[1].ducking = keys[pg.K_s]
        player[1].links = keys[pg.K_a]
        player[1].rechts = keys[pg.K_d]
    
    if keys[pg.K_ESCAPE] :
        escape = True
    
    return escape
        
        
    

def getPlayerKeys(curPL):

    # Resette erst mal die gedrückten Tasten vom letzten durchlauf
    
    player[curPL].links = False
    player[curPL].rechts = False
    player[curPL].ducking = False

    #frag ma die tasten vom Spieler ab und überprüfe ob escape gedrückt wurde ( okay... escape funzt iwie nich <.< ... )
    escape = getPlayerBinds(curPL)
    
    
    if player[curPL].links:
        if (player[curPL].x-player[curPL].speed ) >= rand_links :
            player[curPL].x -= player[curPL].speed
        else :
            player[curPL].x = rand_links
    elif player[curPL].rechts :
        if player[curPL].x+player[curPL].speed <= rand_rechts :
            player[curPL].x += player[curPL].speed
        else :
            player[curPL].x = rand_rechts
            
    elif escape:
        run = False
    else :
        player[curPL].bewegung = 0

    

    
    
    # achso, es wurde nach oben gedrückt?!?!?!
    if player[curPL].springt:
    
        # Aus dem Rand springen VERBOTEN!!
        if player[curPL].rechts :
            if player[curPL].x >= rand_rechts:
                player[curPL].rechts = False
        
        elif player[curPL].links :
            if player[curPL].x <= rand_links:
                player[curPL].links = False
        
        
        
        # Sprung "Animation" - Hoenemeterberrechung
        
        if player[curPL].sprungMeter  >= -sprungHoehe:
            neg = 1
            if player[curPL].sprungMeter  < 0:
                neg = -1
            player[curPL].y -= (player[curPL].sprungMeter  ** 2)  * neg
            player[curPL].sprungMeter  -= 1
        else:
            # Nur wenn der Sprung feddich ist, kann man nochmal nach oben drücken, um zu jumpen
            player[curPL].springt = False
            player[curPL].sprungMeter  = sprungHoehe


    
#Erfasse Bewegung pro Frame

run = True
tick = pg.time.get_ticks()

# Initialisiere Spiele
player = []

# Startpunkte dem Charakter übergeben und initialisieren
player.append(playerO(player1_startX, start_Hoehe, player_breite, player_hoehe))
player.append(playerO(B_player1_startX, start_Hoehe, player_breite, player_hoehe))

scrollingbg = False
negscrollingbg = False

while run:

    
    # Hintergrund-Animation

 
    # Erst mal Hintergrund updaten
    #############################################was stimmtn hier nicht?
    #background X
    bgX = -1200
    

   
        

    if player[0].x > 1000 and player[1].x > 1000:
        scrollingbg = True
        player[0].x = 300
        player[1].x = 300
        if bgX == 1200:
            #scrollingbg = False
            bgX = 0
        
        
        
    if player[0].x <= 200 and player[1].x <= 200:
        negscrollingbg = True
        player[0].x = 900
        player[1].x = 900
        if bgX == -3600:
            #negscrollingbg = False
            bgX = -2400
        
    if scrollingbg is True:
        bgX += 1200    
        
    if negscrollingbg is True:
        bgX -= 1200
    


   
        
            

    win.blit(bg, (bgX,0))

     
    
    if pg.event.get(tick):
        bgframe += 1
        if bgframe > 3:
            bgframe = 1
        


        
       
    
    # Was wird denn alles gedrückt??!
    for curPL in range(spielerA):
        getPlayerKeys(curPL)
       
    
    # print("DX %s   ---   DY %s" % ( player[1].x, player[1].y) )
    
    
           
    #Quit den shit mit ix
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    #print("Player1",player[0].x, "player2", player[1].x)
    print(bgX)
    # dann ...
   
    updateBewegung()
    pg.display.update()
    
