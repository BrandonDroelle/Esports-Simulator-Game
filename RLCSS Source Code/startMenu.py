import pygame, sys
import buttonClassObj

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
                    gameState[1] = 'openSave'
                if btn2Hov == True:
                    print("mouse click save 2 btn")
                    gameState[0] = 'gameData2.txt'
                    gameState[1] = 'openSave'
                if btn3Hov == True:
                    print("mouse click save 3 btn")
                    gameState[0] = 'gameData3.txt'
                    gameState[1] = 'openSave'
                if btn4Hov == True:
                    print("mouse click how to btn")
                    gameState[1] = 'howToPlay'
                if btn5Hov == True:
                    print("mouse click settings btn")
                    gameState[1] = 'settings'


        pygame.display.update()
        buttonClassObj.mainClock.tick(60)