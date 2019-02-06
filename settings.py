class Settings():
    #stores game settings, like screen resolution and ship speed

    def __init__(self):
        #initialize game's settings
        #screen resolution
        self.screen_width = 640
        self.screen_height = 480
        self.bgColor = (47, 47, 47)

        #bullet settings
        self.bullet_speed_factor = 0.75
        self.bullet_width = 8
        self.bullet_height = 16
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3

        #ship's speed
        self.ship_speed_factor = 0.75