import pygame
from pygame.sprite import Group
from sys import exit
from settings import Settings
from char import Char
import game_functions as gf

def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    link_settings = Settings()
    screen = pygame.display.set_mode((link_settings.screen_width, link_settings.screen_height))
    pygame.display.set_caption("The New Adventures of Link")

    #Make a char
    char = Char(link_settings, screen)

    #Make a group to store bullets in.
    bullets = Group()

    #Set the background color.
    bg_color = (230, 230, 230)
    #Start the main loop for the game

    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(link_settings, screen, char, bullets)
        char.update()
        gf.update_bullets(bullets)
        gf.update_screen(link_settings, screen, char, bullets)
        
    
run_game()


