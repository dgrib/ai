import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, stats, aliens, screen, ship, bullets):
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
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, aliens, ship, bullets)

def check_keyup_events(event, ship):
    """Reacts keyups"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Operates key push and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, aliens, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen, stats, play_button,
                            ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
        bullets, mouse_x, mouse_y):
    """Loads new game when pushing play_button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, aliens, ship, bullets)

def start_game(ai_settings, screen, stats, aliens, ship, bullets):
    """Starts game if button play or p-key"""
    # Mouse pointer is off
    pygame.mouse.set_visible(False)
    #Reloads game stats
    stats.reset_stats()
    stats.game_active = True

    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """renewed positions of game elements are used in deriving(вывода) new screen"""
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    """Чтобы перерисовать корабль на экране, мы вызываем ship.blitme()
    после заполнения фона, так что корабль выводится поверх фона"""
    ship.blitme()
    """Когда вы вызываете метод draw() для группы, Pygame автоматически выводит
    каждый элемент группы в позиции, определяемой его атрибутом rect ."""
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Renews bullets positions and removes out of screen bullets"""
    # renews bullets positions
    bullets.update()
	# Removing out of screen bullets
    for bullet in bullets.copy(): # search in copy but delete in bullets
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # check if a bullet hit an alien, removes (True,True) the bullet and the alien
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    # creating a new bullet and including it in the "bullets" group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """Creates alien fleet"""
    alien = Alien(ai_settings, screen)
    # Создание пришельца и вычисление количества пришельцев в ряду.
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # creating alien fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ ctreates an alien and place it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """ detects quantity rows that are in free space"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """ CHeck if an alien by the screen edge and then renews positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # check collisions ship-alien
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """ Reacts when an alient reaches the screen edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Moves the fleet down and changes direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if len(aliens) == 0:
        # destroy existing bullets and creating a new fleet
        bullets.empty() # removes oll sprites from a group
        create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Operate ship-alien collision"""
    if stats.ship_left > 0:
        # Diminishing ship_left
        stats.ship_left -= 1
        # Cleaning aliens and bullets
        aliens.empty()
        bullets.empty()
        #Creating new fleet and shoip position
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Checks if an alien got the bottom edge"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Happens the same as if collision ship-alien
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break