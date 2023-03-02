#generate round robin schedule for the season
import random

def randomizeTeams(teams):
    print('in randomize teams')
    #print("teams: ", teams)
    random.shuffle(teams)
    #print("teams shuffle: ", teams)
    return teams

def printTeams(teams):
    print('teams: ', teams)

def generateRoundRobin(gameState, teams):

    #Randomize list of teams sent in
    teamsShuffle = teams.copy() #makes a copy of the teams list so the teams list stays in the original order
    teamsShuffle = randomizeTeams(teamsShuffle)
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
    print("SCHEDULE\n**********************")
    for i in range(sLength):
        print("Week:", i + 1)
        for j in range(rLength):
            game = ("{} {}".format(schedule[i][j][0],schedule[i][j][1]))
            print(game)
        print()

def getScheduleString(schedule):
    sLength = len(schedule)
    rLength = len(schedule[0])
    print("schedule[o]", schedule[0])
    print("schedule[o] length", rLength)
    scheduleSaveFormat = ""
    team = ''
    for i in range(sLength):
        print("Week:", i + 1)
        for j in range(rLength):
            game = ("{} {}".format(schedule[i][j][0],schedule[i][j][1]))
            print("game:", game)
            print("g", i + 1, 't', i+1, ':', schedule[i][j][0], schedule[i][j][1])
            homeTeam = str(schedule[i][j][0])
            awayTeam = str(schedule[i][j][1])
            print("home team:", homeTeam, "\naway team:", awayTeam)
            scheduleSaveFormat = scheduleSaveFormat + homeTeam + '\n' + awayTeam + '\n'
            print('scheduleSaveFormat:', scheduleSaveFormat)
    return scheduleSaveFormat