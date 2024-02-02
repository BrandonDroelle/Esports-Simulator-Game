#team class
import playerClass

class TeamClass:
    def __init__(self, name):
        self.name = name
        self.p1 = playerClass.PlayerClass('rookie1')
        self.p2 = playerClass.PlayerClass('rookie2')
        self.p3 = playerClass.PlayerClass('rookie3')
        
        self.winsCareer = 0
        self.lossesCareer = 0
        self.goalsCareer = 0
        self.assistsCareer = 0
        self.savesCareer = 0
        self.shotsCareer = 0

        self.goalsSeason = 0
        self.assistsSeason = 0
        self.savesSeason = 0
        self.shotsSeason = 0

        self.WLSeason = "\n"          #string of 1's and 0's with dash in between
                                     #1's = wins 0's = losses
        

    #Setters
    def setName(self, name):
        self.name = name

    def setP1(self, p1):
        self.p1 = p1

    def setP2(self, p2):
        self.p2 = p2

    def setP3(self, p3):
        self.p3 = p3

    def setWLSeason(self, WLSeason):
        self.WLSeason = WLSeason

    def setWinsCareer(self, winsCareer):
        self.winsCareer = winsCareer

    def setLossesCareer(self, lossesCareer):
        self.lossesCareer = lossesCareer

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
    def getTeamName(self):
        return self.name

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getP3(self):
        return self.p3

    def getWLSeason(self):
        return self.WLSeason

    def getWLRCareer(self):
        W = self.getWinsCareer()
        L = self.getLossesCareer()
        W = int(W)
        L = int(L)
        if (W + L) == 0:
            return 0.0
        WLR = (W/(W+L))
        WLR = "{:.3f}".format(WLR)
        return WLR

    def getWLRSeason(self):
        W = self.getWinsSeason()
        L = self.getLossesSeason()
        W = int(W)
        L = int(L)
        if (W + L) == 0:
            return "0:0"
        WLR = (W/(W+L))
        WLR = "{:.3f}".format(WLR)
        return WLR

    def getWinsCareer(self):
        winsCareer = self.winsCareer
        winsSeason = self.getWinsSeason()
        return winsCareer + winsSeason

    def getLossesCareer(self):
        lossesCareer = self.lossesCareer
        lossesSeason = self.getLossesSeason()
        return lossesCareer + lossesSeason

    def getWinsSeason(self):
        WL = self.WLSeason
        statList = WL.split("-")
        w = 0
        for i in range(len(statList)):
            if statList[i] == '1':
                w = w + 1
        return w

    def getLossesSeason(self):
        WL = self.WLSeason
        statList = WL.split("-")
        l = 0
        for i in range(len(statList)):
            if statList[i] == '0':
                l = l + 1
        return l

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

    def getCacheString(self):
        fileString = (self.name + " " + str(self.winsCareer) + " " + 
                           str(self.lossesCareer) + " " + str(self.goalsCareer) + " " +
                           str(self.assistsCareer) + " " + str(self.savesCareer) + " " +
                           str(self.shotsCareer) + " " + str(self.goalsSeason) + " " +
                           str(self.assistsSeason) + " " + str(self.savesSeason) + " " +
                           str(self.shotsSeason) + " " + self.WLSeason)
        return fileString      
    
    #updaters
    def updateGoals(self):
        self.goalsSeason = self.goalsSeason + self.p1.getGoalsSeason() + self.p2.getGoalsSeason() + self.p3.getGoalsSeason()
        self.goalsCareer = self.goalsCareer + self.p1.getGoalsSeason() + self.p2.getGoalsSeason() + self.p3.getGoalsSeason()
        
    def updateAssists(self):
        self.assistsSeason = self.assistsSeason + self.p1.getAssistsSeason() + self.p2.getAssistsSeason() + self.p3.getAssistsSeason()
        self.assistsCareer = self.assistsCareer + self.p1.getAssistsSeason() + self.p2.getAssistsSeason() + self.p3.getAssistsSeason()
        
    def updateSaves(self):
        self.savesSeason = self.savesSeason + self.p1.getSavesSeason() + self.p2.getSavesSeason() + self.p3.getSavesSeason()
        self.savesCareer = self.savesCareer + self.p1.getSavesSeason() + self.p2.getSavesSeason() + self.p3.getSavesSeason()
        
    def updateShots(self):
        self.shotsSeason = self.shotsSeason + self.p1.getShotsSeason() + self.p2.getShotsSeason() + self.p3.getShotsSeason()
        self.shotsCareer = self.shotsCareer + self.p1.getShotsSeason() + self.p2.getShotsSeason() + self.p3.getShotsSeason()
        
    def updateWLR(self, result):
        self.WLSeason = result + self.WLSeason
        if result == "1":
            self.setWinsCareer(self.winsCareer + 1)
        else:
            self.setLossesCareer(self.lossesCareer + 1)

    #Print out team roster
    def printRoster(self):
        teamName = self.getTeamName()
        print("---", teamName.capitalize(), "---")
        print(self.p1.getName())
        print(self.p2.getName())
        print(self.p3.getName())

    #create roster string to go into save file
    def getRosterString(self):
        p1n = self.p1.getName()
        p2n = self.p2.getName()
        p3n = self.p3.getName()
        statsStr = "\ngoals\n0\nassists\n0\nsaves\n0\nshots\n0\n"
        rosterStr = p1n + statsStr + p2n + statsStr + p3n + "\ngoals\n0\nassists\n0\nsaves\n0\nshots\n0"
        return rosterStr
        