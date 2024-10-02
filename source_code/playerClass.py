
class PlayerClass:
    def __init__(self, name):

    #Attributes
        self.name = name
        self.currentTeam = "none"
        self.goalsCareer = 0
        self.assistsCareer = 0
        self.savesCareer = 0
        self.shotsCareer = 0
        self.goalsSeason = 0
        self.assistsSeason = 0
        self.savesSeason = 0
        self.shotsSeason = 0
        self.goalsWeek = 0
        self.assistsWeek = 0
        self.savesWeek = 0
        self.shotsWeek = 0

    #Methods
    #Setters
    def setName(self, name):
        self.name = name

    def setTeam(self, currentTeam):
        self.currentTeam = currentTeam

    def setGoalsCareer(self, goalsCareer):
        self.goalsCareer = goalsCareer

    def setAssistsCareer(self, assistsCareer):
        self.assistsCareer = assistsCareer

    def setSavesCareer(self, savesCareer):
        self.savesCareer = savesCareer

    def setShotsCareer(self, shotsCareer):
        self.shotsCareer = shotsCareer

    def setGoalsSeason(self, goalsSeason):
        self.goalsSeason = goalsSeason

    def setAssistsSeason(self, assistsSeason):
        self.assistsSeason = assistsSeason

    def setSavesSeason(self, savesSeason):
        self.savesSeason = savesSeason

    def setShotsSeason(self, shotsSeason):
        self.shotsSeason = shotsSeason

    def setGoalsWeek(self, goalsWeek):
        self.goalsWeek = goalsWeek

    def setAssistsWeek(self, assistsWeek):
        self.assistsWeek = assistsWeek

    def setSavesWeek(self, savesWeek):
        self.savesWeek = savesWeek

    def setShotsWeek(self, shotsWeek):
        self.shotsWeek = shotsWeek

    #Getters
    def getName(self):
        return self.name

    def getCurrentTeam(self):
        return self.currentTeam

    def getGoalsCareer(self):
        return self.goalsCareer

    def getAssistsCareer(self):
        return self.assistsCareer

    def getSavesCareer(self):
        return self.savesCareer

    def getShotsCareer(self):
        return self.shotsCareer

    def getGoalsSeason(self):
        return self.goalsSeason

    def getAssistsSeason(self):
        return self.assistsSeason

    def getSavesSeason(self):
        return self.savesSeason

    def getShotsSeason(self):
        return self.shotsSeason
    
    def getGoalsWeek(self):
        return self.goalsWeek

    def getAssistsWeek(self):
        return self.assistsWeek

    def getSavesWeek(self):
        return self.savesWeek

    def getShotsWeek(self):
        return self.shotsWeek
    
    #def getFileString(self, gameState):
        #fileString = self.getName + " " + self.get

    #Adders
    def addGoals(self, goals):
        self.goalsWeek = goals
        self.goalsSeason = self.goalsSeason + goals
        self.goalsCareer = self.goalsCareer + goals
        
    def addAssists(self, assists):
        self.assistsWeek = assists
        self.assistsSeason = self.assistsSeason + assists
        self.assistsCareer = self.assistsCareer + assists
        
    def addSaves(self, saves):
        self.savesWeek = saves
        self.savesSeason = self.savesSeason + saves
        self.savesCareer = self.savesCareer + saves
        
    def addShots(self, shots):
        self.shotsWeek = shots
        self.shotsSeason = self.shotsSeason + shots
        self.shotsCareer = self.shotsCareer + shots
        


