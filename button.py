import pygame.font

class Button():
    def __init__(self, gameSettings, screen, message):
        #initialize button attributes
        self.screen = screen
        self.screenRect = screen.get_rect()

        #set dimensions and properties of button
        self.width, self.height = 160, 70
        self.buttonColor = (57, 102, 56)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)

        #build the button's rect, then center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center

        #the button only needs to be prepped once
        self.prepMessage(message)
    
    def prepMessage(self, message):
        #turn the message into a rendered image, and center text on the button
        self.messageImage = self.font.render(message, True, self.textColor, self.buttonColor)
        self.messageImageRect = self.messageImage.get_rect()
        self.messageImageRect.center = self.rect.center
    
    def drawButton(self):
        #draw blank button and then the message
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.messageImage, self.messageImageRect)