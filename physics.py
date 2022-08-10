import pygame as pg

run = True
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500 

CUBE_WIDTH = 5
CUBE_OFFSET = 20

X_L = 2 * CUBE_WIDTH + CUBE_OFFSET
X_R = SCREEN_WIDTH - (CUBE_WIDTH + CUBE_OFFSET)
Y_B = SCREEN_HEIGHT - (CUBE_WIDTH + CUBE_OFFSET)
Y_T = 2 * CUBE_WIDTH + CUBE_OFFSET

WIN = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def invert(list):
    fin = []
    for i in list:
        fin.append(i * -1)
    return fin

class particle:
    def __init__(self, x, y, width):
        self.x_right = x
        self.y_bottom = y

        self.g_force = [.1,0]
        self.final_force = [-0.3,.2]
        self.final_force = [0,0]

        self.width = width

        self.x_left = self.x_right - self.width
        self.y_top = self.y_bottom - self.width

    def vec_add(self):
        self.final_force[0] += self.g_force[0]
        self.final_force[1] += self.g_force[1]

    def walls(self):
        '''if self.y <= Y_T or self.y >= Y_B:
            self.final_force[1] *= -1
        if self.x <= X_L or self.x >= X_R:
            self.final_force[0] *= -1'''
        # <- for walls

        if self.y_bottom >= SCREEN_HEIGHT or self.y_top <= 0:
            self.final_force[1] *= -1

            if self.y_top + self.final_force[1] <= 0:
                self.y_bottom = 1 + self.width

            if self.y_bottom + self.final_force[1] >= SCREEN_HEIGHT:
                self.y_bottom = SCREEN_HEIGHT - 1
            
        if self.x_left <= 0 or self.x_right >= SCREEN_WIDTH:
            self.final_force[0] *= -1

            if self.x_left + self.final_force[0] <= 0:
                self.x_right = 1 + self.width

            if self.x_right + self.final_force[0] >= SCREEN_WIDTH:
                self.x_right = SCREEN_WIDTH - 1

    
    def move(self):
        self.x_right += self.final_force[0]
        self.y_bottom += self.final_force[1]

        self.x_left = self.x_right - self.width
        self.y_top = self.y_bottom - self.width
    
    def draw(self):
        
        pg.draw.rect(WIN, (255, 225, 225), pg.Rect(self.x_left, self.y_top, self.width, self.width))
        
    
par = particle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 5)

def draw_square():
    pg.draw.rect(WIN, WHITE, pg.Rect(CUBE_OFFSET, CUBE_OFFSET, (SCREEN_WIDTH - (2 * CUBE_OFFSET)), (SCREEN_HEIGHT - (2 * CUBE_OFFSET))))
    pg.draw.rect(WIN, BLACK, pg.Rect(CUBE_OFFSET + CUBE_WIDTH, CUBE_OFFSET + CUBE_WIDTH, (SCREEN_WIDTH - (2 * CUBE_OFFSET + 2 * CUBE_WIDTH)), (SCREEN_HEIGHT - (2 * CUBE_OFFSET + 2 * CUBE_WIDTH))))
    #pg.draw.rect(WIN, WHITE, pg.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,10,10))

def main():
    par.walls()
    par.vec_add()
    par.move()

def stuffs():
    clock = pg.time.Clock()
    run = True
    ticks = 0
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        if ticks == 10:
            WIN.fill(BLACK)
            #draw_square()
            main()
            par.draw()
            pg.display.update()
            ticks = 0

        else:
            main()

        clock.tick(300)
        ticks += 1
        #par.move()
    
    pg.quit()

if __name__ == "__main__":
    stuffs()