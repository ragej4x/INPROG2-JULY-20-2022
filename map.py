import pygame as pg
from data.mpdata2 import *

class map_1():
    def __init__(self):
        self.size = 20
        self.tile = tile()


    def Loop(self,window):
        y = 0
        for i in self.tile:
            x = 0
            for row in i:
                if row == -1:
                    pg.draw.rect(window ,(255,0,0) , (x * 15,y * 15, 15,15 ))

                x += 1
        y = 0




map_lvl = map_1()
