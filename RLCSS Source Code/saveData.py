#read and write data to save file

#write to file send(gameState, type of data, data to be added)
def write(gameState, dataType, newData):
    print("in saveData.write")
    print("file: ", gameState[0])
    print("dataType searching for: ", dataType)
    #chooses which data file to open based on gameState
    gameData = open(gameState[0], 'r+')
    found = False
    text = "null"
    count = 0
    flag = False

    #add /n to dataType string to match the txt document
    #dataType = dataType + "/n"

    while found == False:
        text = gameData.readline()
        print("current dataType: ", text)
        print("newData: ", newData)
        if flag == True:
            found = True
        if text == dataType:
            flag = True
        if count > 100:
            found = True
            text = "null"
        count = count + 1
        print("dataType found: ", found)

    print (newData, text)

    gameData.write("test 1")
    gameData.close()

#

#read specific line from file
#input row number integer
def read(gameState, row):
    gameData = open(gameState[0], 'r')
    count = 0
    text = "null"
    setRow = row
    while row > 0:
        print("row: ", row)
        print("count: ", count)
        text = gameData.readline()
        print("text: ", text)
        row = row - 1
    print ("text from row ", setRow, ": ", text)
    gameData.close()
    return text
#return string from specified row

#read specific line from file after set string
#input string, will read the data in the row below
def read(gameState, testStr):
    print("in saveData.read String")
    gameData = open(gameState[0], 'r')
    found = False
    text = "null"
    count = 0
    flag = False

    while found == False:
        text = gameData.readline()
        print("text: ", text)
        print("string: ", testStr)
        if flag == True:
            found = True
        if text == testStr:
            flag = True
        if count > 1000:
            found = True
            text = "null"
        count = count + 1
        print("found: ", found)

    print (testStr, text)
    gameData.close()
    return text
#return string from specified row