import sys
import pygame
from pygame import event

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

ballmiss = 0
ballcatch = 0