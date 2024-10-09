
import random
import saveGame
import saveData
import generateSchedule
import updateStats

#Generate Random Number Between 2 Ints
#Get 2 Ints
#Return 1 Int
def getRandInt(int1, int2):
    int3 = random.randint(int1, int2)
    return int3

def rollGoals():
    teamGoals = getRandInt(0, 5)
    while True:
        if (teamGoals >= 5):
            roll = getRandInt(0, 5)
            if (roll == 5):
                    teamGoals = teamGoals + 1
            else:
                    break
        else:
                break
    return teamGoals

def calcShotPerc(percentRoll):
    if percentRoll <= 15:
          return 0
    elif percentRoll <= 35:
          return 1
    elif percentRoll <= 55:
          return 2
    elif percentRoll <= 70:
          return 3
    elif percentRoll <= 85:
          return 4
    elif percentRoll <= 95:
          return 5
    elif percentRoll <= 100:
          shots = 6
          while True:
                randRoll = getRandInt(0,10)
                if randRoll == 10:
                    shots = shots + 1
                else:
                    break
          return shots
    

#Check for advantage between 2 teams
#A team gets advantage if they 
#Get gameState, Team1 name, Team2 name
#Return team1, team2, or None, depending on who has advantage
def checkAdvantage(gameState, team1, team2):
    advantageTeam = "None"
    currentWeek = int(saveGame.getWeek(gameState))
    floatWeek = float(currentWeek)
    intWeek = int(floatWeek)
    playOffGame = floatWeek - intWeek
    playOffGame = round(playOffGame, 1)
    team1AdvPoints = 0
    team2AdvPoints = 0

    ###ADVANTAGE RULES###
    #For the first three games of the season the top 8 playoff teams from last season get advantage over teams that did not get top 8 in playoffs
    #Otherwise if a team has 3 or more wins than their opponent in the current season they get advantage
    #During playoffs the higher seed of the match gets one adv point
    #During playoffs if the team was top three in the prev playoffs they get 1 adv point
    #During playoffs if each team has 1 adv point they cancel out and no advantage is rewarded
    #During playoffs if a team has 1 more adv point than the other, they get advantage for only game 1
    #During playoffs if a team has 2 more adv points than the other, they get advantage for game1 and game2

    #Get team Objects
    for i in gameState[3]:
            if i.getTeamName() == team1:
                team1Object = i
                break
    for i in gameState[3]:
            if i.getTeamName() == team2:
                team2Object = i
                break

    #check for 3 win lead during season
    if currentWeek <= 3:    
        #get season wins team1
        team1Wins = team1Object.getWinsSeason()
        #get season wins team2
        team2Wins = team2Object.getWinsSeason()
        #compare season wins
        if team1Wins >= (team2Wins + 3):
            advantageTeam = team1
        elif team2Wins >= (team1Wins + 3):
            advantageTeam = team2
        else:
            advantageTeam = "None"
    elif ((currentWeek > 3) and (currentWeek <= 21)):   #check if top 8 playoffs last season
        team1PrevPlayoffPos = team1Object.getPrevPlayoffPos()
        team2PrevPlayoffPos = team2Object.getPrevPlayoffPos()
        if (int(team1PrevPlayoffPos) <= 8) and (int(team2PrevPlayoffPos) > 8):
             advantageTeam = team1
        elif (int(team2PrevPlayoffPos) <= 8) and (int(team1PrevPlayoffPos) > 8):
             advantageTeam = team2
        else:
             advantageTeam = "None"
    elif ((intWeek > 21)):   #Check for Playoff Advantages
        #check for higher playoff seed
        team1Seed = team1Object.getPlayoffSeed()
        team2Seed = team2Object.getPlayoffSeed()
        if(int(team1Seed) > (int(team2Seed))):
            team1AdvPoints = team1AdvPoints + 1
        if(int(team1Seed) < (int(team2Seed))):
            team2AdvPoints = team2AdvPoints + 1
        #check for top three previous playoff seed
        team1PrevPlayoffPos = team1Object.getPrevPlayoffPos()
        team2PrevPlayoffPos = team2Object.getPrevPlayoffPos()
        if (int(team1PrevPlayoffPos) <= 3):
             team1AdvPoints = team1AdvPoints + 1
        elif (int(team2PrevPlayoffPos) <= 3):
             team2AdvPoints = team2AdvPoints + 1

        #Determine the game of the series
        if (str(playOffGame) == "0.1"):
             game = 1
        elif (str(playOffGame) == "0.2"):
             game = 2
        elif (str(playOffGame) == "0.3"):
             game = 3
        elif (str(playOffGame) == "0.4"):
             game = 4
        else:
             game = 5


        #Determine if a team gets advatage or not
        if((team1AdvPoints - team2AdvPoints == 2) and ((game == 1) or (game == 2))):
            advantageTeam = team1
        elif((team2AdvPoints - team1AdvPoints == 2) and ((game == 1) or (game == 2))):
            advantageTeam = team2
        elif((team1AdvPoints - team2AdvPoints == 1) and (game == 1)):
            advantageTeam = team1
        elif((team2AdvPoints - team1AdvPoints == 1) and (game == 1)):
            advantageTeam = team2
        else:
             advantageTeam = "None"

    return advantageTeam

#Roll goals for 2 Teams, take account the advantage if any, and compare to determine winner and loser
#Get gameState, Team1 name string, Team2 name string
#Return gameState with update cache
def simulateGame(gameState, team1, team2):
    #Get team objects
    for i in gameState[3]:
            if i.getTeamName() == team1:
                team1Object = i
                break
    for i in gameState[3]:
            if i.getTeamName() == team2:
                team2Object = i
                break

    #check if for advantage between both teams
    advantageTeam = checkAdvantage(gameState, team1, team2)

    #Roll team1 and team2 goals
    if (advantageTeam == "None"):
        team1Goals = rollGoals()
        team2Goals = rollGoals()
    elif (advantageTeam == team1):
        team1Goals = rollGoals()
        team1GoalsAdv = rollGoals()
        team1Goals = max(team1Goals, team1GoalsAdv)
        team2Goals = rollGoals()
    elif (advantageTeam == team2):
        team1Goals = rollGoals()
        team2Goals = rollGoals()
        team2GoalsAdv = rollGoals()
        team2Goals = max(team2Goals, team2GoalsAdv)

    if (team1Goals == team2Goals):
            randInt = getRandInt(0,1)
            if (randInt == 0):
                team1Goals = team1Goals + 1
            else:
                team2Goals = team2Goals +1

    #Declare variables to hold stats
    T1P1Name = team1Object.p1.name
    T1P2Name = team1Object.p2.name
    T1P3Name = team1Object.p3.name

    T2P1Name = team2Object.p1.name
    T2P2Name = team2Object.p2.name
    T2P3Name = team2Object.p3.name

    T1P1Goals = 0
    T1P1Assists = 0
    T1P1Shots = 0
    T1P1Saves = 0
    T1P2Goals = 0
    T1P2Assists = 0
    T1P2Shots = 0
    T1P2Saves = 0
    T1P3Goals = 0
    T1P3Assists = 0
    T1P3Shots = 0
    T1P3Saves = 0

    T2P1Goals = 0
    T2P1Assists = 0
    T2P1Shots = 0
    T2P1Saves = 0
    T2P2Goals = 0
    T2P2Assists = 0
    T2P2Shots = 0
    T2P2Saves = 0
    T2P3Goals = 0
    T2P3Assists = 0
    T2P3Shots = 0
    T2P3Saves = 0


    #Divide all goals to teams players randomly
    for x in range(team1Goals):
        randInt = getRandInt(1,3)
        if randInt == 1:
            T1P1Goals = T1P1Goals + 1
        elif randInt == 2:
            T1P2Goals = T1P2Goals + 1
        elif randInt == 3:
            T1P3Goals = T1P3Goals + 1
    for x in range(team2Goals):
        randInt = getRandInt(1,3)
        if randInt == 1:
            T2P1Goals = T2P1Goals + 1
        elif randInt == 2:
            T2P2Goals = T2P2Goals + 1
        elif randInt == 3:
            T2P3Goals = T2P3Goals + 1
    
    #Randomly generate and assign assists to players
    team1Assists = getRandInt(0,team1Goals)
    T1P1AssMax = team1Goals - T1P1Goals
    T1P2AssMax = team1Goals - T1P2Goals
    T1P3AssMax = team1Goals - T1P3Goals

    while team1Assists > 0:
        randInt = getRandInt(1,3)
        if ((randInt == 1) and (T1P1AssMax > 0)):
            T1P1Assists = T1P1Assists + 1
            T1P1AssMax = T1P1AssMax - 1
            team1Assists = team1Assists - 1
        elif ((randInt == 2) and (T1P2AssMax > 0)):
            T1P2Assists = T1P2Assists + 1
            T1P2AssMax = T1P2AssMax - 1
            team1Assists = team1Assists - 1
        elif ((randInt == 3) and (T1P3AssMax > 0)):
            T1P3Assists = T1P3Assists + 1
            T1P3AssMax = T1P3AssMax - 1
            team1Assists = team1Assists - 1

    team2Assists = getRandInt(0,team2Goals)
    T2P1AssMax = team2Goals - T2P1Goals
    T2P2AssMax = team2Goals - T2P2Goals
    T2P3AssMax = team2Goals - T2P3Goals

    while team2Assists > 0:
        randInt = getRandInt(1,3)
        if ((randInt == 1) and (T2P1AssMax > 0)):
            T2P1Assists = T2P1Assists + 1
            T2P1AssMax = T2P1AssMax - 1
            team2Assists = team2Assists - 1
        elif ((randInt == 2) and (T2P2AssMax > 0)):
            T2P2Assists = T2P2Assists + 1
            T2P2AssMax = T2P2AssMax - 1
            team2Assists = team2Assists - 1
        elif ((randInt == 3) and (T2P3AssMax > 0)):
            T2P3Assists = T2P3Assists + 1
            T2P3AssMax = T2P3AssMax - 1
            team2Assists = team2Assists - 1

    #Randomly generate and assign shots to players
    #If team lost, those players role with disadvantage
    T1P1Shots = getRandInt(1, 100)
    T1P1Shots = calcShotPerc(T1P1Shots)
    if(team1Goals < team2Goals):
         T1P1ShotsDis = calcShotPerc(getRandInt(1, 100))
         T1P1Shots = min(T1P1Shots, T1P1ShotsDis)
    T1P2Shots = getRandInt(1, 100)
    T1P2Shots = calcShotPerc(T1P2Shots)
    if(team1Goals < team2Goals):
         T1P2ShotsDis = calcShotPerc(getRandInt(1, 100))
         T1P2Shots = min(T1P2Shots, T1P2ShotsDis)
    T1P3Shots = getRandInt(1, 100)
    T1P3Shots = calcShotPerc(T1P3Shots)
    if(team1Goals < team2Goals):
         T1P3ShotsDis = calcShotPerc(getRandInt(1, 100))
         T1P3Shots = min(T1P3Shots, T1P3ShotsDis)
    team1Shots = T1P1Shots + T1P2Shots + T1P3Shots

    T2P1Shots = getRandInt(1, 100)
    T2P1Shots = calcShotPerc(T2P1Shots)
    if(team2Goals < team1Goals):
         T2P1ShotsDis = calcShotPerc(getRandInt(1, 100))
         T2P1Shots = min(T2P1Shots, T2P1ShotsDis)
    T2P2Shots = getRandInt(1, 100)
    T2P2Shots = calcShotPerc(T2P2Shots)
    if(team2Goals < team1Goals):
         T2P2ShotsDis = calcShotPerc(getRandInt(1, 100))
         T2P2Shots = min(T2P2Shots, T2P2ShotsDis)
    T2P3Shots = getRandInt(1, 100)
    T2P3Shots = calcShotPerc(T2P3Shots)
    if(team2Goals < team1Goals):
         T2P3ShotsDis = calcShotPerc(getRandInt(1, 100))
         T2P3Shots = min(T2P3Shots, T2P3ShotsDis)
    team2Shots = T2P1Shots + T2P2Shots + T2P3Shots

    #Randomly generate and add saves to players
    maxSaves = team2Shots - team2Goals
    if maxSaves < 0:
         maxSaves = 0
    team1Saves = getRandInt(0, maxSaves)
    while team1Saves > 0:
        randInt = getRandInt(1,3)
        if (randInt == 1):
            T1P1Saves = T1P1Saves + 1
            team1Saves = team1Saves - 1
        elif (randInt == 2):
            T1P2Saves = T1P2Saves + 1
            team1Saves = team1Saves - 1
        elif (randInt == 3):
            T1P3Saves = T1P3Saves + 1
            team1Saves = team1Saves - 1

    maxSaves = team1Shots - team1Goals
    if maxSaves < 0:
         maxSaves = 0
    team2Saves = getRandInt(0, maxSaves)
    while team2Saves > 0:
        randInt = getRandInt(1,3)
        if (randInt == 1):
            T2P1Saves = T2P1Saves + 1
            team2Saves = team2Saves - 1
        elif (randInt == 2):
            T2P2Saves = T2P2Saves + 1
            team2Saves = team2Saves - 1
        elif (randInt == 3):
            T2P3Saves = T2P3Saves + 1
            team2Saves = team2Saves - 1
    
    statsList = [T1P1Goals, T1P1Assists, T1P1Shots, T1P1Saves, T1P2Goals, T1P2Assists, T1P2Shots, T1P2Saves,
                 T1P3Goals, T1P3Assists, T1P3Shots, T1P3Saves, T2P1Goals, T2P1Assists, T2P1Shots, T2P1Saves,
                 T2P2Goals, T2P2Assists, T2P2Shots, T2P2Saves, T2P3Goals, T2P3Assists, T2P3Shots, T2P3Saves]
    
    return statsList

def updateStatsFromGame(gameState, team1, team2, simResults):

    #check if last week of the season
    week = int(saveGame.getWeek(gameState))

    #Get team objects
    for i in gameState[3]:
            if i.getTeamName() == team1:
                team1Object = i
                break
    for i in gameState[3]:
            if i.getTeamName() == team2:
                team2Object = i
                break

    #get current save data from cache for each team class object
    team1ObjectSaveDataOld = team1Object.getCacheString()
    team2ObjectSaveDataOld = team2Object.getCacheString()

    goalsL1 = simResults[0]
    assistsL1 = simResults[1]
    shotsL1 = simResults[2]
    savesL1 = simResults[3]
    goalsL2 = simResults[4]
    assistsL2 = simResults[5]
    shotsL2 = simResults[6]
    savesL2 = simResults[7]
    goalsL3 = simResults[8]
    assistsL3 = simResults[9]
    shotsL3 = simResults[10]
    savesL3 = simResults[11]
    goalsR1 = simResults[12]
    assistsR1 = simResults[13]
    shotsR1 = simResults[14]
    savesR1 = simResults[15]
    goalsR2 = simResults[16]
    assistsR2 = simResults[17]
    shotsR2 = simResults[18]
    savesR2 = simResults[19]
    goalsR3 = simResults[20]
    assistsR3 = simResults[21]
    shotsR3 = simResults[22]
    savesR3 = simResults[23]

    #Get win loss results
    team1Goals = goalsL1 + goalsL2 + goalsL3
    team2Goals = goalsR1 + goalsR2 + goalsR3
    if team1Goals > team2Goals:
        resultL = 1
    else:
        resultL = 0
    if team2Goals > team1Goals:
        resultR = 1
    else:
        resultR = 0

    #get playernames
    p1L = team1Object.getP1()
    p1LName = p1L.getName()
    p2L = team1Object.getP2()
    p2LName = p2L.getName()
    p3L = team1Object.getP3()
    p3LName = p3L.getName()
    
    p1R = team2Object.getP1()
    p1RName = p1R.getName()
    p2R = team2Object.getP2()
    p2RName = p2R.getName()
    p3R = team2Object.getP3()
    p3RName = p3R.getName()

    #update player stats
    gameState = updateStats.updateStatsPlayer(gameState, p1LName, goalsL1, assistsL1, savesL1, shotsL1)
    gameState = updateStats.updateStatsPlayer(gameState, p2LName, goalsL2, assistsL2, savesL2, shotsL2)
    gameState = updateStats.updateStatsPlayer(gameState, p3LName, goalsL3, assistsL3, savesL3, shotsL3)
    gameState = updateStats.updateStatsPlayer(gameState, p1RName, goalsR1, assistsR1, savesR1, shotsR1)
    gameState = updateStats.updateStatsPlayer(gameState, p2RName, goalsR2, assistsR2, savesR2, shotsR2)
    gameState = updateStats.updateStatsPlayer(gameState, p3RName, goalsR3, assistsR3, savesR3, shotsR3)
    #update team stats in cache
    gameState = updateStats.updateStatsTeam(gameState, team1, p1L, p2L, p3L, resultL)
    gameState = updateStats.updateStatsTeam(gameState, team2, p1R, p2R, p3R, resultR)
    #update team stats in saveFile
    team1ObjectSaveDataNew = team1Object.getCacheString()    #get current save data from cache for each team class object with updated stats from game played
    saveData.replaceLine(gameState, team1ObjectSaveDataOld, team1ObjectSaveDataNew)   #replaces old team data with new team data to save file
    team2ObjectSaveDataNew = team2Object.getCacheString()    #get current save data from cache for each team class object with updated stats from game played
    saveData.replaceLine(gameState, team2ObjectSaveDataOld, team2ObjectSaveDataNew)   #replaces old team data with new team data to save file

def simulateWeek(gameState):
    #Get Week
    week = int(saveGame.getWeek(gameState))
    playersTeamName = saveGame.getTeamName(gameState)

    if week <= 21:
        for i in range(11):
            matchupTeams = generateSchedule.getMatchup(gameState, week, i + 1)
            matchupTeamsList = matchupTeams.split(" ")
            team1 = matchupTeamsList[0]
            team2 = matchupTeamsList[len(matchupTeamsList) - 1]

            if (team1 != "None") and (team2 != "None") and (team1 != playersTeamName) and (team2 != playersTeamName):
                simResults = simulateGame(gameState, team1, team2)
                updateStatsFromGame(gameState, team1, team2, simResults)
    
    if (week > 21) and (week < 28):
        for i in range(4):
            matchupTeams = generateSchedule.getMatchup(gameState, week, i + 1)
            matchupTeamsList = matchupTeams.split(" ")
            team1 = matchupTeamsList[0]
            team2 = matchupTeamsList[len(matchupTeamsList) - 1]

            if (team1 != "None") and (team2 != "None") and (team1 != playersTeamName) and (team2 != playersTeamName):
                simResults = simulateGame(gameState, team1, team2)
                updateStatsFromGame(gameState, team1, team2, simResults)

    if (week > 28) and (week < 37):
        for i in range(2):
            matchupTeams = generateSchedule.getMatchup(gameState, week, i + 1)
            matchupTeamsList = matchupTeams.split(" ")
            team1 = matchupTeamsList[0]
            team2 = matchupTeamsList[len(matchupTeamsList) - 1]

            if (team1 != "None") and (team2 != "None") and (team1 != playersTeamName) and (team2 != playersTeamName):
                simResults = simulateGame(gameState, team1, team2)
                updateStatsFromGame(gameState, team1, team2, simResults)
        


def checkForSeriesGame(gameState):
     

    return False

def updateTimeline(gameState):
    currentSeason = str(saveGame.getSeason(gameState))
    intSeason = int(currentSeason)
    nextSeason = intSeason
    currentWeek = saveGame.getWeek(gameState)
    floatWeek = float(currentWeek)
    intWeek = int(floatWeek)
    playOffGame = floatWeek - intWeek   
    playOffGame = round(playOffGame, 1)     #decimal of the week to determine what game of the series it is
    nextWeek = 0.0

    #addSeriesGame = checkForSeriesGame(gameState)

    if intWeek < 21:
        nextWeek = int(intWeek + 1)
    elif (intWeek >= 21) and (intWeek <= 37):
        #if last week of season played, generate playoff schedule, or update schedule as playoffs continue
        nextWeek = int(intWeek + 1)
        generateSchedule.generatePlayoffSchedule(gameState)
    elif intWeek > 37:
        #if after finals reset to new season
        nextWeek = 1
        nextSeason = intSeason + 1
        saveGame.updateSeason(gameState, nextSeason)#update season to save file

    



    saveGame.updateWeek(gameState, nextWeek)    #update week to save file
    