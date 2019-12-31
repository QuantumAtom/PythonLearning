import pygame
import sys
from sys import exit
from pygame import event

from rectangle import Rectangle
from ship import Ship


def keydown_check(event, screen, rct, ship, bullet):
	"""Press down. Here's what happens"""
	if event.key == pygame.K_up:
		ship.move_up = True
	elif event.key == pygame.K_down:
		ship.move_down = True
	elif event.key == pygame.K_q:
		sys.exit()
		pygame.quit()

def keyup_check(event, screen, rct, ship, bullet):
	"""Let up. Here's what happens"""
	if event.key == pygame.K_up:
		ship.move_up = False
	elif event.key == pygame.K_down:
		ship.move_down = False

def checkevent(event, screen, rct, ship, bullet):
	"""Hey, what happens when you input me hard"""
	for event in pygame.event.get():
		if event.type == pygame.quit():
			sys.exit
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			keydown_check(event, screen, rct, ship, bullet)
		elif event.type == pygame.KEYUP:
			keyup_check(event, screen, rct, ship, bullet)
			func.checkevent(ai_settings, screen, stats, play_button, ship, aliens, bullet)



def shotfire(event, screen, rct, ship):
	#Generate bullets and add to group
	if len(bullet) > 3:
		newshot = Bullet(screen, ship)
		pewpew.add(newshot)

def FleetEdgeCheck(rct):
	if rectangle.edgecheck():
		rectangle.direction *= -1

def rectgenerate(screen, rct):
	rct.rect.x = 1200
	rct.rect.y = 400
	rct.draw_rect()

def screenupdate(screen, rct, ship, bullet):
	"""Update screen images and fip to a new screen"""
	#Redraw screen for everytime the function loops
	screen.fill(230, 230, 230)
	#Redraw the bullets
	for bullets in bullets.sprite():
		bullets.draw_bullet()
	ship.blitme()
	#rectangle.draw(screen)

	#Make the screen visible
	pygame.display.flip()

def bulletupdate(screen, ship, rct, bullet):
	"""Update bullet's position and get rid of old bullets"""
	#Update bullet position
	bullet.update()
	#Get rid of bullets that are off the screen
	for bullets in pewpew.copy():
		if bullet.rect.right >=1200:
			pewpew.remove(bullet)

def ifbullethit(screen, rct, ship, bullet):
	bullethit = pygame.sprite.groupcollide(pewpew, targetgroup, True, True)
	if (len(targetgroup) == 0):
		pewpew.empty()
		rctgen(screen)

def rctgen(screen):
	rct = Rectangles(screen)
	targetgroup.add(rct)

def rctupdate(screen, target, ship, bullet):
	FleetEdgeCheck(rct)
	rct.rctmove()

