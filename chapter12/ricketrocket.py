import pygame

class Rocketeer:

        def __init__(self, screen):
                """Initialize the screen"""
                self.screen = pygame.display.set_mode((1200, 800))

                """initialize rocket"""
                self.image = pygame.image.load('images/rocketship.bmp')
                self.imgrect = self.image.get_rect()
                self.rectscreen = screen.get_rect()

                """Where it's at!"""
                self.imgrect.centerx = self.rectscreen.centerx
                self.imgrect.centery = self.rectscreen.centery

                """Moving flags!!!"""
                self.MoveLeft = False
                self.MoveRight = False
                self.BullUp = False
                self.BearDown = False

        def keydown(self, event):
                """Key press response"""
                if event.key == pygame.K_LEFT:
                        self.MoveLeft = True
                elif event.key == pygame.K_RIGHT:
                        self.MoveRight = True
                elif event.key == pygame.K_UP:
                        self.BullUp = True
                elif event.key == pygame.K_DOWN:
                        self.BearDown = True
        
        def keyup(self, event):
                """Key letting up"""
                if event.key == pygame.K_LEFT:
                        self.MoveLeft = False
                elif event.key == pygame.K_RIGHT:
                        self.MoveRight = False
                elif event.key == pygame.K_UP:
                        self.BullUp = False
                elif event.key == pygame.K_DOWN:
                        self.BearDown = False


        def MoveMe(self):
                """Move like a chess queen"""
                if self.MoveRight and self.imgrect < self.rectscreen.right:
                        self.imgrect.x += 1
                if self.MoveLeft and self.imgrect < 0:
                        self.imgrect.x -= 1
                if self.BullUp and self.imgrect < self.rectscreen.up:
                        self.imgrect.y += 1
                if self.BearDown and self.imgrect < self.rectscreen.down:
                        self.imgrect.y -= 1

        def blitme(self):
                """Draw the ship at its current location."""
                self.screen.blit(self.imgrect, self.rectscreen)

