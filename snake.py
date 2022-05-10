import random
import pygame as pg 
import math


BACKROUND_BLUE = (100,125,150)
BACKROUND_GREEN = (20,50,35)
RED = (200,20,20)

WN_WIDTH = 1200
WN_HEIGHT = 750

STEP = 30


WN = pg.display.set_mode((WN_WIDTH,WN_HEIGHT))
WN.fill(BACKROUND_BLUE)
CLOCK = pg.time.Clock()
tick = 0

def reverse(lst):
    lst.reverse()
    return lst

def invect(vect):
    f_vect = []
    for i in vect:
        f_vect.append(i * -1)
    return f_vect


class apples():
    def new_pos(self):
        self.x = random.randint(0,math.floor(WN_WIDTH / STEP) - 1)
        self.y = random.randint(0,math.floor(WN_HEIGHT / STEP) - 1)
    
    def __init__(self):
        '''self.x = random.randint(0,math.floor(WN_WIDTH / STEP) - 1)
        self.y = random.randint(0,math.floor(WN_HEIGHT / STEP) - 1)'''
        self.new_pos()

    def draw(self):
        pg.draw.rect(WN, RED, (self.x * STEP,self.y * STEP,STEP,STEP))

    def check(self,head,snake):
        if head.x == self.x and head.y == self.y:
            print("got-em")
            '''self.x = random.randint(0,math.floor(WN_WIDTH / STEP))
            self.y = random.randint(0,math.floor(WN_HEIGHT / STEP))'''
            self.new_pos()
            snake.got_apple()
        

        
class block:
    def __init__(self,x,y,vect = [1,0]):
        self.x = x
        self.y = y
        self.direction = vect

    def draw(self,s):
        stepped_x = self.x * STEP
        stepped_y = self.y * STEP
        fac = 5
        if fac * s < 200:
            pg.draw.rect(WN,(5,200 - fac * s,50), (stepped_x,stepped_y,STEP,STEP))
        else:
            pg.draw.rect(WN,(5,0,50), (stepped_x,stepped_y,STEP,STEP))

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]


class snake():
    def __init__(self,x,y ):# initial location of snake
        self.length = 1
        self.body = [block(x,y)]
        self.direction = [1,0]#contains all elements of snake body
    
    def draw(self):
        s=0
        '''for i in range(1,self.length + 1): #iterates over all elements of snake
            stepped_x = self.body[0].x * STEP
            stepped_y = self.body[0].y * STEP
            pg.draw.rect(WN, GREEN, (stepped_x,stepped_y,STEP,STEP))
            s+=1'''
        for block in self.body:
            block.draw(s)
            s+=1
        #print(s)

    def moveBlocks(self):
        count = 0
        for block in self.body:
            if count > 0:
                block.move()
            count += 1

    def block_chainPass(self):
        #TODO: MAKE THIS WORK!!!!!1
        count = 0
        for block in self.body:

            if count != 0:
                prev_direction = this_dir
                this_dir = block.direction
                block.direction = prev_direction
            else:
                this_dir = block.direction
            

            count += 1

    def move(self):
        self.body[0].x += self.body[0].direction[0]
        self.body[0].y += self.body[0].direction[1]
        self.moveBlocks()
        self.block_chainPass()


    def die(self):
        print("you lose")
        pg.quit()
        quit()


    def checkWall(self):
        if (self.body[0].x >= (WN_WIDTH // STEP)) or (self.body[0].x <= -1) or (self.body[0].y >= (WN_HEIGHT // STEP)) or (self.body[0].y <= -1):
            self.die()


    def got_apple(self):
        new_vec = invect(self.body[self.length - 1].direction)
        self.body.append(block(self.body[self.length - 1].x + new_vec[0], self.body[self.length - 1].y + new_vec[1],self.body[self.length - 1].direction))
        self.length += 1

    def self_collosion(self):
        for i in range(1,self.length):
            if self.body[i].x == self.body[0].x and self.body[i].y == self.body[0].y:
                self.die()


snakey = snake(5,5)
apple = apples()
        

def snakeStuff(tick):
    tick+=1
    if tick >= 3:
        snakey.move()
        snakey.self_collosion()
        tick = 0
    snakey.draw()
    apple.check(snakey.body[0],snakey)
    snakey.checkWall()
    return tick

def backround():
    thing = 1
    
    for y in range(0,WN_HEIGHT, STEP):
        thing += 1
        for x in range(0,WN_WIDTH, STEP * 2):
            if thing % 2 == 0:
                xx = x + STEP
            else:
                xx = x
            pg.draw.rect(WN,BACKROUND_GREEN,(xx,y,STEP,STEP))


def stuff():
    run = True
    tick = 0


    while run:

        for event in pg.event.get():           
            if event.type == pg.QUIT:
                pg.quit()
                run = False
        
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            snakey.body[0].direction = [1,0]

        if keys[pg.K_LEFT]:
            snakey.body[0].direction = [-1,0]

        if keys[pg.K_DOWN]:
            snakey.body[0].direction = [0,1]

        if keys[pg.K_UP]:
            snakey.body[0].direction = [0,-1]

        WN.fill(BACKROUND_BLUE)    

        backround()
        apple.draw()
        tick = snakeStuff(tick)


        pg.display.update()
        CLOCK.tick(30)




if __name__ == "__main__":
    stuff()
