import pygame

class Ship():
    def __init__(self, gameSettings, screen):
        """this is where the ship will start off at"""
        self.screen = screen
        self.gameSettings = gameSettings

        #import ship png and get its rect
        self.image = pygame.image.load('bitmap/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #each new ship starts at the bottom center so always put it there
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #decimal value for the center of the ship
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update the ship's position based onthe movement flag. update center values of the ship and NOT rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.gameSettings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.gameSettings.ship_speed_factor
        
        #update rect from self.center
        self.rect.centerx = self.center

    def blit(self):
        #draw ship at current location because duh?
        self.screen.blit(self.image, self.rect)