from turtle import tiltangle
import pygame, sys
import buttonClassObj
import saveGame
import generateSchedule
import createCache

# #display settings menu
def gamePreviewMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, teamLogos, teamNames, keyBoardKeys):

    currentSeason = str(saveGame.getSeason(gameState))
    currentWeek = saveGame.getWeek(gameState)
    playersTeamName = saveGame.getTeamName(gameState)
    opposingTeamName = generateSchedule.getmatchupSpecific(gameState, currentWeek, playersTeamName)
    
    #get team objects from name strings
    playersTeamObject = createCache.getTeamObject(gameState, playersTeamName)
    opposingTeamObject = createCache.getTeamObject(gameState, opposingTeamName)

    #get playernames
    p1L = playersTeamObject.getP1()
    p1LName = p1L.getName()
    p2L = playersTeamObject.getP2()
    p2LName = p2L.getName()
    p3L = playersTeamObject.getP3()
    p3LName = p3L.getName()
    
    p1R = opposingTeamObject.getP1()
    p1RName = p1R.getName()
    p2R = opposingTeamObject.getP2()
    p2RName = p2R.getName()
    p3R = opposingTeamObject.getP3()
    p3RName = p3R.getName()
    
    #Variables to set headers to
    smallFont = pygame.font.SysFont(None,32)
    baseXHeadLeft = 75
    baseXHeadRight = 775
    baseYHead = 475
    baseSpacer = 100
    
    #Variables to set stat strings to
    baseYStat = 475         #sets the top row height
    baseYSpacerStat = 50    #adjusts the spaces in between each row
    baseXStatLeft = 165     #offsets the stat ints passed the names
    baseXStatRight = 140    #offsets the stat ints passed the names
    baseXSpacerStat = 100   #adjusts the spaces in between each int
    baseXLeft = 25          #cordinate for names
    baseXRight = 760        #cordinate for names

    #variables to set arrows to
    baseXLeftArrow = 220
    baseXRightArrow = 920
    baseYUpArrow = 515
    baseYDownArrow = 535
    
    #resize asc/des arrow buttons
    smallArrowSize = 15
    ascArrow = keyBoardKeys[49]
    ascArrow = pygame.transform.scale(ascArrow, (smallArrowSize, smallArrowSize))
    desArrow = keyBoardKeys[50]
    desArrow = pygame.transform.scale(desArrow, (smallArrowSize, smallArrowSize))

    #Variables to set background shapes to
    baseXL = 15
    baseXR = 750
    baseY = 510
    height = 50
    width = 525
    darkGrey = (100, 100, 100)
    lightGrey = (150, 150, 150)

    #set stat variables
    goalsL1 = 0
    assistsL1 = 0
    savesL1 = 0
    shotsL1 = 0
    goalsL2 = 0
    assistsL2 = 0
    savesL2 = 0
    shotsL2 = 0
    goalsL3 = 0
    assistsL3 = 0
    savesL3 = 0
    shotsL3 = 0
    
    goalsR1 = 0
    assistsR1 = 0
    savesR1 = 0
    shotsR1 = 0
    goalsR2 = 0
    assistsR2 = 0
    savesR2 = 0
    shotsR2 = 0
    goalsR3 = 0
    assistsR3 = 0
    savesR3 = 0
    shotsR3 = 0

    teamGoalsL = 0
    teamGoalsR = 0

    #Create Strings
    title = basicFont.render('Season ' + currentSeason, False, (255, 255, 255))
    subTitle = basicFont.render('Week ' + currentWeek, False, (255, 255, 255))
    teamNameLeft = basicFont.render(playersTeamName.capitalize(), False, (255, 255, 255))
    teamNameRight = basicFont.render(opposingTeamName.capitalize(), False, (255, 255, 255))
    teamRecordLeft = basicFont.render(playersTeamObject.getWLRSeason(), False, (255, 255, 255))
    teamRecordRight = basicFont.render(opposingTeamObject.getWLRSeason(), False, (255, 255, 255))
    
    p1Left = smallFont.render(p1LName.capitalize(), False, (255, 255, 255))
    p2Left = smallFont.render(p2LName.capitalize(), False, (255, 255, 255))
    p3Left = smallFont.render(p3LName.capitalize(), False, (255, 255, 255))
    
    p1Right = smallFont.render(p1RName.capitalize(), False, (255, 255, 255))
    p2Right = smallFont.render(p2RName.capitalize(), False, (255, 255, 255))
    p3Right = smallFont.render(p3RName.capitalize(), False, (255, 255, 255))

    goalsLeft = smallFont.render('Goals', False, (255, 255, 255))
    assistsLeft = smallFont.render('Assists', False, (255, 255, 255))
    savesLeft = smallFont.render('Saves', False, (255, 255, 255))
    shotsLeft = smallFont.render('Shots', False, (255, 255, 255))
    
    goalsRight = smallFont.render('Goals', False, (255, 255, 255))
    assistsRight = smallFont.render('Assists', False, (255, 255, 255))
    savesRight = smallFont.render('Saves', False, (255, 255, 255))
    shotsRight = smallFont.render('Shots', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) - 100, basicFont, 'Confirm', 60, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) - 100, basicFont, 'Confirm', 60, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 0, basicFont, 'Cancel', 60, 15)
    btn2H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 0, basicFont, 'Cancel', 60, 15)
    btn3 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) - 200, basicFont, 'Simulate', 60, 15)
    btn3H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) - 200, basicFont, 'Simulate', 60, 15)
    
    #Left Row1 Goals Up/DownArrow
    L1GU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (0 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)      
    L1GD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (0 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    L1AU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (1 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0) 
    L1AD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (1 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)    
    L1SU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (2 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)
    L1SD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (2 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    L1SHU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (3 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)
    L1SHD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (3 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    #Left Row2 Goals Up/DownArrow
    L2GU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (0 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)      
    L2GD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (0 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    L2AU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (1 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0) 
    L2AD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (1 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)    
    L2SU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (2 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    L2SD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (2 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    L2SHU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (3 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    L2SHD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (3 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    #Left Row3 Goals Up/DownArrow
    L3GU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (0 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)      
    L3GD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (0 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    L3AU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (1 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0) 
    L3AD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (1 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)    
    L3SU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (2 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    L3SD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (2 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    L3SHU = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (3 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    L3SHD = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (3 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    
    #Right Row1 Goals Up/DownArrow
    R1GU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (0 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)      
    R1GD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (0 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    R1AU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (1 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0) 
    R1AD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (1 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)    
    R1SU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (2 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)
    R1SD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (2 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    R1SHU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (3 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)
    R1SHD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (3 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    #Right Row2 Goals Up/DownArrow
    R2GU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (0 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)      
    R2GD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (0 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    R2AU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (1 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0) 
    R2AD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (1 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)    
    R2SU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (2 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    R2SD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (2 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    R2SHU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (3 * baseXSpacerStat), (baseYUpArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    R2SHD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (3 * baseXSpacerStat), (baseYDownArrow + 1 * baseYSpacerStat), basicFont, '',0, 0)
    #Right Row3 Goals Up/DownArrow
    R3GU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (0 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)      
    R3GD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (0 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    R3AU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (1 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0) 
    R3AD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (1 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)    
    R3SU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (2 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    R3SD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (2 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    R3SHU = buttonClassObj.buttonClass(ascArrow, baseXRightArrow + (3 * baseXSpacerStat), (baseYUpArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)
    R3SHD = buttonClassObj.buttonClass(desArrow, baseXRightArrow + (3 * baseXSpacerStat), (baseYDownArrow + 2 * baseYSpacerStat), basicFont, '',0, 0)

    #Create Variables

    #gets index for players team icon
    teamLogoIndex = 99
    count = 0
    for i in teamNames:
        if playersTeamName == teamNames[count]:
            #print("match")
            teamLogoIndexPlayer = count
        count = count + 1
    #gets index for opponents team icon
    teamLogoIndex = 99
    count = 0
    for i in teamNames:
        if opposingTeamName == teamNames[count]:
            #print("match")
            teamLogoIndexOpposition = count
        count = count + 1

    #Menu Loop
    while gameState[1] == 'gamePreview':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            
            #Draw Shapes
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseXL,baseY,width,height)) #rect(x,y,length,height) #Slot 1L
            pygame.draw.rect(win, lightGrey, pygame.Rect(baseXL,baseY + 50,width,height)) #rect(x,y,length,height) #Slot 2L
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseXL,baseY + 100,width,height)) #rect(x,y,length,height) #Slot 3L
            
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseXR,baseY,width,height)) #rect(x,y,length,height) #Slot 1R
            pygame.draw.rect(win, lightGrey, pygame.Rect(baseXR,baseY + 50,width,height)) #rect(x,y,length,height) #Slot 2R
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseXR,baseY + 100,width,height)) #rect(x,y,length,height) #Slot 3R

            #Create Dynamic Strings
            goalsL1Str = smallFont.render(str(goalsL1), False, (255, 255, 255))
            assistsL1Str = smallFont.render(str(assistsL1), False, (255, 255, 255))
            savesL1Str = smallFont.render(str(savesL1), False, (255, 255, 255))
            shotsL1Str = smallFont.render(str(shotsL1), False, (255, 255, 255))
            
            goalsL2Str = smallFont.render(str(goalsL2), False, (255, 255, 255))
            assistsL2Str = smallFont.render(str(assistsL2), False, (255, 255, 255))
            savesL2Str = smallFont.render(str(savesL2), False, (255, 255, 255))
            shotsL2Str = smallFont.render(str(shotsL2), False, (255, 255, 255))
            
            goalsL3Str = smallFont.render(str(goalsL3), False, (255, 255, 255))
            assistsL3Str = smallFont.render(str(assistsL3), False, (255, 255, 255))
            savesL3Str = smallFont.render(str(savesL3), False, (255, 255, 255))
            shotsL3Str = smallFont.render(str(shotsL3), False, (255, 255, 255))
            
            goalsR1Str = smallFont.render(str(goalsR1), False, (255, 255, 255))
            assistsR1Str = smallFont.render(str(assistsR1), False, (255, 255, 255))
            savesR1Str = smallFont.render(str(savesR1), False, (255, 255, 255))
            shotsR1Str = smallFont.render(str(shotsR1), False, (255, 255, 255))
            
            goalsR2Str = smallFont.render(str(goalsR2), False, (255, 255, 255))
            assistsR2Str = smallFont.render(str(assistsR2), False, (255, 255, 255))
            savesR2Str = smallFont.render(str(savesR2), False, (255, 255, 255))
            shotsR2Str = smallFont.render(str(shotsR2), False, (255, 255, 255))
            
            goalsR3Str = smallFont.render(str(goalsR3), False, (255, 255, 255))
            assistsR3Str = smallFont.render(str(assistsR3), False, (255, 255, 255))
            savesR3Str = smallFont.render(str(savesR3), False, (255, 255, 255))
            shotsR3Str = smallFont.render(str(shotsR3), False, (255, 255, 255))

            #Draw Strings
            win.blit(title, (530,50))
            win.blit(subTitle, (550,100))
            win.blit(teamNameLeft, (150,50))
            win.blit(teamNameRight, (950,50))
            win.blit(teamRecordLeft, (200,400))
            win.blit(teamRecordRight, (1000,400))
            
            #Draw Stats
            win.blit(goalsL1Str, (baseXLeft + baseXStatLeft + (0 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            win.blit(assistsL1Str, (baseXLeft + baseXStatLeft + (1 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            win.blit(savesL1Str, (baseXLeft + baseXStatLeft + (2 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            win.blit(shotsL1Str, (baseXLeft + baseXStatLeft + (3 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            
            win.blit(goalsL2Str, (baseXLeft + baseXStatLeft + (0 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            win.blit(assistsL2Str, (baseXLeft + baseXStatLeft + (1 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            win.blit(savesL2Str, (baseXLeft + baseXStatLeft + (2 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            win.blit(shotsL2Str, (baseXLeft + baseXStatLeft + (3 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            
            win.blit(goalsL3Str, (baseXLeft + baseXStatLeft + (0 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))
            win.blit(assistsL3Str, (baseXLeft + baseXStatLeft + (1 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))
            win.blit(savesL3Str, (baseXLeft + baseXStatLeft + (2 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))
            win.blit(shotsL3Str, (baseXLeft + baseXStatLeft + (3 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))
            
            win.blit(goalsR1Str, (baseXRight + baseXStatRight + (0 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            win.blit(assistsR1Str, (baseXRight + baseXStatRight + (1 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            win.blit(savesR1Str, (baseXRight + baseXStatRight + (2 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            win.blit(shotsR1Str, (baseXRight + baseXStatRight + (3 * baseXSpacerStat), baseYStat + (1 * baseYSpacerStat)))
            
            win.blit(goalsR2Str, (baseXRight + baseXStatRight + (0 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            win.blit(assistsR2Str, (baseXRight + baseXStatRight + (1 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            win.blit(savesR2Str, (baseXRight + baseXStatRight + (2 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            win.blit(shotsR2Str, (baseXRight + baseXStatRight + (3 * baseXSpacerStat), baseYStat + (2 * baseYSpacerStat)))
            
            win.blit(goalsR3Str, (baseXRight + baseXStatRight + (0 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))
            win.blit(assistsR3Str, (baseXRight + baseXStatRight + (1 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))
            win.blit(savesR3Str, (baseXRight + baseXStatRight + (2 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))
            win.blit(shotsR3Str, (baseXRight + baseXStatRight + (3 * baseXSpacerStat), baseYStat + (3 * baseYSpacerStat)))

            #Draw Player Names
            win.blit(p1Left, (baseXLeft, baseYStat + (1 * baseYSpacerStat)))
            win.blit(p2Left, (baseXLeft, baseYStat + (2 * baseYSpacerStat)))
            win.blit(p3Left, (baseXLeft, baseYStat + (3 * baseYSpacerStat)))

            win.blit(p1Right, (baseXRight, baseYStat + (1 * baseYSpacerStat)))
            win.blit(p2Right, (baseXRight, baseYStat + (2 * baseYSpacerStat)))
            win.blit(p3Right, (baseXRight, baseYStat + (3 * baseYSpacerStat)))

            #Draw Stat Headers
            win.blit(goalsLeft, (baseXHeadLeft + (1 * baseSpacer), baseYHead))
            win.blit(assistsLeft, (baseXHeadLeft + (2 * baseSpacer), baseYHead))
            win.blit(savesLeft, (baseXHeadLeft + (3 * baseSpacer), baseYHead))
            win.blit(shotsLeft, (baseXHeadLeft + (4 * baseSpacer), baseYHead))
            
            win.blit(goalsRight, (baseXHeadRight + (1 * baseSpacer), baseYHead))
            win.blit(assistsRight, (baseXHeadRight + (2 * baseSpacer), baseYHead))
            win.blit(savesRight, (baseXHeadRight + (3 * baseSpacer), baseYHead))
            win.blit(shotsRight, (baseXHeadRight + (4 * baseSpacer), baseYHead))
            
            #Draw Images
            win.blit(teamLogos[teamLogoIndexPlayer], (120, 125))
            win.blit(teamLogos[teamLogoIndexOpposition], (920, 125))

            
            #check for mouse hover on buttons
            btn1Hov = buttonClassObj.imgHover(btn1)
            btn2Hov = buttonClassObj.imgHover(btn2)
            btn3Hov = buttonClassObj.imgHover(btn3)
            
            #left player 1 arrows   
            L1GUHov = buttonClassObj.imgHover(L1GU)
            L1GDHov = buttonClassObj.imgHover(L1GD)
            L1AUHov = buttonClassObj.imgHover(L1AU)
            L1ADHov = buttonClassObj.imgHover(L1AD)
            L1SUHov = buttonClassObj.imgHover(L1SU)
            L1SDHov = buttonClassObj.imgHover(L1SD)
            L1SHUHov = buttonClassObj.imgHover(L1SHU)
            L1SHDHov = buttonClassObj.imgHover(L1SHD)
            #left player 2 arrows   
            L2GUHov = buttonClassObj.imgHover(L2GU)
            L2GDHov = buttonClassObj.imgHover(L2GD)
            L2AUHov = buttonClassObj.imgHover(L2AU)
            L2ADHov = buttonClassObj.imgHover(L2AD)
            L2SUHov = buttonClassObj.imgHover(L2SU)
            L2SDHov = buttonClassObj.imgHover(L2SD)
            L2SHUHov = buttonClassObj.imgHover(L2SHU)
            L2SHDHov = buttonClassObj.imgHover(L2SHD)
            #left player 3 arrows   
            L3GUHov = buttonClassObj.imgHover(L3GU)
            L3GDHov = buttonClassObj.imgHover(L3GD)
            L3AUHov = buttonClassObj.imgHover(L3AU)
            L3ADHov = buttonClassObj.imgHover(L3AD)
            L3SUHov = buttonClassObj.imgHover(L3SU)
            L3SDHov = buttonClassObj.imgHover(L3SD)
            L3SHUHov = buttonClassObj.imgHover(L3SHU)
            L3SHDHov = buttonClassObj.imgHover(L3SHD)
            
            #right player 1 arrows   
            R1GUHov = buttonClassObj.imgHover(R1GU)
            R1GDHov = buttonClassObj.imgHover(R1GD)
            R1AUHov = buttonClassObj.imgHover(R1AU)
            R1ADHov = buttonClassObj.imgHover(R1AD)
            R1SUHov = buttonClassObj.imgHover(R1SU)
            R1SDHov = buttonClassObj.imgHover(R1SD)
            R1SHUHov = buttonClassObj.imgHover(R1SHU)
            R1SHDHov = buttonClassObj.imgHover(R1SHD)
            #right player 2 arrows   
            R2GUHov = buttonClassObj.imgHover(R2GU)
            R2GDHov = buttonClassObj.imgHover(R2GD)
            R2AUHov = buttonClassObj.imgHover(R2AU)
            R2ADHov = buttonClassObj.imgHover(R2AD)
            R2SUHov = buttonClassObj.imgHover(R2SU)
            R2SDHov = buttonClassObj.imgHover(R2SD)
            R2SHUHov = buttonClassObj.imgHover(R2SHU)
            R2SHDHov = buttonClassObj.imgHover(R2SHD)
            #right player 3 arrows   
            R3GUHov = buttonClassObj.imgHover(R3GU)
            R3GDHov = buttonClassObj.imgHover(R3GD)
            R3AUHov = buttonClassObj.imgHover(R3AU)
            R3ADHov = buttonClassObj.imgHover(R3AD)
            R3SUHov = buttonClassObj.imgHover(R3SU)
            R3SDHov = buttonClassObj.imgHover(R3SD)
            R3SHUHov = buttonClassObj.imgHover(R3SHU)
            R3SHDHov = buttonClassObj.imgHover(R3SHD)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)
            if btn2Hov == True:
                btn2H.draw(win)
            else:
                btn2.draw(win)
            if btn3Hov == True:
                btn3H.draw(win)
            else:
                btn3.draw(win)
            #left player 1 arrows 
            if L1GUHov == True:
                L1GU.draw(win)
            else:
                L1GU.draw(win)
            if L1GDHov == True:
                L1GD.draw(win)
            else:
                L1GD.draw(win)
            if L1AUHov == True:
                L1AU.draw(win)
            else:
                L1AU.draw(win)
            if L1ADHov == True:
                L1AD.draw(win)
            else:
                L1AD.draw(win)    
            if L1SUHov == True:
                L1SU.draw(win)
            else:
                L1SU.draw(win) 
            if L1SDHov == True:
                L1SD.draw(win)
            else:
                L1SD.draw(win) 
            if L1SHUHov == True:
                L1SHU.draw(win)
            else:
                L1SHU.draw(win)
            if L1SHDHov == True:
                L1SHD.draw(win)
            else:
                L1SHD.draw(win)
            #left player 2 arrows 
            if L2GUHov == True:
                L2GU.draw(win)
            else:
                L2GU.draw(win)
            if L2GDHov == True:
                L2GD.draw(win)
            else:
                L2GD.draw(win)
            if L2AUHov == True:
                L2AU.draw(win)
            else:
                L2AU.draw(win)
            if L2ADHov == True:
                L2AD.draw(win)
            else:
                L2AD.draw(win)    
            if L2SUHov == True:
                L2SU.draw(win)
            else:
                L2SU.draw(win) 
            if L2SDHov == True:
                L2SD.draw(win)
            else:
                L2SD.draw(win) 
            if L2SHUHov == True:
                L2SHU.draw(win)
            else:
                L2SHU.draw(win)
            if L2SHDHov == True:
                L2SHD.draw(win)
            else:
                L2SHD.draw(win)
            #left player 3 arrows 
            if L3GUHov == True:
                L3GU.draw(win)
            else:
                L3GU.draw(win)
            if L3GDHov == True:
                L3GD.draw(win)
            else:
                L3GD.draw(win)
            if L3AUHov == True:
                L3AU.draw(win)
            else:
                L3AU.draw(win)
            if L3ADHov == True:
                L3AD.draw(win)
            else:
                L3AD.draw(win)    
            if L3SUHov == True:
                L3SU.draw(win)
            else:
                L3SU.draw(win) 
            if L3SDHov == True:
                L3SD.draw(win)
            else:
                L3SD.draw(win) 
            if L3SHUHov == True:
                L3SHU.draw(win)
            else:
                L3SHU.draw(win)
            if L3SHDHov == True:
                L3SHD.draw(win)
            else:
                L3SHD.draw(win)
                
            #right player 1 arrows 
            if R1GUHov == True:
                R1GU.draw(win)
            else:
                R1GU.draw(win)
            if R1GDHov == True:
                R1GD.draw(win)
            else:
                R1GD.draw(win)
            if R1AUHov == True:
                R1AU.draw(win)
            else:
                R1AU.draw(win)
            if R1ADHov == True:
                R1AD.draw(win)
            else:
                R1AD.draw(win)    
            if R1SUHov == True:
                R1SU.draw(win)
            else:
                R1SU.draw(win) 
            if R1SDHov == True:
                R1SD.draw(win)
            else:
                R1SD.draw(win) 
            if R1SHUHov == True:
                R1SHU.draw(win)
            else:
                R1SHU.draw(win)
            if R1SHDHov == True:
                R1SHD.draw(win)
            else:
                R1SHD.draw(win)
            #right player 2 arrows 
            if R2GUHov == True:
                R2GU.draw(win)
            else:
                R2GU.draw(win)
            if R2GDHov == True:
                R2GD.draw(win)
            else:
                R2GD.draw(win)
            if R2AUHov == True:
                R2AU.draw(win)
            else:
                R2AU.draw(win)
            if R2ADHov == True:
                R2AD.draw(win)
            else:
                R2AD.draw(win)    
            if R2SUHov == True:
                R2SU.draw(win)
            else:
                R2SU.draw(win) 
            if R2SDHov == True:
                R2SD.draw(win)
            else:
                R2SD.draw(win) 
            if R2SHUHov == True:
                R2SHU.draw(win)
            else:
                R2SHU.draw(win)
            if R2SHDHov == True:
                R2SHD.draw(win)
            else:
                R2SHD.draw(win)
            #right player 3 arrows 
            if R3GUHov == True:
                R3GU.draw(win)
            else:
                R3GU.draw(win)
            if R3GDHov == True:
                R3GD.draw(win)
            else:
                R3GD.draw(win)
            if R3AUHov == True:
                R3AU.draw(win)
            else:
                R3AU.draw(win)
            if R3ADHov == True:
                R3AD.draw(win)
            else:
                R3AD.draw(win)    
            if R3SUHov == True:
                R3SU.draw(win)
            else:
                R3SU.draw(win) 
            if R3SDHov == True:
                R3SD.draw(win)
            else:
                R3SD.draw(win) 
            if R3SHUHov == True:
                R3SHU.draw(win)
            else:
                R3SHU.draw(win)
            if R3SHDHov == True:
                R3SHD.draw(win)
            else:
                R3SHD.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click confirm btn")
                    gameState[1] = 'weeklyResults'
                if btn2Hov == True:
                    print("mouse click cancel btn")
                    gameState[1] = 'lockerRoom'
                if btn3Hov == True:
                    print("mouse click simulate btn")
                #left player 1 arrows
                if L1GUHov == True:
                    print("mouse click L1G1UHov")
                    goalsL1 = goalsL1 + 1
                if L1GDHov == True:
                    print("mouse click L1G1DHov")
                    if goalsL1 > 0:
                        goalsL1 = goalsL1 - 1
                if L1AUHov == True:
                    print("mouse click L1A1UHov")
                    assistsL1 = assistsL1 + 1
                if L1ADHov == True:
                    print("mouse click L1A1DHov")
                    if assistsL1 > 0:
                        assistsL1 = assistsL1 - 1
                if L1SUHov == True:
                    print("mouse click L1S1UHov")
                    savesL1 = savesL1 + 1
                if L1SDHov == True:
                    print("mouse click L1S1DHov")
                    if savesL1 > 0:
                        savesL1 = savesL1 - 1
                if L1SHUHov == True:
                    print("mouse click L1SH1UHov")
                    shotsL1 = shotsL1 + 1
                if L1SHDHov == True:
                    print("mouse click L1SH1DHov")
                    if shotsL1 > 0:
                        shotsL1 = shotsL1 - 1
                #left player 2 arrows
                if L2GUHov == True:
                    print("mouse click L2G2UHov")
                    goalsL2 = goalsL2 + 1
                if L2GDHov == True:
                    print("mouse click L2G2DHov")
                    if goalsL2 > 0:
                        goalsL2 = goalsL2 - 1
                if L2AUHov == True:
                    print("mouse click L2A2UHov")
                    assistsL2 = assistsL2 + 1
                if L2ADHov == True:
                    print("mouse click L2A2DHov")
                    if assistsL2 > 0:
                        assistsL2 = assistsL2 - 1
                if L2SUHov == True:
                    print("mouse click L2S2UHov")
                    savesL2 = savesL2 + 1
                if L2SDHov == True:
                    print("mouse click L2S2DHov")
                    if savesL2 > 0:
                        savesL2 = savesL2 - 1
                if L2SHUHov == True:
                    print("mouse click L2SH2UHov")
                    shotsL2 = shotsL2 + 1
                if L2SHDHov == True:
                    print("mouse click L2SH2DHov")
                    if shotsL2 > 0:
                        shotsL2 = shotsL2 - 1
                #left player 3 arrows
                if L3GUHov == True:
                    print("mouse click L3G3UHov")
                    goalsL3 = goalsL3 + 1
                if L3GDHov == True:
                    print("mouse click L3G3DHov")
                    if goalsL3 > 0:
                        goalsL3 = goalsL3 - 1
                if L3AUHov == True:
                    print("mouse click L3A3UHov")
                    assistsL3 = assistsL3 + 1
                if L3ADHov == True:
                    print("mouse click L3A3DHov")
                    if assistsL3 > 0:
                        assistsL3 = assistsL3 - 1
                if L3SUHov == True:
                    print("mouse click L3S3UHov")
                    savesL3 = savesL3 + 1
                if L3SDHov == True:
                    print("mouse click L3S3DHov")
                    if savesL3 > 0:
                        savesL3 = savesL3 - 1
                if L3SHUHov == True:
                    print("mouse click L3SH3UHov")
                    shotsL3 = shotsL3 + 1
                if L3SHDHov == True:
                    print("mouse click L3SH3DHov")
                    if shotsL3 > 0:
                        shotsL3 = shotsL3 - 1
                
                #right player 1 arrows
                if R1GUHov == True:
                    print("mouse click R1G1UHov")
                    goalsR1 = goalsR1 + 1
                if R1GDHov == True:
                    print("mouse click R1G1DHov")
                    if goalsR1 > 0:
                        goalsR1 = goalsR1 - 1
                if R1AUHov == True:
                    print("mouse click R1A1UHov")
                    assistsR1 = assistsR1 + 1
                if R1ADHov == True:
                    print("mouse click R1A1DHov")
                    if assistsR1 > 0:
                        assistsR1 = assistsR1 - 1
                if R1SUHov == True:
                    print("mouse click R1S1UHov")
                    savesR1 = savesR1 + 1
                if R1SDHov == True:
                    print("mouse click R1S1DHov")
                    if savesR1 > 0:
                        savesR1 = savesR1 - 1
                if R1SHUHov == True:
                    print("mouse click R1SH1UHov")
                    shotsR1 = shotsR1 + 1
                if R1SHDHov == True:
                    print("mouse click R1SH1DHov")
                    if shotsR1 > 0:
                        shotsR1 = shotsR1 - 1
                #right player 2 arrows
                if R2GUHov == True:
                    print("mouse click R2G2UHov")
                    goalsR2 = goalsR2 + 1
                if R2GDHov == True:
                    print("mouse click R2G2DHov")
                    if goalsR2 > 0:
                        goalsR2 = goalsR2 - 1
                if R2AUHov == True:
                    print("mouse click R2A2UHov")
                    assistsR2 = assistsR2 + 1
                if R2ADHov == True:
                    print("mouse click R2A2DHov")
                    if assistsR2 > 0:
                        assistsR2 = assistsR2 - 1
                if R2SUHov == True:
                    print("mouse click R2S2UHov")
                    savesR2 = savesR2 + 1
                if R2SDHov == True:
                    print("mouse click R2S2DHov")
                    if savesR2 > 0:
                        savesR2 = savesR2 - 1
                if R2SHUHov == True:
                    print("mouse click R2SH2UHov")
                    shotsR2 = shotsR2 + 1
                if R2SHDHov == True:
                    print("mouse click R2SH2DHov")
                    if shotsR2 > 0:
                        shotsR2 = shotsR2 - 1
                #right player 3 arrows
                if R3GUHov == True:
                    print("mouse click R3G3UHov")
                    goalsR3 = goalsR3 + 1
                if R3GDHov == True:
                    print("mouse click R3G3DHov")
                    if goalsR3 > 0:
                        goalsR3 = goalsR3 - 1
                if R3AUHov == True:
                    print("mouse click R3A3UHov")
                    assistsR3 = assistsR3 + 1
                if R3ADHov == True:
                    print("mouse click R3A3DHov")
                    if assistsR3 > 0:
                        assistsR3 = assistsR3 - 1
                if R3SUHov == True:
                    print("mouse click R3S3UHov")
                    savesR3 = savesR3 + 1
                if R3SDHov == True:
                    print("mouse click R3S3DHov")
                    if savesR3 > 0:
                        savesR3 = savesR3 - 1
                if R3SHUHov == True:
                    print("mouse click R3SH3UHov")
                    shotsR3 = shotsR3 + 1
                if R3SHDHov == True:
                    print("mouse click R3SH3DHov")
                    if shotsR3 > 0:
                        shotsR3 = shotsR3 - 1
                    
                    
                    

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)