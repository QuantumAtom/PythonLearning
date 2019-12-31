import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

screen = pygame.display.set_mode((1200, 800))

rainfall = pygame.sprite.Group()

class Droplet(Sprite):
	def __init__(self):
		super(Droplet, self).__init__(rainfall)
		self.screen = screen
		self.screen_rect = screen.get_rect
		self.image = pygame.image.load('images/Glossy_Raindrop.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def update(self):
		self.rect = self.rect.move(0, 1)
		screenie = screen.get_rect()
		if not screenie.contains(self.rect):
			self.kill()
	
def dripdrip(rainfall, dropnum, screen, row_num):
	drop = Droplet()
	drop_width = drop.rect.width
	drop.x = drop_width + 2 * drop_width * dropnum
	drop.rect.x = drop.x
	drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_num
	rainfall.add(drop)

def rain_num(drop_width):
	rain_space_avail = 1200 - 2 * drop_width
	rain_num = int(rain_space_avail / (2 * drop_width))
	#print(rain_num)
	return rain_num

def rainstorm(Droplet, rain_num):
	drop = Droplet()
	drop_num = rain_num(drop.rect.width)
	num_rows = get_row_num(drop.rect.height)
	for row_num in range(drop_num):
		for rain_num in range(drop_num):
			dripdrip(Droplet, rain_num, screen, row_num)

def get_row_num(drop_height):
	avail_y_space = (800 -(2 * drop_height))
	num_rows = int(avail_y_space / (2 * drop_height))
	return num_rows
  
def rain_y_move(drop, rainfall):
	for raindrop in rainfall:
		raindrop.rect.y += 1
		#print(raindrop.rect.y)
	
def update_screen(rainfall):
	#print("Before: " + (str(len(rainfall))))
	screen.fill((135, 206, 235))
	rainamt  = dropcount()
	rainfall.update()
	rainfall.draw(screen)
	pygame.display.flip()
	#print("After: " + (str(len(rainfall))))
	dropground(rainamt)
drop = Droplet()

def dropcount():
	raincount = len(rainfall.sprites())
	print("raincount: " + str(raincount))
	return raincount

def dropground(rainamt):
	#rainamt = dropcount()
	#print("rainamt: " + str(rainamt))
	print("Current rainfall: " + str(len(rainfall)))
	if (rainamt != len(rainfall)):
		print("IT WORKS!")
		dropmorerows(rain_num)
	else:
		print("This does not work")

def stop():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit
			pygame.quit()

def dropmorerows(rain_num):
	drop_num = rain_num(drop.rect.width)
	num_rows = get_row_num(drop.rect.height)
	for rain_num in range(drop_num):
		dripdrip1(Droplet, rain_num, screen, num_rows)

def dripdrip1(rainfall, dropnum, screen, row_num):
	drop = Droplet()
	drop_width = drop.rect.width
	drop.x = drop_width + 2 * drop_width * dropnum
	drop.rect.x = drop.x
	drop.rect.y = drop.rect.height
	rainfall.add(drop)

def rainyday():
	rainstorm(Droplet, rain_num)
	drop = Droplet()
	while True:
		stop()
		update_screen(rainfall)

rainyday()

