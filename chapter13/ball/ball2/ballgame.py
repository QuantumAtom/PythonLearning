import pygame
import sys
from sys import exit
from pygame import event

import random

from ball import Ball
from lamp import Lamp

ballcollect = pygame.sprite.Group()

#Assign sprite a value
ball = Ball()

#Assign sprite a value
lamp = Lamp()

def keydown_check(event, screen, ball, lamp):
	"""Respond to key presses"""
	if event.key == pygame.K_RIGHT:
		lamp.moving_right = True
	elif event.key == pygame.K_LEFT:
		lamp.moving_left = True
	elif event.key == pygame.K_q:
		sys.exit

def keyup_check(event, screen, ball, lamp):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		lamp.moving_right = False
	elif event.key == pygame.K_LEFT:
		lamp.moving_left = False

def key_check(event, screen, ball, lamp):
	"""Tying together all keyboard responses"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			keydown_check(event, screen, ball, lamp)
		elif event.type == pygame.KEYUP:
			keyup_check(event, screen, ball, lamp)

def update_screen(screen, ball, lamp):
	#Show on the screen
	screen.fill((135,206,250))
	lamp.blitme()
	ballcollect.draw(screen)
	ballgen(screen)
	ball.update()
	lamp.update()
	if (ball.rect.y > 800):
		print("Ball Collect worked")
		ballcollect.remove(ball)
		ballcollect.add(ball)
	pygame.display.flip()

def update_ball(screen, ball, lamp):
	collision = pygame.sprite.groupcollide(ball, lamp, True, False)

def ballgen(screen):
	if (ball.rect.y > 800):
		ball.blitme()

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Pixar ball!")
	ballcollect.add(ball)
	while True:
		key_check(event, screen, ball, lamp)
		if ball.ballamt == 0:
			break
		update_screen(screen, ball, lamp)

run_game()