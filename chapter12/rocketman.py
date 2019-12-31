import sys

import pygame

from ricketrocket import Rocketeer

WeylandYutani = Rocketeer()

def game_function():
        pygame.init()
        #Set the display resolution
        screen = pygame.display.set_mode((1200, 800))
        #Set background color variable
        sky_bg = (135, 206, 250)

        #Star the main loop
        while True:
                #Watch for events
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                        elif event.type == pygame.KEYDOWN:
                                Rocketeer.keydown(self, event)
                        elif event.type == pygame.KEYUP:
                                Rocketeer.keyup(self, event)
                WeylandYutani.MoveMe()
                
                screen.fill(sky_bg)
                WeylandYutani.blitme()
                pygame.display.flip()

game_function()

