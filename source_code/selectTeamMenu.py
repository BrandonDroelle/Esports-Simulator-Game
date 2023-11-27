import pygame, sys
import buttonClassObj
import random
import saveGame
import generateSchedule
import createCache
import teamClass

#select team menu
def selectTeamMenuFunc(gameState, win, basicFont, smallFont, backgroundimg, buttonimg, button2img, teamLogos, teamNames, playerNames):

    print('in select team menu - ', gameState)

    #Create Variables
    length = len(teamLogos)
    length2 = len(teamNames)

    #print("teamLogos length: ", length)
    #print("teams length: ", length2)
    leftSelect = 0
    rightSelect = 0
    team = ''
    #determine two random teams for player to choose from
    flag = 0
    team1 = random.randrange(0, length, 1)
    while flag == 0:
        team2 = random.randrange(0, length, 1)
        if team2 == team1:
            flag = 0
        else:
            flag = 1
    #rigged teams
    #team1 = 0
    #team2 = 1

    #print("team 1: ", team1)
    #print("team 2: ", team2)

    team1Name = teamNames[team1]
    team2Name = teamNames[team2]
    #print("team 1: ", team1Name)
    #print("team 2: ", team2Name)

    #Create Strings
    title = basicFont.render('Choose Your Team', False, (255, 255, 255))
    msg = smallFont.render('Congratulations, your hardwork and dedication', False, (255, 255, 255))
    msg2 = smallFont.render('have finally paid off. You have recieved two', False, (255, 255, 255))
    msg3 = smallFont.render('offers to join the RLCS. Select the team that', False, (255, 255, 255))
    msg4 = smallFont.render('you wish to start your RLCS career with, and', False, (255, 255, 255))
    msg5 = smallFont.render('good luck rookie!', False, (255, 255, 255))
    teamLeft = basicFont.render(team1Name.capitalize(), False, (255, 255, 255))
    teamRight = basicFont.render(team2Name.capitalize(), False, (255, 255, 255))

    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Accept', 75, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Accept', 75, 15)
    btn2 = buttonClassObj.buttonClass(buttonimg, win.get_width() - 400, (win.get_height() / 2) + 200, basicFont, 'Select', 75, 15) #right
    btn2H = buttonClassObj.buttonClass(button2img, win.get_width() - 400, (win.get_height() / 2) + 200, basicFont, 'Select', 75, 15) #right
    btn3 = buttonClassObj.buttonClass(buttonimg, 100, (win.get_height() / 2) + 200, basicFont, 'Select', 75, 15) #left
    btn3H = buttonClassObj.buttonClass(button2img, 100, (win.get_height() / 2) + 200, basicFont, 'Select', 75, 15) #left

    

    #Menu Loop
    while gameState[1] == 'selectTeam':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (400,70))
            win.blit(msg, (380, 230))
            win.blit(msg2, (380, 260))
            win.blit(msg3, (380, 290))
            win.blit(msg4, (380, 320))
            win.blit(msg5, (380, 350))
            win.blit(teamLeft, (120, 160))
            win.blit(teamRight, (900, 160))

            #Draw Shapes
            if rightSelect == 1:
                pygame.draw.rect(win, (250,250,250), pygame.Rect(890,215,270,270)) #rect(x,y,length,height)
            if leftSelect == 1:
                pygame.draw.rect(win, (250,250,250), pygame.Rect(110,215,270,270)) #rect(x,y,length,height)
            

            #Draw Images
            win.blit(teamLogos[team1], (120, 225)) #left
            win.blit(teamLogos[team2], (900, 225))  #right
            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            btn2Hov = buttonClassObj.imgHover(btn2)
            btn3Hov = buttonClassObj.imgHover(btn3)

            #Draw Buttons
            #if button hovered change img to hovered image
            if rightSelect == 1:
                if btn1Hov == True:
                    btn1H.draw(win)
                else:
                    btn1.draw(win)
            if leftSelect == 1:
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
                if rightSelect == 1 or leftSelect == 1:
                    if btn1Hov == True:
                        print("mouse click accept team btn")
                        if rightSelect == 1:
                            team = team2Name
                        else:
                            team = team1Name

                        ###Update Save File###

                        #call function to update save file with current season
                        saveGame.updateSeason(gameState, 1)

                        ###Update Cache Data###

                        #generate players
                        playerObjects = createCache.createPlayerObjects(gameState, playerNames) #here is when the player name is added to the list of player names
                        gameState[2] = playerObjects
                        print("player objects generated")
                        #generate teams
                        teamObjects = createCache.createTeamObjects(teamNames)
                        print("team objects generated")
                        gameState[3] = teamObjects
                        #call function to generate season schedule
                        schedule = generateSchedule.generateRoundRobin(gameState, teamNames)
                        #generateSchedule.printSchedule(schedule)
                        #generateSchedule.printTeams(teamNames)
                        scheduleString = generateSchedule.getScheduleString(gameState, schedule, teamObjects)
                        #print("schedule string: ", scheduleString)
                        gameState[4] = scheduleString
                        

                        
                        ###Update Save File###

                        #call function to update save file to not new save
                        saveGame.updateSave(gameState)
                        #call function to update save file with current users team name
                        saveGame.updateTeam(gameState, team)
                        #call function to update save file with current week
                        saveGame.updateWeek(gameState, 1)
                        
                        #fill team rosters, each team gets three players (Have to update save file with team name before filling team rosters)
                        teamObjects = createCache.fillTeamRosters(gameState)
                        #assign user to the team they picked instead of a random team
                        gameState = createCache.swapUserWithNPC(gameState)

                        #call function to add player object data to save file
                        saveGame.updatePlayers(gameState)
                        #call function to add team objects data to save file
                        saveGame.updateTeams(gameState)
                        #save season schedule to save file
                        saveGame.updateSchedule(gameState, scheduleString)


                        
                        
                        


                        gameState[1] = 'lockerRoom'
                if btn2Hov == True:
                    print("mouse click right choose btn")
                    if rightSelect == 0:
                        rightSelect = 1
                        leftSelect = 0
                    else:
                        rightSelect = 0
                    print("right select: ", rightSelect)
                if btn3Hov == True:
                    print("mouse click left choose btn")
                    if leftSelect == 0:
                        leftSelect = 1
                        rightSelect = 0
                    else:
                        leftSelect = 0
                    print("left select: ", leftSelect)

        pygame.display.update()
        buttonClassObj.mainClock.tick(60)