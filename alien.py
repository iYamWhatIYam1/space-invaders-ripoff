import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #this class represents a single alien in a fleet
    def __init__(self, gameSettings, screen):
        #initialize alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.gameSettings = gameSettings

        #load alien png from images folder, set rect
        self.image = pygame.image.load('bitmap/alien.png')
        self.rect = self.image.get_rect()

        #start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blit(self):
        #draw alien at current location, always
        self.screen.blit(self.image, self.rect)

    def checkEdges(self):
        #return True if the aliens are at the edge of the screen
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        #move the alien right or left
        self.x += (self.gameSettings.alien_speed_factor * self.gameSettings.fleet_direction)
        self.rect.x = self.x