import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represents one alien"""

    def __init__(self, ai_settings, screen):
        """initialise an alien and creates its start position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # loads image and assign rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # avery new alien emerges in up-left screen corner with intervals !!! rect.width
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saving definite alien position
        self.x = float(self.rect.x)
    
    def blitme(self):
        # creates an alien in a current position
        self.screen.blit(self.image, self.rect)

        