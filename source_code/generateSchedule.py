#generate round robin schedule for the season
import random
import saveGame
import sortFunctions
import saveData

def randomizeList(teams):
    print('in randomize list')
    #print("teams: ", teams)
    random.shuffle(teams)
    #print("teams shuffle: ", teams)
    return teams

def printTeams(teams):
    print('teams: ', teams)

def generateRoundRobin(gameState, teams):

    #Randomize list of teams sent in
    teamsShuffle = teams.copy() #makes a copy of the teams list so the teams list stays in the original order
    teamsShuffle = randomizeList(teamsShuffle)
    #print("teams: ", teams)
    #print("teamsShuffle: ", teamsShuffle)
    
    #Create a schedule for the players in the list and return it
    schedule = []
    if len(teamsShuffle) % 2 == 1: teamsShuffle = teamsShuffle + [None]
    # manipulate map (array of indexes for list) instead of list itself
    # this takes advantage of even/odd indexes to determine home vs. away
    n = len(teamsShuffle)
    map = list(range(n))
    mid = n // 2
    for i in range(n-1):
        l1 = map[:mid]
        l2 = map[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = teamsShuffle[l1[j]]
            t2 = teamsShuffle[l2[j]]
            if j == 0 and i % 2 == 1:
                # flip the first match only, every other round
                # (this is because the first match always involves the last player in the list)
                round.append((t2, t1))
            else:
                round.append((t1, t2))
        #randomize each week as its added to the schedule
        schedule.insert(random.randrange(len(schedule)+1), round)

        #rotate list by n/2, leaving last element at the end
        map = map[mid:-1] + map[:mid] + map[-1:]
        
    return schedule

def printSchedule(schedule):
    sLength = len(schedule)
    rLength = len(schedule[0])
    #print("SCHEDULE\n**********************")
    for i in range(sLength):
        #print("Week:", i + 1)
        for j in range(rLength):
            game = ("{} {}".format(schedule[i][j][0],schedule[i][j][1]))
            #print(game)
        #print()

#create a string from the schedule tuple formated to store data in the save file
def getScheduleString(gameState, schedule, teamObjects):
    sLength = len(schedule)
    rLength = len(schedule[0])
    #print("schedule[o]", schedule[0])
    #print("schedule[o] length", rLength)
    currentSeason = str(saveGame.getSeason(gameState))
    #print("current season:", currentSeason)
    scheduleSaveFormat = 'Season ' + currentSeason + '\n'
    count = 0
    weekCount = 1
    #scheduleSaveFormat = scheduleSaveFormat + "Week " + '1' + "\n"
    for i in range(sLength):
        #add the current week to the schedule string
        print("$$$$$$Week:", i + 1,"$$$$$$$$")
        weekCountStr = str(i + 1)
        #scheduleSaveFormat = scheduleSaveFormat + "Week " + weekCountStr + " "
        count = 0
        for j in range(rLength):
            #add each team in order every week to the schedule string
            game = ("{} {}".format(schedule[i][j][0],schedule[i][j][1]))
            #print("game:", game)
            #print("g", i + 1, 't', i+1, ':', schedule[i][j][0], schedule[i][j][1])
            homeTeam = str(schedule[i][j][0])
            awayTeam = str(schedule[i][j][1])
            #print("home team:", homeTeam, "\naway team:", awayTeam)
            #reformat schedule list to fit save data file
            scheduleSaveFormat = scheduleSaveFormat + homeTeam + " " + awayTeam + " "
            #print('scheduleSaveFormat:', scheduleSaveFormat)
            count = count + 1
      
    #scheduleSaveFormat = scheduleSaveFormat + 'Season ' + currentSeason + ' End\n'
    scheduleSaveFormat = scheduleSaveFormat + "\n"
    
    return scheduleSaveFormat

    
#Send in gameState, current week as an int, and current game as an int
#Return the result of which team won and lost as a string
def getMatchup(gameState, week, game):
    team1 = "team 1"
    team2 = "team 2"
    matchup = "team1   W   -   L   team2"
    game = (game * 2) - 1
    
    if week <= 21: 
        schedule = gameState[4]
        numOfTeamsPlayingWeekly = 22
        index = ((week * numOfTeamsPlayingWeekly) - numOfTeamsPlayingWeekly) + (game) - 1
    elif week <= 27:
        schedule = saveGame.getPlayoffSchedule(gameState)
        numOfTeamsPlayingWeekly = 8
        index = game - 1
    elif week <= 37:
        schedule = saveGame.getPlayoffSchedule(gameState)
        numOfTeamsPlayingWeekly = 4
        index = game - 1
    
    scheduleList = list(schedule.split(" "))
    scheduleListlength = len(scheduleList)

    
    #print("team1: ", scheduleList[index])
    team1 = scheduleList[index]
    #print("team2: ", scheduleList[index])
    team2 = scheduleList[index + 1]

    #Check each teams WLRSeason for the current week to see if they won or lost previously
    #If game not yet played indicated as 

    #Get team1object from name
    for t in gameState[3]:
        if t.getTeamName() == team1:
            team1Object = t
            break
    #Get team1 weekly result
    if(team1 != "None"):
        team1Results = team1Object.getWLSeason()
        team1ResultsList = team1Results.split("-")
        if week <= 21:
            team1Result = team1ResultsList[week - 1]
        else:
            team1Result = team1ResultsList[week - 22]
    else:
        team1Result = " "

    if team1Result == "\n" or "3":
        team1Result = " "
    elif team1Result == "1":
        team1Result = "W"
    elif team1Result == "0":
        team1Result = "L"
    elif team1Result == "2":
        team1Result = "B"

    #Get team2object from name
    for t in gameState[3]:
        if t.getTeamName() == team2:
            team2Object = t
            break
    #Get team2 weekly result
    if(team2 != "None"):
        team2Results = team2Object.getWLSeason()
        team2ResultsList = team2Results.split("-")
        if week <= 21:
            team2Result = team2ResultsList[week - 1]
        else:
            team2Result = team2ResultsList[week - 22]
    else:
        team2Result = " "

    if team2Result == "\n" or "3":
        team2Result = " "
    elif team2Result == "1":
        team2Result = "W"
    elif team2Result == "0":
        team2Result = "L"
    elif team2Result == "2":
        team2Result = "BYE"

    matchup = team1 + "  " + team1Result + "  -  " + team2Result + "  " + team2

    return matchup

#in this function you send in a week number and a team name and get the opposing team for the team sent that week
def getmatchupSpecific(gameState, week, team):
    schedule = gameState[4]
    team1 = "team 1"
    team2 = "team 2"
    scheduleList = list(schedule.split(" "))

    #Get Current Week
    currentWeek = week
    floatWeek = float(currentWeek)
    intWeek = int(floatWeek)
    weekCount = intWeek
    
    if intWeek <= 21:
        for i in range(len(scheduleList)):
            if (scheduleList[i] == team):#searches list for index of players team, continues to next instance of team name until instance equals week
                if (weekCount == 1):
                    if i%2 == 0:                    #checks if players team is an odd or even integer. If even their opponent is the next index, or vice versa
                        team2 = scheduleList[i + 1]
                        break
                    else:
                        team2 = scheduleList[i - 1]
                        break
                else:
                    weekCount = weekCount - 1
        return team2
    
    if intWeek > 21:
        #check if team is playing this week
        schedule = saveGame.getPlayoffSchedule(gameState)
        scheduleList = list(schedule.split(" "))
        team2 = "tbd"
        for i in range(len(scheduleList)):
            if (scheduleList[i] == team):#searches list for index of players team, continues to next instance of team name until instance equals week
                if (weekCount == 22):
                    if i%2 == 0:                    #checks if players team is an odd or even integer. If even their opponent is the next index, or vice versa
                        team2 = scheduleList[i + 1]
                        break
                    else:
                        team2 = scheduleList[i - 1]
                        break
                else:
                    weekCount = weekCount - 1

        return team2


def assignPlayoffSeeds(gameState):
    #Get a copy of the original data
    oldData = []
    for i in range(len(gameState[3])):
        oldData.append(gameState[3][i].getCacheString())
    #Assign playoffSeed to each team
    #Sort teams by wins ascending
    gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "wins season")
    #Create copy of list
    sortedTeams = list(gameState[3])
    for x in range(len(sortedTeams)):
        for i in range(len(gameState[3])):
            #Skip over itself
            if sortedTeams[x] != gameState[3][i]:
                #Check each team if wins are equal
                if sortedTeams[x].getWinsSeason() == gameState[3][i].getWinsSeason():
                    #If wins equal then sort by higher goals
                    if sortedTeams[x].goalsSeason > gameState[3][i].goalsSeason:
                        sortedTeams[i], sortedTeams[x] = sortedTeams[x], sortedTeams[i]
                        #If goals equal then sort by higher shots
                        if sortedTeams[x].shotsSeason > gameState[3][i].shotsSeason:
                            sortedTeams[i], sortedTeams[x] = sortedTeams[x], sortedTeams[i]
                            #If shots equal then sort by higher saves
                            if sortedTeams[x].savesSeason > gameState[3][i].savesSeason:
                                sortedTeams[i], sortedTeams[x] = sortedTeams[x], sortedTeams[i]
                                #If saves equal then sort by higher assists
                                if sortedTeams[x].assistsSeason > gameState[3][i].assistsSeason:
                                    sortedTeams[i], sortedTeams[x] = sortedTeams[x], sortedTeams[i]
                                    #If all stats equal then higher seed is kept as is

    for i in range(len(sortedTeams)):
        sortedTeams[i].setPlayoffSeed(i + 1)

    #update save file with updated team data
    gameState[3] = sortedTeams
    saveGame.rewriteTeams(gameState, oldData)
    print("Playoff Seeds Assigned")
    return gameState

        
#generates a string to be appended to save file
def generatePlayoffSchedule(gameState):

    #get current week
    currentWeek = saveGame.getWeek(gameState)
    intWeek = int(currentWeek)

    newPlayoffScheduleString = []
    oldPlayoffScheduleString = []

    if (intWeek == 21):
        #assign playoff seeds to all team objects
        assignPlayoffSeeds(gameState)
        #find and add each team by seed to playoff schedule
        notComplete = True
        while notComplete:
            for i in range(len(gameState[3])):
                seed = gameState[3][i].getPlayoffSeed()
                if ((len(newPlayoffScheduleString) == 0) and int(seed) == 5):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    break
                if ((len(newPlayoffScheduleString) == 1) and int(seed) == 12):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    break
                if ((len(newPlayoffScheduleString) == 2) and int(seed) == 6):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    break
                if ((len(newPlayoffScheduleString) == 3) and int(seed) == 11):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    break
                if ((len(newPlayoffScheduleString) == 4) and int(seed) == 7):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    break
                if ((len(newPlayoffScheduleString) == 5) and int(seed) == 10):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    break
                if ((len(newPlayoffScheduleString) == 6) and int(seed) == 8):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    break
                if ((len(newPlayoffScheduleString) == 7) and int(seed) == 9):
                    newPlayoffScheduleString.append(gameState[3][i].getTeamName())
                    notComplete = False
                    break

        #after adding the teams for the first round of playoffs, add "tbd" for each schedule position after the first round
        #two more rounds with eight teams in eight finals is 8 "tbd"s, 3 rounds with 8 teams for additional 12 "tbd"s for
        #quarters, semis is four teams with 5 rounds so 10 "tbd"s, and finals is the same amount as semis so 10 more "tbds"
        #with a total of potiential of 44 playoff games, but the first 8 games are already on the schedule so 36 playoff games
        #so 36*2(2 teams play each game) = 72 'tbd' will be added to the schedule

        for i in range(72):
            newPlayoffScheduleString.append("tbd")

    if (intWeek == 22):
        #schedule is the same as previous week, no changes needed.
        newPlayoffScheduleString = saveGame.getPlayoffSchedule(gameState)
        newPlayoffScheduleString = list(newPlayoffScheduleString.split(" "))
        for i in range(8):
            newPlayoffScheduleString[i + 8] = newPlayoffScheduleString[i]

    if (intWeek == 23):
        newPlayoffScheduleString = saveGame.getPlayoffSchedule(gameState)
        newPlayoffScheduleString = list(newPlayoffScheduleString.split(" "))
        notComplete = True
        for i in range(len(gameState[3])):
            seed = gameState[3][i].getPlayoffSeed()
            if (int(seed) == 5):
                game1result = gameState[3][i].getGameResult(22) #Add This
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[16] = "None"
                    newPlayoffScheduleString[17] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(50)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file

                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[16] = "None"
                    newPlayoffScheduleString[17] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[16] = (gameState[3][i].getTeamName())
            if (int(seed) == 12):
                game1result = gameState[3][i].getGameResult(22)
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[16] = "None"
                    newPlayoffScheduleString[17] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(50)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[16] = "None"
                    newPlayoffScheduleString[17] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[17] = (gameState[3][i].getTeamName())
            if (int(seed) == 6):
                game1result = gameState[3][i].getGameResult(22)
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[18] = "None"
                    newPlayoffScheduleString[19] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(60)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[18] = "None"
                    newPlayoffScheduleString[19] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[18] = (gameState[3][i].getTeamName())
            if (int(seed) == 11):
                game1result = gameState[3][i].getGameResult(22)
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[18] = "None"
                    newPlayoffScheduleString[19] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(60)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[18] = "None"
                    newPlayoffScheduleString[19] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[19] = (gameState[3][i].getTeamName())
            if (int(seed) == 7):
                game1result = gameState[3][i].getGameResult(22)
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[20] = "None"
                    newPlayoffScheduleString[21] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(70)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[20] = "None"
                    newPlayoffScheduleString[21] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[20] = (gameState[3][i].getTeamName())
            if (int(seed) == 10):
                game1result = gameState[3][i].getGameResult(22)
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[20] = "None"
                    newPlayoffScheduleString[21] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(70)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[20] = "None"
                    newPlayoffScheduleString[21] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[21] = (gameState[3][i].getTeamName())
            if (int(seed) == 8):
                game1result = gameState[3][i].getGameResult(22)
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[22] = "None"
                    newPlayoffScheduleString[23] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(80)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[22] = "None"
                    newPlayoffScheduleString[23] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[22] = (gameState[3][i].getTeamName())
            if (int(seed) == 9):
                notComplete = False
                game1result = gameState[3][i].getGameResult(22)
                game2result = gameState[3][i].getGameResult(23)
                #check if last 2 games where both wins or losses, if so no game necessary next week, else add them to next weeks schedule
                if ((game1result == 1) and (game2result == 1)):
                    newPlayoffScheduleString[22] = "None"
                    newPlayoffScheduleString[23] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(80)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif ((game1result == 0) and (game2result == 0)):
                    newPlayoffScheduleString[22] = "None"
                    newPlayoffScheduleString[23] = "None"
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                else:
                    newPlayoffScheduleString[23] = (gameState[3][i].getTeamName())

    if (intWeek == 24):
        newPlayoffScheduleString = saveGame.getPlayoffSchedule(gameState)
        newPlayoffScheduleString = list(newPlayoffScheduleString.split(" "))
        newPlayoffScheduleString[8] = newPlayoffScheduleString[8].strip()
        notComplete = True
        #while notComplete:
        for i in range(len(gameState[3])):
            seed = gameState[3][i].getPlayoffSeed()
            #add top 4 seeded teams to schedule for start of quarterfinals
            if (int(seed) == 1):
                newPlayoffScheduleString[24] = gameState[3][i].getTeamName()
            if (int(seed) == 2):
                newPlayoffScheduleString[26] = gameState[3][i].getTeamName()
            if (int(seed) == 3):
                newPlayoffScheduleString[28] = gameState[3][i].getTeamName()
            if (int(seed) == 4):
                newPlayoffScheduleString[30] = gameState[3][i].getTeamName()
            #add any teams that won in two games in previous round of playoffs and have a bye this week
            if (int(seed) == 50):
                newPlayoffScheduleString[25] = gameState[3][i].getTeamName()
            if (int(seed) == 60):
                newPlayoffScheduleString[27] = gameState[3][i].getTeamName()
            if (int(seed) == 70):
                newPlayoffScheduleString[29] = gameState[3][i].getTeamName()
            if (int(seed) == 80):
                newPlayoffScheduleString[31] = gameState[3][i].getTeamName()

            if (int(seed) == 5):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[25] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(50)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
            if (int(seed) == 12):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[25] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(50)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
        
            if (int(seed) == 6):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[27] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(60)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
            if (int(seed) == 11):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[27] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(60)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file

            if (int(seed) == 7):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[29] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(70)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
            if (int(seed) == 10):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[29] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(70)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file

            if (int(seed) == 8):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[31] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(80)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
            if (int(seed) == 9):
                game1result = gameState[3][i].getGameResult(24)
                #check if last game was a win or loss, if win, add them to schedule, if not eliminate them
                if (game1result == 1):
                    newPlayoffScheduleString[31] = gameState[3][i].getTeamName()
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(80)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                elif (game1result == 0):
                    #update cache and save file with new seed
                    oldData = gameState[3][i].getCacheString()
                    gameState[3][i].setPlayoffSeed(13)
                    gameState[3][i].setPrevPlayoffPos(13)
                    newData = gameState[3][i].getCacheString()
                    saveData.replaceLine(gameState, oldData, newData)   #replaces old team data with new team data to save file
                    
    if (intWeek == 25):
        #schedule is the same as previous week, no changes needed.
        newPlayoffScheduleString = saveGame.getPlayoffSchedule(gameState)
        newPlayoffScheduleString = list(newPlayoffScheduleString.split(" "))
        for i in range(8):
            newPlayoffScheduleString[(i + 24) + 8] = newPlayoffScheduleString[i + 24]  
              


    #After playoff string is updated for the week save it so save file
    newPlayoffScheduleString = ' '.join(newPlayoffScheduleString)
    newPlayoffScheduleString = newPlayoffScheduleString + '\n'
    saveGame.updatePlayoffSchedule(gameState, newPlayoffScheduleString)





    


    