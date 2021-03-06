import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

from button import Button
from bullet import Bullet


def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Generate the play button
    play_button = Button(ai_settings, screen, "Play")
    
    #Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    #Make a ship, a group of bullets, and a group of aliens.
    
    #Make a ship
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets in.
    bullets = Group()

    #Make a group to store aliens in
    aliens = Group()

    #Generate a fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens, ship)

    #Set the background color.
    bg_color = (230, 230, 230)

    #Start the main loop for the game

    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, ship, stats, aliens, bullets, play_button)
        
    
run_game()
