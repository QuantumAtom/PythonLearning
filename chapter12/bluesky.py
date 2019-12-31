import sys

import pygame

from videogamecharacter import Link

def game_function():
    pygame.init()
    #Set the display resolution
    screen = pygame.display.set_mode((1200, 800))

    #Set background color variable
    sky_bg = (135, 206, 250)

    link = Link(screen)

    #Star the main loop
    while True:
        #Watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(sky_bg)
        link.blitme()
        pygame.display.flip()

game_function()

