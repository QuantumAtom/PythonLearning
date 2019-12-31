import sys

import pygame

"""initialize rocket"""
image = pygame.image.load('images/rocketship.bmp')
imgrect = image.get_rect()
rectscreen = screen.get_rect()

"""Where it's at!"""
imgrect.centerx = rectscreen.centerx
imgrect.centery = rectscreen.centery

"""Moving flags!!!"""
MoveLeft = False
MoveRight = False
BullUp = False
BearDown = False

def keydown(self, event):
    """Key press response"""
    if event.key == pygame.K_LEFT:
            self.MoveLeft = True
    elif event.key == pygame.K_RIGHT:
            self.MoveRight = True
    elif event.key == pygame.K_UP:
            self.BullUp = True
    elif event.key == pygame.K_DOWN:
            self.BearDown = True

def keyup(event):
    """Key letting up"""
    if event.key == pygame.K_LEFT:
        MoveLeft = False
    elif event.key == pygame.K_RIGHT:
        MoveRight = False
    elif event.key == pygame.K_UP:
        BullUp = False
    elif event.key == pygame.K_DOWN:
        BearDown = False


def MoveMe():
    """Move like a chess queen"""
    if MoveRight and self.imgrect < self.rectscreen.right:
        imgrect.x += 1
    if MoveLeft and self.imgrect < 0:
        imgrect.x -= 1
    if BullUp and self.imgrect < self.rectscreen.up:
        imgrect.y += 1
    if self.BearDown and self.imgrect < self.rectscreen.down:
        imgrect.y -= 1

def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.imgrect, self.rectscreen)



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
                            keydown(event)
                        elif event.type == pygame.KEYUP:
                            keyup(event)
                WeylandYutani.MoveMe()
                
                screen.fill(sky_bg)
                WeylandYutani.blitme()
                pygame.display.flip()

game_function()

