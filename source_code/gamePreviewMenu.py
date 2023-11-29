from turtle import tiltangle
import pygame, sys
import buttonClassObj
import saveGame
import generateSchedule

# #display settings menu
def gamePreviewMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, teamLogos, teamNames):

    currentSeason = str(saveGame.getSeason(gameState))
    currentWeek = saveGame.getWeek(gameState)
    playersTeam = saveGame.getTeamName(gameState)
    opposingTeam = generateSchedule.getmatchupSpecific(gameState, currentWeek, playersTeam)

    print('in game preview - ', gameState)

    #Create Strings
    title = basicFont.render('Season ' + currentSeason, False, (255, 255, 255))
    subTitle = basicFont.render('Week ' + currentWeek, False, (255, 255, 255))
    teamNameLeft = basicFont.render(playersTeam.capitalize(), False, (255, 255, 255))
    teamNameRight = basicFont.render(opposingTeam.capitalize(), False, (255, 255, 255))
    #goalsLeft = basicFont.render(opposingTeam.capitalize(), False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 0, basicFont, 'Confirm', 60, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 0, basicFont, 'Confirm', 60, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 100, basicFont, 'Cancel', 60, 15)
    btn2H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 100, basicFont, 'Cancel', 60, 15)
    btn3 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) - 100, basicFont, 'Simulate', 60, 15)
    btn3H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) - 100, basicFont, 'Simulate', 60, 15)

    #Create Variables
    #gets index for players team icon
    teamLogoIndex = 99
    count = 0
    for i in teamNames:
        if playersTeam == teamNames[count]:
            #print("match")
            teamLogoIndexPlayer = count
        count = count + 1
    #gets index for opponents team icon
    teamLogoIndex = 99
    count = 0
    for i in teamNames:
        if opposingTeam == teamNames[count]:
            #print("match")
            teamLogoIndexOpposition = count
        count = count + 1

    #Menu Loop
    while gameState[1] == 'gamePreview':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            
            #Draw Strings
            win.blit(title, (530,50))
            win.blit(subTitle, (550,100))
            win.blit(teamNameLeft, (150,100))
            win.blit(teamNameRight, (950,100))
            
            #Draw Images
            win.blit(teamLogos[teamLogoIndexPlayer], (120, 150))
            win.blit(teamLogos[teamLogoIndexOpposition], (920, 150))

            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btn2Hov = buttonClassObj.imgHover(btn2)
            btn3Hov = buttonClassObj.imgHover(btn3)

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

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if btn1Hov == True:
                    print("mouse click confirm btn")
                    gameState[1] = 'weeklyResults'
                if btn2Hov == True:
                    print("mouse click cancel btn")
                if btn3Hov == True:
                    print("mouse click simulate btn")
                    

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)