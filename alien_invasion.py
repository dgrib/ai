import pygame
from pygame.sprite import Group
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
	ship = Ship(ai_settings, screen)

	# Creatin a group for bullet containing
	"""Эта группа создается за пределами цикла while , чтобы новая 
	группа пуль не создавалась при каждом проходе цикла."""
	bullets = Group()

	# Запуск основного цикла игры.
	while True:
		"""Объект bullets передается методам check_events() и update_screen() .
		В check_events() он используется при обработке клавиши «пробел», а в update_screen()
		необходимо перерисовать выводимые на экран пули"""
		gf.check_events(ai_settings, screen, ship, bullets)
		"""Позиция корабля будет обновляться после проверки событий клавиатуры,
		но перед обновлением экрана. Таким образом, позиция корабля обновляется
		в ответ на действия пользователя и будет использоваться при перерисовке корабля на экране"""
		ship.update()
		"""Вызов update() для группы bullets приводит к автоматическому вызову update() для
		каждого спрайта в группе. Строка bullets.update() вызывает bullet.update() для
		каждой пули, включенной в группу bullets ."""
		bullets.update()
		# При каждом проходе цикла перерисовывается экран.
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()