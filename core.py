import pygame as pg
import engine
import random
import atk , jump , idle, run

pg.init()

display_res = 1024,600
display = pg.display.set_mode(display_res, pg.DOUBLEBUF )
clock = pg.time.Clock()
pg.display.set_caption("AlphaV0.0.0.0 invdev")


window = pg.Surface((300 ,200))

def onLoop():
	global loop
	for event in pg.event.get():
		if event.type == pg.QUIT:
			loop = False


	dynamic_res = pg.transform.scale(window,(display_res))
	display.blit(dynamic_res,(0,0))
	clock.tick(60)
	



player = False
animation = False
movement = False

def fps():
	ren_font = pg.font.Font("data/monogram.ttf", 35)
	count_fps = str(int(clock.get_fps()))
	display_fps = ren_font.render(count_fps, False, (150,0,0))
	display_txt = ren_font.render("FPS:",False , (0,0,0))
	display.blit(display_fps,(60,0))
	display.blit(display_txt,(5,0))


def optimize():

	run.run_animation.animation_list_left[0].convert()
	run.run_animation.animation_list_left[1].convert()
	run.run_animation.animation_list_left[2].convert()
	run.run_animation.animation_list_left[3].convert()
	run.run_animation.animation_list_left[4].convert()
	run.run_animation.animation_list_left[5].convert()

	run.run_animation.animation_list_right[0].convert()
	run.run_animation.animation_list_right[1].convert()
	run.run_animation.animation_list_right[2].convert()
	run.run_animation.animation_list_right[3].convert()
	run.run_animation.animation_list_right[4].convert()
	run.run_animation.animation_list_right[5].convert()

	idle.idle_animation.animation_list_left[0].convert()
	idle.idle_animation.animation_list_left[1].convert()
	idle.idle_animation.animation_list_left[2].convert()
	idle.idle_animation.animation_list_left[3].convert()

	idle.idle_animation.animation_list_right[0].convert()
	idle.idle_animation.animation_list_right[1].convert()
	idle.idle_animation.animation_list_right[2].convert()
	idle.idle_animation.animation_list_right[3].convert()


	atk.atk_K1_animation.animation_list_left[0].convert()
	atk.atk_K1_animation.animation_list_left[1].convert()
	atk.atk_K1_animation.animation_list_left[2].convert()
	atk.atk_K1_animation.animation_list_left[3].convert()
	atk.atk_K1_animation.animation_list_left[4].convert()

	atk.atk_K1_animation.animation_list_right[0].convert()
	atk.atk_K1_animation.animation_list_right[1].convert()
	atk.atk_K1_animation.animation_list_right[2].convert()
	atk.atk_K1_animation.animation_list_right[3].convert()
	atk.atk_K1_animation.animation_list_right[4].convert()

	atk.atk_K2_animation.animation_list_left[0].convert()
	atk.atk_K2_animation.animation_list_left[1].convert()
	atk.atk_K2_animation.animation_list_left[2].convert()
	atk.atk_K2_animation.animation_list_left[3].convert()
	atk.atk_K2_animation.animation_list_left[4].convert()
	atk.atk_K2_animation.animation_list_left[5].convert()

	atk.atk_K2_animation.animation_list_right[0].convert()
	atk.atk_K2_animation.animation_list_right[1].convert()
	atk.atk_K2_animation.animation_list_right[2].convert()
	atk.atk_K2_animation.animation_list_right[3].convert()
	atk.atk_K2_animation.animation_list_right[4].convert()
	atk.atk_K2_animation.animation_list_right[5].convert()


	atk.atk_K3_animation.animation_list_left[0].convert()
	atk.atk_K3_animation.animation_list_left[1].convert()
	atk.atk_K3_animation.animation_list_left[2].convert()
	atk.atk_K3_animation.animation_list_left[3].convert()
	atk.atk_K3_animation.animation_list_left[4].convert()
	atk.atk_K3_animation.animation_list_left[5].convert()

	atk.atk_K3_animation.animation_list_right[0].convert()
	atk.atk_K3_animation.animation_list_right[1].convert()
	atk.atk_K3_animation.animation_list_right[2].convert()
	atk.atk_K3_animation.animation_list_right[3].convert()
	atk.atk_K3_animation.animation_list_right[4].convert()
	atk.atk_K3_animation.animation_list_right[5].convert()


#LOOP
loop = True
while loop == True:
	window.fill((200,200,200))
	#display.fill((200,200,200))
	keyinput = pg.key.get_pressed()


	engine.player.movement(window,keyinput)
	engine.player.animation(window,keyinput)
	engine.player.combat(window,keyinput)
	#map.map_lvl.Loop(window)

	optimize()
	onLoop()
	fps()
	pg.display.flip()