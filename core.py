import pygame as pg
import engine
import random
from data.mp_data import mp_data

pg.init()

width ,height = 1024,600
display = pg.display.set_mode((width,height))
clock = pg.time.Clock()
pg.display.set_caption("AlphaV0.0.0.0 invdev")
font = pg.font.Font("data/pix.ttf", 18)

window = pg.Surface((300 ,200))

def onLoop():
	global loop
	for event in pg.event.get():
		if event.type == pg.QUIT:
			loop = False


	dynamic_res = pg.transform.scale(window,(width , height))
	display.blit(dynamic_res,(0,0))
	pg.display.flip()
	clock.tick(60)


a = font.render("INDEV=MISSINGTESXTURE",True,(255,255,255),(255,55,255))


player = False
animation = False
movement = False


#LOOP
loop = True
while loop == True:
	window.fill((200,200,200))
	display.fill((200,200,200))
	keyinput = pg.key.get_pressed()


	#engine.player.player(window,keyinput)
	
	engine.player.movement(window,keyinput)
	engine.player.animation(window,keyinput)
	engine.player.combat(window,keyinput)
	engine.player.camera(window,keyinput)
	pg.draw.rect(window,(255,255,0),(20,100,30,30))
	#map.map_1.tiles(window)
	#fx.vfx.animate_left(window,10,10)
	mp_data.map_lvl.Loop(window)


	#window.blit(a,(0,0))

	onLoop()