import pygame

class Link():
    def __init__(self, screen):
        """initialize Link's amazing adventure"""
        self.screen = screen

        self.pixel = pygame.image.load('images/link.bmp')
        self.rect = self.pixel.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.pixel, self.rect)