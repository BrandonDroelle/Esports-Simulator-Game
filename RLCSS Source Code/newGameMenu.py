import pygame, sys
import buttonClassObj
import saveData

# #display locker room menu
def newGameMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img):

    print('in new game menu - ', gameState)

    #Create Strings
    title = basicFont.render('New Game', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Game', 35, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Game', 35, 15)


    #Menu Loop
    while gameState[1] == 'newSave':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (510,70))
            #Draw Images
            #win.blit(upArrowUIimg, (100, 150))
            
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
                    print("mouse click start game btn")
                    #update save file to not new save so when reopened goes directly to locker room and not new game
                    if gameState[0] == 'gameData1.txt':
                        saveNum = 1
                    if gameState[0] == 'gameData2.txt':
                        saveNum = 2
                    if gameState[0] == 'gameData3.txt':
                        saveNum = 3
                    saveNum = str(saveNum)
                    #creates the string to search the data file in this case "save x\n" (x being 1 2 3 depending on which file to be opened)
                    saveState = "save " + saveNum + "\n"
                    print ("saveState: ", saveState)
                    saveData.write(gameState, saveState, 1) #gameState, type of data, new data to be written
                    gameState[1] = 'openSave'
                    


        pygame.display.update()
        buttonClassObj.mainClock.tick(60)