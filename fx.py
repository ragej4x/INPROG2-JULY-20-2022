import pygame as pg

class Visual_effects():
    def __init__(self):
        self.frames_left = []
        self.frames_right = []
        self.count = 0
    
        for i in range(2,9):
            smoke = pg.image.load(f"data/effects/smoke/frame ({i}).asset")
            smoke = pg.transform.scale(smoke, (50,20))
            smoke.set_colorkey(0)
            self.frames_left.append(smoke)
        

        for j in range(2,9):
            smoke = pg.image.load(f"data/effects/smoke/frame ({i}).asset")
            smoke = pg.transform.scale(smoke, (200,100))
            smoke.set_colorkey(0)
            self.frames_right.append(smoke)
        

    def animate_left(self , window, x,y):

        self.count += 0.15
        if self.count >= 7:
            self.count = 0
        
        self.image = self.frames_left[int(self.count)]

        pass
        
        window.blit(self.image,(x,y))


    def animate_right(self , window, x,y):

        self.count += 0.15
        if self.count >= 7:
            self.count = 0
        
        self.image = self.frames_right[int(self.count)]

        pass
        
        window.blit(self.image,(x,y))

vfx = Visual_effects()