import gameFunctions

class gameStats():
    #let's keep track of the game statistics!

    def __init__(self, gameSettings):
        #initialize statistics
        self.gameSettings = gameSettings
        self.resetStats()

    def resetStats(self):
        #initialize statistics that can change in-game
        self.shipsLeft = self.gameSettings.shipsLeft

        #start the game in an inactive state
        self.gameActive = False