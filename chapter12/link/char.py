import pygame

class Char():

    def __init__(self, link_settings, screen):
        """Initialize the char and set it's starting position."""
        self.screen = screen
        self.link_settings = link_settings

        #Load the char image and get it's rect.

        self.image = pygame.image.load('images/link.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new char at the bottom center of the screen.

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        #Store a decimal value for the char's center.
        self.center = float(self.rect.centery)


        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the character's position based on the movement flag"""
        #Update the char's center value, not the rect.

        if self.moving_up and self.rect.top > 0:
            #print("It works moving up")
            self.center -= self.link_settings.char_speed_factor
        if self.moving_down and self.rect.bottom < 800:
            #print("It works moving down")
            self.center += self.link_settings.char_speed_factor
        
        #Update rect object from self.center
        self.rect.centery = self.center
    

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)