import pygame

screen = pygame.display.set_mode((1200, 800))

class Lamp():
	def __init__(self):
		super(Lamp, self).__init__()
		self.screen = screen

		self.image = pygame.image.load('images/PixarLamp.bmp')
		self.rect = self.image.get_rect
		self.screen_rect = screen.get_rect()
		self.rect = self.image.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the lamp's position based on the movement flag"""
		#Update lamp's center value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 1
		
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= 1
	
	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)


