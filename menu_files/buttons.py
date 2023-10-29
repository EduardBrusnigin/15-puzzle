import pygame as pg

from settings import *


class Button:
	def __init__(self, text, size, pos):
		self.text = text

		self.width = size[0]
		self.height = size[1]

		self.x = pos[0]
		self.y = pos[1]

		self.btn_color = GREEN_COLOR


	def is_click(self, mouse):  # return True - click, or False - not click
		mouse_pos = mouse[0]
		m_x, m_y = mouse_pos[0], mouse_pos[1]

		mouse_click = mouse[1]


		if (self.x <= m_x <= self.x + self.width) and \
			(self.y <= m_y <= self.y + self.height):  # aim check
			self.btn_color = RED_COLOR

			if mouse_click:
				return True

		else:
			self.btn_color = GREEN_COLOR

		return False


	def render(self, surface):
		pg.draw.rect(surface, self.btn_color, \
			(self.x, self.y, self.width, self.height))

		medium_font = pg.font.Font('UbuntuMono-Regular.ttf', 42)

		text = medium_font.render(self.text, True, (90, 90, 90))

		text_width = text.get_rect().width 
		text_height = text.get_rect().height

		text_x = self.x + self.width//2 - text_width//2
		text_y = self.y + self.height//2 - text_height//2 - 4

		surface.blit(text, (text_x, text_y))
