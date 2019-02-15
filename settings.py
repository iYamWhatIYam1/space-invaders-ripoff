class Settings():
    #stores game settings, like screen resolution and ship speed

    def __init__(self):
        #initialize game's settings
        #screen resolution
        self.screen_width = 640
        self.screen_height = 560
        self.bgColor = (47, 47, 47)

        #bullet settings
        self.bullet_speed_factor = 0.75
        self.bullet_width = 8
        self.bullet_height = 16
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3

        #ship settings
        self.ship_speed_factor = 0.75
        self.shipsLeft = 2

        #alien speed settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        #fleet direction: 1 goes right, -1 goes left
        self.fleet_direction = 1