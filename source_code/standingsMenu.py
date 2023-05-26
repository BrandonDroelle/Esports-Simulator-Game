import pygame, sys
import buttonClassObj

# #display settings menu
def standingsMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img):

    print('in standings - ', gameState)

    #Create Strings
    title = basicFont.render('Standings', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) + 200, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) + 200, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 450, (win.get_height() / 2) + 200, basicFont, 'Player Awards', 10, 15)
    btn2H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 450, (win.get_height() / 2) + 200, basicFont, 'Player Awards', 10, 15)

    #Menu Loop
    while gameState[1] == 'standings':
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
                    print("mouse click locker room btn")
                    gameState[1] = 'lockerRoom'
                if btn2Hov == True:
                    print("mouse click player awards btn")
                    gameState[1] = 'playerAwards'

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)