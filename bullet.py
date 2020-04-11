import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями, выпущеннными кораблем"""

    def __init__(self, ai_settings, screen, ship):
        # creates a bullet object in the current ship pos
    # super(Bullet, self).__init__() # python 2.7
        super().__init__()
        self.screen = screen

        # creating a bullet in position 0,0 and assignment the correct position
        """Пуля не создается на основе готового изображения, поэтому прямоугольник 
        приходится строить «с нуля» при помощи класса pygame.Rect()"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        """Прямоугольник инициализируется в точке (0, 0), но в следующих двух строках
        он перемещается в нужное место, так как позиция пули зависит от позиции корабля."""
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # bullet position reserves in float format
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet upwards"""
        # renews bullet pos in float format
        self.y -= self.speed_factor
        # renews rect pos
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)