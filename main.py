import sys, pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import gameFunctions as gf

def runGame():
    #runs the game and sets proper display resolution
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height) #imports screen resolution from settings.py
    )

    #draws the ship on the screen, bottom center
    ship = Ship(ai_settings, screen)

    #store bullets in a group
    bullets = Group()

    #main loop for the game
    while True:
        #window title
        pygame.display.set_caption("Space Invaders Ripoff") 

        #draw everything on screen constantly
        screen.fill(ai_settings.bgColor)
        ship.blitme()

        #updates the ship based on real-time occurences in-game
        gf.checkEvents(ai_settings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        #drawing the most recent screen refresh
        pygame.display.flip()

runGame()