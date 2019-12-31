import pygame
import random

class Rectangle():

	def __init__(self, screen):
		"""Intialize the class attributes"""
		super(Rectangle, self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#Set the size of the rectangle
		self.width = 50
		self.height = 200
		self.a = random.randint(0, 255)
		self.b = random.randint(0, 255)
		self.c = random.randint(0, 255)
		self.rect_color = (self.a, self.b, self.c)

		#Build the surface
		self.gamesurface = pygame.Surface((1200, 800))
		#Build the rect object and start it from the top
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		
		#self.rect.TopRight = self.screen_rect.topright()

		#Misc Definitions
		self.vert = random.randint(0, 800)
		self.pos = (1200, self.vert)
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
		self.rctsurface = pygame.Surface((self.width, self.height))
		self.rctsurface.fill(self.rect_color)
		print(self.rctsurface)
		self.screen.blit(self.rctsurface, self.pos)