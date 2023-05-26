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
def write(gameState, dataType, newData, multiple = 1):
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
    skips = 0   #counts number of dataType matches to skip
    skipsTotal = 1  #counts number of times through the loop to add 


    #print(lines)
    while multiple > 0:
        print ("multiple: ", multiple)
        while found == False:                       #checks each line from txt file to see if it matches the data type thats being searched for
            #print("line", count, ":", lines[count])
            currentLine = lines[count]
            if currentLine == dataType:
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
    
    #for index in lines:
        #gameData.write(lines[index])

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

#read specific line from file
#input row number integer
def read(gameState, row):
    print("in new saveData.read row")
    #get file path
    path = getSaveFilePath(gameState)
    gameData = open(path, 'r')
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
    path = getSaveFilePath(gameState)
    gameData = open(path, 'r')
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
    #get file path
    path = getSaveFilePath(gameState)
    gameData = open(path, 'a')
    gameData.write(newData)
    print("new data appended")
    gameData.close