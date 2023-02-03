#Import pygame & other functions
from pickletools import string4
import pygame, sys
import startMenu
import helpMenu
import settingsMenu
import lockerRoomMenu
import saveData
import newGameMenu
import updateSave

#Setup pygame
#mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("RLCS Simulator Alpha")
WIN_WIDTH = 1280
WIN_HEIGHT = 720
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#Set up the basic text font
basicFont = pygame.font.SysFont(None,64)
smallFont = pygame.font.SysFont(None,32) #Fits about 150 characters per line at 32 font size

#Import Images
backgroundimg = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\blackvectorbackground.jpg')
buttonimg = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\blankbutton.png')
button2img = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\blankbutton2.png')
trophyimg = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\rltrophy2.png')
helptxt1img = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\helpText1.png')
helptxt2img = pygame.image.load(r'C:\Users\bmdro\Documents\Visual Studio Code\Project_RLCSS\images\helpText2.png')

#resize images
trophyimg = pygame.transform.scale(trophyimg, (319, 400))
helptxt1img = pygame.transform.scale(helptxt1img, (1100, 77))
helptxt2img = pygame.transform.scale(helptxt2img, (1100, 77))

#Create gamestate
gameState = ['gameData1.txt', 'start'] #[current save, current menu]

#####################
# F U N C T I O N S #
#####################

#get image length and height
def imgDim(img):
    imgWid = img.get_width()
    imgHei = img.get_height()
    return imgWid, imgHei

#check if new save
def checkNewSave(gameState):
    if gameState[0] == 'gameData1.txt':
        saveNum = 1
    if gameState[0] == 'gameData2.txt':
        saveNum = 2
    if gameState[0] == 'gameData3.txt':
        saveNum = 3
    saveNum = str(saveNum)
    saveState = "save " + saveNum + "\n"
    print ("saveState: ", saveState)
    newSave = saveData.read(gameState, saveState)
    print("newSave: ", newSave)
    return newSave

#main
def main(gameState):
    #sets default gamestate ['save file', 'current menu']
    gameState = gameState
    print(gameState)

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Displays current menu
        if gameState[1] == 'start':
            print('run start menu')
            startMenu.startMenuFunc(gameState, win, basicFont, backgroundimg, trophyimg, buttonimg, button2img)
            print('exit start menu')
        if gameState[1] == 'howToPlay':
            print('run how to play menu')
            helpMenu.helpMenuFunc(gameState, win, basicFont, backgroundimg, helptxt1img, helptxt2img, buttonimg, button2img)
            print('exit how to play menu')
        if gameState[1] == 'settings':
            print('run settings menu')
            settingsMenu.settingsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit settings menu')
        if gameState[1] == 'openSave':
            #check if save file is new
            newSave = checkNewSave(gameState)
            print("new save", newSave)
            if newSave == " 0":
                print('run new game menu')
                newGameMenu(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
                newSave = updateSave(gameState, newSave)
            print('run locker room menu')
            lockerRoomMenu.lockerRoomMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit locker room menu')


        #pygame.display.update()
        #mainClock.tick(60)

main(gameState)

