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

#update player name to save file
def updateTeam(gameState, team):
    #updates save file with player name
    print("Add team to save file")
    saveState = "player team" + "\n"
    saveData.write(gameState, saveState, team) #gameState, type of data, new data to be written
    print("Player team added to save file")