#generate round robin schedule for the season
import random
import saveGame

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
    scheduleSaveFormat = scheduleSaveFormat
    
    return scheduleSaveFormat

    
#Send in gameState, current week as an int, and current game as an int
#Return the result of which team won and lost as a string
def getMatchup(gameState, week, game):
    schedule = gameState[4]
    team1 = "team 1"
    team2 = "team 2"
    matchup = "team1   W   -   L   team2"
    scheduleList = list(schedule.split(" "))
    numOfTeamsPlayingWeekly = 22
    game = (game * 2) - 1

    scheduleListlength = len(scheduleList)

    index = ((week * numOfTeamsPlayingWeekly) - numOfTeamsPlayingWeekly) + (game) - 1
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
        team1Result = team1ResultsList[week - 1]
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
        team2Result = team2ResultsList[week - 1]
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
    numOfTeamsPlayingWeekly = 22
    
    for i in range(numOfTeamsPlayingWeekly):
        if scheduleList[i] == team:         #searches list for index of players team
            if i%2 == 0:                    #checks if players team is an odd or even integer. If even their opponent is the next index, or vice versa
                team2 = scheduleList[i + 1]
            else:
                team2 = scheduleList[i - 1]
    
    return team2