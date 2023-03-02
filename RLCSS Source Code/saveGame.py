import saveData

#update save file to not new save so when reopened goes directly to locker room and not new game
def updateSave(gameState):
    if gameState[0] == 'gameData1.txt':
        saveNum = 1
    if gameState[0] == 'gameData2.txt':
        saveNum = 2
    if gameState[0] == 'gameData3.txt':
        saveNum = 3
    saveNum = str(saveNum)
    #creates the string to search the data file in this case "save x\n" (x being 1 2 3 depending on which file to be opened)
    saveState = "save " + saveNum + "\n"
    print ("saveState: ", saveState)
    saveData.write(gameState, saveState, 1) #gameState, type of data, new data to be written

#update player name to save file
def updatePlayerName(gameState, name):
    #updates save file with player name
    print("Add player name to save file")
    saveState = "player name" + "\n"
    saveData.write(gameState, saveState, name) #gameState, type of data, new data to be written
    print("Player name added to save file")

#get player name
def getPlayerName(gameState):
    print('get player name')
    name = saveData.read(gameState, 'player name\n')
    name = name.replace("\n", "")
    return name

#update team name to save file
def updateTeam(gameState, team):
    #updates save file with team name
    print("Add team to save file")
    saveState = "player team" + "\n"
    saveData.write(gameState, saveState, team) #gameState, type of data, new data to be written
    print("Player team added to save file")

#get team name
def getTeamName(gameState):
    print('get team name')
    teamName = saveData.read(gameState, 'player team\n')
    teamName = teamName.replace("\n", "")
    teamName = teamName.replace(" ", "")
    return teamName

#update season number to save file
def updateSeason(gameState, season):
    #updates save file with current season
    print("Add current season to save file")
    saveState = "current season" + "\n"
    saveData.write(gameState, saveState, season) #gameState, type of data, new data to be written
    print("current season added to save file")

#get current season
def getSeason(gameState):
    print('get current season')
    x = saveData.read(gameState, 'current season\n')
    x = x.replace("\n", "")
    x = x.replace(" ", "")
    return x

#update week number to save file
def updateWeek(gameState, week):
    #updates save file with week number
    print("Add week number to save file")
    saveState = "current week" + "\n"
    saveData.write(gameState, saveState, week) #gameState, type of data, new data to be written
    print("current week added to save file")

#get current week
def getWeek(gameState):
    print('get current week')
    x = saveData.read(gameState, 'current week\n')
    x = x.replace("\n", "")
    x = x.replace(" ", "")
    return x

#update schedule to save file
def updateSchedule(gameState, schedule):
    print('Add schedule to sace file')
    saveData.append(gameState, schedule)