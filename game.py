import pygame as pg

from datetime import datetime as dt

from game_files.grid import Grid

from settings import WIN_TITLE_PERIOD


class Game():
	def __init__(self):
		self.grid = Grid()

		self.moments = [dt.now(), dt.now()]  # two points of time to count the difference

		self.time = 0
		self.moves = 0

		self.f_time = None  # formatted time

		self.flag = False  # flag is needed to reset absolute time when winning


	def render(self, surface):
		self.grid.render(surface)


	def update(self):
		self.moments[1] = dt.now()

		if (self.moments[1] - self.moments[0]).total_seconds() >= 1:
			self.time += 1
			self.moments[0], self.moments[1] = dt.now(), dt.now()


		if not self.grid.is_win():
			seconds = str(self.time % 60).rjust(2, '0')
			minutes = str(self.time // 60).rjust(2, '0')
			self.f_time = f"{minutes}:{seconds}"

			title = f"15 Puzzle (moves: {self.moves}, time: {self.f_time})"
			pg.display.set_caption(title)

			mouse_pos = pg.mouse.get_pos()
			mouse_click = pg.mouse.get_pressed()[0]

			mouse = (mouse_pos, mouse_click)

			if self.grid.update(mouse=mouse):
				self.moves += 1


		else:
			if self.time != 0 and not self.flag:
				self.time = 0
				self.moments = [dt.now(), dt.now()]
				self.flag = True

			if self.time % (2*WIN_TITLE_PERIOD) == 0:
				title = f"15 Puzzle (moves: {self.moves}, time: {self.f_time})"
				pg.display.set_caption(title)

			elif self.time % WIN_TITLE_PERIOD == 0:
				title = "You win! Press Escape"
				pg.display.set_caption(title)


	def is_escape(self):
		keys = pg.key.get_pressed()

		if keys[pg.K_ESCAPE]:
			return True
