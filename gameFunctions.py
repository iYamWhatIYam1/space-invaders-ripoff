import sys, pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #checks for key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    #lets make a bullet when space is pressed, and add it to the bullet group
    elif event.key == pygame.K_SPACE:
        newBullet = Bullet(ai_settings, screen, ship)
        bullets.add(newBullet)

def check_keyup_events(event, ship):
    #checks for key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def checkEvents(ai_settings, screen, ship, bullets):
    """this responds to keystrokes and mouse input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    #redraw the screen constantly
    screen.fill(ai_settings.bgColor)
    ship.blitme()

    #draw bullets on-screen
    for bullet in bullets.sprites():
        bullet.drawBullet()