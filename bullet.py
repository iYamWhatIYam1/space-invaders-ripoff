import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """this class manages bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        #bullet object at the ship's current spot on screen
        super(Bullet, self).__init__()
        self.screen = screen

        #create bullet rect at (0, 0), then set the correct position (top of ship)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #bullet position is a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #update bullets position. start with decimal position and move up
        self.y -= self.speed_factor
        #update rect position
        self.rect.y = self.y

    def drawBullet(self):
        #draw bullet on screen constantly
        pygame.draw.rect(self.screen, self.color, self.rect)