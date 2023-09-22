

#class PlayerClass:
#    def __init__(self, name):
#        self.name = name
        #self.goals = 0
        #self.assists = 0
        #self.saves = 0
        #self.shots = 0
        #self.wins = 0
        #self.losses = 0
        #self.team = "Free Agent"

    #Setters
    #def setName(self, name):
    #    self.name = name

    #def setGoals(self, goals):
    #    self.goals = goals

    #def setAssists(self, assists):
    #    self.assists = assists

    #def setSaves(self, saves):
    #    self.saves = saves

    #def setShots(self, shots):
    #    self.saves = shots

    #def setWins(self, wins):
    #    self.wins = wins

    #def setLosses(self, losses):
    #    self.losses = losses

    #def setTeam(self, team):
    #    self.team = team

    ##Getters
    #def getName(self, name):
    #    return self.name

    #def getGoals(self, goals):
    #    return self.goals

    #def getAssists(self, assists):
    #    return self.assists

    #def getSaves(self, saves):
    #    return self.saves

    #def getShots(self, shots):
    #    return self.shots

    #def getWins(self, wins):
    #    return self.wins

    #def getLosses(self, losses):
    #    return self.losses

    #def getTeam(self, team):
    #    return self.team

    #print("test")
    #testPlayerClassObject = PlayerClass("testPlayer")
    #print("created player object")

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

    #Getters
    def getName(self):
        return self.name

    def getCurrentTeam(self):
        return self.currentTeam

    def getGoalsCareer(self):
        return self.savesCareer

    def getSavesCareer(self):
        return self.savesCareer

    def getAssistsCareer(self):
        return self.assistsCareer

    def getShotsCareer(self):
        return self.shotsCareer

    def getGoalsSeason(self):
        return self.goalsSeason

    def getSavesSeason(self):
        return self.savesSeason

    def getAssistsSeason(self):
        return self.assistsSeason

    def getShotsSeason(self):
        return self.shotsSeason


