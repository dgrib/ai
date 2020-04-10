import sys

import pygame

def check_events(ship):
    """Operates key push and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(ai_settings, screen, ship):

    screen.fill(ai_settings.bg_color)
    """Чтобы перерисовать корабль на экране, мы вызываем ship.blitme()
    после заполнения фона, так что корабль выводится поверх фона"""
    ship.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()