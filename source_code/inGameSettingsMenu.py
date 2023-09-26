import pygame, sys
import buttonClassObj
import createCache

# #display settings menu
def inGameSettingsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, playerNames):

    print('in in game settings - ', gameState)

    #Create Strings
    title = basicFont.render('In Game Settings', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) + 200, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) + 200, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 450, (win.get_height() / 2) + 200, basicFont, 'Main Menu', 30, 15)
    btn2H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 450, (win.get_height() / 2) + 200, basicFont, 'Main Menu', 30, 15)

    #Menu Loop
    while gameState[1] == 'inGameSettings':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (480,70))
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
                    print("mouse click return to locker room btn")
                    gameState[1] = 'lockerRoom'
                if btn2Hov == True:
                    print("mouse click return to main manu btn")
                    createCache.rmvPlayerName(gameState, playerNames)
                    gameState[2] = []
                    gameState[3] = []
                    gameState[1] = 'start'

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)