import pygame
from pygame.sprite import Sprite
import random

screen = pygame.display.set_mode((1200, 800))

class Ball(Sprite):
	def __init__(self):
		super(Ball, self).__init__()
		self.screen = screen

		self.image = pygame.image.load('images/PixarBall.bmp')
		self.rect = self.image.get_rect()

		self.rect.y = self.rect.height
		self.rect.x = self.rect.width

		self.x = random.randint(0, 800)
		self.rect.x = self.x

		self.y = 1

	def blitme(self):
		"""Draw the ball at it's current location."""
		self.screen.blit(self.image, self.rect)
		print(self.rect.y)
	
	def update(self):
		"""Move the ball down"""
		self.y = self.y + 1
		self.rect.y = self.y 
		#print("Screen is: " + str(pygame.surface.rect()))
		print("Object is: " + str(self.rect))
		if (self.rect.y >= 800):
			self.kill()
		#if not pygame.Surface.rect.contains(self.rect):
			#self.kill()


		



