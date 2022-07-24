import pygame as pg

class Enemy_logic():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pg.Rect(self.x , self.y , 30,30)

    
    def movement(self, window):
        pass

enemy = Enemy_logic()