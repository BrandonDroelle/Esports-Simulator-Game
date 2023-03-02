import pygame, sys, os
import buttonClassObj
import saveData

# #display delete save menu
def deleteSaveMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img):

    print('in delete save menu - ', gameState)

    #Create Strings

    if gameState[0] == 'gameData1.txt':
        saveFileName = "save 1"
    if gameState[0] == "gameData2.txt":
        saveFileName = "save 2"
    if gameState[0] == "gameData3.txt":
        saveFileName = "save 3"

    #This string replaces text in save file
    newSaveData = saveFileName + "\n0\nplayer name\n\nplayer team\n\ncareer goals\n\ncareer assists\n\ncareer saves\n\ncareer shots\n\ncurrent season\n\ncurrent week\n\n"

    title = basicFont.render('Delete ' + saveFileName, False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) - 200, basicFont, 'Delete', 70, 15)
    btn2H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) - 200, basicFont, 'Delete', 70, 15)

    #Menu Loop
    while gameState[1] == 'deleteSave':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (510,70))
            #Draw Images

            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btn2Hov = buttonClassObj.imgHover(btn2)

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

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click start menu btn")
                    gameState[1] = 'start'
                if btn2Hov == True:
                    print("mouse click delete save btn")
                    #update save file to brand new save
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
                    fileLocationString = r"C:\Users\bmdro\Documents\Python Projects\RLCS Simulator\RLCSS (GitRepo)\\" + gameState[0]
                    print("file to remove" + fileLocationString)
                    #deletes specified file
                    os.remove(fileLocationString)
                    print("save file deleted")
                    #create to file with tempalte
                    saveData.create(gameState, newSaveData)
                    print("save file created")
                    gameState[1] = 'start'

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)