import sys
from sys import exit

import pygame

from bullet import Bullet



def check_keydown_events(event, link_settings, screen, char, bullet):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        char.moving_up = True
    elif event.key == pygame.K_DOWN:
        char.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(link_settings, screen, char, bullet)
    
def check_keyup_events(event, char):
    """Respond to key releases"""
    if event.key == pygame.K_UP:
        char.moving_up = False
    elif event.key == pygame.K_DOWN:
        char.moving_down = False

def check_events(link_settings, screen, char, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event, link_settings, screen, char, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, char)
           

def update_screen(link_settings, screen, char, bullets):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop
    screen.fill(link_settings.bg_color)
    # Redraw all bullets behind char and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    char.blitme()

    #Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions.
    bullets.update()
        #Get rid of bullets that have disappeared
    #for bullet in bullets.copy():
            #if bullet.rect.left >= 0:
                    #bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(link_settings, screen, char, bullet):
       # Make a new bullet and add it to the bullets group.
        #if len(bullet) < link_settings.bullets_allowed:
        new_bullet = Bullet(link_settings, screen, char)
        bullet.add(new_bullet)
