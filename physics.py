import pygame as pg

run = True
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500 

CUBE_WIDTH = 5
CUBE_OFFSET = 20

X_L = CUBE_WIDTH + CUBE_OFFSET
X_R = SCREEN_WIDTH - (CUBE_WIDTH + CUBE_OFFSET)
Y_B = SCREEN_HEIGHT - (CUBE_WIDTH + CUBE_OFFSET)
Y_T = CUBE_WIDTH + CUBE_OFFSET

WIN = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

class particle:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.g_force = [0,-2]
        self.final_force = [0,-2]
        self.width = width
    
    def move(self):
        self.x += self.final_force[0]
        self.y -= self.final_force[1]
    
    def draw(self):
        pg.draw.rect(WIN, WHITE, pg.Rect(self.x - self.width, self.y - self.width, self.x + self.width, self.y + self.width))
        pg.draw.rect(WIN, WHITE, pg.Rect(SCREEN_WIDTH / 2 - self.width, SCREEN_HEIGHT / 2 - self.width, self.width, self.width))
        pg.draw.rect(WIN, WHITE, pg.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,10,10))
        #print("helo")
    
par = particle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 5)

def draw_square():
    pg.draw.rect(WIN, WHITE, pg.Rect(CUBE_OFFSET, CUBE_OFFSET, (SCREEN_WIDTH - (2 * CUBE_OFFSET)), (SCREEN_HEIGHT - (2 * CUBE_OFFSET))))
    pg.draw.rect(WIN, BLACK, pg.Rect(CUBE_OFFSET + CUBE_WIDTH, CUBE_OFFSET + CUBE_WIDTH, (SCREEN_WIDTH - (2 * CUBE_OFFSET + 2 * CUBE_WIDTH)), (SCREEN_HEIGHT - (2 * CUBE_OFFSET + 2 * CUBE_WIDTH))))
    #pg.draw.rect(WIN, WHITE, pg.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,10,10))

def main():
    WIN.fill(BLACK)
    draw_square()

def stuffs():
    clock = pg.time.Clock()
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        main()
        pg.display.update()
        clock.tick(60)
        #par.move()
        par.draw()
    
    pg.quit()

if __name__ =="__main__":
    stuffs()