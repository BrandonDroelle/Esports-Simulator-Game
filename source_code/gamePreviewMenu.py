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
    baseXRightArrow = 200
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
    teamRecordLeft = basicFont.render(playersTeamObject.getWLSeason(), False, (255, 255, 255))
    teamRecordRight = basicFont.render(opposingTeamObject.getWLSeason(), False, (255, 255, 255))
    
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
    
    L1G1U = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (0 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)      #Left row1 Goals row1 Up
    L1G1D = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (0 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    L1A1U = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (1 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0) 
    L1A1D = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (1 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)    
    L1S1U = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (2 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)
    L1S1D = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (2 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)
    L1SH1U = buttonClassObj.buttonClass(ascArrow, baseXLeftArrow + (3 * baseXSpacerStat), baseYUpArrow, basicFont, '',0, 0)
    L1SH1D = buttonClassObj.buttonClass(desArrow, baseXLeftArrow + (3 * baseXSpacerStat), baseYDownArrow, basicFont, '',0, 0)

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
            
            #stats
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

            #players
            win.blit(p1Left, (baseXLeft, baseYStat + (1 * baseYSpacerStat)))
            win.blit(p2Left, (baseXLeft, baseYStat + (2 * baseYSpacerStat)))
            win.blit(p3Left, (baseXLeft, baseYStat + (3 * baseYSpacerStat)))

            win.blit(p1Right, (baseXRight, baseYStat + (1 * baseYSpacerStat)))
            win.blit(p2Right, (baseXRight, baseYStat + (2 * baseYSpacerStat)))
            win.blit(p3Right, (baseXRight, baseYStat + (3 * baseYSpacerStat)))

            #headers
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

            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btn2Hov = buttonClassObj.imgHover(btn2)
            btn3Hov = buttonClassObj.imgHover(btn3)

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
                
            L1G1U.draw(win)
            L1G1D.draw(win)
            L1A1U.draw(win)
            L1A1D.draw(win)
            L1S1U.draw(win)
            L1S1D.draw(win)
            L1SH1U.draw(win)
            L1SH1D.draw(win)

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
                    

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)