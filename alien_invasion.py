import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

#http://pixabay.com/ изображения тут

def run_game():

	# Инициализирует pygame, settings и объект экрана.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# Создание корабля.
	ship = Ship(screen)

	# Запуск основного цикла игры.
	while True:
		gf.check_events(ship)
		"""Позиция корабля будет обновляться после проверки событий клавиатуры,
		но перед обновлением экрана. Таким образом, позиция корабля обновляется
		в ответ на действия пользователя и будет использоваться при перерисовке корабля на экране"""
		ship.update()
		# При каждом проходе цикла перерисовывается экран.
		gf.update_screen(ai_settings, screen, ship)

run_game()