import pygame, sys
import buttonClassObj
import saveData

#check if new save by checking if second row in corrosponding game data file is 0 (new save) or 1 (old save)
def checkNewSave(gameState):
    print("in checkNewSave Function")
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
    #this calls the cunction to search for thestrings and return the string in the row below (so either a 0 or 1)
    newSave = saveData.read(gameState, saveState)
    print("newSave: ", newSave)
    return newSave

#display start menu
def startMenuFunc(gameState, win, basicFont, backgroundimg, trophyimg, buttonimg, button2img):

    print('in start menu func')

    #Create Strings
    title = basicFont.render('Rocket League Championship Series Simulator', False, (255, 255, 255))

    #create buttons (button image, image x, image y, font, string, text x offset, text y offset)
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) - 150, basicFont, 'Save 1', 75, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) - 150, basicFont, 'Save 1', 75, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2), basicFont, 'Save 2', 75, 15)
    btn2H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2), basicFont, 'Save 2', 75, 15)
    btn3 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 150, basicFont, 'Save 3', 75, 15)
    btn3H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 150, basicFont, 'Save 3', 75, 15)
    btn4 = buttonClassObj.buttonClass(buttonimg, win.get_width() - 400, (win.get_height() / 2) + 200, basicFont, 'How to Play', 25, 15)
    btn4H = buttonClassObj.buttonClass(button2img, win.get_width() - 400, (win.get_height() / 2) + 200, basicFont, 'How to Play', 25, 15)
    btn5 = buttonClassObj.buttonClass(buttonimg, 100, (win.get_height() / 2) + 200, basicFont, 'Settings', 50, 15)
    btn5H = buttonClassObj.buttonClass(button2img, 100, (win.get_height() / 2) + 200, basicFont, 'Settings', 50, 15)

    #Menu Loop
    while gameState[1] == 'start':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Title
            win.blit(title, (150,70))
            #Draw Images
            win.blit(trophyimg, (100, 150))
            win.blit(trophyimg, (win.get_width() - 419, 150))

            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btn2Hov = buttonClassObj.imgHover(btn2)
            btn3Hov = buttonClassObj.imgHover(btn3)
            btn4Hov = buttonClassObj.imgHover(btn4)
            btn5Hov = buttonClassObj.imgHover(btn5)

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
            if btn4Hov == True:
                btn4H.draw(win)
            else:
                btn4.draw(win)
            if btn5Hov == True:
                btn5H.draw(win)
            else:
                btn5.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click save 1 btn")
                    #change gamestate[0] to number of file to check for match in textfile
                    gameState[0] = 'gameData1.txt'
                    #check if save file is new
                    newSave = checkNewSave(gameState)
                    print("newSave After check:",newSave)
                    print(type(newSave))
                    #checks if data file is new (0) or already used (1)
                    if newSave == "0\n":
                        print('run new game menu')
                        gameState[1] = 'newSave'
                    else:
                        print('run locker room menu')
                        gameState[1] = 'openSave'
                if btn2Hov == True:
                    print("mouse click save 2 btn")
                    #change gamestate[0] to number of file to check for match in textfile
                    gameState[0] = 'gameData2.txt'
                    #check if save file is new
                    newSave = checkNewSave(gameState)
                    print("newSave After check:",newSave)
                    print(type(newSave))
                    #checks if data file is new (0) or already used (1)
                    if newSave == "0\n":
                        print('run new game menu')
                        gameState[1] = 'newSave'
                    else:
                        print('run locker room menu')
                        gameState[1] = 'openSave'
                if btn3Hov == True:
                    print("mouse click save 3 btn")
                    #change gamestate[0] to number of file to check for match in textfile
                    gameState[0] = 'gameData3.txt'
                    #check if save file is new
                    newSave = checkNewSave(gameState)
                    print("newSave After check:",newSave)
                    print(type(newSave))
                    #checks if data file is new (0) or already used (1)
                    if newSave == "0\n":
                        print('run new game menu')
                        gameState[1] = 'newSave'
                    else:
                        print('run locker room menu')
                        gameState[1] = 'openSave'
                if btn4Hov == True:
                    print("mouse click how to btn")
                    gameState[1] = 'howToPlay'
                if btn5Hov == True:
                    print("mouse click settings btn")
                    gameState[1] = 'settings'


        pygame.display.update()
        buttonClassObj.mainClock.tick(60)