import pygame
import sys
from catcher_settings import Settings
from catcher import Catcher
from ball import Ball
from pygame.sprite import Group

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

def create_ball(ai_settings, screen):
    ball = Ball(ai_settings, screen)
    balls.add(ball)

def collisions_catcher_ball(ai_settings):
    collision = pygame.sprite.groupcollide(catchers, balls, False, True)
    if len(balls) == 0:
        create_ball(ai_settings, screen)

def update_balls(ai_settings, screen, balls):
    balls.update()
    for ball in balls.copy():
        if ball.rect.bottom >= ai_settings.screen_height + ball.rect.height:
            balls.remove(ball)
            create_ball(ai_settings, screen)
    collisions_catcher_ball(ai_settings)
    balls.draw(screen)

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Catcher')

screen.fill(ai_settings.bg_color)
catcher = Catcher(ai_settings, screen)
catchers = Group()
catchers.add(catcher)

balls = Group()

create_ball(ai_settings, screen)

while True:
    screen.fill(ai_settings.bg_color)
    check_events()    
    catchers.update()
    catchers.draw(screen)

    update_balls(ai_settings, screen, balls)

    pygame.display.flip()