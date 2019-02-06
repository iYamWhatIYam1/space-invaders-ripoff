import sys, pygame
from bullet import Bullet

def fireBullet(gameSettings, screen, ship, bullets):
        #lets make a bullet when space is pressed, and add it to the bullet group
        if len(bullets) < gameSettings.bullets_allowed:
            newBullet = Bullet(gameSettings, screen, ship)
            bullets.add(newBullet)

def checkKeydownEvents(event, gameSettings, screen, ship, bullets):
    #checks for key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fireBullet(gameSettings, screen, ship, bullets)

def checkKeyupEvents(event, ship):
    #checks for key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def checkEvents(gameSettings, screen, ship, bullets):
    #this responds to keystrokes and mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, gameSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)

def updateScreen(gameSettings, screen, ship, bullets):
    #redraw the screen constantly
    screen.fill(gameSettings.bgColor)
    ship.blit()

    #draw bullets on-screen
    for bullet in bullets.sprites():
        bullet.drawBullet()

def updateBullets(bullets):
    #lets update our bullet positions
    bullets.update()

    #lets trash bullets that are off-screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)