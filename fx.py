import pygame as pg

class Visual_effects():
    def __init__(self):
        self.frames = []
        self.count = 0
        for i in range(2,9):
            smoke = pg.image.load(f"data/effects/smoke/frame ({i}).asset")
            smoke = pg.transform.scale(smoke, (50,20))
            
            self.frames.append(smoke)
        

        
    def smokeFx(self , window, x,y):

        self.count += 0.1
        if self.count >= 7:
            self.count = 0
        
        self.image = self.frames[int(self.count)]


        pass
        
        window.blit(self.image,(x,y))


vfx = Visual_effects()