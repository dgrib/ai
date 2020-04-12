import pygame
from drop_settings import Settings
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

class Drop(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # loads image and assign rect attribute
        self.image = pygame.image.load('images/drop.bmp')
        self.rect = self.image.get_rect()

        # avery new drop emerges in up-left screen corner with intervals !!! rect.width
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saves definite drop pos
        self.x = float(self.rect.x)

    def blitme(self):
        # creates a drop in a current position
        self.screen.blit(self.image, self.rect)

def get_number_drops_x(ai_settings, drop_width):
    number_drops_x = int(ai_settings.screen_width / (2 * drop_width))
    return number_drops_x

def create_drop(ai_settings, screen, drops, drop_number, row_number):
    """ ctreates a drop and place it in a row"""
    random_number = randint(-50,50)
    drop = Drop(ai_settings, screen)
    drop_width = drop.rect.width
    drop.x = drop_width + 2 * drop_width * drop_number
    drop.rect.x = drop.x
    drop.rect.x += random_number
    drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number
    drop.rect.y += random_number
    drops.add(drop)

def get_number_rows(ai_settings, drop_height):
    number_rows = int(ai_settings.screen_height / drop_height)
    return number_rows

def move_drops_down(ai_settings, aliens):
    """Moves drops down"""
    for drop in drops.sprites():
        drop.rect.y += ai_settings.drop_speed_factor
        
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Drops')
screen.fill(ai_settings.bg_color)
drop = Drop(ai_settings, screen)
drops = Group()
number_drops_x = get_number_drops_x(ai_settings, drop.rect.width)
number_rows = get_number_rows(ai_settings, drop.rect.height)
for row_number in range(number_rows):
    for drop_number in range(number_drops_x):
        create_drop(ai_settings, screen, drops, drop_number, row_number)
drops.draw(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    move_drops_down(ai_settings, screen)

    drops.draw(screen)

    pygame.display.flip()