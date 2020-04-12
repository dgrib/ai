class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""
	ship_speed_factor = 1.5 #ship settings

	def __init__(self):
		"""Инициализирует настройки игры."""
		# Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		# Назначение цвета фона.
		self.bg_color = (230, 230, 230)
		# bullet parameters
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		# aliens settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet direction = 1 means move right, -1 move left
		"""Для настройки fleet_direction можно использовать текстовое значение
		(например, 'left' или 'right' ), но, скорее всего, в итоге придется
		использовать набор команд if - elif для проверки направления."""
		self.fleet_direction = 1