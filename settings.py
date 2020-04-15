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
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		# rect param
		self.target_width = 50
		self.target_height = 300
		self.target_speed_factor = 1
		self.target_color = 200, 60, 60
		self.target_direction = 1
		self.miss_limit = 3
	