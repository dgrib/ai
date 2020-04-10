import pygame

class Ship():
	def __init__(self, screen):
		"""Инициализирует корабль и задает его начальную позицию."""
		self.screen = screen

		"""Load ship image , making rectangle"""
		self.image = pygame.image.load('images/ship.bmp')
		"""Функция возвращает поверхность, представляющую корабль;
		полученный объект сохраняется в self.image"""
		
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		"""Every new ship emerges beside the screen lower edge"""
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#Movoing flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Renews ship position taking into account the flag"""
		"""В update() используются два отдельных блока if вместо elif ,
		чтобы при нажатии обеих клавиш со стрелками атрибут rect.centerx сначала увеличивался,
		а потом уменьшался. В результате корабль остается на месте."""
		if self.moving_right:
			self.rect.centerx += 1
		if self.moving_left:
			self.rect.centerx -= 1

	def blitme(self):
		"""Draws a ship into the current position"""
		self.screen.blit(self.image, self.rect)

