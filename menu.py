import pygame as pg

from menu_files.buttons import Button

from settings import *


class Menu:
	def __init__(self):
		self.play_btn = Button(text='play', size=(180, 50), pos=(122, 150))

		self.exit_btn = Button(text='exit', size=(180, 50), pos=(122, 265))


	def render(self, surface):
		surface.fill(BG_COLOR)

		big_font = pg.font.Font('UbuntuMono-Regular.ttf', 52)
		small_font = pg.font.Font('UbuntuMono-Regular.ttf', 14)

		game_title = big_font.render(MENU_TITLE, True, TEXT_COLOR)
		author = small_font.render("developed by Eduard Brusnigin", True, 
			TEXT_COLOR)

		surface.blit(game_title, (95, 50))
		surface.blit(author, (5, 408))

		self.play_btn.render(surface)
		self.exit_btn.render(surface)


	def update(self):
		pg.display.set_caption(MENU_TITLE)

		mouse_pos = pg.mouse.get_pos()
		mouse_click = pg.mouse.get_pressed()[0]

		mouse = (mouse_pos, mouse_click)

		if self.play_btn.is_click(mouse=mouse):
			return True

		elif self.exit_btn.is_click(mouse=mouse):
			exit()
