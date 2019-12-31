import pygame
import sys
from sys import exit
from pygame import event

from rectangle import Rectangle
from ship import Ship
from bullet import Bullet

import gamefunc as func

def execute():
	#Initialize Pygame library and set a caption for the game window
	pygame.init()
	pygame.display.set_caption("Practice shots")

	screen = pygame.display.set_mode((1200, 800))

	targetgroup = pygame.sprite.Group()

	#Assign target sprite a value
	rct = Rectangle(screen)

	#Assign ship sprite a value
	ship = Ship(screen)

	#Assign bullets sprite a value
	bullet = Bullet(screen, ship)
	#assign a group for bullets
	pewpew = pygame.sprite.Group()
	
	#generate rectangle to practice shooting
	func.rectgenerate(screen, rct)
	
	#Set background color
	backcolor = (135, 206, 250)

	#Main loop for game
	while True:
		#Event happenings
		func.checkevent(event, screen, rct, ship, bullet)

		ship.movement()
		func.bulletupdate(screen, ship, rct, bullet)
		func.rctupdate(screen, target, ship, bullet)
		func.screenupdate(screen, rct, ship, bullet)

execute()

