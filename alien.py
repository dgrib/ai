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

    def check_edges(self):
        """ Returns True if an alien is by the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ moves an alien to right or to left"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

        