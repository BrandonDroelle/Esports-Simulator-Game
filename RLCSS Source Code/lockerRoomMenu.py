import pygame, sys
import buttonClassObj
import saveData

# #display locker room menu
def lockerRoomMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img):

    print('in locker room - ', gameState)

    #Create Strings
    title = basicFont.render('Locker Room', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) - 200, basicFont, 'test file', 35, 15)
    btn2H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) - 200, basicFont, 'test file', 35, 15)

    #Menu Loop
    while gameState[1] == 'lockerRoom':
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
                    print("mouse click test file btn")
                    #saveData.write()
                    testStr = "player name" + "\n"
                    saveData.read(gameState, testStr)


        pygame.display.update()
        buttonClassObj.mainClock.tick(60)