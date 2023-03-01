#Import pygame & other functions
import pygame, sys
import startMenu
import helpMenu
import settingsMenu
import lockerRoomMenu
import deleteSaveMenu
import createProfileMenu

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
backgroundimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\blackvectorbackground.jpg')
buttonimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\blankbutton.png')
button2img = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\blankbutton2.png')
trophyimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\rltrophy2.png')
helptxt1img = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\helpText1.png')
helptxt2img = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\helpText2.png')
upArrowUIimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\upArrowUI.png')
leftArrowUIimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\leftArrowUI.png')
rightArrowUIimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\rightArrowUI.png')
downArrowUIimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\downArrowUI.png')
xButtonUIimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\xButtonUI.png')
barracudasLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\barracudasLogo.png')
bearsLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\bearsLogo.png')
bombersLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\bombersLogo.png')
crusadorsLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\crusadorsLogo.png')
cyclonesLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\cyclonesLogo.png')
destroyersLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\destroyersLogo.png')
dragonsLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\dragonslogo.png')
expressLogoimg = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\expressLogo.png')
guardiansLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\guardiansLogo.png')
mammothsLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\mammothsLogo.png')
monarchsLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\monarchsLogo.png')
pharosLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\pharosLogo.png')
predatorsLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\predatorsLogo.png')
ravagersLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\ravagersLogo.png')
reapersLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\reapersLogo.png')
rebelsLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\rebelsLogo.png')
roversLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\roversLogo.png')
scorpiansLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\scorpiansLogo.png')
seekersLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\seekersLogo.png')
skyhawksLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\skyhawksLogo.png')
wolvesLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\wolvesLogo.png')
but1 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but1.png')
but2 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but2.png')
but3 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but3.png')
but4 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but4.png')
but5 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but5.png')
but6 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but6.png')
but7 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but7.png')
but8 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but8.png')
but9 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but9.png')
but0 = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but0.png')
but1S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but1S.png')
but2S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but2S.png')
but3S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but3S.png')
but4S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but4S.png')
but5S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but5S.png')
but6S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but6S.png')
but7S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but7S.png')
but8S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but8S.png')
but9S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but9S.png')
but0S = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\but0S.png')
butQ = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butQ.png')
butW = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butW.png')
butE = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butE.png')
butR = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butR.png')
butT = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butT.png')
butY = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butY.png')
butU = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butU.png')
butI = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butI.png')
butO = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butO.png')
butP = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butP.png')
butA = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butA.png')
butS = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butS.png')
butD = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butD.png')
butF = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butF.png')
butG = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butG.png')
butH = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butH.png')
butJ = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butJ.png')
butK = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butK.png')
butL = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butL.png')
butZ = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butZ.png')
butX = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butX.png')
butC = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butC.png')
butV = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butV.png')
butB = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butB.png')
butN = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butN.png')
butM = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butM.png')
butSpace = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butSpace.png')
butBack = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butBack.png')
butCaps = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\butCaps.png')


#create list of all keyboard keys
keyBoardKeysRaw = [but1, but2, but3, but4, but5, but6, but7, but8, but9, but0, but1S, but2S, but3S, but4S, but5S, but6S, but7S, but8S, but9S, but0S,
                butQ, butW, butE, butR, butT, butY, butU, butI, butO, butP, butA, butS, butD, butF, butG ,butH, butJ, butK, butL, butZ, butX, butC, butV, butB, butN, butM, butBack, butCaps]
#updated list of all keyboard keys after resize
keyBoardKeys = []

#resize images
trophyimg = pygame.transform.scale(trophyimg, (319, 400))
helptxt1img = pygame.transform.scale(helptxt1img, (1100, 77))
helptxt2img = pygame.transform.scale(helptxt2img, (1100, 77))
xButtonUIimg = pygame.transform.scale(xButtonUIimg, (50, 50))
butSpace = pygame.transform.scale(butSpace, (400, 50))

#resize list of key buttons
keySize = 75
for i in range(len(keyBoardKeysRaw)):
    print("i: ", i)
    keyBoardKeysRaw[i] = pygame.transform.scale(keyBoardKeysRaw[i], (keySize, keySize))
    keyBoardKeys.append(keyBoardKeysRaw[i])
#add space to end of list
keyBoardKeys.append(butSpace)





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
            startMenu.startMenuFunc(gameState, win, basicFont, backgroundimg, trophyimg, buttonimg, button2img, xButtonUIimg)
            print('exit start menu')
        if gameState[1] == 'exit':
            print('exit game')
            sys.exit()
        if gameState[1] == 'howToPlay':
            print('run how to play menu')
            helpMenu.helpMenuFunc(gameState, win, basicFont, backgroundimg, helptxt1img, helptxt2img, buttonimg, button2img)
            print('exit how to play menu')
        if gameState[1] == 'settings':
            print('run settings menu')
            settingsMenu.settingsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit settings menu')
        if gameState[1] == 'deleteSave':
            print('run delete save menu')
            deleteSaveMenu.deleteSaveMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit delete save menu')
        if gameState[1] == 'newSave':
            print('run new game menu')
            createProfileMenu.createProfileMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, keyBoardKeys, keyBoardKeys) #sends in same sprites for hover keys atm
            print('exit new save menu')
        if gameState[1] == 'openSave':
            print('run locker room menu')
            lockerRoomMenu.lockerRoomMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit locker room menu')


        #pygame.display.update()
        #mainClock.tick(60)

main(gameState)

