#read and write data to save file

#new write function which creates a list of the lines from the data sheet, and then replaces the data at the correct index, then rewrites it onto the txt document
def write(gameState, dataType, newData, multiple):
    print("in new saveData.write")
    #print("file: ", gameState[0])
    #print("dataType searching for:", dataType)
    #chooses which data file to open based on gameState
    gameData = open(gameState[0], 'r+')
    #convert newData to string
    newData = str(newData)
    #get list of data
    lines = gameData.readlines()
    found = False
    count = 0

    #print(lines)
    if multiple >= 1:
    #checks each line from txt file to see if it matches the data type thats being searched for
        while found == False:
            if count <= len(lines):
                #print("line ", count, ":", lines[count])
                currentLine = lines[count]
                if currentLine == dataType:
                    found = True
                #print("found: ", found)
                if found == True:
                    lines[count + 1] = newData + "\n"#when dataTypes match the list is updated with the new data (+1 is added to count because data is stored in the index after the data type)

                count = count + 1
            else:
                print("Data Type:", dataType, "is not in file")
        #print(lines)
        #Now that the data location has been found the list will be rewritten onto the txt file
        with open(gameState[0], "w") as gameData:
            for line in lines:
                gameData.write(line)
        multiple = multiple - 1
    
    #for index in lines:
        #gameData.write(lines[index])

#create function which creates a new txt document with newData added
def create(gameState, newData):
    print("in new saveData.create")
    #print("file: ", gameState[0])
    #chooses which data file to open based on gameState
    gameData = open(gameState[0], 'a+')
    #convert newData to string
    newData = str(newData)
    gameData.write(newData)

#read specific line from file
#input row number integer
def read(gameState, row):
    print("in new saveData.read row")
    gameData = open(gameState[0], 'r')
    count = 0
    text = "null"
    setRow = row
    while row > 0:
        #print("row: ", row)
        #print("count: ", count)
        text = gameData.readline()
        #print("text: ", text)
        row = row - 1
    #print ("text from row ", setRow, ": ", text)
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
        #print("text: ", text)
        #print("string: ", testStr)
        if flag == True:
            found = True
        if text == testStr:
            flag = True
        if count > 1000:
            found = True
            text = "null"
        count = count + 1
        #print("found: ", found)

    #print (testStr, text)
    gameData.close()
    return text
#return string from specified row

#append new data to end of save file
def append(gameState, newData):
    print("in saveData.append")
    gameData = open(gameState[0], 'a')
    gameData.write(newData)
    print("new data appended")
    gameData.close