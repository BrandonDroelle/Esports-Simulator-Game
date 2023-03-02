import pygame, sys
import buttonClassObj
import saveGame

#create profile menu
def createProfileMenuFunc(gameState, win, basicFont, backgroundimg, buttonimg, button2img, keyBoardKeys, keyBoardKeysH):

    print('Create Profile - ', gameState)

    #caps lock varible to determine which buttons to show (0=F,1=T)
    caps = 0

    #create variable to hold players name
    name = ''

    #max name length variable
    maxLen = 12

    #Create Strings
    title = basicFont.render('Enter Name', False, (255, 255, 255))
    nameDisplay = basicFont.render(name, False, (255, 255, 255))
    #variable to set keyboard position
    baseX = 400
    baseY = 250
    #Create Buttons
    btn1 = buttonClassObj.buttonClass(buttonimg, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Accept', 75, 15)
    btn1H = buttonClassObj.buttonClass(button2img, (win.get_width() / 2) - 150, (win.get_height() / 2) + 200, basicFont, 'Accept', 75, 15)
    but1 = buttonClassObj.buttonClass(keyBoardKeys[0], baseX, baseY, basicFont, '',0, 0)
    but2 = buttonClassObj.buttonClass(keyBoardKeys[1], baseX + 50, baseY, basicFont, '',0, 0)
    but3 = buttonClassObj.buttonClass(keyBoardKeys[2], baseX + 100, baseY, basicFont, '',0, 0)
    but4 = buttonClassObj.buttonClass(keyBoardKeys[3], baseX + 150, baseY, basicFont, '',0, 0)
    but5 = buttonClassObj.buttonClass(keyBoardKeys[4], baseX + 200, baseY, basicFont, '',0, 0)
    but6 = buttonClassObj.buttonClass(keyBoardKeys[5], baseX + 250, baseY, basicFont, '',0, 0)
    but7 = buttonClassObj.buttonClass(keyBoardKeys[6], baseX + 300, baseY, basicFont, '',0, 0)
    but8 = buttonClassObj.buttonClass(keyBoardKeys[7], baseX + 350, baseY, basicFont, '',0, 0)
    but9 = buttonClassObj.buttonClass(keyBoardKeys[8], baseX + 400, baseY, basicFont, '',0, 0)
    but0 = buttonClassObj.buttonClass(keyBoardKeys[9], baseX + 450, baseY, basicFont, '',0, 0)
    but1S = buttonClassObj.buttonClass(keyBoardKeys[10], baseX, baseY, basicFont, '',0, 0)
    but2S = buttonClassObj.buttonClass(keyBoardKeys[11], baseX + 50, baseY, basicFont, '',0, 0)
    but3S = buttonClassObj.buttonClass(keyBoardKeys[12], baseX +100, baseY, basicFont, '',0, 0)
    but4S = buttonClassObj.buttonClass(keyBoardKeys[13], baseX + 150, baseY, basicFont, '',0, 0)
    but5S = buttonClassObj.buttonClass(keyBoardKeys[14], baseX + 200, baseY, basicFont, '',0, 0)
    but6S = buttonClassObj.buttonClass(keyBoardKeys[15], baseX + 250, baseY, basicFont, '',0, 0)
    but7S = buttonClassObj.buttonClass(keyBoardKeys[16], baseX + 300, baseY, basicFont, '',0, 0)
    but8S = buttonClassObj.buttonClass(keyBoardKeys[17], baseX + 350, baseY, basicFont, '',0, 0)
    but9S = buttonClassObj.buttonClass(keyBoardKeys[18], baseX + 400, baseY, basicFont, '',0, 0)
    but0S = buttonClassObj.buttonClass(keyBoardKeys[19], baseX + 450, baseY, basicFont, '',0, 0)
    butQ = buttonClassObj.buttonClass(keyBoardKeys[20], baseX, baseY + 50, basicFont, '',0, 0)
    butW = buttonClassObj.buttonClass(keyBoardKeys[21], baseX + 50, baseY + 50, basicFont, '',0, 0)
    butE = buttonClassObj.buttonClass(keyBoardKeys[22], baseX + 100, baseY + 50, basicFont, '',0, 0)
    butR = buttonClassObj.buttonClass(keyBoardKeys[23], baseX + 150, baseY + 50, basicFont, '',0, 0)
    butT = buttonClassObj.buttonClass(keyBoardKeys[24], baseX + 200, baseY + 50, basicFont, '',0, 0)
    butY = buttonClassObj.buttonClass(keyBoardKeys[25], baseX + 250, baseY + 50, basicFont, '',0, 0)
    butU = buttonClassObj.buttonClass(keyBoardKeys[26], baseX + 300, baseY + 50, basicFont, '',0, 0)
    butI = buttonClassObj.buttonClass(keyBoardKeys[27], baseX + 350, baseY + 50, basicFont, '',0, 0)
    butO = buttonClassObj.buttonClass(keyBoardKeys[28], baseX + 400, baseY + 50, basicFont, '',0, 0)
    butP = buttonClassObj.buttonClass(keyBoardKeys[29], baseX + 450, baseY + 50, basicFont, '',0, 0)
    butA = buttonClassObj.buttonClass(keyBoardKeys[30], baseX + 25, baseY + 100, basicFont, '',0, 0)
    butS = buttonClassObj.buttonClass(keyBoardKeys[31], baseX + 75, baseY + 100, basicFont, '',0, 0)
    butD = buttonClassObj.buttonClass(keyBoardKeys[32], baseX + 125, baseY + 100, basicFont, '',0, 0)
    butF = buttonClassObj.buttonClass(keyBoardKeys[33], baseX + 175, baseY + 100, basicFont, '',0, 0)
    butG = buttonClassObj.buttonClass(keyBoardKeys[34], baseX + 225, baseY + 100, basicFont, '',0, 0)
    butH = buttonClassObj.buttonClass(keyBoardKeys[35], baseX + 275, baseY + 100, basicFont, '',0, 0)
    butJ = buttonClassObj.buttonClass(keyBoardKeys[36], baseX + 325, baseY + 100, basicFont, '',0, 0)
    butK = buttonClassObj.buttonClass(keyBoardKeys[37], baseX + 375, baseY + 100, basicFont, '',0, 0)
    butL = buttonClassObj.buttonClass(keyBoardKeys[38], baseX + 425, baseY + 100, basicFont, '',0, 0)
    butZ = buttonClassObj.buttonClass(keyBoardKeys[39], baseX + 75, baseY + 150, basicFont, '',0, 0)
    butX = buttonClassObj.buttonClass(keyBoardKeys[40], baseX + 125, baseY + 150, basicFont, '',0, 0)
    butC = buttonClassObj.buttonClass(keyBoardKeys[41], baseX + 175, baseY + 150, basicFont, '',0, 0)
    butV = buttonClassObj.buttonClass(keyBoardKeys[42], baseX + 225, baseY + 150, basicFont, '',0, 0)
    butB = buttonClassObj.buttonClass(keyBoardKeys[43], baseX + 275, baseY + 150, basicFont, '',0, 0)
    butN = buttonClassObj.buttonClass(keyBoardKeys[44], baseX + 325, baseY + 150, basicFont, '',0, 0)
    butM = buttonClassObj.buttonClass(keyBoardKeys[45], baseX + 375, baseY + 150, basicFont, '',0, 0)
    butBack = buttonClassObj.buttonClass(keyBoardKeys[46], baseX + 450, baseY + 155, basicFont, '',0, 0)
    butCaps = buttonClassObj.buttonClass(keyBoardKeys[47], baseX, baseY + 155, basicFont, '',0, 0)
    butSpace = buttonClassObj.buttonClass(keyBoardKeys[48], baseX + 60, baseY + 215, basicFont, '',0, 0)
    
    

    #Menu Loop
    while gameState[1] == 'createProfile':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #update variables
            length = len(name)
            nameDisplay = basicFont.render(name, False, (255, 255, 255))
            #Draw Background
            win.blit(backgroundimg, (0, 0))
            #Draw Strings
            win.blit(title, (520,70))
            win.blit(nameDisplay, (500,170))
            #Draw Images
            
            #check for mouse hover
            btn1Hov = buttonClassObj.imgHover(btn1)
            but1Hov = buttonClassObj.imgHover(but1)
            but2Hov = buttonClassObj.imgHover(but2)
            but3Hov = buttonClassObj.imgHover(but3)
            but4Hov = buttonClassObj.imgHover(but4)
            but5Hov = buttonClassObj.imgHover(but5)
            but6Hov = buttonClassObj.imgHover(but6)
            but7Hov = buttonClassObj.imgHover(but7)
            but8Hov = buttonClassObj.imgHover(but8)
            but9Hov = buttonClassObj.imgHover(but9)
            but0Hov = buttonClassObj.imgHover(but0)
            butQHov = buttonClassObj.imgHover(butQ)
            butWHov = buttonClassObj.imgHover(butW)
            butEHov = buttonClassObj.imgHover(butE)
            butRHov = buttonClassObj.imgHover(butR)
            butTHov = buttonClassObj.imgHover(butT)
            butYHov = buttonClassObj.imgHover(butY)
            butUHov = buttonClassObj.imgHover(butU)
            butIHov = buttonClassObj.imgHover(butI)
            butOHov = buttonClassObj.imgHover(butO)
            butPHov = buttonClassObj.imgHover(butP)
            butAHov = buttonClassObj.imgHover(butA)
            butSHov = buttonClassObj.imgHover(butS)
            butDHov = buttonClassObj.imgHover(butD)
            butFHov = buttonClassObj.imgHover(butF)
            butGHov = buttonClassObj.imgHover(butG)
            butHHov = buttonClassObj.imgHover(butH)
            butJHov = buttonClassObj.imgHover(butJ)
            butKHov = buttonClassObj.imgHover(butK)
            butLHov = buttonClassObj.imgHover(butL)
            butZHov = buttonClassObj.imgHover(butZ)
            butXHov = buttonClassObj.imgHover(butX)
            butCHov = buttonClassObj.imgHover(butC)
            butVHov = buttonClassObj.imgHover(butV)
            butBHov = buttonClassObj.imgHover(butB)
            butNHov = buttonClassObj.imgHover(butN)
            butMHov = buttonClassObj.imgHover(butM)
            butBackHov = buttonClassObj.imgHover(butBack)
            butCapsHov = buttonClassObj.imgHover(butCaps)
            butSpaceHov = buttonClassObj.imgHover(butSpace)

            #Draw Buttons
            #if button hovered change img to hovered image
            if length > 0: #make sure name string is atleast length one
                if btn1Hov == True:
                    btn1H.draw(win)
                else:
                    btn1.draw(win)

            if caps == 0:
                #print('draw number keys')
                but1.draw(win)
                but2.draw(win)
                but3.draw(win)
                but4.draw(win)
                but5.draw(win)
                but6.draw(win)
                but7.draw(win)
                but8.draw(win)
                but9.draw(win)
                but0.draw(win)
            if caps == 1:
                #print('draw symbol keys')
                but1S.draw(win)
                but2S.draw(win)
                but3S.draw(win)
                but4S.draw(win)
                but5S.draw(win)
                but6S.draw(win)
                but7S.draw(win)
                but8S.draw(win)
                but9S.draw(win)
                but0S.draw(win)
            butQ.draw(win)
            butW.draw(win)
            butE.draw(win)
            butR.draw(win)
            butT.draw(win)
            butY.draw(win)
            butU.draw(win)
            butI.draw(win)
            butO.draw(win)
            butP.draw(win)
            butA.draw(win)
            butS.draw(win)
            butD.draw(win)
            butF.draw(win)
            butG.draw(win)
            butH.draw(win)
            butJ.draw(win)
            butK.draw(win)
            butL.draw(win)
            butZ.draw(win)
            butX.draw(win)
            butC.draw(win)
            butV.draw(win)
            butB.draw(win)
            butN.draw(win)
            butM.draw(win)
            butBack.draw(win)
            butCaps.draw(win)
            butSpace.draw(win)

            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                if length > 0: #make sure name string is atleast length one
                    if btn1Hov == True:
                        print("mouse accept name btn")
                        #call function to update save file with new player name
                        saveGame.updatePlayerName(gameState, name)
                        gameState[1] = 'selectTeam'

                if length < maxLen:
                    if but1Hov == True:
                        print("mouse click 1")
                        if caps == 1:
                            name = name + "!"
                        else:
                            name = name + "1"
                        print('name: ', name)
                    if but2Hov == True:
                        print("mouse click 2")
                        if caps == 1:
                            name = name + "@"
                        else:
                            name = name + "2"
                        print('name: ', name)
                    if but3Hov == True:
                        print("mouse click 3")
                        if caps == 1:
                            name = name + "#"
                        else:
                            name = name + "3"
                        print('name: ', name)
                    if but4Hov == True:
                        print("mouse click 4")
                        if caps == 1:
                            name = name + "$"
                        else:
                            name = name + "4"
                        print('name: ', name)
                    if but5Hov == True:
                        print("mouse click 5")
                        if caps == 1:
                            name = name + "%"
                        else:
                            name = name + "5"
                        print('name: ', name)
                    if but6Hov == True:
                        print("mouse click 6")
                        if caps == 1:
                            name = name + "^"
                        else:
                            name = name + "6"
                        print('name: ', name)
                    if but7Hov == True:
                        print("mouse click 7")
                        if caps == 1:
                            name = name + "&"
                        else:
                            name = name + "7"
                        print('name: ', name)
                    if but8Hov == True:
                        print("mouse click 8")
                        if caps == 1:
                            name = name + "*"
                        else:
                            name = name + "8"
                        print('name: ', name)
                    if but9Hov == True:
                        print("mouse click 9")
                        if caps == 1:
                            name = name + "("
                        else:
                            name = name + "9"
                        print('name: ', name)
                    if but0Hov == True:
                        print("mouse click 0")
                        if caps == 1:
                            name = name + ")"
                        else:
                            name = name + "0"
                        print('name: ', name)
                    if butQHov == True:
                        print("mouse click Q")
                        if caps == 1:
                            name = name + "Q"
                        else:
                            name = name + "q"
                        print('name: ', name)
                    if butWHov == True:
                        print("mouse click W")
                        if caps == 1:
                            name = name + "W"
                        else:
                            name = name + "w"
                        print('name: ', name)
                    if butEHov == True:
                        print("mouse click E")
                        if caps == 1:
                            name = name + "E"
                        else:
                            name = name + "e"
                        print('name: ', name)
                    if butRHov == True:
                        print("mouse click R")
                        if caps == 1:
                            name = name + "R"
                        else:
                            name = name + "r"
                        print('name: ', name)
                    if butTHov == True:
                        print("mouse click T")
                        if caps == 1:
                            name = name + "T"
                        else:
                            name = name + "t"
                        print('name: ', name)
                    if butYHov == True:
                        print("mouse click Y")
                        if caps == 1:
                            name = name + "Y"
                        else:
                            name = name + "y"
                        print('name: ', name)
                    if butUHov == True:
                        print("mouse click U")
                        if caps == 1:
                            name = name + "U"
                        else:
                            name = name + "u"
                        print('name: ', name)
                    if butIHov == True:
                        print("mouse click I")
                        if caps == 1:
                            name = name + "I"
                        else:
                            name = name + "i"
                        print('name: ', name)
                    if butOHov == True:
                        print("mouse click O")
                        if caps == 1:
                            name = name + "O"
                        else:
                            name = name + "o"
                        print('name: ', name)
                    if butPHov == True:
                        print("mouse click P")
                        if caps == 1:
                            name = name + "P"
                        else:
                            name = name + "p"
                        print('name: ', name)
                    if butAHov == True:
                        print("mouse click A")
                        if caps == 1:
                            name = name + "A"
                        else:
                            name = name + "a"
                        print('name: ', name)
                    if butSHov == True:
                        print("mouse click S")
                        if caps == 1:
                            name = name + "S"
                        else:
                            name = name + "s"
                        print('name: ', name)
                    if butDHov == True:
                        print("mouse click D")
                        if caps == 1:
                            name = name + "D"
                        else:
                            name = name + "d"
                        print('name: ', name)
                    if butFHov == True:
                        print("mouse click F")
                        if caps == 1:
                            name = name + "F"
                        else:
                            name = name + "f"
                        print('name: ', name)
                    if butGHov == True:
                        print("mouse click G")
                        if caps == 1:
                            name = name + "G"
                        else:
                            name = name + "g"
                        print('name: ', name)
                    if butHHov == True:
                        print("mouse click H")
                        if caps == 1:
                            name = name + "H"
                        else:
                            name = name + "h"
                        print('name: ', name)
                    if butJHov == True:
                        print("mouse click J")
                        if caps == 1:
                            name = name + "J"
                        else:
                            name = name + "j"
                        print('name: ', name)
                    if butKHov == True:
                        print("mouse click K")
                        if caps == 1:
                            name = name + "K"
                        else:
                            name = name + "k"
                        print('name: ', name)
                    if butLHov == True:
                        print("mouse click L")
                        if caps == 1:
                            name = name + "L"
                        else:
                            name = name + "l"
                        print('name: ', name)
                    if butZHov == True:
                        print("mouse click Z")
                        if caps == 1:
                            name = name + "Z"
                        else:
                            name = name + "z"
                        print('name: ', name)
                    if butXHov == True:
                        print("mouse click X")
                        if caps == 1:
                            name = name + "X"
                        else:
                            name = name + "x"
                        print('name: ', name)
                    if butCHov == True:
                        print("mouse click C")
                        if caps == 1:
                            name = name + "C"
                        else:
                            name = name + "c"
                        print('name: ', name)
                    if butVHov == True:
                        print("mouse click V")
                        if caps == 1:
                            name = name + "V"
                        else:
                            name = name + "v"
                        print('name: ', name)
                    if butBHov == True:
                        print("mouse click B")
                        if caps == 1:
                            name = name + "B"
                        else:
                            name = name + "b"
                        print('name: ', name)
                    if butNHov == True:
                        print("mouse click N")
                        if caps == 1:
                            name = name + "N"
                        else:
                            name = name + "n"
                        print('name: ', name)
                    if butMHov == True:
                        print("mouse click M")
                        if caps == 1:
                            name = name + "M"
                        else:
                            name = name + "m"
                        print('name: ', name)
                    if butSpaceHov == True:
                        print("mouse click Space")
                        name = name + " "
                        print('name: ', name)

                if butBackHov == True:
                    print("mouse click Back")
                    print('name len: ', length)
                    if length > 0:
                        #creates a new string in reverse order of name
                        lastC = name[length - 1]
                        print('last character in name: ', lastC)
                        nameReverse = ''
                        count = 1
                        for i in range(length):
                            print('i: ', i)
                            print('len: ', length)
                            nameReverse = nameReverse + name[length - count]
                            count = count + 1
                        print('name: ', name)
                        print('nameReverse: ', nameReverse)
                        #replace first character from reversed name string with empty string
                        nameReverse.replace(lastC, "")
                        #un-reverse string and copy to name string
                        count = 1
                        name = ""
                        for i in range(length - 1):
                            print('i: ', i)
                            print('len: ', length)
                            name = name + nameReverse[length - count]
                            count = count + 1
                    print('name: ', name)

                if butCapsHov == True:
                    print("mouse clickCaps")
                    if caps == 0:
                        print("Caps turned on")
                        caps = 1
                        print("caps: ", caps)
                    else:
                        print("Caps turned off")
                        caps = 0
                        print("caps: ", caps)
                



        pygame.display.update()
        buttonClassObj.mainClock.tick(60)