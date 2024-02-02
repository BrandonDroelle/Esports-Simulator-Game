#updateStats

def updateStatsPlayer(gameState, playerName, goals, assists, saves, shots):
    for i in gameState[2]:
        if i.getName() == playerName:
            i.addGoals(goals)
            i.addAssists(assists)
            i.addSaves(saves)
            i.addShots(shots)
    
    return gameState

def updateStatsTeam(gameState, teamName, P1, P2, P3, result):
    for i in gameState[3]:
        if i.getTeamName() == teamName:
            i.setP1(P1)
            i.setP2(P2)
            i.setP3(P3)
            i.updateGoals()
            i.updateAssists()
            i.updateSaves()
            i.updateShots()
            i.updateWLR(result)
            
    return gameState
