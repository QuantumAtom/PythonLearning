import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class to manage bullets fired from the ship"""
    def __init__(self, link_settings, screen, link):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, link_settings.bullet_width, link_settings.bullet_height)
        self.rect.centery = link.rect.centery
        self.rect.right = link.rect.right

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

        self.color = link_settings.bullet_color
        self.speed_factor = link_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.rect.x += self.speed_factor
        #print(self.rect)
        # Update the rect position
        self.rect.x = self.rect.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)        