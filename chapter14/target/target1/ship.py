import pygame

class Ship():

	def __init__(self, screen):
		self.screen = screen

		#import picture
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		#Initial position
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		#Movement flag
		self.move_up = False
		self.move_down = False

	def movement(self):
		if self.move_up and self.rect.top < self.screen_rect.top:
			self.rect.centery += 1
		if self.move_down and self.rect.bottom > self.screen_rect.bottom:
			self.rect.centery -= 1
	
	def blitship(self):
		self.screen.blit(self.rect, self.image)




