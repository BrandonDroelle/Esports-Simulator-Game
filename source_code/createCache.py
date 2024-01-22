from math import gamma
from sqlite3 import TimestampFromTicks
import playerClass
import saveGame
import saveData
import teamClass
import generateSchedule

def loadSchedule(gameState):
    schedule = 'empty schedule'
    currentSeason = saveGame.getSeason(gameState)
    currentSeason = "Season " + str(currentSeason) + "\n"
    extraRows = 0

    schedule = saveData.read(gameState, currentSeason, 1, "RLCS Save Data\n", extraRows)
    return schedule


#creates list of player objects from list of default player name strings when creating a new save
def createPlayerObjects(gameState, playerNames):
    #add user to list of players
    userName = saveGame.getPlayerName(gameState)
    #print("userName:", userName)
    #check is username is already on list so it doesn't get added multiple times
    print("players:", playerNames)
    l = len(playerNames)
    nameOnList = False
    for i in range(l):
        if userName == playerNames[i]:
            nameOnList = True
            break

    if nameOnList == False:
        playerNames.append(userName)
        l = len(playerNames)

    print("User Name On List: ", nameOnList)
    print("players:", playerNames)
    print("len:", l)

    #create list of player objects
    players = []
    for i in range(l):
        #print("i:", i)
        playerTemp = playerClass.PlayerClass(playerNames[i]) #creates player object with name from list
        players.append(playerTemp)                           #add player object to list of player objects
        name = players[i].getName()
        #print("Player Name:", name)
    print("Player Objects: ", players)
    return players

#remove player from playerNames list
def rmvPlayerName (gameState, playerNames):
    print("In remove player names")
    print("PlayerNames: ", playerNames)
    userName = saveGame.getPlayerName(gameState)
    playerNames.remove(userName)
    print("PlayerNames: ", playerNames)
    return playerNames


#Load player data from save file to cache
def loadPlayerObjects(gameState):
    print("In loadPlayerObjects")
    extraRows = -1
    statList = []
    statIndex = 0
    end = False
    
    while end == False:
        extraRows = extraRows + 1 #determines how many rows will be skipped when after reading playerObjects in save file
        playerStats = saveData.read(gameState, "player objects\n", 1, "RLCS Save Data\n", extraRows)
        print("stats: ", playerStats)
        print("extra rows: ", extraRows)
        #split the data string into a list
        statList = playerStats.split(" ")
        print("stats list: ", statList)

        #check if there is player data 
        if playerStats == "\n":
            end = True
            break

        #create player object, and set all attributes
        i = playerClass.PlayerClass(statList[0])
        i.setTeam(statList[1])
        i.setGoalsCareer(int(statList[2]))
        i.setAssistsCareer(int(statList[3]))
        i.setSavesCareer(int(statList[4]))
        i.setShotsCareer(int(statList[5]))
        i.setGoalsSeason(int(statList[6]))
        i.setAssistsSeason(int(statList[7]))
        i.setSavesSeason(int(statList[8]))
        i.setShotsSeason(int(statList[9]))

        #add player object to list of player objects
        gameState[2].append(i)

    print("Leave loadPlayerObjects")
    return gameState[2]

def addPlayerGoalsToObject(gameState, playerObjects):
    print("In addPlayerGoalsToObject")
    currentSeason = "Season " + saveGame.getSeason(gameState) + "\n"
    numWeeksPerSeason = 21
    extraRows = 1
    seasonGoals = 0

    for i in range(len(playerObjects)):
        for j in range(numWeeksPerSeason):
            currentWeek = j + 1
            print("playName: ", playerObjects[i].getName() + "\n")
            print("current week: ", currentWeek)
            print("current season: ", currentSeason)
            print("extraRows: ", extraRows)
            gameGoals = saveData.read(gameState, playerObjects[i].getName() + "\n", currentWeek, currentSeason, extraRows)
            gameGoals = int(gameGoals)
            seasonGoals = seasonGoals + gameGoals
            print("gameGoals: ", gameGoals)
            print("seasonGoals: ", seasonGoals)
            print("done")
            #seasonGoals = 



    print("Leave addPlayerGoalsToObject")
    return playerObjects

#creates list of team objects from list of default team name strings when creating a new save
def createTeamObjects(teamNames):
    
    l = len(teamNames)
    #print("len:", l)

    #create list of team objects
    teams = []
    for i in range(l):
        #print("i:", i)
        teamTemp = teamClass.TeamClass(teamNames[i])    #creates team object with name from teamNames list
        teams.append(teamTemp)                          #adds new team to list of team objects
        #name = teams[i].getTeamName()
        #print("Team Name:", name)
    #print("Team Objects: ", teams)
    return teams

#Load team data cache from player objects
def loadTeamObjects(gameState):
    print("In load team objects")

    #CREATE TEAM OBJECTS AND ADD PLAYERS TO THEM
    count = 0
    teamNames = []
    teamName = ""

    for i in gameState[2]:
        teamName = i.getCurrentTeam()
        #check if team name is on list of teams
        #if the team name is not on the list then add it
        #and create a new teamClass object

        #set add team to true
        addTeam = True

        #check if teamNames list is empty. If it is create a teamobject with that player and add the object to gameState
        #if len(teamNames) == 0:
            #addTeam = True

        for j in teamNames:
            if teamName == j:         #check if teamName is on list of team names
                addTeam = False
                for x in range (len(gameState[3])):
                    permTeamName = gameState[3][x].getTeamName()
                    if permTeamName == teamName:            #x is the index for the team to add this player to
                        p2Object = gameState[3][x].getP2()    #get the P2 object from the current team
                        p2Name = p2Object.getName()         #get the name for P2
                        if p2Name == 'rookie2':             #there is no player 2 for this team
                            gameState[3][x].setP2(i)  #set current player to P2 for their team
                        else:
                            gameState[3][x].setP3(i)  #set current player to P3 for their team

        if addTeam == True:
            #add team name to list of team names
            teamNames.append(teamName)
            #create team object from the new team name
            tempTeam = teamClass.TeamClass(teamName)
            #set P1 on the new team with the current player
            tempTeam.setP1(i)
            #add new team object to list
            gameState[3].append(tempTeam)

    #ADD TEAM STATS FROM SAVE FILE TO TEAM OBJECTS
    extraRows = -1
    statList = []
    
    for i in gameState[3]:
        extraRows = extraRows + 1 #determines how many rows will be skipped after reading playerObjects in save file
        teamStats = saveData.read(gameState, "team objects\n", 1, "RLCS Save Data\n", extraRows)
        print("stats: ", teamStats)
        print("extra rows: ", extraRows)
        #split the data string into a list
        statList = teamStats.split(" ")

        #create a new string without the first three items in statList to make the WLSeason
        WLSeason = ""
        num = ""
        for x in range(len(statList)):
            print("stat: ", statList[x])
            if x > 10:
                if statList[x] != "\n":
                    num = statList[x]
                    WLSeason = WLSeason + (num) + " "

        #create player object, and set all attributes
        i.setWinsCareer(int(statList[1]))
        i.setLossesCareer(int(statList[2]))
        i.setGoalsCareer(int(statList[3]))
        i.setAssistsCareer(int(statList[4]))
        i.setSavesCareer(int(statList[5]))
        i.setShotsCareer(int(statList[6]))
        i.setGoalsSeason(int(statList[7]))
        i.setAssistsSeason(int(statList[8]))
        i.setSavesSeason(int(statList[9]))
        i.setShotsSeason(int(statList[10]))
        i.setWLSeason(WLSeason)
        

                
    print("leave load team objects")
    return gameState[3]
        



#load saved data from file to cache for each player
#def loadPlayerObjectData(gameState, playerNames):
#    #create player objects
#    playerObjects = createPlayerObjects(gameState, playerNames) #here is when the player name is added to the list of player names

#    l = len(playerNames)
#    for i in range(l):
#        playerObjects[i]

#Sets the player objects teamName to the teamName of the team object
def updatePlayersTeam(teamObject, playerObject):
    teamName = teamObject.getTeamName()
    playerObject.setTeam(teamName)
    return playerObject
#Returns the player object with the updated teamName attribute
    

#randomly fill each team with three players
def fillTeamRosters(gameState):

    #Randomly assigns 3 players from playerObjects to each teamObject
    playerObjects = gameState[2]
    teamObjects = gameState[3]
    #playersShuffle = playerObjects.copy() #makes a copy of the playerObject list so the playerObject list stays in the original order
    playersShuffle = generateSchedule.randomizeList(playerObjects)
    tcount = 0 #plus one every loop to change team
    pcount = 0 #plus one every assignment to change player
    #pcount = len(playersShuffle)
    #print("Number of Players:", len(playersShuffle))
    #print("Number of teams:", len(teamObjects))
    #randomly assigns three players to each team
    c = 0
    for i in playerObjects:
        n = playerObjects[c].getName()
        #print("players", n)
        c = c + 1

    print("playerShuffleLen: ", len(playersShuffle))

    while pcount < len(playersShuffle):
        print("pcount: ", pcount)
        teamObjects[tcount].setP1(playersShuffle[pcount])   #adds random player object to P1 on current team
        playersShuffle[pcount] = updatePlayersTeam(teamObjects[tcount], playersShuffle[pcount]) #updates player object with new team name
        pcount = pcount + 1
        teamObjects[tcount].setP2(playersShuffle[pcount])   #adds random player object to P2 on current team
        playersShuffle[pcount] = updatePlayersTeam(teamObjects[tcount], playersShuffle[pcount]) #updates player object with new team name
        pcount = pcount + 1
        teamObjects[tcount].setP3(playersShuffle[pcount])   #adds random player object to P3 on current team
        playersShuffle[pcount] = updatePlayersTeam(teamObjects[tcount], playersShuffle[pcount]) #updates player object with new team name
        pcount = pcount + 1
        tcount = tcount + 1

    #for i in pcount:
    #    teamObjects[tcount].setP1(playersShuffle[pcount])
    #    teamObjects[tcount].setP2(playersShuffle[pcount])
    #    teamObjects[tcount].setP3(playersShuffle[pcount])
    #    tcount = tcount + 1

    count = 0
    for i in teamObjects:
        teamObjects[count].printRoster()
        count = count + 1

    #update gameState with updated team and player objects
    gameState[2] = playersShuffle
    gameState[3] = teamObjects

    return gameState

#finds the users player index
def getUserPLayerIndex(gameState, playerObjects):
    userName = saveGame.getPlayerName(gameState)    #gets users playerName from save file
    #print("User Name:", userName)

    flag = 0
    count = 0
    while flag == 0:
        tempUserName = playerObjects[count].getName()
        #print("userName:", userName)
        #print("tempUsersName:", tempUserName)
        if userName == tempUserName:
            #print("Found User Player Object")
            userPlayerObject = playerObjects[count] #get user player object
            userPlayerIndex = count                 #get user player index
            flag = 1
        if count == 1000:
            #print("Did Not Found User Player Object")
            flag = 1
        count = count + 1

    #print("Users Player Name:", tempUserName)
    #print("Users Player Index:", userPlayerIndex)
    return userPlayerIndex

def getUserTeamIndex(gameState, teamObjects):
    userTeam = saveGame.getTeamName(gameState)      #gets users teamName from save file
    #print("User Team:", userTeam)

    flag = 0
    count = 0
    #print("Number of teams:", len(teamObjects))
    #print("User Team:", userTeam)
    while flag == 0:
        tempTeamName = teamObjects[count].getTeamName()
        #print("User Team:", userTeam)
        #print("Temp Team:", tempTeamName)
        if userTeam == tempTeamName:
            #print("Found User Team Object")
            userTeamObject = teamObjects[count] #get user team object
            userTeamIndex = count               #get user team index of team to be swapped to
            flag = 1
            #print("flag if match:", flag)
        if count == 1000:
            #print("Did Not Found User Team Object")
            flag = 1
            #print("flag if no match:", flag)
        count = count + 1
        #print("flag:", flag)

    #print("Users Team Name:", tempTeamName)
    #print("Users Team Index:", userTeamIndex)
    return userTeamIndex

#get player index from name
def getPlayerIndex (gameState, name, playerObjects):
    flag = 0
    count = 0
    while flag == 0:
        tempName = playerObjects[count].getName()
        if name == tempName:
            #print("Found NPC player Object")
            npcPlayerObject = playerObjects[count] #get npc player object
            npcPlayerIndex = count                 #get npc player index
            flag = 1
        if count == 1000:
            #print("Did Not Found User Player Object")
            flag = 1
        count = count + 1
    return npcPlayerIndex

#create

#after teams are randomly filled with players the users player object will be swapped to the team they picked
def swapUserWithNPC(gameState):
    playerObjects = gameState[2]
    teamObjects = gameState[3]
    userName = saveGame.getPlayerName(gameState)                    #gets users playerName from save file
    userPlayerIndex = getUserPLayerIndex(gameState, playerObjects)  #gets users current player index
    userTeam = saveGame.getTeamName(gameState)                      #gets users teamName from save file
    userTeamIndex = getUserTeamIndex(gameState, teamObjects)        #gets users current team index (The player will leave this team, and the NPC will join this team)

    #print team the player picked before swap
    teamObjects[userTeamIndex].printRoster()


    #This while loop checks each player on each team to find the user
    #Then the  location of the user is stored so that the NPC on the Users team
    #can be placed here
    flag = 0
    count = 0
    pos = 1                                 #sets the position for the NPC to swap to
    while flag == 0:
        p1 = teamObjects[count].getP1()     #gets p1 from team
        p1n = p1.getName()                  #gets p1 name
        if p1n == userName:                 #checks for match
            #print("found name")
            tempTeamName = teamObjects[count].getTeamName()     #get temp team name
            tempTeamObject = teamObjects[count]             #get temp team object
            tempTeamIndex = count                           #get temp team index for NPC to be swapped to
            pos = 1                                         
            flag = 1
        p2 = teamObjects[count].getP2() #gets p2 from team
        n2 = p2.getName()               #gets p2 name
        if n2 == userName:              #checks for match
            #print("found name")
            tempTeamName = teamObjects[count].getTeamName() #get temp team name
            tempTeamObject = teamObjects[count]         #get temp team object
            tempTeamIndex = count                       #get temp team index for NPC to be swapped to
            pos = 2
            flag = 1
        p3 = teamObjects[count].getP3() #gets p3 from team
        n3 = p3.getName()               #gets p3 name
        if n3 == userName:              #checks for match
            #print("found name")
            tempTeamName = teamObjects[count].getTeamName() #get temp team name
            tempTeamObject = teamObjects[count]         #get temp team object
            tempTeamIndex = count                       #get temp team index for NPC to be swapped to
            pos = 3
            flag = 1
        if count == 1000:
            #print("Did Not NPC player name")
            flag = 1
            tempTeamName = "Not Found"
        count = count + 1

    #print team the player picked before swap
    #print("\nTeam user picked before swap")
    teamObjects[userTeamIndex].printRoster()
    #print team the player got randomly assigned before swap
    #print("Team user got randomly assigned before swap")
    teamObjects[tempTeamIndex].printRoster()

    #print("team to be swapped from:", tempTeamName)

    #get name of player from tempTeamObject
    npcObject = teamObjects[userTeamIndex].getP1()
    npcName = npcObject.getName()

    #print("npc to be swapped:", npcName)

    #This function returns the index of a player based on the name string
    npcIndex = getPlayerIndex(gameState, npcName, playerObjects)

    tempTeamName = teamObjects[tempTeamIndex].getTeamName()
    #print("Team User was on:", tempTeamName)
    npcName = playerObjects[npcIndex].getName()
    #print("NPC being swapped:", npcName)
    tempTeamName2 = teamObjects[userTeamIndex].getTeamName()
    #print("Team User is going to:", tempTeamName2)
    userName2 = playerObjects[userPlayerIndex].getName()
    #print("player being swapped:", userName2)

    #Swap the users player object to the team they picked with the npc player object on that team
    if pos == 1:
        #print("set npc to p1")
        teamObjects[tempTeamIndex].setP1(playerObjects[npcIndex]) #sets NPC player object to team that User was on
        playerObjects[npcIndex] = updatePlayersTeam(teamObjects[tempTeamIndex], playerObjects[npcIndex])    #updates the player objects teamName attribute to the new teamName
    if pos == 2:
        #print("set npc to p2")
        teamObjects[tempTeamIndex].setP2(playerObjects[npcIndex]) #sets NPC player object to team that User was on
        playerObjects[npcIndex] = updatePlayersTeam(teamObjects[tempTeamIndex], playerObjects[npcIndex])    #updates the player objects teamName attribute to the new teamName
    if pos == 3:
        #print("set npc to p3")
        teamObjects[tempTeamIndex].setP3(playerObjects[npcIndex]) #sets NPC player object to team that User was on
        playerObjects[npcIndex] = updatePlayersTeam(teamObjects[tempTeamIndex], playerObjects[npcIndex])    #updates the player objects teamName attribute to the new teamName
    
    teamObjects[userTeamIndex].setP1(playerObjects[userPlayerIndex]) #sets User player object to team that NPC was on
    playerObjects[userPlayerIndex] = updatePlayersTeam(teamObjects[userTeamIndex], playerObjects[userPlayerIndex])    #updates the player objects teamName attribute to the new teamName

    userName = playerObjects[userPlayerIndex].getName()

    npcName = playerObjects[npcIndex].getName()

    teamObjects[tempTeamIndex].printRoster()

    teamObjects[userTeamIndex].printRoster()

    gameState[2] = playerObjects
    gameState[3] = teamObjects
    return gameState

def getTeamObject(gameState, teamName):
    teamObjects = gameState[3]
    count = 0
    for i in teamObjects:
        name = teamObjects[count].getTeamName()
        if teamName == name:
            teamObject = teamObjects[count]
            return teamObject
        count = count + 1
        
    return "team object not found"
