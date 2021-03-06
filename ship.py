import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		"""Инициализирует корабль и задает его начальную позицию."""
		self.screen = screen
		self.ai_settings = ai_settings

		"""Load ship image , making rectangle"""
		self.image = pygame.image.load('images/ship.bmp')
		"""Функция возвращает поверхность, представляющую корабль;
		полученный объект сохраняется в self.image"""
		
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		"""Every new ship emerges beside the screen lower edge"""
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# Сохранение вещественной координаты центра корабля.
		self.center = float(self.rect.centerx)
		#Movoing flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Renews ship position taking into account the flag"""
		"""В update() используются два отдельных блока if вместо elif ,
		чтобы при нажатии обеих клавиш со стрелками атрибут rect.centerx сначала увеличивался,
		а потом уменьшался. В результате корабль остается на месте."""
		# Обновляется атрибут center, не rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		# Обновление атрибута rect на основании self.center.
		self.rect.centerx = self.center

	def blitme(self):
		"""Draws a ship into the current position"""
		self.screen.blit(self.image, self.rect)

