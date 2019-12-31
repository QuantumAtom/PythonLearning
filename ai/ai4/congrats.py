import pygame
from  pygame.locals import *
import time

class Congrats():

	def __init__(self, screen):
		self.screen = screen

	def text(self, screen):
		pygame.font.init()
		fontastic = pygame.font.SysFont('notosans', 50, bold=False, italic=False)
		rendersurf = fontastic.render("Congratulations battlestar! Get Ready!", False, (102, 51, 153))
		screen.blit(rendersurf,(200,400))
		pygame.display.update()
		print("Congratulations battlestar! But our planet is in another galaxy!")
		time.sleep(10)

