#read and write data to save file
import os

def printSaveFilePath():
    print('Get current working directory: ', os.getcwd())

def printFilesInCurrentDirectory():
    path = os.getcwd()
    path = path + "\saves\\"
    dirList = os.listdir(path)
    print("Files in current directory: ", dirList)

def getSaveFilePath(gameState):
    path = os.getcwd()
    path = path + "\saves\\" + gameState[0]
    return path
    #"C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)"
    #"C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\saves\\" + gameState[0]

#new write function which creates a list of the lines from the data sheet, and then replaces the data at the correct index, then rewrites it onto the txt document
def write(gameState, dataType, newData, multiple = 1, exception = "RLCS Save Data\n"):
    #multiple is used to write the same data multiple times
    print("in new saveData.write")
    #print("file: ", gameState[0])
    #print("dataType searching for:", dataType)
    #get file path
    path = getSaveFilePath(gameState)
    #print("Current path: ", path)
    #printFilesInCurrentDirectory()
    #chooses which data file to open based on gameState
    gameData = open(path, 'r+')
    #convert newData to string
    newData = str(newData)
    #get list of data
    lines = gameData.readlines()
    found = False
    count = 0   #counts current line in save file
    exceptionFlag = False #This is False the the string exception has not been read yet

    #print(lines)
    while multiple > 0:
        #print ("multiple: ", multiple)
        while found == False:                       #checks each line from txt file to see if it matches the data type thats being searched for
            print("line", count, ":", lines[count])
            currentLine = lines[count]
            if currentLine == exception:            #checks current line for exception
                exceptionFlag = True
            if currentLine == dataType:             #check current line for data type
                if exceptionFlag == True:           #checks that the exception has been passed before allowing data to be written
                   found = True
            #print("found: ", found)
            if found == True:
                    lines[count + 1] = newData + "\n" #when dataTypes match the list is updated with the new data (+1 is added to count because data is stored in the index after the data type)
                    #Now that the data location has been found the list will be rewritten onto the txt file
                    with open(path, "w") as gameData:
                        for line in lines:
                            gameData.write(line)
            count = count + 1
        #reset lines with new data
        gameData = open(path, 'r+')
        newData = str(newData)
        lines = gameData.readlines()
        found = False
        multiple = multiple - 1
    #print(lines)

#delete function which creates a list of the lines from the data sheet, and then deletes the data at the correct index, then rewrites it onto the txt document
def deleteLine(gameState, dataType, multiple = 1, exception = "RLCS Save Data\n"):
    #multiple is used to write the same data multiple times
    print("in new saveData.deleteLine")
    #get file path
    path = getSaveFilePath(gameState)
    #chooses which data file to open based on gameState
    gameData = open(path, 'r+')
    #convert newData to string
    #get list of data
    lines = gameData.readlines()
    found = False
    count = 0   #counts current line in save file
    exceptionFlag = False #This is False the the string exception has not been read yet

    #print(lines)
    while multiple > 0:
        #print ("multiple: ", multiple)
        while found == False:                       #checks each line from txt file to see if it matches the data type thats being searched for
            print("line", count, ":", lines[count])
            currentLine = lines[count]
            if currentLine == exception:            #checks current line for exception
                exceptionFlag = True
            if currentLine == dataType:             #check current line for data type
                if exceptionFlag == True:           #checks that the exception has been passed before allowing data to be written
                   found = True
            #print("found: ", found)
            if found == True:
                    del lines[count] #when dataTypes match the current list index is deleted from the list
                    #Now that the data location has been found the list will be rewritten onto the txt file without the selected line
                    with open(path, "w") as gameData:
                        for line in lines:
                            gameData.write(line)
            count = count + 1
        #reset lines with new data
        gameData = open(path, 'r+')
        lines = gameData.readlines()
        found = False
        multiple = multiple - 1
    #print(lines)

#replace function which creates a list of the lines from the data sheet, and then replaces the data at the correct index, then rewrites it onto the txt document
def replaceLine(gameState, dataType, newData, multiple = 1, exception = "RLCS Save Data\n"):
    #multiple is used to write the same data multiple times
    print("in new saveData.replaceLine")
    #get file path
    path = getSaveFilePath(gameState)
    #chooses which data file to open based on gameState
    gameData = open(path, 'r+')
    #convert newData to string
    #get list of data
    lines = gameData.readlines()
    found = False
    count = 0   #counts current line in save file
    exceptionFlag = False #This is False the the string exception has not been read yet

    #print(lines)
    while multiple > 0:
        #print ("multiple: ", multiple)
        while found == False:                       #checks each line from txt file to see if it matches the data type thats being searched for
            print("line", count, ":", lines[count])
            currentLine = lines[count]
            if currentLine == exception:            #checks current line for exception
                exceptionFlag = True
            if currentLine == dataType:             #check current line for data type
                if exceptionFlag == True:           #checks that the exception has been passed before allowing data to be written
                   found = True
            #print("found: ", found)
            if found == True:
                    lines[count] = newData#when dataTypes match the current list index is deleted from the list
                    #Now that the data location has been found the list will be rewritten onto the txt file without the selected line
                    with open(path, "w") as gameData:
                        for line in lines:
                            gameData.write(line)
            count = count + 1
        #reset lines with new data
        gameData = open(path, 'r+')
        lines = gameData.readlines()
        found = False
        multiple = multiple - 1
    #print(lines)

#create function which creates a new txt document with newData added
def create(gameState, newData):
    print("in new saveData.create")
    #print("file: ", gameState[0])
    #get file path
    path = getSaveFilePath(gameState)
    print("file path: ", path)
    #chooses which data file to open based on gameState
    gameData = open(path, 'a+')
    #convert newData to string
    newData = str(newData)
    gameData.write(newData)

#read specific line from file after set string
#input string, will read the data in the row below
#gameState = to know which save file to read
#dataType = to know what kind of data you are searching for
#multiple = number of times you want to skip the dataType you are looking for before you read the data
    #For instance when set to 1 it reads the first instance of the DataType,
    #but when set to 3 it reads the 3rd instance of the dataType skipping over the first 2
#exception = dont start searching for dataType until the exception is read
#extraRows = once dataType is found this is how many extra rows to read over before sending that specific line of data
def read(gameState, dataType, multiple = 1, exception = "RLCS Save Data\n", extraRows = 0):
    print("in saveData.read String")
    path = getSaveFilePath(gameState)
    gameData = open(path, 'r')
    found = False        #This represents if the data has been found so the loop can stop
    text = "null"
    count = 0
    flag = False          #this flag marks when the dataType is read so the loop goes one more time to read the data in the line below
    exceptionFlag = False #This is False the the string exception has not been read yet
    extraRowCount = extraRows

    while multiple > 0:
        while found == False:
            text = gameData.readline()
            print("Looking at: ", text)
            print("Searching for: ", dataType)
            print("Exception String: ", exception)
            print("Exception Flag: ", exceptionFlag)
            print("Multiple: ", multiple)
            print("Found Flag: ", flag)
            print("Found Variable: ", found)
            if text == exception:            #checks current line for exception
                exceptionFlag = True
            if flag == True:
                if multiple == 1:
                    found = True
                    multiple = multiple - 1
                if multiple > 1:
                    multiple = multiple - 1
                    flag = False
            if text == dataType:
                if exceptionFlag == True:    #checks that the exception has been passed before allowing data to be read
                    flag = True
            if count > 999999:
                found = True
                text = "null"
            count = count + 1
            print("found: ", found)

    if extraRows > 0:
        while extraRowCount > 0:
            text = gameData.readline()
            print("text: ", text)
            print("string: ", dataType)
            extraRowCount = extraRowCount - 1

    #print (testStr, text)
    gameData.close()
    return text
#return string from specified row

#append new data to end of save file
def append(gameState, newData):
    print("in saveData.append")
    #get file path
    path = getSaveFilePath(gameState)
    gameData = open(path, 'a')
    gameData.write(newData)
    print("new data appended")
    gameData.close
