import pygame
from asyncio.windows_events import NULL

mainClock = pygame.time.Clock()

#get mouse position
def mouse():
    mosX, mosY = pygame.mouse.get_pos()
    #print('mosX: ', mosX, ' - ', 'mosY: ', mosY)
    return(mosX, mosY)

#test if mouse is hovering over a button
def imgHover(btn):
    #get mouse position
    mosX, mosY = mouse()
    #check if mouse x is within image width
    if (mosX>btn.getX()) and (mosX<btn.getX() + btn.getW()):
        insideX = True
    else:
        insideX = False
    #check if mouse y is within image height
    if (mosY>btn.getY()) and (mosY<btn.getY() + btn.getH()):
        insideY = True
    else:
        insideY = False
    #check if both x and y are true
    if (insideX == True) and (insideY == True):
        hover = True
    else:
        hover = False
    #print (hover)
    return hover 

class buttonClass:
    def __init__(self, img, x, y, font = 0, text = '', tx = 0, ty = 0):
        self.img = img
        self.x = x
        self.y = y
        self.w = img.get_width()
        self.h = img.get_height()
        self.font = font
        self.text = font.render(text, True, (255, 255, 255))
        self.tx = tx
        self.ty = ty

    #draw button onto screen
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        win.blit(self.text, (self.x + self.tx, self.y + self.ty))
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getW(self):
        return self.w

    def getH(self):
        return self.h