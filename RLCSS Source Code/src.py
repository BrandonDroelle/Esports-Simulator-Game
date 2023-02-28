#Import pygame & other functions
from pickletools import string4
import pygame, sys
import startMenu
import helpMenu
import settingsMenu
import lockerRoomMenu
import deleteSaveMenu
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

#resize images
trophyimg = pygame.transform.scale(trophyimg, (319, 400))
helptxt1img = pygame.transform.scale(helptxt1img, (1100, 77))
helptxt2img = pygame.transform.scale(helptxt2img, (1100, 77))
xButtonUIimg = pygame.transform.scale(xButtonUIimg, (50, 50))

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
            newGameMenu.newGameMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit new save menu')
        if gameState[1] == 'openSave':
            print('run locker room menu')
            lockerRoomMenu.lockerRoomMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img)
            print('exit locker room menu')


        #pygame.display.update()
        #mainClock.tick(60)

main(gameState)

