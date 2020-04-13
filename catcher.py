import pygame
from pygame.sprite import Sprite

class Catcher(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Loads image and assign rect attributes
        self.image = pygame.image.load('images/bo.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Catcher appiars
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.catcher_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.catcher_speed_factor
        self.rect.centerx = self.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
