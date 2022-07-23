import pygame as pg

class Visual_effects():
    def __init__(self):
        self.count = 1
        self.smoke = pg.image.load("data/effects/smoke/frame ("+ str(self.count) +").asset")

    def smoke_fx(self , window, x,y):
        #self.count += 0.1
        window.blit(self.smoke, x,y)


        pass



vfx = Visual_effects()