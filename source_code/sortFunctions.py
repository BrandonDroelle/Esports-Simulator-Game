def sortAscendingObjectList(objectList, dataType):

    pos1 = 0
    pos2 = 0

    if dataType == "player names":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getName().lower() < objectList[x].getName().lower():
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "player team":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getCurrentTeam().lower() < objectList[x].getCurrentTeam().lower():
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "team name":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getTeamName().lower() < objectList[x].getTeamName().lower():
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wlr career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if str(objectList[i].getWLRCareer()) <= str(objectList[x].getWLRCareer()):
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wins career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getWinsCareer() <= objectList[x].getWinsCareer():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "losses career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getLossesCareer() <= objectList[x].getLossesCareer():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "goals career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getGoalsCareer() <= objectList[x].getGoalsCareer():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "assists career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getAssistsCareer() <= objectList[x].getAssistsCareer():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "saves career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getSavesCareer() <= objectList[x].getSavesCareer():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "shots career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getShotsCareer() <= objectList[x].getShotsCareer():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wlr season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if str(objectList[i].getWLRSeason()) <= str(objectList[x].getWLRSeason()):
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wins season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getWinsSeason() <= objectList[x].getWinsSeason():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "losses season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getLossesSeason() <= objectList[x].getLossesSeason():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "goals season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getGoalsSeason() <= objectList[x].getGoalsSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "assists season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getAssistsSeason() <= objectList[x].getAssistsSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "saves season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getSavesSeason() <= objectList[x].getSavesSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "shots season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getShotsSeason() <= objectList[x].getShotsSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj


    return objectList

def sortDescendingObjectList(objectList, dataType):

    pos1 = 0
    pos2 = 0

    if dataType == "player names":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getName().lower() > objectList[x].getName().lower():
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "player team":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getCurrentTeam().lower() > objectList[x].getCurrentTeam().lower():
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "team name":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getTeamName().lower() > objectList[x].getTeamName().lower():
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wlr career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if str(objectList[i].getWLRCareer()) >= str(objectList[x].getWLRCareer()):
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wins career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getWinsCareer() >= objectList[x].getWinsCareer():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "losses career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getLossessCareer() >= objectList[x].getLossessCareer():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "goals career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getGoalsCareer() >= objectList[x].getGoalsCareer():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "assists career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getAssistsCareer() >= objectList[x].getAssistsCareer():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "saves career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getSavesCareer() >= objectList[x].getSavesCareer():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "shots career":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getShotsCareer() >= objectList[x].getShotsCareer():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wlr season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if str(objectList[i].getWLRSeason()) >= str(objectList[x].getWLRSeason()):
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "wins season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getWinsSeason() >= objectList[x].getWinsSeason():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "losses season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getLossesSeason() >= objectList[x].getLossesSeason():
                    print("dont swap")
                else:
                    print("swap")
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "goals season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getGoalsSeason() >= objectList[x].getGoalsSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "assists season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getAssistsSeason() >= objectList[x].getAssistsSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "saves season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getSavesSeason() >= objectList[x].getSavesSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj

    if dataType == "shots season":
        for i in range(len(objectList)):
            print("i: ", i)
            for x in range(len(objectList)):
                print("x: ", x)
                if objectList[i].getShotsSeason() >= objectList[x].getShotsSeason():
                    print("dont swap")
                else:
                    tempObj = objectList[i]
                    objectList[i] = objectList[x]
                    objectList[x] = tempObj


    return objectList