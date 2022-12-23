import pygame as pg



def invert(list):
    fin = []
    for i in list:
        fin.append(i * -1)
    return fin

class cube:
    def __init__(self, x, y, width):
        self.x_right = x
        self.y_bottom = y

        self.g_force = [.1,0]
        self.final_force = [-0.3,.2]
        self.final_force = [0,0]

        self.width = width

        self.x_left = self.x_right - self.width
        self.y_top = self.y_bottom - self.width

        self.dead = False
        self.deadzone = 1

    def vec_add(self):
        if not self.dead:
            self.final_force[0] += self.g_force[0]
            self.final_force[1] += self.g_force[1]
        
    def checkDeadzone(self):
        if self.final_force[0] - self.g_force[1] <= self.deadzone and self.final_force[1] - self.g_force[1] <= self.deadzone:
            self.dead = True

    def walls(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        '''if self.y <= self.Y_T or self.y >= self.Y_B:
            self.final_force[1] *= -1
        if self.x <= self.X_L or self.x >= self.X_R:
            self.final_force[0] *= -1'''
        # ^ for walls

        if self.y_bottom >= SCREEN_HEIGHT or self.y_top <= 0:
            self.final_force[1] *= -1

            if self.y_top + self.final_force[1] <= 0:
                self.y_bottom = 1 + self.width
                self.checkDeadzone()

            if self.y_bottom + self.final_force[1] >= SCREEN_HEIGHT:
                self.y_bottom = SCREEN_HEIGHT - 1
                self.checkDeadzone()
            
        if self.x_left <= 0 or self.x_right >= SCREEN_WIDTH:
            self.final_force[0] *= -1

            if self.x_left + self.final_force[0] <= 0:
                self.x_right = 1 + self.width
                self.checkDeadzone()

            if self.x_right + self.final_force[0] >= SCREEN_WIDTH:
                self.x_right = SCREEN_WIDTH - 1
                self.checkDeadzone()

    
    def move(self):
        if not self.dead:

            self.x_right += self.final_force[0]
            self.y_bottom += self.final_force[1]

            self.x_left = self.x_right - self.width
            self.y_top = self.y_bottom - self.width
    
    def draw(self, WN):
        
        pg.draw.rect(WN, (255, 225, 225), pg.Rect(self.x_left, self.y_top, self.width, self.width))
        
    
class window():

    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 500 

        self.CUBE_WIDTH = 5
        self.CUBE_OFFSET = 20

        self.X_L = 2 * self.CUBE_WIDTH + self.CUBE_OFFSET
        self.X_R = self.SCREEN_WIDTH - (self.CUBE_WIDTH + self.CUBE_OFFSET)
        self.Y_B = self.SCREEN_HEIGHT - (self.CUBE_WIDTH + self.CUBE_OFFSET)
        self.Y_T = 2 * self.CUBE_WIDTH + self.CUBE_OFFSET

        self.WIN = pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.cube = cube(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2, 5)

        self.breaks = True

        self.clock = pg.time.Clock()
        self.ticks = 0

    def draw_square(self):
        pg.draw.rect(self.WIN, self.WHITE, pg.Rect(self.CUBE_OFFSET, self.CUBE_OFFSET, (self.SCREEN_WIDTH - (2 * self.CUBE_OFFSET)), (self.SCREEN_HEIGHT - (2 * self.CUBE_OFFSET))))
        pg.draw.rect(self.WIN, self.BLACK, pg.Rect(self.CUBE_OFFSET + self.CUBE_WIDTH, self.CUBE_OFFSET + self.CUBE_WIDTH, (self.SCREEN_WIDTH - (2 * self.CUBE_OFFSET + 2 * self.CUBE_WIDTH)), (self.SCREEN_HEIGHT - (2 * self.CUBE_OFFSET + 2 * self.CUBE_WIDTH))))
        #pg.draw.rect(self.WIN, self.WHITE, pg.Rect(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2,10,10))

    def main(self):
        self.cube.walls(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.cube.vec_add()
        self.cube.move()

    def stuffs(self):
        clock = pg.time.Clock()
        self.breaks = True
        ticks = 0
        while self.breaks:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.breaks = False

            if ticks == 10:
                self.WIN.fill(self.BLACK)
                #draw_square()
                self.main()
                self.cube.draw(self.WIN)
                pg.display.update()
                ticks = 0

            else:
                self.main()

            clock.tick(300)
            ticks += 1
            #cube.move()
        
        pg.quit()

        
    def run(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.breaks = False
        
                    
        if self.ticks == 10:
                self.WIN.fill(self.BLACK)
                self.main()
                self.cube.draw(self.WIN)
                pg.display.update()
                self.ticks = 0

        else:
            self.main()

        self.clock.tick(300)
        self.ticks += 1



        
    def quit(self):
        pg.quit()

    

if __name__ == "__main__":
    WIN = window()

    while WIN.breaks:
        WIN.run()

    WIN.quit()