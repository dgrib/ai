import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, stats, target, screen, ship, bullets):
    """Rects keydowns"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
        """Здесь возможно использовать блоки elif , потому что каждое событие связано
        только с одной клавишей. Если же игрок нажимает обе клавиши одновременно,
        то программа обнаруживает два разных события"""
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, target, bullets)

def check_keyup_events(event, ship):
    """Reacts keyups"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, play_button, ship, target, bullets):
    """Operates key push and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, target, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, target, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, target,
        bullets, mouse_x, mouse_y):
    """Loads new game when pushing play_button"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        start_game(ai_settings, screen, stats, ship, target, bullets)
        
def start_game(ai_settings, screen, stats, ship, target, bullets):
    #Reloads game stats
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True
    target.center_target()
    bullets.empty()
    ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, bullets, target, play_button):
    """renewed positions of game elements are used in deriving(вывода) new screen"""
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    """Чтобы перерисовать корабль на экране, мы вызываем ship.blitme()
    после заполнения фона, так что корабль выводится поверх фона"""
    ship.blitme()
    target.blitme()
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def update_target(ai_settings, target):
    """ CHeck if the target by the screen edge and then renews positions the target"""
    if target.check_edges():
        ai_settings.target_direction *= -1
    target.update()

def update_bullets(ai_settings, bullets, target, stats):
    """Renews bullets positions and removes out of screen bullets"""
    # renews bullets positions
    if stats.miss_left > 0:
        bullets.update()
        # if pygame.sprite.spritecollideany(target, bullets):
        #     pass
        # Removing out of screen bullets
        for bullet in bullets.copy(): # search in copy but delete in bullets
            if bullet.rect.left >= ai_settings.screen_width:
                bullets.remove(bullet)
                stats.miss_left -= 1
            elif pygame.sprite.spritecollideany(target, bullets):
                bullets.remove(bullet)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def fire_bullet(ai_settings, screen, ship, bullets):
    # creating a new bullet and including it in the "bullets" group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)