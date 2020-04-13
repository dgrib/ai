import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.top = self.screen_rect.top
        self.rect.x = randint(0, ai_settings.screen_width - self.rect.width)

        self.speed_factor = ai_settings.ball_falls_factor

    def update(self):
        self.rect.y += self.speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)





