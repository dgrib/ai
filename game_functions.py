import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Rects keydowns"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        """Здесь возможно использовать блоки elif , потому что каждое событие связано
        только с одной клавишей. Если же игрок нажимает обе клавиши одновременно,
        то программа обнаруживает два разных события"""
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Reacts keyups"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Operates key push and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(ai_settings, screen, ship, alien, bullets):
    """renewed positions of game elements are used in deriving(вывода) new screen"""
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    """Чтобы перерисовать корабль на экране, мы вызываем ship.blitme()
    после заполнения фона, так что корабль выводится поверх фона"""
    ship.blitme()
    """Пришелец выводится после прорисовки корабля и пуль,
    так что пришельцы будут находиться на верхнем «слое» экрана."""
    alien.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def update_bullets(bullets):
    """Renews bullets positions and removes out of screen bullets"""
    # renews bullets positions
    bullets.update()
	# Removing out of screen bullets
    for bullet in bullets.copy(): # search in copy but delete in bullets
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # creating a new bullet and including it in the "bullets" group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)