import sys, pygame
from settings import Settings
from ship import Ship
import gameFunctions as gf

def runGame():
    #this is basically running the actual game lmao.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height) #imports screen shit from settings.py
    )

    #wheres the goddamn ship???????1
    ship = Ship(ai_settings, screen)

    #YES
    while True:
        #window title
        pygame.display.set_caption("Space Invaders Ripoff")

        #draw everything on screen constantly
        screen.fill(ai_settings.bgColor)
        ship.blitme()

        #idk
        gf.checkEvents(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        #drawing the most recent screen refresh
        pygame.display.flip()

runGame()