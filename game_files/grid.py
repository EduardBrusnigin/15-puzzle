import pygame as pg

from game_files.mixing import get_mixed
from game_files.moving import *

from settings import *


class Grid:
	def __init__(self):
		self.grid = get_mixed()

		self.mouse_ready = False  
		# free variable for interaction 
		# between iterations of the loop.
		# free variable is needing to remove mouse sticking (method update)
		# mouse sticking can be enabled in settings.py (MOUSE_STICKING = True)


	def render(self, surface):
		surface.fill(BG_COLOR)

		big_font = pg.font.Font('UbuntuMono-Regular.ttf', 52)

		for i in range(4):
			for j in range(4):
				if self.grid[i][j] == (i*4 + (j+1)):  # if right position
					color = GREEN_COLOR  # green

				elif self.grid[i][j] == 0:  # if empty cell
					color = BG_COLOR

				else:  # if wrong position
					color = RED_COLOR  # red


				x = CELL_SIZE*j + SPACE*(j+1)
				y = CELL_SIZE*i + SPACE*(i+1)

				pg.draw.rect(surface, color, (x, y, CELL_SIZE, CELL_SIZE))

				number = big_font.render(str(self.grid[i][j]), \
					True, TEXT_COLOR)

				if self.grid[i][j] in (1, 2, 3, 4, 5, 6, 7, 8, 9):
					surface.blit(number, (x+36, y+22))  # if number is 1 char

				elif self.grid[i][j] == 0:
					pass  # if empty cell

				else:
					surface.blit(number, (x+23, y+22))	# if number is 2 chars	


	def update(self, mouse):  # returns True if some cell moves
		mouse_pos = mouse[0]
		m_x, m_y = mouse_pos[0], mouse_pos[1]

		mouse_click = mouse[1]

		if not mouse_click:
			self.mouse_ready = True


		for i in range(4):
			for j in range(4):
				x = CELL_SIZE*j + SPACE*(j+1)
				y = CELL_SIZE*i + SPACE*(i+1)

				is_aim = (x <= m_x <= (x + CELL_SIZE)) and \
					(y <= m_y <= (y + CELL_SIZE))

				if is_aim and mouse_click:
					if is_possible(self.grid, i, j, self.mouse_ready):
						self.grid = move(self.grid, i, j)
						return True

					self.mouse_ready = False


	def is_win(self):
		if self.grid == [[1, 2, 3, 4],
						 [5, 6, 7, 8],
						 [9, 10, 11, 12],
						 [13, 14, 15, 0]]:

			return True

		return False
