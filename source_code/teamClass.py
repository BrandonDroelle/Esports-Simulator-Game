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
        self.WLSeason = ""

    #Setters
    def setName(self, name):
        self.name = name

    def setP1(self, p1):
        self.p1 = p1

    def setP2(self, p2):
        self.p2 = p2

    def setP3(self, p3):
        self.p3 = p3

    def setWinsCareer(self, winsCareer):
        self.winsCareer = winsCareer

    def setLossesCareer(self, lossesCareer):
        self.lossesCareer = lossesCareer

    def setWLSeason(self, WLSeason):
        self.WLSeason = WLSeason

    #Getters
    def getTeamName(self):
        return self.name

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getP3(self):
        return self.p3

    def getWinsCareer(self):
        return self.winsCareer

    def getLossesCareer(self):
        return self.lossesCareer

    def getWLSeason(self):
        return self.WLSeason

    def getWinsSeason(self):
        WL = self.WLSeason
        statList = WL.split(" ")
        W = 0
        for i in range(len(statList)):
            if statList[i] == 1:
                w = w + 1
        return W

    def getLossesSeason(self):
        WL = self.WLSeason
        statList = WL.split(" ")
        L = 0
        for i in range(len(statList)):
            if statList[i] == 0:
                w = w + 1
        return L

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
        