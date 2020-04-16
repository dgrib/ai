import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Class for printing game info."""
    def __init__(self, ai_settings, screen, stats):
        """Initialise score counting attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Score font settings.
        self.text_color = (30, 30, 30)
        # создается экземпляр объекта шрифта
        self.font = pygame.font.SysFont(None, 48)
        self.prep_images()
    
    """Также переместите четыре метода, 
    вызываемых в методе __init__() класса Scoreboard, 
    в метод prep_images() для сокращения длины __init__()."""
    def prep_images(self):
        # Prepares score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        #собираемся создать группу кораблей,
        # программа импортирует классы Group и Ship
        self.prep_ships()


    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        #отрицательное число, round() округляет значение до ближайших десятков, сотен и т. д
        rounded_score = int(round(self.stats.score, -1))
        score_str = f"Score {rounded_score:,}".replace(',', '.')
        self.score_image = self.font.render(score_str, True, self.text_color,
                self.ai_settings.bg_color)
        #Prints score in right-up screen part
        #мы создаем прямоугольник rect с именем score_rect
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = f"Record {high_score:,}".replace(',', '.')
        #для рекорда строится графическое изображение
        self.high_score_image = self.font.render(high_score_str, True,
                    self.text_color, self.ai_settings.bg_color)
        # Allign record by up-center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        self.level_image = self.font.render(('Level ' + str(self.stats.level)), True,
                    self.text_color, self.ai_settings.bg_color)
        # LEver appears under score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.level_rect.bottom + 30

    def prep_ships(self):
        """Informs сообщает left ship quantity"""
        #Метод prep_ships() создает пустую группу self.ships
        # для хранения экземпляров кораблей
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def show_score(self):
        """Prints the score on the screen."""
        #Метод выводит счет на экран в позиции, определяемой score_rect
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Вывод кораблей.
        self.ships.draw(self.screen)
        #При выводе кораблей на экран мы вызываем метод draw() для группы,
        # а Pygame рисует каждый отдельный корабль.




