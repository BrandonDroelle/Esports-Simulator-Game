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
    baseXStat = 250
    baseYStat = 175
    baseSpacerStat = 120
    pos0 = 0

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
    

    #Menu Loop
    while gameState[1] == 'playerStats':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #create Dynamic Variable
            pos1 = pos0 + 1
            pos2 = pos0 + 1
            pos3 = pos0 + 1
            pos4 = pos0 + 1
            pos5 = pos0 + 1
            pos6 = pos0 + 1
            pos7 = pos0 + 1
            pos8 = pos0 + 1

            #Create Dynamic Strings
            name0 = smallFont.render(playerNames[pos0], False, (255, 255, 255))


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
            win.blit(header1, (baseXHead + baseSpacer, baseYHead))
            win.blit(header2, (baseXHead + (baseSpacer * 2), baseYHead))
            win.blit(header3, (baseXHead + (baseSpacer * 3), baseYHead))
            win.blit(header4, (baseXHead + (baseSpacer * 4), baseYHead))
            win.blit(header5, (baseXHead + (baseSpacer * 5), baseYHead))
            win.blit(header6, (baseXHead + (baseSpacer * 6), baseYHead))

            win.blit(name0, (baseXStat + baseSpacerStat, baseYStat))

            #Draw Images
            btnUpArrow.draw(win)
            btnDownArrow.draw(win)

            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click locker room btn")
                    gameState[1] = 'lockerRoom'

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)