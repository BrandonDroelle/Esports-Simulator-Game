from sqlite3 import TimestampFromTicks
import playerClass
import saveGame
import saveData
import teamClass
import generateSchedule

#creates list of player objects from list of player name strings
def createPlayerObjects(gameState, playerNames):
    #add user to list of players
    userName = saveGame.getPlayerName(gameState)
    #print("userName:", userName)
    #check is username is already on list so it doesn't get added multiple times
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
    print("PlayerNames: ")
    userName = saveGame.getPlayerName(gameState)
    playerNames.remove(userName)
    print("PlayerNames: ")
    return playerNames


#creates list of player objects from data on save file
def loadPlayerAndTeamsIntoCache(gameState, teamNames, playerNames):
    print("loading player and team objects into cache")
    teamObjects = createTeamObjects(teamNames)
    lenTeams = len(teamObjects)
    playerObjects = createPlayerObjects(gameState, playerNames)
    lenPlayers = len(playerObjects)
    currentSeason = saveGame.getSeason(gameState) + "\n"
    currentSeason = "Season " + currentSeason

    for i in range(lenTeams):
        extraRows = 0
        count = 0
        teamName = teamObjects[i].getTeamName() + "\n"
        print("Current Team: ", teamName)
        while count < 3:
            currentName = saveData.read(gameState, teamName, 1, currentSeason, extraRows)
            print("p1 Name: ", currentName)
            count = count + 1
            for j in range(lenPlayers):
                tempPlayerName = playerObjects[j].getName() + "\n"
                print("temp Name: ", tempPlayerName)
                if currentName == tempPlayerName:
                    if count == 1:
                        print("add P1")
                        print(playerObjects[j].getName())
                        teamObjects[i].setP1(playerObjects[j])
                        extraRows = 9
                        break
                    if count == 2:
                        print("add P2")
                        print(playerObjects[j].getName())
                        teamObjects[i].setP2(playerObjects[j])
                        extraRows = 18
                        break
                    if count == 3:
                        print("add P3")
                        print(playerObjects[j].getName())
                        teamObjects[i].setP3(playerObjects[j])
                        break
                    
    for i in range(lenTeams):       
        teamObjects[i].printRoster()
    print("loaded player and team objects into cache")

#creates list of team objects from list of team name strings
def createTeamObjects(teamNames):
    
    l = len(teamNames)
    #print("len:", l)

    #create list of team objects
    teams = []
    for i in range(l):
        #print("i:", i)
        teamTemp = teamClass.TeamClass(teamNames[i])
        teams.append(teamTemp)
        name = teams[i].getTeamName()
        #print("Team Name:", name)
    #print("Team Objects: ", teams)
    return teams

#load saved data from file to cache for each player
def loadPlayerObjectData(gameState, playerNames):
    #create player objects
    playerObjects = createPlayerObjects(gameState, playerNames) #here is when the player name is added to the list of player names

    l = len(playerNames)
    for i in range(l):
        playerObjects[i]


#randomly fill each team with three players
def fillTeamRosters(gameState, playerObjects, teamObjects):

    #Randomly assigns 3 players from playerObjects to each teamObject
    playersShuffle = playerObjects.copy() #makes a copy of the playerObject list so the playerObject list stays in the original order
    playersShuffle = generateSchedule.randomizeList(playersShuffle)
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
        teamObjects[tcount].setP1(playersShuffle[pcount])
        pcount = pcount + 1
        teamObjects[tcount].setP2(playersShuffle[pcount])
        pcount = pcount + 1
        teamObjects[tcount].setP3(playersShuffle[pcount])
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

    return teamObjects

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
def swapUserWithNPC(gameState, playerObjects, teamObjects):
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

    #print("initiate player and NPC swap")
    #Swap the users player object to the team they picked with the npc player object on that team
    if pos == 1:
        #print("set npc to p1")
        teamObjects[tempTeamIndex].setP1(playerObjects[npcIndex]) #sets NPC player object to team that User was on
    if pos == 2:
        #print("set npc to p2")
        teamObjects[tempTeamIndex].setP2(playerObjects[npcIndex]) #sets NPC player object to team that User was on
    if pos == 3:
        #print("set npc to p3")
        teamObjects[tempTeamIndex].setP3(playerObjects[npcIndex]) #sets NPC player object to team that User was on
    
    teamObjects[userTeamIndex].setP1(playerObjects[userPlayerIndex]) #sets User player object to team that NPC was on

    userName = playerObjects[userPlayerIndex].getName()
    #print("Users Name from player object:", userName)
    npcName = playerObjects[npcIndex].getName()
    #print("npcs Name from player object:", npcName)

    #print team the player got randomly assigned after swap
    #print("Team user got randomly assigned after swap\n")
    teamObjects[tempTeamIndex].printRoster()
    #print team the player picked after swap
    #print("Team user picked after swap\n")
    teamObjects[userTeamIndex].printRoster()
    

    #print("Users team after swap")
    #print("Users Player Name:", userName)
    #print("Users Player Index:", userPlayerIndex)
    #print("Users Team Name:", userTeam)
    #print("Users Team Index:", userTeamIndex)

    

    #print("npcs team after swap")
    #print("npcs Player Name:", npcName)
    #print("npcs Player Index:", npcIndex)
    #print("npcs Team Name:", tempTeamName)
    #print("npcs Team Index:", tempTeamIndex)