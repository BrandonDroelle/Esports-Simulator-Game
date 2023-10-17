from tracemalloc import start
import pygame, sys
import buttonClassObj
import sortFunctions

# #display player stats menu
def playerStatsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, keyBoardKeys):

    print('in player stats - ', gameState)

    #Variable to determine which stats to display
    seasonStats = True

    #varible to track how stats are currently sorted
    sortType = "none"
    #set default sort to player name asc
    gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "player names")

    #Variables to set background shapes to
    baseX = 250
    baseY = 175
    height = 50
    width = 750
    darkGrey = (100, 100, 100)
    lightGrey = (150, 150, 150)

    #Variables to set headers to
    smallFont = pygame.font.SysFont(None,32)
    baseXHead = 175
    baseYHead = 140
    baseSpacer = 120

    #Variables to set stat strings to
    startPos = 0
    baseYStat = 140
    baseYSpacerStat = 50

    baseXRank = 215
    baseXName = 265
    baseXTeam = 400
    baseXGoals = 585
    baseXAssists = 690
    baseXSaves = 805
    baseXShots = 920
    
    #resize asc/des arrow buttons
    smallArrowSize = 15
    ascArrow = keyBoardKeys[49]
    ascArrow = pygame.transform.scale(ascArrow, (smallArrowSize, smallArrowSize))
    desArrow = keyBoardKeys[50]
    desArrow = pygame.transform.scale(desArrow, (smallArrowSize, smallArrowSize))

    ascArrowY = 135
    desArrowy = 150

    #print("length of player objects: ", len(gameState[2]))
    lenPlayers = len(gameState[2])
    #print("Player 0 Name: ", gameState[2][0].getName())
    extraSpaces = 8 - (lenPlayers % 8)   #Get mod to avoid out of bounds errors when bottom of list is not mod 0
    spacesNeeded = 0
    #print("mod lenPlayers: ", extraSpaces)
 

    #Create Strings
    title = basicFont.render('Player Stats', False, (255, 255, 255))
    subTitle1 = basicFont.render('Season', False, (255, 255, 255))
    subTitle2 = basicFont.render('Career', False, (255, 255, 255))
    header1 = smallFont.render('Player', False, (255, 255, 255))
    header2 = smallFont.render('Team', False, (255, 255, 255))
    header3 = smallFont.render('Goals', False, (255, 255, 255))
    header4 = smallFont.render('Assists', False, (255, 255, 255))
    header5 = smallFont.render('Saves', False, (255, 255, 255))
    header6 = smallFont.render('Shots', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, 'Locker Room', 10, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, 'Locker Room', 10, 15)
    btnUpArrow = buttonClassObj.buttonClass(keyBoardKeys[49], 1000, 170, basicFont, '',0, 0)
    btnDownArrow = buttonClassObj.buttonClass(keyBoardKeys[50], 1000, 500, basicFont, '',0, 0)
    btnSeasonStats = buttonClassObj.buttonClass(buttonimg, 100, (win.get_height() / 2) + 250, basicFont, 'Season Stats',10, 15)
    btnSeasonStatsH = buttonClassObj.buttonClass(button2img, 100, (win.get_height() / 2) + 250, basicFont, 'Season Stats',10, 15)
    btnCareerStats = buttonClassObj.buttonClass(buttonimg, (win.get_width() - 400), (win.get_height() / 2) + 250, basicFont, 'Career Stats',10, 15)
    btnCareerStatsH = buttonClassObj.buttonClass(button2img, (win.get_width() - 400), (win.get_height() / 2) + 250, basicFont, 'Career Stats',10, 15)
    btnPlayerAsc = buttonClassObj.buttonClass(ascArrow, 340, ascArrowY, basicFont, '',0, 0)
    btnTeamAsc = buttonClassObj.buttonClass(ascArrow, 455, ascArrowY, basicFont, '',0, 0)
    btnGoalsAsc = buttonClassObj.buttonClass(ascArrow, 620, ascArrowY, basicFont, '',0, 0)
    btnAssistsAsc = buttonClassObj.buttonClass(ascArrow, 740, ascArrowY, basicFont, '',0, 0)
    btnSavesAsc = buttonClassObj.buttonClass(ascArrow, 845, ascArrowY, basicFont, '',0, 0)
    btnShotsAsc = buttonClassObj.buttonClass(ascArrow, 960, ascArrowY, basicFont, '',0, 0)
    btnPlayerDes = buttonClassObj.buttonClass(desArrow, 340, desArrowy, basicFont, '',0, 0)
    btnTeamDes = buttonClassObj.buttonClass(desArrow, 455, desArrowy, basicFont, '',0, 0)
    btnGoalsDes = buttonClassObj.buttonClass(desArrow, 620, desArrowy, basicFont, '',0, 0)
    btnAssistsDes = buttonClassObj.buttonClass(desArrow, 740, desArrowy, basicFont, '',0, 0)
    btnSavesDes = buttonClassObj.buttonClass(desArrow, 845, desArrowy, basicFont, '',0, 0)
    btnShotsDes = buttonClassObj.buttonClass(desArrow, 960, desArrowy, basicFont, '',0, 0)

    #Menu Loop
    while gameState[1] == 'playerStats':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if startPos + 8 > lenPlayers:
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
                name0 = smallFont.render(gameState[2][pos0].getName(), False, (255, 255, 255))
                team0 = smallFont.render(gameState[2][pos0].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals0 = smallFont.render(str(gameState[2][pos0].getGoalsSeason()), False, (255, 255, 255))
                    assists0 = smallFont.render(str(gameState[2][pos0].getAssistsSeason()), False, (255, 255, 255))
                    saves0 = smallFont.render(str(gameState[2][pos0].getSavesSeason()), False, (255, 255, 255))
                    shots0 = smallFont.render(str(gameState[2][pos0].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals0 = smallFont.render(str(gameState[2][pos0].getGoalsCareer()), False, (255, 255, 255))
                    assists0 = smallFont.render(str(gameState[2][pos0].getAssistsCareer()), False, (255, 255, 255))
                    saves0 = smallFont.render(str(gameState[2][pos0].getSavesCareer()), False, (255, 255, 255))
                    shots0 = smallFont.render(str(gameState[2][pos0].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 7:
                num1 = smallFont.render(str(pos1 + 1), False, (255, 255, 255))
                name1 = smallFont.render(gameState[2][pos1].getName(), False, (255, 255, 255))
                team1 = smallFont.render(gameState[2][pos1].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals1 = smallFont.render(str(gameState[2][pos1].getGoalsSeason()), False, (255, 255, 255))
                    assists1 = smallFont.render(str(gameState[2][pos1].getAssistsSeason()), False, (255, 255, 255))
                    saves1 = smallFont.render(str(gameState[2][pos1].getSavesSeason()), False, (255, 255, 255))
                    shots1 = smallFont.render(str(gameState[2][pos1].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals1 = smallFont.render(str(gameState[2][pos1].getGoalsCareer()), False, (255, 255, 255))
                    assists1 = smallFont.render(str(gameState[2][pos1].getAssistsCareer()), False, (255, 255, 255))
                    saves1 = smallFont.render(str(gameState[2][pos1].getSavesCareer()), False, (255, 255, 255))
                    shots1 = smallFont.render(str(gameState[2][pos1].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 6:
                num2 = smallFont.render(str(pos2 + 1), False, (255, 255, 255))
                name2 = smallFont.render(gameState[2][pos2].getName(), False, (255, 255, 255))
                team2 = smallFont.render(gameState[2][pos2].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals2 = smallFont.render(str(gameState[2][pos2].getGoalsSeason()), False, (255, 255, 255))
                    assists2 = smallFont.render(str(gameState[2][pos2].getAssistsSeason()), False, (255, 255, 255))
                    saves2 = smallFont.render(str(gameState[2][pos2].getSavesSeason()), False, (255, 255, 255))
                    shots2 = smallFont.render(str(gameState[2][pos2].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals2 = smallFont.render(str(gameState[2][pos2].getGoalsCareer()), False, (255, 255, 255))
                    assists2 = smallFont.render(str(gameState[2][pos2].getAssistsCareer()), False, (255, 255, 255))
                    saves2 = smallFont.render(str(gameState[2][pos2].getSavesCareer()), False, (255, 255, 255))
                    shots2 = smallFont.render(str(gameState[2][pos2].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 5:
                num3 = smallFont.render(str(pos3 + 1), False, (255, 255, 255))
                name3 = smallFont.render(gameState[2][pos3].getName(), False, (255, 255, 255))
                team3 = smallFont.render(gameState[2][pos3].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals3 = smallFont.render(str(gameState[2][pos3].getGoalsSeason()), False, (255, 255, 255))
                    assists3 = smallFont.render(str(gameState[2][pos3].getAssistsSeason()), False, (255, 255, 255))
                    saves3 = smallFont.render(str(gameState[2][pos3].getSavesSeason()), False, (255, 255, 255))
                    shots3 = smallFont.render(str(gameState[2][pos3].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals3 = smallFont.render(str(gameState[2][pos3].getGoalsCareer()), False, (255, 255, 255))
                    assists3 = smallFont.render(str(gameState[2][pos3].getAssistsCareer()), False, (255, 255, 255))
                    saves3 = smallFont.render(str(gameState[2][pos3].getSavesCareer()), False, (255, 255, 255))
                    shots3 = smallFont.render(str(gameState[2][pos3].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 4:
                num4 = smallFont.render(str(pos4 + 1), False, (255, 255, 255))
                name4 = smallFont.render(gameState[2][pos4].getName(), False, (255, 255, 255))
                team4 = smallFont.render(gameState[2][pos4].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals4 = smallFont.render(str(gameState[2][pos4].getGoalsSeason()), False, (255, 255, 255))
                    assists4 = smallFont.render(str(gameState[2][pos4].getAssistsSeason()), False, (255, 255, 255))
                    saves4 = smallFont.render(str(gameState[2][pos4].getSavesSeason()), False, (255, 255, 255))
                    shots4 = smallFont.render(str(gameState[2][pos4].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals4 = smallFont.render(str(gameState[2][pos4].getGoalsCareer()), False, (255, 255, 255))
                    assists4 = smallFont.render(str(gameState[2][pos4].getAssistsCareer()), False, (255, 255, 255))
                    saves4 = smallFont.render(str(gameState[2][pos4].getSavesCareer()), False, (255, 255, 255))
                    shots4 = smallFont.render(str(gameState[2][pos4].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 3:
                num5 = smallFont.render(str(pos5 + 1), False, (255, 255, 255))
                name5 = smallFont.render(gameState[2][pos5].getName(), False, (255, 255, 255))
                team5 = smallFont.render(gameState[2][pos5].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals5 = smallFont.render(str(gameState[2][pos5].getGoalsSeason()), False, (255, 255, 255))
                    assists5 = smallFont.render(str(gameState[2][pos5].getAssistsSeason()), False, (255, 255, 255))
                    saves5 = smallFont.render(str(gameState[2][pos5].getSavesSeason()), False, (255, 255, 255))
                    shots5 = smallFont.render(str(gameState[2][pos5].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals5 = smallFont.render(str(gameState[2][pos5].getGoalsCareer()), False, (255, 255, 255))
                    assists5 = smallFont.render(str(gameState[2][pos5].getAssistsCareer()), False, (255, 255, 255))
                    saves5 = smallFont.render(str(gameState[2][pos5].getSavesCareer()), False, (255, 255, 255))
                    shots5 = smallFont.render(str(gameState[2][pos5].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 2:
                num6 = smallFont.render(str(pos6 + 1), False, (255, 255, 255))
                name6 = smallFont.render(gameState[2][pos6].getName(), False, (255, 255, 255))
                team6 = smallFont.render(gameState[2][pos6].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals6 = smallFont.render(str(gameState[2][pos6].getGoalsSeason()), False, (255, 255, 255))
                    assists6 = smallFont.render(str(gameState[2][pos6].getAssistsSeason()), False, (255, 255, 255))
                    saves6 = smallFont.render(str(gameState[2][pos6].getSavesSeason()), False, (255, 255, 255))
                    shots6 = smallFont.render(str(gameState[2][pos6].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals6 = smallFont.render(str(gameState[2][pos6].getGoalsCareer()), False, (255, 255, 255))
                    assists6 = smallFont.render(str(gameState[2][pos6].getAssistsCareer()), False, (255, 255, 255))
                    saves6 = smallFont.render(str(gameState[2][pos6].getSavesCareer()), False, (255, 255, 255))
                    shots6 = smallFont.render(str(gameState[2][pos6].getShotsCareer()), False, (255, 255, 255))
            if spacesNeeded < 1:
                num7 = smallFont.render(str(pos7 + 1), False, (255, 255, 255))
                name7 = smallFont.render(gameState[2][pos7].getName(), False, (255, 255, 255))
                team7 = smallFont.render(gameState[2][pos7].getCurrentTeam(), False, (255, 255, 255))
                if seasonStats == True:
                    goals7 = smallFont.render(str(gameState[2][pos7].getGoalsSeason()), False, (255, 255, 255))
                    assists7 = smallFont.render(str(gameState[2][pos7].getAssistsSeason()), False, (255, 255, 255))
                    saves7 = smallFont.render(str(gameState[2][pos7].getSavesSeason()), False, (255, 255, 255))
                    shots7 = smallFont.render(str(gameState[2][pos7].getShotsSeason()), False, (255, 255, 255))
                else:
                    goals7 = smallFont.render(str(gameState[2][pos7].getGoalsCareer()), False, (255, 255, 255))
                    assists7 = smallFont.render(str(gameState[2][pos7].getAssistsCareer()), False, (255, 255, 255))
                    saves7 = smallFont.render(str(gameState[2][pos7].getSavesCareer()), False, (255, 255, 255))
                    shots7 = smallFont.render(str(gameState[2][pos7].getShotsCareer()), False, (255, 255, 255))

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
            win.blit(title, (400,50))
            if seasonStats == True:
                win.blit(subTitle1, (675,50))
            else:
                win.blit(subTitle2, (675,50))

            #Draw headers
            win.blit(header1, (baseXHead + (baseSpacer - 30), baseYHead))
            win.blit(header2, (baseXHead + (baseSpacer * 2) - 20, baseYHead))
            win.blit(header3, (baseXHead + (baseSpacer * 3) + 20, baseYHead))
            win.blit(header4, (baseXHead + (baseSpacer * 4), baseYHead))
            win.blit(header5, (baseXHead + (baseSpacer * 5), baseYHead))
            win.blit(header6, (baseXHead + (baseSpacer * 6), baseYHead))

            #Draw Dynamic Strings
            if spacesNeeded < 8:
                win.blit(num0, (baseXRank, baseYStat + (baseYSpacerStat * 1)))
                win.blit(name0, (baseXName, baseYStat + (baseYSpacerStat * 1)))
                win.blit(team0, (baseXTeam, baseYStat + (baseYSpacerStat * 1)))
                win.blit(goals0, (baseXGoals, baseYStat + (baseYSpacerStat * 1)))
                win.blit(assists0, (baseXAssists, baseYStat + (baseYSpacerStat * 1)))
                win.blit(saves0, (baseXSaves, baseYStat + (baseYSpacerStat * 1)))
                win.blit(shots0, (baseXShots, baseYStat + (baseYSpacerStat * 1)))
            if spacesNeeded < 7:
                win.blit(num1, (baseXRank, baseYStat + (baseYSpacerStat * 2)))
                win.blit(name1, (baseXName, baseYStat + (baseYSpacerStat * 2)))
                win.blit(team1, (baseXTeam, baseYStat + (baseYSpacerStat * 2)))
                win.blit(goals1, (baseXGoals, baseYStat + (baseYSpacerStat * 2)))
                win.blit(assists1, (baseXAssists, baseYStat + (baseYSpacerStat * 2)))
                win.blit(saves1, (baseXSaves, baseYStat + (baseYSpacerStat * 2)))
                win.blit(shots1, (baseXShots, baseYStat + (baseYSpacerStat * 2)))
            if spacesNeeded < 6:
                win.blit(num2, (baseXRank, baseYStat + (baseYSpacerStat * 3)))
                win.blit(name2, (baseXName, baseYStat + (baseYSpacerStat * 3)))
                win.blit(team2, (baseXTeam, baseYStat + (baseYSpacerStat * 3)))
                win.blit(goals2, (baseXGoals, baseYStat + (baseYSpacerStat * 3)))
                win.blit(assists2, (baseXAssists, baseYStat + (baseYSpacerStat * 3)))
                win.blit(saves2, (baseXSaves, baseYStat + (baseYSpacerStat * 3)))
                win.blit(shots2, (baseXShots, baseYStat + (baseYSpacerStat * 3)))
            if spacesNeeded < 5:
                win.blit(num3, (baseXRank, baseYStat + (baseYSpacerStat * 4)))
                win.blit(name3, (baseXName, baseYStat + (baseYSpacerStat * 4)))
                win.blit(team3, (baseXTeam, baseYStat + (baseYSpacerStat * 4)))
                win.blit(goals3, (baseXGoals, baseYStat + (baseYSpacerStat * 4)))
                win.blit(assists3, (baseXAssists, baseYStat + (baseYSpacerStat * 4)))
                win.blit(saves3, (baseXSaves, baseYStat + (baseYSpacerStat * 4)))
                win.blit(shots3, (baseXShots, baseYStat + (baseYSpacerStat * 4)))
            if spacesNeeded < 4:
                win.blit(num4, (baseXRank, baseYStat + (baseYSpacerStat * 5)))
                win.blit(name4, (baseXName, baseYStat + (baseYSpacerStat * 5)))
                win.blit(team4, (baseXTeam, baseYStat + (baseYSpacerStat * 5)))
                win.blit(goals4, (baseXGoals, baseYStat + (baseYSpacerStat * 5)))
                win.blit(assists4, (baseXAssists, baseYStat + (baseYSpacerStat * 5)))
                win.blit(saves4, (baseXSaves, baseYStat + (baseYSpacerStat * 5)))
                win.blit(shots4, (baseXShots, baseYStat + (baseYSpacerStat * 5)))
            if spacesNeeded < 3:
                win.blit(num5, (baseXRank, baseYStat + (baseYSpacerStat * 6)))
                win.blit(name5, (baseXName, baseYStat + (baseYSpacerStat * 6)))
                win.blit(team5, (baseXTeam, baseYStat + (baseYSpacerStat * 6)))
                win.blit(goals5, (baseXGoals, baseYStat + (baseYSpacerStat * 6)))
                win.blit(assists5, (baseXAssists, baseYStat + (baseYSpacerStat * 6)))
                win.blit(saves5, (baseXSaves, baseYStat + (baseYSpacerStat * 6)))
                win.blit(shots5, (baseXShots, baseYStat + (baseYSpacerStat * 6)))
            if spacesNeeded < 2:
                win.blit(num6, (baseXRank, baseYStat + (baseYSpacerStat * 7)))
                win.blit(name6, (baseXName, baseYStat + (baseYSpacerStat * 7)))
                win.blit(team6, (baseXTeam, baseYStat + (baseYSpacerStat * 7)))
                win.blit(goals6, (baseXGoals, baseYStat + (baseYSpacerStat * 7)))
                win.blit(assists6, (baseXAssists, baseYStat + (baseYSpacerStat * 7)))
                win.blit(saves6, (baseXSaves, baseYStat + (baseYSpacerStat * 7)))
                win.blit(shots6, (baseXShots, baseYStat + (baseYSpacerStat * 7)))
            if spacesNeeded < 1:
                win.blit(num7, (baseXRank, baseYStat + (baseYSpacerStat * 8)))
                win.blit(name7, (baseXName, baseYStat + (baseYSpacerStat * 8)))
                win.blit(team7, (baseXTeam, baseYStat + (baseYSpacerStat * 8)))
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
            btnPlayerAscHov = buttonClassObj.imgHover(btnPlayerAsc)
            btnTeamAscHov = buttonClassObj.imgHover(btnTeamAsc)
            btnGoalsAscHov = buttonClassObj.imgHover(btnGoalsAsc)
            btnSavesAscHov = buttonClassObj.imgHover(btnSavesAsc)
            btnAssistsAscHov = buttonClassObj.imgHover(btnAssistsAsc)
            btnShotsAscHov = buttonClassObj.imgHover(btnShotsAsc)
            btnPlayerDesHov = buttonClassObj.imgHover(btnPlayerDes)
            btnTeamDesHov = buttonClassObj.imgHover(btnTeamDes)
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
            #Ascending Arrows
            if btnPlayerAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(340, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnPlayerAsc.draw(win)
            else:
                btnPlayerAsc.draw(win)
            if btnTeamAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(455, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnTeamAsc.draw(win)
            else:
                btnTeamAsc.draw(win)
            if btnGoalsAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(620, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnGoalsAsc.draw(win)
            else:
                btnGoalsAsc.draw(win)
            if btnAssistsAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(740, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnAssistsAsc.draw(win)
            else:
                btnAssistsAsc.draw(win)
            if btnSavesAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(845, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnSavesAsc.draw(win)
            else:
                btnSavesAsc.draw(win)
            if btnShotsAscHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(960, ascArrowY, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnShotsAsc.draw(win)
            else:
                btnShotsAsc.draw(win)
            #Descending Arrows
            if btnPlayerDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(340, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnPlayerDes.draw(win)
            else:
                btnPlayerDes.draw(win)
            if btnTeamDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(455, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnTeamDes.draw(win)
            else:
                btnTeamDes.draw(win)
            if btnGoalsDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(620, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnGoalsDes.draw(win)
            else:
                btnGoalsDes.draw(win)
            if btnAssistsDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(740, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnAssistsDes.draw(win)
            else:
                btnAssistsDes.draw(win)
            if btnSavesDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(845, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
                btnSavesDes.draw(win)
            else:
                btnSavesDes.draw(win)
            if btnShotsDesHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(960, desArrowy, smallArrowSize, smallArrowSize)) #rect(x,y,length,height) #Slot 1
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
                    if startPos + 8 < lenPlayers:
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

                if btnPlayerAscHov == True:
                    print("mouse click player asc btn")
                    gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "player names")
                if btnTeamAscHov == True:
                    print("mouse click team asc btn")
                    if sortType != "player team":
                        gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "player team")
                        sortType = "player team"
                if btnGoalsAscHov == True:
                    print("mouse click goals asc btn")
                    if seasonStats == True:
                        if sortType != "player goals season":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "goals season")
                            sortType = "player goals season"
                    else:
                        if sortType != "player goals career":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "goals career")
                            sortType = "player goals career"
                if btnAssistsAscHov == True:
                    print("mouse click assists asc btn")
                    if seasonStats == True:
                        if sortType != "player assists season":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "assists season")
                            sortType = "player assists season"
                    else:
                        if sortType != "player assists career":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "assists career")
                            sortType = "player assists career"
                if btnSavesAscHov == True:
                    print("mouse click saves asc btn")
                    if seasonStats == True:
                        if sortType != "player saves season":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "saves season")
                            sortType = "player saves season"
                    else:
                        if sortType != "player saves career":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "saves career")
                            sortType = "player saves career"
                if btnShotsAscHov == True:
                    print("mouse click shots asc btn")
                    if seasonStats == True:
                        if sortType != "player shots season":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "shots season")
                            sortType = "player shots season"
                    else:
                        if sortType != "player shots career":
                            gameState[2] = sortFunctions.sortAscendingObjectList(gameState[2], "shots career")
                            sortType = "player shots career"

                if btnPlayerDesHov == True:
                    print("mouse click player des btn")
                    gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "player names")
                if btnTeamDesHov == True:
                    print("mouse click team des btn")
                    if sortType != "player team des":
                        gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "player team")
                        sortType = "player team des"
                if btnGoalsDesHov == True:
                    print("mouse click goals des btn")
                    if seasonStats == True:
                        if sortType != "player goals season des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "goals season")
                            sortType = "player goals season des"
                    else:
                        if sortType != "player goals career des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "goals career")
                            sortType = "player goals career des"
                if btnAssistsDesHov == True:
                    print("mouse click assists des btn")
                    if seasonStats == True:
                        if sortType != "player assists season des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "assists season")
                            sortType = "player assists season des"
                    else:
                        if sortType != "player assists career des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "assists career")
                            sortType = "player assists career des"
                if btnSavesDesHov == True:
                    print("mouse click saves des btn")
                    if seasonStats == True:
                        if sortType != "player saves season des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "saves season")
                            sortType = "player saves season des"
                    else:
                        if sortType != "player saves career des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "saves career")
                            sortType = "player saves career des"
                if btnShotsDesHov == True:
                    print("mouse click shots des btn")
                    if seasonStats == True:
                        if sortType != "player shots season des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "shots season")
                            sortType = "player shots season des"
                    else:
                        if sortType != "player shots career des":
                            gameState[2] = sortFunctions.sortDescendingObjectList(gameState[2], "shots career")
                            sortType = "player shots career des"

                    

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)