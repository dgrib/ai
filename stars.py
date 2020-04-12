import pygame
from settings import Settings
from pygame.sprite import Sprite
from pygame.sprite import Group

class Star(Sprite):
    """Represents one star"""

    def __init__(self, ai_settings, screen):
        """initialise an alien and creates its start position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # loads image and assign rect attribute
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # avery new alien emerges in up-left screen corner with intervals !!! rect.width
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def blitme(self):
        # creates an alien in a current position
        self.screen.blit(self.image, self.rect)

def get_number_stars_x(ai_settings, star_width):
    number_stars_x = int(ai_settings.screen_width / (2 * star_width))
    return number_stars_x

def create_star(ai_settings, screen, aliens, star_number, row_number):
    """ ctreates an alien and place it in a row"""
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)

def get_number_rows(ai_settings, star_height):
    number_rows = int(ai_settings.screen_height / star_height)
    return number_rows

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Stars")
star = Star(ai_settings, screen)
stars = Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)
    stars.draw(screen)
    pygame.display.flip()