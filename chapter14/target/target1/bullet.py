import pygame
from pygame.sprite import Sprite

class Bullet():

	def __init__(self, screen, ship):
		"""initiate the bullet sprite"""
		super(Bullet, self).__init__()
		self.screen = screen

		#Places everyone, places
		self.rect = pygame.Rect(0, 0, 3, 15)
		self.rect.centery = ship.rect.centery
		self.rect.top = ship.rect.top

		#Decimal and delightful colors!
		self.x = float(self.rect.x)
		self.color = 60, 60, 60
		
	def update(self):
		#almost faster than superman
		self.x =+ 5
		self.rect.x = self.x
	
	def draw_bullet(self):
		"""Animate"""
		pygame.draw.rect(self.screen, self.color, self.rect)
