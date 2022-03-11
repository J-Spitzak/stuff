import pygame as pg
import math

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vect = [0,0]
        self.mag = math.sqrt((self.vect[0] ** 2) + (self.vect[1] ** 2))

    def draw(self,WN):
        pg.draw.polygon(WN, (100, 100, 100), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))

class field:
    def __init__(self,width,height,substeps):
        self.BLACK = (0,0,0)
        self.GRAY = (60,60,60)
        self.BLUE = (0,0,40)
        
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.substeps = substeps
        self.width = width / substeps
        self.height = height / substeps
        self.color = self.BLACK
        self.win = pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.vector_rows = []
        for y in range(self.height):
            xs = {}
            for x in range(self.width):
                heller = vector(x,y)
                xs.append(str(x,y) : heller )


    def draw(self):
        self.win.fill(self.BLACK)