class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship settings
        self.ship_limit = 3
        # bullet parameters
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 50
        # aliens settings
        self.fleet_drop_speed = 10
        # Game accelerate factor
        self.speedup_scale = 1.1
        """Значения, которые остаются неизменными,
		по-прежнему инициализируются в методе __init__()"""

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Эти скорости будут увеличиваться по ходу игры
        # и будут сбрасываться каждый раз, когда игрок запускает новую игру.
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet direction = 1 means move right, -1 move left
        """Для настройки fleet_direction можно использовать текстовое значение
		(например, 'left' или 'right' ), но, скорее всего, в итоге придется
		использовать набор команд if - elif для проверки направления."""
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
