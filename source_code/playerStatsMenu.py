from tracemalloc import start
import pygame, sys
import buttonClassObj
import createCache

# #display player stats menu
def playerStatsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, keyBoardKeys):

    print('in player stats - ', gameState)

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
    baseYHead = 150
    baseSpacer = 120

    #Variables to set stat strings to
    baseXStat = 275
    baseYStat = 140
    baseXSpacerStat = 60
    baseYSpacerStat = 50
    startPos = 0

    #get stats from save file and add them to a list
    playerNames = []
    playerTeams = []
    playerGoals = []
    playerAssists = []
    playerSaves = []
    playerShots = []

    #add player names to list
    for i in (gameState[2]):
        playerName = i.getName()
        playerNames.append(playerName)
    print("playerNames: ", playerNames)
    lenPlayers = len(playerNames)
    extraSpaces = 8 - (lenPlayers % 8)   #Get mod to avoid out of bounds errors when bottom of list is not mod 0
    spacesNeeded = 0
    #print("mod lenPlayers: ", extraSpaces)

    #add player goals to list
    for i in (gameState[2]):
        print("Player: ", i.getName())
        #playerSeasonGoals = createCache.getPlayerSeasonGoals(gameState, i)
        #playerGoals.append(playerSeasonGoals)

    #Create Strings
    title = basicFont.render('Player Stats', False, (255, 255, 255))
    header1 = smallFont.render('Player', False, (255, 255, 255))
    header2 = smallFont.render('Team', False, (255, 255, 255))
    header3 = smallFont.render('Goals', False, (255, 255, 255))
    header4 = smallFont.render('Assists', False, (255, 255, 255))
    header5 = smallFont.render('Saves', False, (255, 255, 255))
    header6 = smallFont.render('Shots', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, 'Locker Room', 10, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 250, basicFont, 'Locker Room', 10, 15)
    btnUpArrow = buttonClassObj.buttonClass(keyBoardKeys[49], 1000, 150, basicFont, '',0, 0)
    btnDownArrow = buttonClassObj.buttonClass(keyBoardKeys[50], 1000, 500, basicFont, '',0, 0)
    
    print("Player Names List: ", playerNames)

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
                name0 = smallFont.render(playerNames[pos0], False, (255, 255, 255))
            if spacesNeeded < 7:
                num1 = smallFont.render(str(pos1 + 1), False, (255, 255, 255))
                name1 = smallFont.render(playerNames[pos1], False, (255, 255, 255))
            if spacesNeeded < 6:
                num2 = smallFont.render(str(pos2 + 1), False, (255, 255, 255))
                name2 = smallFont.render(playerNames[pos2], False, (255, 255, 255))
            if spacesNeeded < 5:
                num3 = smallFont.render(str(pos3 + 1), False, (255, 255, 255))
                name3 = smallFont.render(playerNames[pos3], False, (255, 255, 255))
            if spacesNeeded < 4:
                num4 = smallFont.render(str(pos4 + 1), False, (255, 255, 255))
                name4 = smallFont.render(playerNames[pos4], False, (255, 255, 255))
            if spacesNeeded < 3:
                num5 = smallFont.render(str(pos5 + 1), False, (255, 255, 255))
                name5 = smallFont.render(playerNames[pos5], False, (255, 255, 255))
            if spacesNeeded < 2:
                num6 = smallFont.render(str(pos6 + 1), False, (255, 255, 255))
                name6 = smallFont.render(playerNames[pos6], False, (255, 255, 255))
            if spacesNeeded < 1:
                num7 = smallFont.render(str(pos7 + 1), False, (255, 255, 255))
                name7 = smallFont.render(playerNames[pos7], False, (255, 255, 255))



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
            win.blit(title, (520,70))

            #Draw headers
            win.blit(header1, (baseXHead + baseSpacer, baseYHead))
            win.blit(header2, (baseXHead + (baseSpacer * 2), baseYHead))
            win.blit(header3, (baseXHead + (baseSpacer * 3), baseYHead))
            win.blit(header4, (baseXHead + (baseSpacer * 4), baseYHead))
            win.blit(header5, (baseXHead + (baseSpacer * 5), baseYHead))
            win.blit(header6, (baseXHead + (baseSpacer * 6), baseYHead))

            #Draw Dynamic Strings
            if spacesNeeded < 8:
                win.blit(num0, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 1)))
                win.blit(name0, (baseXStat, baseYStat + (baseYSpacerStat * 1)))
            if spacesNeeded < 7:
                win.blit(num1, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 2)))
                win.blit(name1, (baseXStat, baseYStat + (baseYSpacerStat * 2)))
            if spacesNeeded < 6:
                win.blit(num2, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 3)))
                win.blit(name2, (baseXStat, baseYStat + (baseYSpacerStat * 3)))
            if spacesNeeded < 5:
                win.blit(num3, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 4)))
                win.blit(name3, (baseXStat, baseYStat + (baseYSpacerStat * 4)))
            if spacesNeeded < 4:
                win.blit(num4, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 5)))
                win.blit(name4, (baseXStat, baseYStat + (baseYSpacerStat * 5)))
            if spacesNeeded < 3:
                win.blit(num5, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 6)))
                win.blit(name5, (baseXStat, baseYStat + (baseYSpacerStat * 6)))
            if spacesNeeded < 2:
                win.blit(num6, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 7)))
                win.blit(name6, (baseXStat, baseYStat + (baseYSpacerStat * 7)))
            if spacesNeeded < 1:
                win.blit(num7, (baseXStat - baseXSpacerStat, baseYStat + (baseYSpacerStat * 8)))
                win.blit(name7, (baseXStat, baseYStat + (baseYSpacerStat * 8)))
            
            

            #Draw Images
            btnUpArrow.draw(win)
            btnDownArrow.draw(win)

            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btnUpArrowHov = buttonClassObj.imgHover(btnUpArrow)
            btnDownArrowHov = buttonClassObj.imgHover(btnDownArrow)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)

            if btnUpArrowHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(1000,150,75,75)) #rect(x,y,length,height) #Slot 1
                btnUpArrow.draw(win)
            else:
                btnUpArrow.draw(win)

            if btnDownArrowHov == True:
                pygame.draw.rect(win, darkGrey, pygame.Rect(1000,500,75,75)) #rect(x,y,length,height) #Slot 1
                btnDownArrow.draw(win)
            else:
                btnDownArrow.draw(win)

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

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)