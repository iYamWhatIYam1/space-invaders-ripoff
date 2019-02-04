import sys, pygame

def check_keydown_events(event, ship):
    #checks for key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    #checks for key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def checkEvents(ship):
    """this responds to keystrokes and mouse input lol"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    #redraw the screen constantly
    screen.fill(ai_settings.bgColor)
    ship.blitme()

    #make most recently drawn frame visible
    pygame.display.flip