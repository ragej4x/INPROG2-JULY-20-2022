import pygame as pg
import run , atk , idle
import random


class player_mechanics():
    def __init__(self, x , y):
        self.x = 0
        self.y = 0

        self.camera_x = 0
        self.camera_y = 0

        self.y_vel = 0
        self.jump = False

        self.rect = pg.Rect(self.x , self.y,15,30)
        self.rect.x = x
        self.rect.y = y

        self.left = False
        self.right = False

        self.skill_1 = False
        self.skill_2 = False
        self.skill_3 = False

        self.cd = 10
        self.cd_bool = False



    def movement(self,window , keyinput):
        player = pg.draw.rect(window,(255,0,0),(self.rect),1)
        dx = 0
        dy = 0
        
        # MOVE LEFT & RIGHT

        if keyinput[pg.K_LEFT] and self.skill_1 == False and self.skill_2 == False and self.skill_3 == False:
            self.left = True
            self.right = False
            

            dx = -2

        if keyinput[pg.K_RIGHT] and self.skill_1 == False and self.skill_2 == False and self.skill_3 == False:
            self.left = False
            self.right = True
            

            dx = +2

        # JUMP

        if keyinput[pg.K_UP]:
            self.jump = True



        if self.jump == True and self.y_vel == 10:
            self.y_vel = -8

        if self.rect.y <= 200:
            self.jump = False

        #GRAVITY & VEL

        self.y_vel += 0.5
        if self.y_vel > 10:
            self.y_vel = 10

        dy += self.y_vel


        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.bottom > 190:
            self.rect.bottom = 190
            dy = 0
    


    def animation(self,window , keyinput):
        

        if self.left == True and keyinput[pg.K_LEFT] and self.skill_1 == False and self.skill_2 == False and self.skill_3 == False:
            run.run_animation.animate_left(window, self.rect.x - 15, self.rect.y -7)

        if self.right == True and keyinput[pg.K_RIGHT] and self.skill_1 == False and self.skill_2 == False and self.skill_3 == False:
            run.run_animation.animate_right(window, self.rect.x - 20, self.rect.y - 7)

        
        if self.left == True and keyinput[pg.K_LEFT] == False and self.skill_1 == False and self.skill_2 == False and self.skill_3 == False:
            idle.idle_animation.animate_left(window, self.rect.x - 15, self.rect.y - 7)


        if self.right == True and keyinput[pg.K_RIGHT] == False and self.skill_1 == False and self.skill_2 == False and self.skill_3 == False:
            idle.idle_animation.animate_right(window, self.rect.x - 15, self.rect.y - 7)


    def combat(self, window , keyinput):

        self.cd += 0.1
        if self.cd > 10:
            self.cd = 10
            self.cd_bool = True

        # SKILL 1

        if keyinput[pg.K_q] and self.cd_bool == True:
            self.skill_1 = True
            self.cd = 0
            self.cd_bool = False
        

        if self.skill_1 == True  and self.left == True:
            atk.atk_K1_animation.animate_left(window,self.rect.x - 15, self.rect.y -7)

        if self.skill_1 == True  and self.right == True :
            atk.atk_K1_animation.animate_right(window,self.rect.x - 15, self.rect.y -7)


        if atk.atk_K1_animation.count == 0:
            self.skill_1 = False


        # SKILL 2

        if atk.atk_K1_animation.count >= 4:
            self.skill_2 = True


        if self.skill_2 == True and self.right == True:
            atk.atk_K2_animation.animate_right(window,self.rect.x - 15, self.rect.y -7)


        if self.skill_2 == True and self.left == True:
            atk.atk_K2_animation.animate_left(window,self.rect.x - 15, self.rect.y -7)


        if atk.atk_K2_animation.count == 0:
            self.skill_2 = False


        # SKILL 3

        if atk.atk_K2_animation.count >= 5:
            self.skill_3 = True


        if self.skill_3 == True and self.left == True:
            atk.atk_K3_animation.animate_left(window,self.rect.x - 15, self.rect.y -7)


        if self.skill_3 == True and self.right == True:
            atk.atk_K3_animation.animate_right(window,self.rect.x - 15, self.rect.y -7)


        if atk.atk_K3_animation.count == 0:
            self.skill_3 = False


        #SWING PHYSICS

        if atk.atk_K3_animation.count == 1.05 and self.right == True:
            self.rect.x += 5
        if atk.atk_K3_animation.count == 1.2 and self.right == True:
            self.rect.x += 5
            #LEFT
        if atk.atk_K3_animation.count == 1.05 and self.left == True:
            self.rect.x -= 5
        if atk.atk_K3_animation.count == 1.2 and self.left == True:
            self.rect.x -= 5

player = player_mechanics(100,0)