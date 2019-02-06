import sys, pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import gameFunctions as gf

def runGame():
    #runs the game and sets proper display resolution
    pygame.init()
    gameSettings = Settings()
    screen = pygame.display.set_mode(
        (gameSettings.screen_width, gameSettings.screen_height) #imports screen resolution from settings.py
    )

    #draws the ship on the screen, bottom center
    ship = Ship(gameSettings, screen)

    #store bullets in a group
    bullets = Group()

    #main loop for the game
    while True:
        #window title
        pygame.display.set_caption("Space Invaders Ripoff") 

        #draw everything on screen constantly
        screen.fill(gameSettings.bgColor)
        ship.blit()

        #updates the ship based on real-time occurences in-game
        gf.checkEvents(gameSettings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateScreen(gameSettings, screen, ship, bullets)

        #drawing the most recent screen refresh
        pygame.display.flip()

runGame()