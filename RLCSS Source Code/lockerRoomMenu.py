import pygame, sys
import buttonClassObj
import saveData
import saveGame

# #display locker room menu
def lockerRoomMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, teamLogos, teams):

    print('in locker room - ', gameState)

    #Create Variables
    teamName = saveGame.getTeamName(gameState)
    titleText = teamName.capitalize() + ' Locker Room'
    print('titletext: ', titleText)
    #get team logo from list
    teamLogoIndex = 99
    count = 0
    for i in teams:
        print("team name: ", teamName)
        print("teams[i]: ", teams[count])
        if teamName == teams[count]:
            print("match")
            teamLogoIndex = count
        count = count + 1
    print("team logo index: ", teamLogoIndex)
    #Create Strings
    title = basicFont.render( titleText, False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Play Next', 45, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Play Next', 45, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, 100, (win.get_height() / 2) - 200, basicFont, 'Team Stats', 30, 15)
    btn2H = buttonClassObj.buttonClass(button2img, 100, (win.get_height() / 2) - 200, basicFont, 'Team Stats', 30, 15)
    btn3 = buttonClassObj.buttonClass(buttonimg, 100, (win.get_height() / 2) - 0, basicFont, 'Player Stats', 20, 15)
    btn3H = buttonClassObj.buttonClass(button2img, 100, (win.get_height() / 2) - 0, basicFont, 'Player Stats', 20, 15)
    btn4 = buttonClassObj.buttonClass(buttonimg, 100, (win.get_height() / 2) + 200, basicFont, 'Hall of Fame', 20, 15)
    btn4H = buttonClassObj.buttonClass(button2img, 100, (win.get_height() / 2) + 200, basicFont, 'Hall of Fame', 20, 15)
    btn5 = buttonClassObj.buttonClass(buttonimg, (win.get_width() - 400), (win.get_height() / 2) - 200, basicFont, 'Schedule', 45, 15)
    btn5H = buttonClassObj.buttonClass(button2img, (win.get_width() - 400), (win.get_height() / 2) - 200, basicFont, 'Schedule', 45, 15)
    btn6 = buttonClassObj.buttonClass(buttonimg, (win.get_width() - 400), (win.get_height() / 2) - 0, basicFont, 'Standings', 35, 15)
    btn6H = buttonClassObj.buttonClass(button2img, (win.get_width() - 400), (win.get_height() / 2) - 0, basicFont, 'Standings', 35, 15)
    btn7 = buttonClassObj.buttonClass(buttonimg, (win.get_width() - 400), (win.get_height() / 2) + 200, basicFont, 'Settings', 50, 15)
    btn7H = buttonClassObj.buttonClass(button2img, (win.get_width() - 400), (win.get_height() / 2) + 200, basicFont, 'Settings', 50, 15)

    #Menu Loop
    while gameState[1] == 'lockerRoom':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (400,70))
            #Draw Images
            win.blit(teamLogos[teamLogoIndex], (520, 225))
            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btn2Hov = buttonClassObj.imgHover(btn2)
            btn3Hov = buttonClassObj.imgHover(btn3)
            btn4Hov = buttonClassObj.imgHover(btn4)
            btn5Hov = buttonClassObj.imgHover(btn5)
            btn6Hov = buttonClassObj.imgHover(btn6)
            btn7Hov = buttonClassObj.imgHover(btn7)

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
            if btn6Hov == True:
                btn6H.draw(win)
            else:
                btn6.draw(win)
            if btn7Hov == True:
                btn7H.draw(win)
            else:
                btn7.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click start menu btn")
                    gameState[1] = 'start'
                if btn2Hov == True:
                    print("mouse click team stats btn")

                if btn3Hov == True:
                    print("mouse click player stats btn")

                if btn4Hov == True:
                    print("mouse click Hall of Fame stats btn")

                if btn5Hov == True:
                    print("mouse click Schedule btn")

                if btn6Hov == True:
                    print("mouse click Standings btn")

                if btn7Hov == True:
                    print("mouse click Settings btn")




        pygame.display.update()
        buttonClassObj.mainClock.tick(60)