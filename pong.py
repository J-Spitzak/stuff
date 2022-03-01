import pygame as pg

pg.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600 

FONT = pg.font.Font('freesansbold.ttf', 32) #useless, I wanted tet to appear showing score, it didn't work but the code remains 

WIN = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # making the window

DIST = 20 #distance beetween wall and paddle

PADDLE_H = 40 #paddle width,height and speed
PADDLE_W = 5
PADDLE_SPEED = 5

CUBE_W = 10 #cube properties
CUBE_SPD = 5

TXT_DIST = 100 #more stuff for the text, again it is now useless
TXT_Y = 80


RX = SCREEN_WIDTH - DIST #x cordonite of the right panel

"""
--------------------------------------------------------------------------------------
If you came to this file and you are not Akshay first of all wow,
second of all you may be confused by the large amount of comments, 
I wrote this program for myself but recently I have learned a freind of mine (Akshay)
is intrested in learning pygame so I am uploading this to my git repo so he can see it 
with comments explaining certain functions, please enjoy
--------------------------------------------------------------------------------------
"""

def stuffs():
    clock = pg.time.Clock()
    run = True

    ly = SCREEN_HEIGHT // 2 - PADDLE_H // 2 #initializing the starting y values of the paddles
    ry = SCREEN_HEIGHT // 2 - PADDLE_H // 2

    x = SCREEN_WIDTH // 2 - CUBE_W #initializing the starting position of the cube
    y = SCREEN_HEIGHT // 2 - CUBE_W

    vectx = 0 #vectors controlling the x and y direction, remember, in pong it will always be travelling diagonally
    vecty = 0 #so in both cases 0 should actually be -1 but hey.

    l_score = 0 #useless
    r_score = 0


    while run:
        #checking for the game being quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        #getting key inputs:
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            ry = ry - PADDLE_SPEED #each moves ry or ly which controlls the y position of the paddles
        if keys[pg.K_DOWN]:
            ry = ry + PADDLE_SPEED
        if keys[pg.K_w]:
            ly = ly - PADDLE_SPEED
        if keys[pg.K_s]:
            ly = ly + PADDLE_SPEED
        #collisions:
        #cieling:
        if y - CUBE_SPD <= 0 and vecty == 1:
            vecty = 0 
        #floor:
        if y + CUBE_SPD >= SCREEN_HEIGHT and vecty == 0:
            vecty = 1
        
        #left
        if x <= DIST + PADDLE_W and x >= DIST and y >= ly and y <= ly + PADDLE_H:
            vectx = 1
        #right
        if x + CUBE_W >= RX and x + CUBE_W <= RX + PADDLE_W and y >= ry and y <= ry + PADDLE_H:
            vectx = 0

        #reseting if cube goes offscreen:
        #left:
        if x <= 0 and vectx == 0:
            r_score += 1
            x = SCREEN_WIDTH // 2 - CUBE_W
            y = SCREEN_HEIGHT // 2 - CUBE_W
            vectx = 1
        #right:
        if x + CUBE_W >= SCREEN_WIDTH and vectx == 1:
            l_score += 1
            x = SCREEN_WIDTH // 2 - CUBE_W
            y = SCREEN_HEIGHT // 2 - CUBE_W
            vectx = 0

        #movement based on vectors
        if vecty == 1:
            y = y - CUBE_SPD
        else:
            y = y + CUBE_SPD
        if vectx == 1:
            x = x + CUBE_SPD
        else:
            x = x - CUBE_SPD

        '''
        l_text = FONT.render(l_score, True, WHITE, BLACK)
        r_text = FONT.render(r_score, True, WHITE, BLACK)
        L_TEXT_RECT = l_text.get_rect()
        R_TEXT_RECT = r_text.get_rect()
        L_TEXT_RECT.center = (SCREEN_WIDTH // 2 - TXT_DIST, TXT_Y)
        R_TEXT_RECT.center = (SCREEN_WIDTH // 2 + TXT_DIST, TXT_Y)
        stuff for score'''
        # drawing stuff:
        WIN.fill(BLACK)
        # left text:
        #WIN.blit(l_text, L_TEXT_RECT)
        # right text:
        #WIN.blit(r_text, R_TEXT_RECT)
        # right
        pg.draw.rect(WIN, WHITE, (RX,ry, PADDLE_W, PADDLE_H))
        # left
        pg.draw.rect(WIN, WHITE, (DIST,ly, PADDLE_W, PADDLE_H))
        # cube
        pg.draw.rect(WIN, WHITE, (x,y, CUBE_W, CUBE_W))

        pg.display.update()
        clock.tick(60)
    pg.quit()

if __name__ =="__main__":
    stuffs()