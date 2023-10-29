import pygame as pg

from menu import Menu
from game import Game

from settings import *


pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


menu = Menu()

game_stage = 'menu'


while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()


	if game_stage == 'menu':
		menu.render(window)

		if menu.update():  # func returns True if play_btn is clicked
			game = Game()  # new game instance
			game_stage = 'game'


	elif game_stage == 'game':
		game.render(window)
		game.update()

		if game.is_escape():
			game_stage = 'menu'


	clock.tick(FPS)
	pg.display.update()
