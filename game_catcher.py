import pygame
import sys
from catcher_settings import Settings
from catcher import Catcher

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kedown_events(event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)

def check_kedown_events(event):
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event):
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    if event.key == pygame.K_LEFT:
        catcher.moving_left = False

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Catcher')

screen.fill(ai_settings.bg_color)
catcher = Catcher(ai_settings, screen)

while True:
    screen.fill(ai_settings.bg_color)
    check_events()    

    catcher.update()
    catcher.blitme()
    
    pygame.display.flip()