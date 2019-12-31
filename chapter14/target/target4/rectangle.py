import pygame
import random

class Rectangle():

	def __init__(self, screen):
		"""Intialize the class attributes"""
		super(Rectangle, self).__init__()
		self.screen = screen.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Set the size of the rectangle
		self.width = 50
		self.height = 200
		a = random.randint(0, 255)
		b = random.randint(0, 255)
		c = random.randint(0, 255)
		self.rect_color = (a, b, c)

		#Build the surface
		self.gamesurface = pygame.Surface((1200, 800))
		#Build the rect object and start it from the top
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		#self.rect.TopRight = self.screen_rect.topright()

		#Misc Definitions

		#Increasing the number moves rct down, decreasing the number moves it up
		self.direction = 1 

	def edgecheck(self):
		"""Returns true if rectangle reaches the edge of the screen"""
		#screen_rect = self.screen.get_rect()
		#Check if rectangle hits a wall
		if self.rect.top >= 0:
			return True
		elif self.rect.bottom >= self.screen.rect.bottom:
			return True
	
	def rctmove(self):
		self.rect.y =+ 1

	def draw_rect(self):
		#Make it so!
		rctsurface = pygame.Surface((self.width, self.height))
		rctsurface.fill(self.rect_color)
		