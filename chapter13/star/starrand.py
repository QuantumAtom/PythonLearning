import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
import sys
from sys import exit
from random import randint

screen = pygame.display.set_mode((1200, 800))


class Starstruck(Sprite):
    def __init__(self):
        super(Starstruck, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
    def blitme(self):
        self.screen.blitme(self.image, self.rect)
        print("Blit works")

def starborn(starstream, starnum, row_number, screen):
    star = Starstruck()
    star_width = star.rect.width
    star_height = star.rect.height
    star.rect.x = randint(1, (1200-star_width))
    star.rect.y = randint(1, (800-star_height))
    starstream.add(star) 

def star_numbers(star_width):
    star_space_avail = 1200 - 2 * star_width
    num_star = int(star_space_avail / (2 * star_width))
    return num_star

def starry_sky(starstream):
    star = Starstruck()
    num_stars = star_numbers(star.rect.width)
    num_rows = get_row_numbers(star.rect.height)
    for row_nums in range(num_rows):
        for star_nums in range(num_stars):
            starborn(starstream, star_nums, row_nums, screen)

def get_row_numbers(star_height):
    print ("Star Height is " + str(star_height))
    available_y_space = (800 - (2 * star_height))
    print ("Available Y space is " + str(available_y_space))
    num_rows = int(available_y_space / (2 * star_height))
    print ("The number of rows is " + str(num_rows))
    return num_rows

def update_screen(starstream):
    screen.fill((0, 0, 0))
    starstream.draw(screen)
    pygame.display.flip()

def stop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
            pygame.quit()
    

def nightsky():
    starstream = Group()
    starry_sky(starstream)
    while True:
        stop()
        update_screen(starstream)


nightsky()









