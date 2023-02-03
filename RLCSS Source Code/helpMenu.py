import pygame, sys
import buttonClassObj

# #display help menu
def helpMenuFunc(gameState, win, basicFont, backgroundimg, helptxt1img, helptxt2img, buttonimg, button2img):

    print('in how to play menu - ', gameState)

    #Create Strings
    title = basicFont.render('How to Play', False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Start Menu', 35, 15)

    #Menu Loop
    while gameState[1] == 'howToPlay':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (510,70))
            #Draw Images
            win.blit(helptxt1img, (75, 200))
            win.blit(helptxt2img, (75, 300))
            
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
                    print("mouse click start menu btn")
                    gameState[1] = 'start'

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)