import pygame, sys
import createCache
import generateSchedule
import saveGame
import buttonClassObj
import generateSchedule


# #display schedule menu
def scheduleMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, keyBoardKeys):

    print('in schedule - ', gameState)

    numberOfWeeks = 21
    extraSpaces = 3 - (numberOfWeeks % 3)   #Get mod to avoid out of bounds errors when bottom of list is not mod 0
    spacesNeeded = 0

    #Variables to set background shapes to
    darkGrey = (100, 100, 100)
    lightGrey = (150, 150, 150)

    #Variables to set headers to
    smallFont = pygame.font.SysFont(None,32)
    baseYHead = 125
    baseXHead = 225
    baseXHeadSpacer = 350

    
    


    #variables to set dynamic strings to
    page = 0            #adjusts which week shows for each column
    pageMax = (numberOfWeeks // 3) - 1
    startPos = 0
    baseYStat = 140
    baseYSpacerStat = 35

    baseX = 125
    spacerX = 350

    #Create Strings
    currentSeason = saveGame.getSeason(gameState)
    titleText = "Season " + str(currentSeason)
    title = basicFont.render(titleText, False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)
    btnRightArrow = buttonClassObj.buttonClass(keyBoardKeys[52], 1175, 300, basicFont, '',0, 0)
    btnLeftArrow = buttonClassObj.buttonClass(keyBoardKeys[51], 25, 300, basicFont, '',0, 0)

    #Menu Loop
    while gameState[1] == 'schedule':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #create Dynamic Variable
            col1Week = 1 + (page * 3)
            col2Week = 2 + (page * 3)
            col3Week = 3 + (page * 3)

            #print("W1G1: ", generateSchedule.getMatchup(gameState, 1, 1))
            #print("W1G2: ", generateSchedule.getMatchup(gameState, 1, 2))
            #print("W1G3: ", generateSchedule.getMatchup(gameState, 1, 3))
            #print("W1G4: ", generateSchedule.getMatchup(gameState, 1, 4))
            #print("W1G5: ", generateSchedule.getMatchup(gameState, 1, 5))
            #print("W1G6: ", generateSchedule.getMatchup(gameState, 1, 6))
            #print("W1G7: ", generateSchedule.getMatchup(gameState, 1, 7))
            #print("W1G8: ", generateSchedule.getMatchup(gameState, 1, 8))
            #print("W1G9: ", generateSchedule.getMatchup(gameState, 1, 9))
            #print("W1G10: ", generateSchedule.getMatchup(gameState, 1, 10))
            #print("W1G11: ", generateSchedule.getMatchup(gameState, 1, 11))

            #print("W2G1: ", generateSchedule.getMatchup(gameState, 2, 1))
            #print("W2G2: ", generateSchedule.getMatchup(gameState, 2, 2))
            #print("W2G3: ", generateSchedule.getMatchup(gameState, 2, 3))
            #print("W2G4: ", generateSchedule.getMatchup(gameState, 2, 4))
            #print("W2G5: ", generateSchedule.getMatchup(gameState, 2, 5))
            #print("W2G6: ", generateSchedule.getMatchup(gameState, 2, 6))
            #print("W2G7: ", generateSchedule.getMatchup(gameState, 2, 7))
            #print("W2G8: ", generateSchedule.getMatchup(gameState, 2, 8))
            #print("W2G9: ", generateSchedule.getMatchup(gameState, 2, 9))
            #print("W2G10: ", generateSchedule.getMatchup(gameState, 2, 10))
            #print("W2G11: ", generateSchedule.getMatchup(gameState, 2, 11))

            #Create Dynamic Strings
            if col1Week <= numberOfWeeks:
                header1 = smallFont.render('Week ' + str(col1Week), False, (255, 255, 255))
                wag1 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 1), False, (255, 255, 255))
                wag2 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 2), False, (255, 255, 255))
                wag3 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 3), False, (255, 255, 255))
                wag4 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 4), False, (255, 255, 255))
                wag5 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 5), False, (255, 255, 255))
                wag6 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 6), False, (255, 255, 255))
                wag7 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 7), False, (255, 255, 255))
                wag8 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 8), False, (255, 255, 255))
                wag9 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 9), False, (255, 255, 255))
                wag10 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 10), False, (255, 255, 255))
                wag11 = smallFont.render(generateSchedule.getMatchup(gameState, col1Week, 11), False, (255, 255, 255))

            if col2Week <= numberOfWeeks:
                header2 = smallFont.render('Week ' + str(col2Week), False, (255, 255, 255))
                wbg1 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 1), False, (255, 255, 255))
                wbg2 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 2), False, (255, 255, 255))
                wbg3 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 3), False, (255, 255, 255))
                wbg4 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 4), False, (255, 255, 255))
                wbg5 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 5), False, (255, 255, 255))
                wbg6 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 6), False, (255, 255, 255))
                wbg7 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 7), False, (255, 255, 255))
                wbg8 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 8), False, (255, 255, 255))
                wbg9 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 9), False, (255, 255, 255))
                wbg10 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 10), False, (255, 255, 255))
                wbg11 = smallFont.render(generateSchedule.getMatchup(gameState, col2Week, 11), False, (255, 255, 255))

            if col3Week <= numberOfWeeks:
                header3 = smallFont.render('Week ' + str(col3Week), False, (255, 255, 255))
                wcg1 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 1), False, (255, 255, 255))
                wcg2 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 2), False, (255, 255, 255))
                wcg3 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 3), False, (255, 255, 255))
                wcg4 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 4), False, (255, 255, 255))
                wcg5 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 5), False, (255, 255, 255))
                wcg6 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 6), False, (255, 255, 255))
                wcg7 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 7), False, (255, 255, 255))
                wcg8 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 8), False, (255, 255, 255))
                wcg9 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 9), False, (255, 255, 255))
                wcg10 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 10), False, (255, 255, 255))
                wcg11 = smallFont.render(generateSchedule.getMatchup(gameState, col3Week, 11), False, (255, 255, 255))


            #Draw Background
            win.blit(backgroundimg, (0, 0))
            
            #Draw headers
            win.blit(title, (525,70))
            win.blit(header1, (baseXHead + (baseXHeadSpacer * 0), baseYHead))
            win.blit(header2, (baseXHead + (baseXHeadSpacer * 1), baseYHead))
            win.blit(header3, (baseXHead + (baseXHeadSpacer * 2), baseYHead))

            #Draw Strings

            #Draw Images

            #Draw Dynamic Strings
            if col1Week <= numberOfWeeks:
                win.blit(wag1, (baseX, baseYStat + (baseYSpacerStat * 1)))
                win.blit(wag2, (baseX, baseYStat + (baseYSpacerStat * 2)))
                win.blit(wag3, (baseX, baseYStat + (baseYSpacerStat * 3)))
                win.blit(wag4, (baseX, baseYStat + (baseYSpacerStat * 4)))
                win.blit(wag5, (baseX, baseYStat + (baseYSpacerStat * 5)))
                win.blit(wag6, (baseX, baseYStat + (baseYSpacerStat * 6)))
                win.blit(wag7, (baseX, baseYStat + (baseYSpacerStat * 7)))
                win.blit(wag8, (baseX, baseYStat + (baseYSpacerStat * 8)))
                win.blit(wag9, (baseX, baseYStat + (baseYSpacerStat * 9)))
                win.blit(wag10, (baseX, baseYStat + (baseYSpacerStat * 10)))
                win.blit(wag11, (baseX, baseYStat + (baseYSpacerStat * 11)))

            if col2Week <= numberOfWeeks:
                win.blit(wbg1, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 1)))
                win.blit(wbg2, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 2)))
                win.blit(wbg3, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 3)))
                win.blit(wbg4, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 4)))
                win.blit(wbg5, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 5)))
                win.blit(wbg6, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 6)))
                win.blit(wbg7, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 7)))
                win.blit(wbg8, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 8)))
                win.blit(wbg9, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 9)))
                win.blit(wbg10, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 10)))
                win.blit(wbg11, (baseX + (spacerX * 1), baseYStat + (baseYSpacerStat * 11)))

            if col3Week <= numberOfWeeks:
                win.blit(wcg1, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 1)))
                win.blit(wcg2, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 2)))
                win.blit(wcg3, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 3)))
                win.blit(wcg4, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 4)))
                win.blit(wcg5, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 5)))
                win.blit(wcg6, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 6)))
                win.blit(wcg7, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 7)))
                win.blit(wcg8, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 8)))
                win.blit(wcg9, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 9)))
                win.blit(wcg10, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 10)))
                win.blit(wcg11, (baseX + (spacerX * 2), baseYStat + (baseYSpacerStat * 11)))
            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btnRightArrowHov = buttonClassObj.imgHover(btnRightArrow)
            btnLeftArrowHov = buttonClassObj.imgHover(btnLeftArrow)

            #Draw Buttons
            #if button hovered change img to hovered image
            if btn1Hov == True:
                btn1H.draw(win)
            else:
                btn1.draw(win)

            if page < pageMax:
                if btnRightArrowHov == True:
                    pygame.draw.rect(win, darkGrey, pygame.Rect(1175, 300,75,75)) #rect(x,y,length,height) #Slot 1
                    btnRightArrow.draw(win)
                else:
                    btnRightArrow.draw(win)

            if page > 0:
                if btnLeftArrowHov == True:
                    pygame.draw.rect(win, darkGrey, pygame.Rect(25, 300,75,75)) #rect(x,y,length,height) #Slot 1
                    btnLeftArrow.draw(win)
                else:
                    btnLeftArrow.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click locker room btn")
                    gameState[1] = 'lockerRoom'
                if btnRightArrowHov == True:
                    print("mouse click right arrow btn")
                    if page < pageMax:
                        page = page + 1
                if btnLeftArrowHov == True:
                    print("mouse click left arrow btn")
                    if page > 0:
                        page = page - 1

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)