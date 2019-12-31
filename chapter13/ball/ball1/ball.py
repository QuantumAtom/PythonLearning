import pygame
from pygame.sprite import Sprite
import random
from lamp import Lamp

screen = pygame.display.set_mode((1200, 800))

lamp = Lamp()

class Ball(Sprite):
	def __init__(self):
		super(Ball, self).__init__()
		self.screen = screen

		self.image = pygame.image.load('images/PixarBall.bmp')
		self.rect = self.image.get_rect()

		self.rect.y = self.rect.height
		self.rect.x = self.rect.width

		self.x = random.randint(0, 1200)
		self.rect.x = self.x

		self.rect.y = 1

	def blitme(self):
		"""Draw the ball at it's current location."""
		self.screen.blit(self.image, self.rect)
		print(self.rect.y)
	
	def update(self):
		"""Move the ball down"""
		self.rect.y = self.rect.y + 1 
		#print("Screen is: " + str(pygame.surface.rect()))
		print("Object is: " + str(self.rect.y))
		if not pygame.display.get_surface().get_rect().contains(self.rect) or self.rect.colliderect(lamp.rect):
			if self.rect.colliderect(lamp.rect):
				print("Ball hit")
			self.rect.y = 1
			self.rect.x = random.randint(0, 1200)