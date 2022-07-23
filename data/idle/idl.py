import pygame as pg

class idle():
	def __init__(self):
			self.x = 0
			self.y = 0
			self.count = 0

			self.animation_list_right = [
			pg.image.load("idl1.asset"),
			pg.image.load("idl2.asset"),
			pg.image.load("idl3.asset"),
			pg.image.load("idl4.asset"),
			]



	def animate(self,window):
		window.blit()		




idle_animation = idle()