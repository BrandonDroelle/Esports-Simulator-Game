#Import pygame & other functions
import pygame, sys
import startMenu
import helpMenu
import settingsMenu
import lockerRoomMenu
import deleteSaveMenu
import createProfileMenu
import selectTeamMenu
import inGameSettingsMenu
import standingsMenu
import teamStatsMenu
import playerStatsMenu
import scheduleMenu
import hallOfFameMenu
import playerAwardsMenu
import gamePreviewMenu
import recordResultsMenu
import weeklyResultsMenu
import saveData

#check directory
saveData.printSaveFilePath()

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

barracudasLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\barracudasLogo.png')
bearsLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\bearsLogo.png')
bombersLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\bombersLogo.png')
crusadorsLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\crusadorsLogo.png')
cyclonesLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\cyclonesLogo.png')
destroyersLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\destroyersLogo.png')
dragonsLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\dragonslogo.png')
expressLogo = pygame.image.load(r'C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\images\expressLogo.png')
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

#create list of all team logos
teamLogosRaw = [barracudasLogo, bearsLogo, bombersLogo, crusadorsLogo, cyclonesLogo, destroyersLogo, dragonsLogo, expressLogo, guardiansLogo,
                mammothsLogo, monarchsLogo, pharosLogo, predatorsLogo, ravagersLogo, reapersLogo, rebelsLogo, roversLogo, scorpiansLogo,
                seekersLogo, skyhawksLogo, wolvesLogo]
#updated list of all team logos after resize
teamLogos = []

#resize images
trophyimg = pygame.transform.scale(trophyimg, (319, 400))
helptxt1img = pygame.transform.scale(helptxt1img, (1100, 77))
helptxt2img = pygame.transform.scale(helptxt2img, (1100, 77))
xButtonUIimg = pygame.transform.scale(xButtonUIimg, (50, 50))
butSpace = pygame.transform.scale(butSpace, (400, 50))

#resize list of key buttons
keySize = 75
for i in range(len(keyBoardKeysRaw)):
    #print("i: ", i)
    keyBoardKeysRaw[i] = pygame.transform.scale(keyBoardKeysRaw[i], (keySize, keySize))
    keyBoardKeys.append(keyBoardKeysRaw[i])
#add space to end of list
keyBoardKeys.append(butSpace)

#resize list of team logos
logoSize = 250
for i in range(len(teamLogosRaw)):
    #print("i: ", i)
    teamLogosRaw[i] = pygame.transform.scale(teamLogosRaw[i], (logoSize, logoSize))
    teamLogos.append(teamLogosRaw[i])

#list of teams (list of players found in selectTeamMenu)
teamNames = ['barracudas', 'bears', 'bombers', 'crusadors', 'cyclones', 'destroyers', 'dragons', 'express', 'guardians', 'mammoths', 'monarchs', 'pharos',
             'predators', 'ravagers', 'reapers', 'rebels', 'rovers', 'scorpians', 'seekers', 'skyhawks', 'wolves']

#list of players
playerNames = ['marley', 'casper', 'myrtle', 'samara', 'storm', 'fury', 'rainmaker', 'squall', 'hound', 'viper', 'imp', 'mountain', 'tusk', 'sabretooth',
               'beast', 'roundhouse', 'gerwin', 'c-block', 'centice', 'junker', 'foamer', 'sticks', 'boomer', 'caveman', 'rex', 'khan', 'Raja', 'sultan',
               'saltie', 'scout', 'swabbie', 'middy', 'bandit', 'outlaw', 'poncho', 'dude', 'buzz', 'armstrong', 'shepard', 'yuri', 'maverick', 'iceman',
               'goose', 'cougar', 'tex', 'merlin', 'stinger', 'hollywood', 'sundown', 'jester', 'heater', 'slider', 'chipper', 'wolfman', 'stig', 'clu',
               'fulcrum', 'alleycat', 'soap', 'echo', 'heavy', 'fives']

#create empty lists of team and player objects
playerObjects = [0]
teamObjects = [0]

#Create gamestate
gameState = ['gameData1.txt', 'start', playerObjects, teamObjects] #[current save, current menu, playersObjects, teamObjects]

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
            startMenu.startMenuFunc(gameState, win, basicFont, backgroundimg, trophyimg, buttonimg, button2img, xButtonUIimg, teamNames, playerNames)
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
        if gameState[1] == 'createProfile':
            print('run create profile menu')
            createProfileMenu.createProfileMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, keyBoardKeys, keyBoardKeys) #sends in same sprites for hover keys atm
            print('exit create profile menu')
        if gameState[1] == 'selectTeam':
            print('run select team menu')
            selectTeamMenu.selectTeamMenuFunc(gameState, win, basicFont, smallFont, backgroundimg, buttonimg, button2img, teamLogos, teamNames, playerNames)
            print('exit select team menu')
        if gameState[1] == 'lockerRoom':
            print('run locker room menu')
            lockerRoomMenu.lockerRoomMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, teamLogos, teamNames, playerNames)
            print('exit locker room menu')
        if gameState[1] == 'inGameSettings':
            print('run in game settings menu')
            inGameSettingsMenu.inGameSettingsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, playerNames)
            print('exit in game settings menu')
        if gameState[1] == 'standings':
            print('run standings menu')
            standingsMenu.standingsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit standings menu')
        if gameState[1] == 'teamStats':
            print('run Team Stats menu')
            teamStatsMenu.teamStatsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit team stats menu')
        if gameState[1] == 'playerStats':
            print('run player Stats menu')
            playerStatsMenu.playerStatsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit player stats menu')
        if gameState[1] == 'schedule':
            print('run schedule menu')
            scheduleMenu.scheduleMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit schedule menu')
        if gameState[1] == 'hallOfFame':
            print('run hall of fame menu')
            hallOfFameMenu.hallOfFameMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit hall of fame menu')
        if gameState[1] == 'playerAwards':
            print('run player awards menu')
            playerAwardsMenu.playerAwardsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit player awards menu')
        if gameState[1] == 'gamePreview':
            print('run game preview menu')
            gamePreviewMenu.gamePreviewMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit game preview menu')
        if gameState[1] == 'recordResults':
            print('run record results menu')
            recordResultsMenu.recordResultsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit record results menu')
        if gameState[1] == 'weeklyResults':
            print('run weekly results menu')
            weeklyResultsMenu.weeklyResultsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit weekly results menu')


        #pygame.display.update()
        #mainClock.tick(60)

main(gameState)

