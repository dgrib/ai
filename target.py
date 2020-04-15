import pygame
from settings import Settings

class Target():
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, ai_settings.target_width, ai_settings.target_height)
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        # bullet position reserves in float format
        self.y = float(self.rect.y)

        self.color = ai_settings.target_color
        self.speed_factor = ai_settings.target_speed_factor

    def update(self):
        """ moves a target to right or to left"""
        self.y += self.ai_settings.target_speed_factor * self.ai_settings.target_direction
        self.rect.y = self.y

    def check_edges(self):
        """ Returns True if the target is by the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def blitme(self):
        """Draws the target into the current position"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def center_target(self):
        # Points target in the center right
        self.center = self.screen_rect.centery