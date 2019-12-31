import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class to manage bullets fired from the char"""
    def __init__(self, link_settings, screen, char):
        """Create a bullet object at the char's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, link_settings.bullet_width, link_settings.bullet_height)
        self.rect.centery = char.rect.centery
        self.rect.right = char.rect.right

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

        self.color = link_settings.bullet_color
        self.speed_factor = link_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.x -= self.speed_factor
        # Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        print(self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect) 