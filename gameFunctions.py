import sys, pygame
from bullet import Bullet
from alien import Alien

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
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

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

def updateScreen(gameSettings, screen, ship, aliens, bullets):
    #redraw the screen constantly
    screen.fill(gameSettings.bgColor)
    ship.blit()
    aliens.draw(screen)

    #draw bullets on-screen
    for bullet in bullets.sprites():
        bullet.drawBullet()
    
    ship.blit()

def updateBullets(aliens, bullets):
    #lets update our bullet positions and get rid of old ones
    bullets.update()
    #let's see if any bullets have hit any aliens. if so, delete them and kill the alien it hit
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    #lets trash bullets that are off-screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def getNumberAliens_X(gameSettings, alienWidth):
    #find number of aliens that fit in a row.
    availableSpaceX = gameSettings.screen_width - 2 * alienWidth
    #next line places the aliens in a row
    numberAliensX = int(availableSpaceX / (2 * alienWidth))
    return numberAliensX

def getNumberRows(gameSettings, shipHeight, alienHeight):
    #how many rows of aliens fit on the screen?
    availableSpaceY = (gameSettings.screen_height -
                        (3 * alienHeight) - shipHeight)
                        
    numberRows = int(availableSpaceY / (2 * alienHeight))
    return numberRows

def createAlien(gameSettings, screen, aliens, alienNumber, rowNumber):
    #create an alien and place it in the row
    alien = Alien(gameSettings, screen)
    alienWidth = alien.rect.width

    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)

def createFleet(gameSettings, screen, ship, aliens):
    #create a full fleet of aliens!
    alien = Alien(gameSettings, screen)
    numberAliensX = getNumberAliens_X(gameSettings, alien.rect.width)
    numberRows = getNumberRows(gameSettings, ship.rect.height, alien.rect.height)

    #let's make the first row of aliens!
    for rowNumber in range(numberRows):
        for alienNumber in range(numberAliensX):
            createAlien(gameSettings, screen, aliens, alienNumber, rowNumber)

def changeFleetDirection(gameSettings, aliens):
    #drop the fleet and change direction
    for alien in aliens.sprites():
        alien.rect.y += gameSettings.fleet_drop_speed
    gameSettings.fleet_direction *= -1

def checkFleetEdges(gameSettings, aliens):
    #respond appropriately if any aliens have hit the edges of the screen
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(gameSettings, aliens)
            break

def updateAliens(gameSettings, aliens):
    #check if the fleet is at the edge of the screen, then update their positions on screen
    checkFleetEdges(gameSettings, aliens)
    aliens.update()