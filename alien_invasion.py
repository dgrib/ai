import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button

#http://pixabay.com/ изображения тут

def run_game():

	# Инициализирует pygame, settings и объект экрана.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#Creating Play button
	
	# Creating an instance for keeping game statistics
	stats = GameStats(ai_settings)
	# Создание корабля.
	ship = Ship(ai_settings, screen)

	# Creatin a group for bullet containing
	"""Эта группа создается за пределами цикла while , чтобы новая 
	группа пуль не создавалась при каждом проходе цикла."""
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	play_button = Button(ai_settings, screen, 'Play')

	# Запуск основного цикла игры.
	while True:
		"""Объект bullets передается методам check_events() и update_screen() .
		В check_events() он используется при обработке клавиши «пробел», а в update_screen()
		необходимо перерисовать выводимые на экран пули"""
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets) # checks data from playes
		# При каждом проходе цикла перерисовывается экран.
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
		
		if stats.game_active:
			"""Позиция корабля будет обновляться после проверки событий клавиатуры,
			но перед обновлением экрана. Таким образом, позиция корабля обновляется
			в ответ на действия пользователя и будет использоваться при перерисовке корабля на экране"""
			ship.update() #renews ship position
			"""Вызов update() для группы bullets приводит к автоматическому вызову update() для
			каждого спрайта в группе. Строка bullets.update() вызывает bullet.update() для
			каждой пули, включенной в группу bullets ."""
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			# print(len(bullets))
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			
run_game()