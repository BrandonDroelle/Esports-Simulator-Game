#team class
import playerClass

class TeamClass:
    def __init__(self, name):
        self.name = name
        self.p1 = playerClass.PlayerClass('rookie1')
        self.p1Name = 'rookie1'
        self.p2 = playerClass.PlayerClass('rookie2')
        self.p2Name = 'rookie2'
        self.p3 = playerClass.PlayerClass('rookie3')
        self.p3Name = 'rookie3'

    #Setters
    def setName(self, name):
        self.name = name

    def setP1(self, p1):
        self.p1 = p1
        #self.p1Name = p1.getName()

    def setP2(self, p2):
        self.p2 = p2
        #self.p2Name = p2.getName()

    def setP3(self, p3):
        self.p3 = p3
        #self.p3Name = p3.getName()

    #Getters
    def getTeamName(self):
        return self.name

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getP3(self):
        return self.p3

    #def getP1Name(self):
        #p1Name = self.p1.getName()
        #return p1Name

    #Print out team roster
    def printRoster(self):
        teamName = self.getTeamName()
        print("---", teamName.capitalize(), "---")
        print(self.p1.getName())
        print(self.p2.getName())
        print(self.p3.getName())

    #create roster string to go into save file
    def rosterString(self):
        p1n = self.p1.getName()
        p2n = self.p2.getName()
        p3n = self.p3.getName()
        statsStr = "\ngoals\n\nassists\n\nsaves\n\nshots\n\n"
        rosterStr = p1n + statsStr + p2n + statsStr + p3n + statsStr
        return rosterStr
        