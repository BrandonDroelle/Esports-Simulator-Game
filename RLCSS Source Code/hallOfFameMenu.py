import pygame, sys
import buttonClassObj

# #display hall of fame menu
def hallOfFameMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img):

    print('in hall of fame - ', gameState)

    #Create Strings
    title = basicFont.render('Hall of Fame', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Locker Room', 10, 15)

    #Menu Loop
    while gameState[1] == 'hallOfFame':
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