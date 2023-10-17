from tracemalloc import start
import pygame, sys
import buttonClassObj
import sortFunctions

#display team stats menu menu

def teamStatsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, keyBoardKeys):

    print('in team Stats - ', gameState)

    #Variable to determine which stats to display
    seasonStats = True

    #varible to track how stats are currently sorted
    sortType = "none"
    #set default sort to team name asc
    gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "team name")

    #Variables to set background shapes to
    baseX = 250
    baseY = 175
    height = 50
    width = 750
    darkGrey = (100, 100, 100)
    lightGrey = (150, 150, 150)

    #Variables to set headers to
    smallFont = pygame.font.SysFont(None,32)
    baseYHead = 140

    baseXNameH = 265     
    baseXWLRH = 415
    baseXWinsH = 490
    baseXLossesH = 560
    baseXGoalsH = 655
    baseXAssistsH = 735
    baseXSavesH = 830
    baseXShotsH = 910

    #Variables to set stat strings to
    startPos = 0
    baseYStat = 140
    baseYSpacerStat = 50

    baseXRank = 215
    baseXName = 265        
    baseXWLR = 425
    baseXWins = 510
    baseXLosses = 595
    baseXGoals = 680
    baseXAssists = 765
    baseXSaves = 850
    baseXShots = 935
    
    #resize asc/des arrow buttons
    smallArrowSize = 15
    ascArrow = keyBoardKeys[49]
    ascArrow = pygame.transform.scale(ascArrow, (smallArrowSize, smallArrowSize))
    desArrow = keyBoardKeys[50]
    desArrow = pygame.transform.scale(desArrow, (smallArrowSize, smallArrowSize))

    ascArrowY = 135
    desArrowy = 150

    #print("length of team objects: ", len(gameState[3]))
    lenTeams = len(gameState[3])
    #print("team 0 Name: ", gameState[3][0].getName())
    extraSpaces = 8 - (lenTeams % 8)   #Get mod to avoid out of bounds errors when bottom of list is not mod 0
    spacesNeeded = 0
    #print("mod lenTeams: ", extraSpaces)
 

    #Create Strings
    title = basicFont.render('Team Stats', False, (255, 255, 255))
    subTitle1 = basicFont.render('Season', False, (255, 255, 255))
    subTitle2 = basicFont.render('Career', False, (255, 255, 255))
    header1 = smallFont.render('Team', False, (255, 255, 255))
    header2 = smallFont.render('W/L%', False, (255, 255, 255))
    header3 = smallFont.render('Wins', False, (255, 255, 255))
    header4 = smallFont.render('Losses', False, (255, 255, 255))
    header5 = smallFont.render('Goals', False, (255, 255, 255))
    header6 = smallFont.render('Assists', False, (255, 255, 255))
    header7 = smallFont.render('Saves', False, (255, 255, 255))
    header8 = smallFont.render('Shots', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, 'Locker Room', 10, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, 'Locker Room', 10, 15)
    btnUpArrow = buttonClassObj.buttonClass(keyBoardKeys[49], 1000, 170, basicFont, '',0, 0)
    btnDownArrow = buttonClassObj.buttonClass(keyBoardKeys[50], 1000, 500, basicFont, '',0, 0)
    btnSeasonStats = buttonClassObj.buttonClass(buttonimg, 100, (win.get_height() / 2) + 250, basicFont, 'Season Stats',10, 15)
    btnSeasonStatsH = buttonClassObj.buttonClass(button2img, 100, (win.get_height() / 2) + 250, basicFont, 'Season Stats',10, 15)
    btnCareerStats = buttonClassObj.buttonClass(buttonimg, (win.get_width() - 400), (win.get_height() / 2) + 250, basicFont, 'Career Stats',10, 15)
    btnCareerStatsH = buttonClassObj.buttonClass(button2img, (win.get_width() - 400), (win.get_height() / 2) + 250, basicFont, 'Career Stats',10, 15)

    btnTeamAsc = buttonClassObj.buttonClass(ascArrow, 330, ascArrowY, basicFont, '',0, 0)
    btnWLAsc = buttonClassObj.buttonClass(ascArrow, 475, ascArrowY, basicFont, '',0, 0)
    btnWinsAsc = buttonClassObj.buttonClass(ascArrow, 542, ascArrowY, basicFont, '',0, 0)
    btnLossAsc = buttonClassObj.buttonClass(ascArrow, 635, ascArrowY, basicFont, '',0, 0)
    btnGoalsAsc = buttonClassObj.buttonClass(ascArrow, 715, ascArrowY, basicFont, '',0, 0)
    btnAssistsAsc = buttonClassObj.buttonClass(ascArrow, 815, ascArrowY, basicFont, '',0, 0)
    btnSavesAsc = buttonClassObj.buttonClass(ascArrow, 895, ascArrowY, basicFont, '',0, 0)
    btnShotsAsc = buttonClassObj.buttonClass(ascArrow, 970, ascArrowY, basicFont, '',0, 0)

    btnTeamDes = buttonClassObj.buttonClass(desArrow, 330, desArrowy, basicFont, '',0, 0)
    btnWLDes = buttonClassObj.buttonClass(desArrow, 475, desArrowy, basicFont, '',0, 0)
    btnWinsDes = buttonClassObj.buttonClass(desArrow, 542, desArrowy, basicFont, '',0, 0)
    btnLossDes = buttonClassObj.buttonClass(desArrow, 635, desArrowy, basicFont, '',0, 0)
    btnGoalsDes = buttonClassObj.buttonClass(desArrow, 715, desArrowy, basicFont, '',0, 0)
    btnAssistsDes = buttonClassObj.buttonClass(desArrow, 815, desArrowy, basicFont, '',0, 0)
    btnSavesDes = buttonClassObj.buttonClass(desArrow, 895, desArrowy, basicFont, '',0, 0)
    btnShotsDes = buttonClassObj.buttonClass(desArrow, 970, desArrowy, basicFont, '',0, 0)

    #Menu Loop
    while gameState[1] == 'teamStats':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if startPos + 8 > lenTeams:
                spacesNeeded = extraSpaces
            else:
                spacesNeeded = 0


            #create Dynamic Variable
            pos0 = startPos
            pos1 = pos0 + 1
            pos2 = pos1 + 1
            pos3 = pos2 + 1
            pos4 = pos3 + 1
            pos5 = pos4 + 1
            pos6 = pos5 + 1
            pos7 = pos6 + 1


            #Create Dynamic Strings
            if spacesNeeded < 8:
                num0 = smallFont.render(str(pos0 + 1), False, (255, 255, 255))
                name0 = smallFont.render(gameState[3][pos0].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr0 = smallFont.render(str(gameState[3][pos0].getWLRSeason()), False, (255, 255, 255))
                    wins0 = smallFont.render(str(gameState[3][pos0].getWinsSeason()), False, (255, 255, 255))
                    losses0 = smallFont.render(str(gameState[3][pos0].getLossesSeason()), False, (255, 255, 255))
                    goals0 = smallFont.render(str(gameState[3][pos0].getGoalsSeason()), False, (255, 255, 255))
                    assists0 = smallFont.render(str(gameState[3][pos0].getAssistsSeason()), False, (255, 255, 255))
                    saves0 = smallFont.render(str(gameState[3][pos0].getSavesSeason()), False, (255, 255, 255))
                    shots0 = smallFont.render(str(gameState[3][pos0].getShotsSeason()), False, (255, 255, 255))
                else:
                    wlr0 = smallFont.render(str(gameState[3][pos0].getWLRCareer()), False, (255, 255, 255))
                    wins0 = smallFont.render(str(gameState[3][pos0].getWinsCareer()), False, (255, 255, 255))
                    losses0 = smallFont.render(str(gameState[3][pos0].getLossesCareer()), False, (255, 255, 255))
                    goals0 = smallFont.render(str(gameState[3][pos0].getGoalsCareer()), False, (255, 255, 255))
                    assists0 = smallFont.render(str(gameState[3][pos0].getAssistsCareer()), False, (255, 255, 255))
                    saves0 = smallFont.render(str(gameState[3][pos0].getSavesCareer()), False, (255, 255, 255))
                    shots0 = smallFont.render(str(gameState[3][pos0].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 7:
                num1 = smallFont.render(str(pos1 + 1), False, (255, 255, 255))
                name1 = smallFont.render(gameState[3][pos1].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr1 = smallFont.render(str(gameState[3][pos1].getWLRSeason()), False, (255, 255, 255))
                    wins1 = smallFont.render(str(gameState[3][pos1].getWinsSeason()), False, (255, 255, 255))
                    losses1 = smallFont.render(str(gameState[3][pos1].getLossesSeason()), False, (255, 255, 255))
                    goals1 = smallFont.render(str(gameState[3][pos1].getGoalsSeason()), False, (255, 255, 255))
                    assists1 = smallFont.render(str(gameState[3][pos1].getAssistsSeason()), False, (255, 255, 255))
                    saves1 = smallFont.render(str(gameState[3][pos1].getSavesSeason()), False, (255, 255, 255))
                    shots1 = smallFont.render(str(gameState[3][pos1].getShotsSeason()), False, (255, 255, 255))
                else:
                    wins1 = smallFont.render(str(gameState[3][pos1].getWinsCareer()), False, (255, 255, 255))
                    losses1 = smallFont.render(str(gameState[3][pos1].getLossesCareer()), False, (255, 255, 255))
                    goals1 = smallFont.render(str(gameState[3][pos1].getGoalsCareer()), False, (255, 255, 255))
                    assists1 = smallFont.render(str(gameState[3][pos1].getAssistsCareer()), False, (255, 255, 255))
                    saves1 = smallFont.render(str(gameState[3][pos1].getSavesCareer()), False, (255, 255, 255))
                    shots1 = smallFont.render(str(gameState[3][pos1].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 6:
                num2 = smallFont.render(str(pos2 + 1), False, (255, 255, 255))
                name2 = smallFont.render(gameState[3][pos2].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr2 = smallFont.render(str(gameState[3][pos2].getWLRSeason()), False, (255, 255, 255))
                    wins2 = smallFont.render(str(gameState[3][pos2].getWinsSeason()), False, (255, 255, 255))
                    losses2 = smallFont.render(str(gameState[3][pos2].getLossesSeason()), False, (255, 255, 255))
                    goals2 = smallFont.render(str(gameState[3][pos2].getGoalsSeason()), False, (255, 255, 255))
                    assists2 = smallFont.render(str(gameState[3][pos2].getAssistsSeason()), False, (255, 255, 255))
                    saves2 = smallFont.render(str(gameState[3][pos2].getSavesSeason()), False, (255, 255, 255))
                    shots2 = smallFont.render(str(gameState[3][pos2].getShotsSeason()), False, (255, 255, 255))
                else:
                    wins2 = smallFont.render(str(gameState[3][pos2].getWinsCareer()), False, (255, 255, 255))
                    losses2 = smallFont.render(str(gameState[3][pos2].getLossesCareer()), False, (255, 255, 255))
                    goals2 = smallFont.render(str(gameState[3][pos2].getGoalsCareer()), False, (255, 255, 255))
                    assists2 = smallFont.render(str(gameState[3][pos2].getAssistsCareer()), False, (255, 255, 255))
                    saves2 = smallFont.render(str(gameState[3][pos2].getSavesCareer()), False, (255, 255, 255))
                    shots2 = smallFont.render(str(gameState[3][pos2].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 5:
                num3 = smallFont.render(str(pos3 + 1), False, (255, 255, 255))
                name3 = smallFont.render(gameState[3][pos3].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr3 = smallFont.render(str(gameState[3][pos3].getWLRSeason()), False, (255, 255, 255))
                    wins3 = smallFont.render(str(gameState[3][pos3].getWinsSeason()), False, (255, 255, 255))
                    losses3 = smallFont.render(str(gameState[3][pos3].getLossesSeason()), False, (255, 255, 255))
                    goals3 = smallFont.render(str(gameState[3][pos3].getGoalsSeason()), False, (255, 255, 255))
                    assists3 = smallFont.render(str(gameState[3][pos3].getAssistsSeason()), False, (255, 255, 255))
                    saves3 = smallFont.render(str(gameState[3][pos3].getSavesSeason()), False, (255, 255, 255))
                    shots3 = smallFont.render(str(gameState[3][pos3].getShotsSeason()), False, (255, 255, 255))
                else:
                    wins3 = smallFont.render(str(gameState[3][pos3].getWinsCareer()), False, (255, 255, 255))
                    losses3 = smallFont.render(str(gameState[3][pos3].getLossesCareer()), False, (255, 255, 255))
                    goals3 = smallFont.render(str(gameState[3][pos3].getGoalsCareer()), False, (255, 255, 255))
                    assists3 = smallFont.render(str(gameState[3][pos3].getAssistsCareer()), False, (255, 255, 255))
                    saves3 = smallFont.render(str(gameState[3][pos3].getSavesCareer()), False, (255, 255, 255))
                    shots3 = smallFont.render(str(gameState[3][pos3].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 4:
                num4 = smallFont.render(str(pos4 + 1), False, (255, 255, 255))
                name4 = smallFont.render(gameState[3][pos4].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr4 = smallFont.render(str(gameState[3][pos4].getWLRSeason()), False, (255, 255, 255))
                    wins4 = smallFont.render(str(gameState[3][pos4].getWinsSeason()), False, (255, 255, 255))
                    losses4 = smallFont.render(str(gameState[3][pos4].getLossesSeason()), False, (255, 255, 255))
                    goals4 = smallFont.render(str(gameState[3][pos4].getGoalsSeason()), False, (255, 255, 255))
                    assists4 = smallFont.render(str(gameState[3][pos4].getAssistsSeason()), False, (255, 255, 255))
                    saves4 = smallFont.render(str(gameState[3][pos4].getSavesSeason()), False, (255, 255, 255))
                    shots4 = smallFont.render(str(gameState[3][pos4].getShotsSeason()), False, (255, 255, 255))
                else:
                    wins4 = smallFont.render(str(gameState[3][pos4].getWinsCareer()), False, (255, 255, 255))
                    losses4 = smallFont.render(str(gameState[3][pos4].getLossesCareer()), False, (255, 255, 255))
                    goals4 = smallFont.render(str(gameState[3][pos4].getGoalsCareer()), False, (255, 255, 255))
                    assists4 = smallFont.render(str(gameState[3][pos4].getAssistsCareer()), False, (255, 255, 255))
                    saves4 = smallFont.render(str(gameState[3][pos4].getSavesCareer()), False, (255, 255, 255))
                    shots4 = smallFont.render(str(gameState[3][pos4].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 3:
                num5 = smallFont.render(str(pos5 + 1), False, (255, 255, 255))
                name5 = smallFont.render(gameState[3][pos5].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr5 = smallFont.render(str(gameState[3][pos5].getWLRSeason()), False, (255, 255, 255))
                    wins5 = smallFont.render(str(gameState[3][pos5].getWinsSeason()), False, (255, 255, 255))
                    losses5 = smallFont.render(str(gameState[3][pos5].getLossesSeason()), False, (255, 255, 255))
                    goals5 = smallFont.render(str(gameState[3][pos5].getGoalsSeason()), False, (255, 255, 255))
                    assists5 = smallFont.render(str(gameState[3][pos5].getAssistsSeason()), False, (255, 255, 255))
                    saves5 = smallFont.render(str(gameState[3][pos5].getSavesSeason()), False, (255, 255, 255))
                    shots5 = smallFont.render(str(gameState[3][pos5].getShotsSeason()), False, (255, 255, 255))
                else:
                    wins5 = smallFont.render(str(gameState[3][pos5].getWinsCareer()), False, (255, 255, 255))
                    losses5 = smallFont.render(str(gameState[3][pos5].getLossesCareer()), False, (255, 255, 255))
                    goals5 = smallFont.render(str(gameState[3][pos5].getGoalsCareer()), False, (255, 255, 255))
                    assists5 = smallFont.render(str(gameState[3][pos5].getAssistsCareer()), False, (255, 255, 255))
                    saves5 = smallFont.render(str(gameState[3][pos5].getSavesCareer()), False, (255, 255, 255))
                    shots5 = smallFont.render(str(gameState[3][pos5].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 2:
                num6 = smallFont.render(str(pos6 + 1), False, (255, 255, 255))
                name6 = smallFont.render(gameState[3][pos6].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr6 = smallFont.render(str(gameState[3][pos6].getWLRSeason()), False, (255, 255, 255))
                    wins6 = smallFont.render(str(gameState[3][pos6].getWinsSeason()), False, (255, 255, 255))
                    losses6 = smallFont.render(str(gameState[3][pos6].getLossesSeason()), False, (255, 255, 255))
                    goals6 = smallFont.render(str(gameState[3][pos6].getGoalsSeason()), False, (255, 255, 255))
                    assists6 = smallFont.render(str(gameState[3][pos6].getAssistsSeason()), False, (255, 255, 255))
                    saves6 = smallFont.render(str(gameState[3][pos6].getSavesSeason()), False, (255, 255, 255))
                    shots6 = smallFont.render(str(gameState[3][pos6].getShotsSeason()), False, (255, 255, 255))
                else:
                    wins6 = smallFont.render(str(gameState[3][pos6].getWinsCareer()), False, (255, 255, 255))
                    losses6 = smallFont.render(str(gameState[3][pos6].getLossesCareer()), False, (255, 255, 255))
                    goals6 = smallFont.render(str(gameState[3][pos6].getGoalsCareer()), False, (255, 255, 255))
                    assists6 = smallFont.render(str(gameState[3][pos6].getAssistsCareer()), False, (255, 255, 255))
                    saves6 = smallFont.render(str(gameState[3][pos6].getSavesCareer()), False, (255, 255, 255))
                    shots6 = smallFont.render(str(gameState[3][pos6].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 1:
                num7 = smallFont.render(str(pos7 + 1), False, (255, 255, 255))
                name7 = smallFont.render(gameState[3][pos7].getTeamName(), False, (255, 255, 255))
                if seasonStats == True:
                    wlr7 = smallFont.render(str(gameState[3][pos7].getWLRSeason()), False, (255, 255, 255))
                    wins7 = smallFont.render(str(gameState[3][pos7].getWinsSeason()), False, (255, 255, 255))
                    losses7 = smallFont.render(str(gameState[3][pos7].getLossesSeason()), False, (255, 255, 255))
                    goals7 = smallFont.render(str(gameState[3][pos7].getGoalsSeason()), False, (255, 255, 255))
                    assists7 = smallFont.render(str(gameState[3][pos7].getAssistsSeason()), False, (255, 255, 255))
                    saves7 = smallFont.render(str(gameState[3][pos7].getSavesSeason()), False, (255, 255, 255))
                    shots7 = smallFont.render(str(gameState[3][pos7].getShotsSeason()), False, (255, 255, 255))
                else:
                    wins7 = smallFont.render(str(gameState[3][pos7].getWinsCareer()), False, (255, 255, 255))
                    losses7 = smallFont.render(str(gameState[3][pos7].getLossesCareer()), False, (255, 255, 255))
                    goals7 = smallFont.render(str(gameState[3][pos7].getGoalsCareer()), False, (255, 255, 255))
                    assists7 = smallFont.render(str(gameState[3][pos7].getAssistsCareer()), False, (255, 255, 255))
                    saves7 = smallFont.render(str(gameState[3][pos7].getSavesCareer()), False, (255, 255, 255))
                    shots7 = smallFont.render(str(gameState[3][pos7].getShotsCareer()), False, (255, 255, 255))

            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Shapes
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseX,baseY,width,height)) #rect(x,y,length,height) #Slot 1
            pygame.draw.rect(win, lightGrey, pygame.Rect(baseX,baseY + 50,width,height)) #rect(x,y,length,height) #Slot 2
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseX,baseY + 100,width,height)) #rect(x,y,length,height) #Slot 3
            pygame.draw.rect(win, lightGrey, pygame.Rect(baseX,baseY + 150,width,height)) #rect(x,y,length,height) #Slot 4
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseX,baseY + 200,width,height)) #rect(x,y,length,height) #Slot 5
            pygame.draw.rect(win, lightGrey, pygame.Rect(baseX,baseY + 250,width,height)) #rect(x,y,length,height) #Slot 6
            pygame.draw.rect(win, darkGrey, pygame.Rect(baseX,baseY + 300,width,height)) #rect(x,y,length,height) #Slot 7
            pygame.draw.rect(win, lightGrey, pygame.Rect(baseX,baseY + 350,width,height)) #rect(x,y,length,height) #Slot 8
            #Draw Strings
            win.blit(title, (425,50))
            if seasonStats == True:
                win.blit(subTitle1, (675,50))
            else:
                win.blit(subTitle2, (675,50))

            #Draw headers
            win.blit(header1, (baseXNameH, baseYHead))
            win.blit(header2, (baseXWLRH, baseYHead))
            win.blit(header3, (baseXWinsH, baseYHead))
            win.blit(header4, (baseXLossesH, baseYHead))
            win.blit(header5, (baseXGoalsH, baseYHead))
            win.blit(header6, (baseXAssistsH, baseYHead))
            win.blit(header7, (baseXSavesH, baseYHead))
            win.blit(header8, (baseXShotsH, baseYHead))

            #Draw Dynamic Strings
            if spacesNeeded < 8:
                win.blit(num0, (baseXRank, baseYStat + (baseYSpacerStat * 1)))
                win.blit(name0, (baseXName, baseYStat + (baseYSpacerStat * 1)))
                win.blit(wlr0, (baseXWLR, baseYStat + (baseYSpacerStat * 1)))
                win.blit(wins0, (baseXWins, baseYStat + (baseYSpacerStat * 1)))
                win.blit(losses0, (baseXLosses, baseYStat + (baseYSpacerStat * 1)))
                win.blit(goals0, (baseXGoals, baseYStat + (baseYSpacerStat * 1)))
                win.blit(assists0, (baseXAssists, baseYStat + (baseYSpacerStat * 1)))
                win.blit(saves0, (baseXSaves, baseYStat + (baseYSpacerStat * 1)))
                win.blit(shots0, (baseXShots, baseYStat + (baseYSpacerStat * 1)))
            if spacesNeeded < 7:
                win.blit(num1, (baseXRank, baseYStat + (baseYSpacerStat * 2)))
                win.blit(name1, (baseXName, baseYStat + (baseYSpacerStat * 2)))
                win.blit(wlr1, (baseXWLR, baseYStat + (baseYSpacerStat * 2)))
                win.blit(wins1, (baseXWins, baseYStat + (baseYSpacerStat * 2)))
                win.blit(losses1, (baseXLosses, baseYStat + (baseYSpacerStat * 2)))
                win.blit(goals1, (baseXGoals, baseYStat + (baseYSpacerStat * 2)))
                win.blit(assists1, (baseXAssists, baseYStat + (baseYSpacerStat * 2)))
                win.blit(saves1, (baseXSaves, baseYStat + (baseYSpacerStat * 2)))
                win.blit(shots1, (baseXShots, baseYStat + (baseYSpacerStat * 2)))
            if spacesNeeded < 6:
                win.blit(num2, (baseXRank, baseYStat + (baseYSpacerStat * 3)))
                win.blit(name2, (baseXName, baseYStat + (baseYSpacerStat * 3)))
                win.blit(wlr2, (baseXWLR, baseYStat + (baseYSpacerStat * 3)))
                win.blit(wins2, (baseXWins, baseYStat + (baseYSpacerStat * 3)))
                win.blit(losses2, (baseXLosses, baseYStat + (baseYSpacerStat * 3)))
                win.blit(goals2, (baseXGoals, baseYStat + (baseYSpacerStat * 3)))
                win.blit(assists2, (baseXAssists, baseYStat + (baseYSpacerStat * 3)))
                win.blit(saves2, (baseXSaves, baseYStat + (baseYSpacerStat * 3)))
                win.blit(shots2, (baseXShots, baseYStat + (baseYSpacerStat * 3)))
            if spacesNeeded < 5:
                win.blit(num3, (baseXRank, baseYStat + (baseYSpacerStat * 4)))
                win.blit(name3, (baseXName, baseYStat + (baseYSpacerStat * 4)))
                win.blit(wlr3, (baseXWLR, baseYStat + (baseYSpacerStat * 4)))
                win.blit(wins3, (baseXWins, baseYStat + (baseYSpacerStat * 4)))
                win.blit(losses3, (baseXLosses, baseYStat + (baseYSpacerStat * 4)))
                win.blit(goals3, (baseXGoals, baseYStat + (baseYSpacerStat * 4)))
                win.blit(assists3, (baseXAssists, baseYStat + (baseYSpacerStat * 4)))
                win.blit(saves3, (baseXSaves, baseYStat + (baseYSpacerStat * 4)))
                win.blit(shots3, (baseXShots, baseYStat + (baseYSpacerStat * 4)))
            if spacesNeeded < 4:
                win.blit(num4, (baseXRank, baseYStat + (baseYSpacerStat * 5)))
                win.blit(name4, (baseXName, baseYStat + (baseYSpacerStat * 5)))
                win.blit(wlr4, (baseXWLR, baseYStat + (baseYSpacerStat * 5)))
                win.blit(wins4, (baseXWins, baseYStat + (baseYSpacerStat * 5)))
                win.blit(losses4, (baseXLosses, baseYStat + (baseYSpacerStat * 5)))
                win.blit(goals4, (baseXGoals, baseYStat + (baseYSpacerStat * 5)))
                win.blit(assists4, (baseXAssists, baseYStat + (baseYSpacerStat * 5)))
                win.blit(saves4, (baseXSaves, baseYStat + (baseYSpacerStat * 5)))
                win.blit(shots4, (baseXShots, baseYStat + (baseYSpacerStat * 5)))
            if spacesNeeded < 3:
                win.blit(num5, (baseXRank, baseYStat + (baseYSpacerStat * 6)))
                win.blit(name5, (baseXName, baseYStat + (baseYSpacerStat * 6)))
                win.blit(wlr5, (baseXWLR, baseYStat + (baseYSpacerStat * 6)))
                win.blit(wins5, (baseXWins, baseYStat + (baseYSpacerStat * 6)))
                win.blit(losses5, (baseXLosses, baseYStat + (baseYSpacerStat * 6)))
                win.blit(goals5, (baseXGoals, baseYStat + (baseYSpacerStat * 6)))
                win.blit(assists5, (baseXAssists, baseYStat + (baseYSpacerStat * 6)))
                win.blit(saves5, (baseXSaves, baseYStat + (baseYSpacerStat * 6)))
                win.blit(shots5, (baseXShots, baseYStat + (baseYSpacerStat * 6)))
            if spacesNeeded < 2:
                win.blit(num6, (baseXRank, baseYStat + (baseYSpacerStat * 7)))
                win.blit(name6, (baseXName, baseYStat + (baseYSpacerStat * 7)))
                win.blit(wlr6, (baseXWLR, baseYStat + (baseYSpacerStat * 7)))
                win.blit(wins6, (baseXWins, baseYStat + (baseYSpacerStat * 7)))
                win.blit(losses6, (baseXLosses, baseYStat + (baseYSpacerStat * 7)))
                win.blit(goals6, (baseXGoals, baseYStat + (baseYSpacerStat * 7)))
                win.blit(assists6, (baseXAssists, baseYStat + (baseYSpacerStat * 7)))
                win.blit(saves6, (baseXSaves, baseYStat + (baseYSpacerStat * 7)))
                win.blit(shots6, (baseXShots, baseYStat + (baseYSpacerStat * 7)))
            if spacesNeeded < 1:
                win.blit(num7, (baseXRank, baseYStat + (baseYSpacerStat * 8)))
                win.blit(name7, (baseXName, baseYStat + (baseYSpacerStat * 8)))
                win.blit(wlr7, (baseXWLR, baseYStat + (baseYSpacerStat * 8)))
                win.blit(wins7, (baseXWins, baseYStat + (baseYSpacerStat * 8)))
                win.blit(losses7, (baseXLosses, baseYStat + (baseYSpacerStat * 8)))
                win.blit(goals7, (baseXGoals, baseYStat + (baseYSpacerStat * 8)))
                win.blit(assists7, (baseXAssists, baseYStat + (baseYSpacerStat * 8)))
                win.blit(saves7, (baseXSaves, baseYStat + (baseYSpacerStat * 8)))
                win.blit(shots7, (baseXShots, baseYStat + (baseYSpacerStat * 8)))
            

            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btnUpArrowHov = buttonClassObj.imgHover(btnUpArrow)
            btnDownArrowHov = buttonClassObj.imgHover(btnDownArrow)
            seasonStatsHov  = buttonClassObj.imgHover(btnSeasonStats)
            careerStatsHov  = buttonClassObj.imgHover(btnCareerStats)

            btnTeamAscHov = buttonClassObj.imgHover(btnTeamAsc)
            btnWLAscHov = buttonClassObj.imgHover(btnWLAsc)
            btnWinsAscHov = buttonClassObj.imgHover(btnWinsAsc)
            btnLossesAscHov = buttonClassObj.imgHover(btnLossAsc)
            btnGoalsAscHov = buttonClassObj.imgHover(btnGoalsAsc)
            btnSavesAscHov = buttonClassObj.imgHover(btnSavesAsc)
            btnAssistsAscHov = buttonClassObj.imgHover(btnAssistsAsc)
            btnShotsAscHov = buttonClassObj.imgHover(btnShotsAsc)

            btnTeamDesHov = buttonClassObj.imgHover(btnTeamDes)
            btnWLDesHov = buttonClassObj.imgHover(btnWLDes)
            btnWinsDesHov = buttonClassObj.imgHover(btnWinsDes)
            btnLossesDesHov = buttonClassObj.imgHover(btnLossDes)
            btnGoalsDesHov = buttonClassObj.imgHover(btnGoalsDes)
            btnSavesDesHov = buttonClassObj.imgHover(btnSavesDes)
            btnAssistsDesHov = buttonClassObj.imgHover(btnAssistsDes)
            btnShotsDesHov = buttonClassObj.imgHover(btnShotsDes)





            #Draw Buttons
            #if button hovered change img to hovered image

            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)

            if btnUpArrowHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(1000,170,75,75)) #rect(x,y,length,height) #Slot 1
                btnUpArrow.draw(win)
            else:
                btnUpArrow.draw(win)

            if btnDownArrowHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(1000,500,75,75)) #rect(x,y,length,height) #Slot 1
                btnDownArrow.draw(win)
            else:
                btnDownArrow.draw(win)

            if seasonStatsHov == True:
                btnSeasonStatsH.draw(win)
            else:
                btnSeasonStats.draw(win)

            if careerStatsHov == True:
                btnCareerStatsH.draw(win)
            else:
                btnCareerStats.draw(win)
            ##Ascending Arrows
            if btnTeamAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(330, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnTeamAsc.draw(win)
            else:
                btnTeamAsc.draw(win)
            if btnWLAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(475, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnWLAsc.draw(win)
            else:
                btnWLAsc.draw(win)
            if btnWinsAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(542, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnWinsAsc.draw(win)
            else:
                btnWinsAsc.draw(win)
            if btnLossesAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(635, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnLossAsc.draw(win)
            else:
                btnLossAsc.draw(win)
            if btnGoalsAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(715, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnGoalsAsc.draw(win)
            else:
                btnGoalsAsc.draw(win)
            if btnAssistsAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(815, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnAssistsAsc.draw(win)
            else:
                btnAssistsAsc.draw(win)
            if btnSavesAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(895, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnSavesAsc.draw(win)
            else:
                btnSavesAsc.draw(win)
            if btnShotsAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(970, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnShotsAsc.draw(win)
            else:
                btnShotsAsc.draw(win)
            ##Descending Arrows
            if btnTeamDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(330, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnTeamDes.draw(win)
            else:
                btnTeamDes.draw(win)
            if btnWLDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(475, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnWLDes.draw(win)
            else:
                btnWLDes.draw(win)
            if btnWinsDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(542, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnWinsDes.draw(win)
            else:
                btnWinsDes.draw(win)
            if btnLossesDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(635, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnLossDes.draw(win)
            else:
                btnLossDes.draw(win)
            if btnGoalsDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(715, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnGoalsDes.draw(win)
            else:
                btnGoalsDes.draw(win)
            if btnAssistsDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(815, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnAssistsDes.draw(win)
            else:
                btnAssistsDes.draw(win)
            if btnSavesDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(895, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnSavesDes.draw(win)
            else:
                btnSavesDes.draw(win)
            if btnShotsDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(970, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnShotsDes.draw(win)
            else:
                btnShotsDes.draw(win)


            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click locker room btn")
                    gameState[1] = 'lockerRoom'
                if btnUpArrowHov == True:
                    print("mouse click up arrow btn")
                    if startPos > 7:
                        startPos = startPos - 8
                    print("pos0: ", startPos)
                    print("spaces needed:", spacesNeeded)
                if btnDownArrowHov == True:
                    print("mouse click down arrow btn")
                    if startPos + 8 < lenTeams:
                        startPos = startPos + 8
                    print("pos0: ", startPos)
                    print("spaces needed:", spacesNeeded)
                    print("extra spaces: ", extraSpaces)
                if seasonStatsHov == True:
                    print("mouse click season stats btn")
                    seasonStats = True
                if careerStatsHov == True:
                    print("mouse click career stats btn")
                    seasonStats = False


                if btnTeamAscHov == True:
                    print("mouse click team asc btn")
                    if sortType != "player team":
                        gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "team name")
                        sortType = "player team"
                if btnWLAscHov == True:
                    print("mouse click wlr asc btn")
                    if seasonStats == True:
                        if sortType != "wlr season":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "wlr season")
                            sortType = "wlr season"
                    else:
                        if sortType != "wlr career":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "wlr career")
                            sortType = "wlr career"
                if btnWinsAscHov == True:
                    print("mouse click wlr asc btn")
                    if seasonStats == True:
                        if sortType != "wins season":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "wins season")
                            sortType = "wins season"
                    else:
                        if sortType != "wins career":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "wins career")
                            sortType = "wins career"
                if btnLossesAscHov == True:
                    print("mouse click wlr asc btn")
                    if seasonStats == True:
                        if sortType != "losses season":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "losses season")
                            sortType = "losses season"
                    else:
                        if sortType != "losses career":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "losses career")
                            sortType = "losses career"
                if btnGoalsAscHov == True:
                    print("mouse click goals asc btn")
                    if seasonStats == True:
                        if sortType != "goals season":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "goals season")
                            sortType = "goals season"
                    else:
                        if sortType != "goals career":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "goals career")
                            sortType = "goals career"
                if btnAssistsAscHov == True:
                    print("mouse click assists asc btn")
                    if seasonStats == True:
                        if sortType != "assists season":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "assists season")
                            sortType = "assists season"
                    else:
                        if sortType != "assists career":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "assists career")
                            sortType = "assists career"
                if btnSavesAscHov == True:
                    print("mouse click saves asc btn")
                    if seasonStats == True:
                        if sortType != "saves season":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "saves season")
                            sortType = "saves season"
                    else:
                        if sortType != "saves career":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "saves career")
                            sortType = "saves career"
                if btnShotsAscHov == True:
                    print("mouse click shots asc btn")
                    if seasonStats == True:
                        if sortType != "shots season":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "shots season")
                            sortType = "shots season"
                    else:
                        if sortType != "shots career":
                            gameState[3] = sortFunctions.sortAscendingObjectList(gameState[3], "shots career")
                            sortType = "shots career"

                if btnTeamDesHov == True:
                    print("mouse click team des btn")
                    if sortType != "team name des":
                        gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "team name")
                        sortType = "team name des"
                if btnWLDesHov == True:
                    print("mouse click wlr des btn")
                    if seasonStats == True:
                        if sortType != "wlr season des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "wlr season")
                            sortType = "wlr season des"
                    else:
                        if sortType != "wlr career des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "wlr career")
                            sortType = "wlr career des"
                if btnWinsDesHov == True:
                    print("mouse click wlr des btn")
                    if seasonStats == True:
                        if sortType != "wins season des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "wins season")
                            sortType = "wins season des"
                    else:
                        if sortType != "wins career des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "wins career")
                            sortType = "wins career des"
                if btnLossesDesHov == True:
                    print("mouse click wlr des btn")
                    if seasonStats == True:
                        if sortType != "losses season des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "losses season")
                            sortType = "losses season des"
                    else:
                        if sortType != "losses career des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "losses career")
                            sortType = "losses career des"
                if btnGoalsDesHov == True:
                    print("mouse click goals des btn")
                    if seasonStats == True:
                        if sortType != "goals season des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "goals season")
                            sortType = "goals season des"
                    else:
                        if sortType != "goals career des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "goals career")
                            sortType = "goals career des"
                if btnAssistsDesHov == True:
                    print("mouse click assists des btn")
                    if seasonStats == True:
                        if sortType != "assists season des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "assists season")
                            sortType = "assists season des"
                    else:
                        if sortType != "assists career des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "assists career")
                            sortType = "assists career des"
                if btnSavesDesHov == True:
                    print("mouse click saves des btn")
                    if seasonStats == True:
                        if sortType != "saves season des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "saves season")
                            sortType = "saves season des"
                    else:
                        if sortType != "saves career des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "saves career")
                            sortType = "saves career des"
                if btnShotsDesHov == True:
                    print("mouse click shots des btn")
                    if seasonStats == True:
                        if sortType != "shots season des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "shots season")
                            sortType = "shots season des"
                    else:
                        if sortType != "shots career des":
                            gameState[3] = sortFunctions.sortDescendingObjectList(gameState[3], "shots career")
                            sortType = "shots career des"

                    

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)