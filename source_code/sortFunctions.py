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

    if dataType == "player goals career":
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

    if dataType == "player assists career":
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

    if dataType == "player saves career":
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

    if dataType == "player shots career":
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

    if dataType == "player goals season":
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

    if dataType == "player assists season":
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

    if dataType == "player saves season":
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

    if dataType == "player shots season":
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

    if dataType == "player goals career":
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

    if dataType == "player assists career":
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

    if dataType == "player saves career":
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

    if dataType == "player shots career":
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

    if dataType == "player goals season":
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

    if dataType == "player assists season":
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

    if dataType == "player saves season":
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

    if dataType == "player shots season":
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