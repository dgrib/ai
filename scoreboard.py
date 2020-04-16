import pygame.font

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
        # Prepares score image.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        #отрицательное число, round() округляет значение до ближайших десятков, сотен и т. д
        rounded_score = int(round(self.stats.score, -1))
        score_str = f"{rounded_score:,}".replace(',', '.')
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
        high_score_str = f"{high_score:,}".replace(',', '.')
        #для рекорда строится графическое изображение
        self.high_score_image = self.font.render(high_score_str, True,
                    self.text_color, self.ai_settings.bg_color)
        # Allign record by up-center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def show_score(self):
        """Prints the score on the screen."""
        #Метод выводит счет на экран в позиции, определяемой score_rect
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)



