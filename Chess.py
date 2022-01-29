import pygame,sys
import random

pygame.init()
widt=650
heig=650
pygame.display.set_caption("Chess")
clock=pygame.time.Clock()
board=pygame.image.load("Board.jpg")
win=pygame.display.set_mode((widt,heig))
cent=[]
wturn=True
selected=False
BlackPos=[]
WhitePos=[]
AvPos=[]
Colour2=(random.randint(50,200),random.randint(50,200),random.randint(50,200)) #CursorColour
Colour1=(random.randint(50,200),random.randint(50,200),random.randint(50,200)) #BorderColour
for y in range(8):                  #Taking Centers
    ref=[]
    for x in range(8):
        ref.append((45+x*80,45+y*80))
    cent.append(ref)

    
class Player(object):
    global cent
    def __init__(self,x,y,Name):
        (self.x,self.y)=(x,y)
        self.name=Name
        self.img=pygame.image.load("{}.png".format(self.name))
    def draw(self):
        self.posi=cent[self.x][self.y]
        win.blit(self.img,(self.posi[0]-40,self.posi[1]-40))
        
    def getPosition(self):
        return (self.x,self.y)
    
    def setPosition(self,x,y):
        (self.x,self.y)=(x,y)

    def getName(self):
        return self.name
    
    def setName(self,newName):
        self.name=newName
        self.img=pygame.image.load("{}.png".format(self.name))

        
def PawnAtEnd(color):   
    surf=pygame.Surface((400,400))
    surf=surf.convert_alpha()
    font=pygame.font.Font(None,61)
    option=["Queen","Rook","Bishop","Knite"]
    text=[font.render(option[0],True,(236,213,198)),font.render(option[2],True,(236,213,198)),font.render(option[1],True,(236,213,198)),font.render(option[3],True,(236,213,198))]
    player=[]
    for name in option:
        player.append(pygame.image.load("{}_{}.png".format(name,color)))
    n=0
    x,y=0,0
    while True:
        pygame.time.delay(85)
        win.blit(surf,(125,125))
        surf.fill((109,102,117,125))

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit(0)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return option[n]+"_"+color
                if event.key==pygame.K_LEFT and x-200>=0:
                    x-=200
                    n-=1
                if event.key==pygame.K_RIGHT and x+200<=350:
                    x+=200
                    n+=1
                if event.key==pygame.K_UP and y-200>=0:
                    y-=200
                    n-=2
                if event.key==pygame.K_DOWN and y+200<=350:
                    y+=200
                    n+=2
        surf.blit(player[0],(60,20))
        surf.blit(text[0],(45,105))
        surf.blit(player[1],(260,20))
        surf.blit(text[1],(45,305))
        surf.blit(player[2],(60,220))
        surf.blit(text[2],(245,105))
        surf.blit(player[3],(260,220))
        surf.blit(text[3],(245,305))
        pygame.draw.rect(surf,(14,22,51),(x,y,200,200),5)
        
        pygame.display.update()
    


def rotate():
    global WhitePos,BlackPos,Colour2
    for el in cent:
        el.reverse()
    cent.reverse()
    Colour2=(random.randint(150,250),random.randint(155,245),random.randint(150,255))
    
##################################          REDRAW GAME WINDOW                          #######################          
def reDrawWindow():
    global WhiteArmy,BlackArmy,BlackPos,WhitePos
    win.blit(board,(5,5))
    if selected:        
        pygame.draw.rect(win,(113,223,206),(cent[curpos[0]][curpos[1]][0]-35,cent[curpos[0]][curpos[1]][1]-35,70,70))
    for pos in AvPos:
        pygame.draw.rect(win,(51,203,7),(cent[pos[0]][pos[1]][0]-35,cent[pos[0]][pos[1]][1]-35,70,70))
    for player in BlackArmy:
        player.draw()
    for player in WhiteArmy:
        player.draw()
        
    pygame.draw.rect(win,Colour2,(posX,posY,80,80),5)
    
    
    pygame.display.update()
#################################           GET POSITIONS                           #######################
def getPos():
    global WhitePos,BlackPos
    WhitePos=[]
    BlackPos=[]
    for posel in WhiteArmy:
        WhitePos.append(posel.getPosition())
    for posel in BlackArmy:
        BlackPos.append(posel.getPosition())

##################################          AVAILABLE POSITIONS                     #########################
def availPos(name,MyPos,OtherPos,x,y):
    global AvPos
    
    def Rook(MPos,OPos,x,y):
        APos=[]
        wall=[False,False,False,False]
        for i in range(1,8):
            if x-i>=0 and not wall[0]:
                if (x-i,y) in OPos:
                    APos.append((x-i,y))
                    wall[0]=True
                elif (x-i,y) in MPos:
                    wall[0]=True
                else:
                    APos.append((x-i,y))
            if x+i<=7 and not wall[1]:
                if (x+i,y) in OPos:
                    APos.append((x+i,y))
                    wall[1]=True
                elif (x+i,y) in MPos:
                    wall[1]=True
                else:
                    APos.append((x+i,y))
            if y-i>=0 and not wall[2]:
                if (x,y-i) in OPos:
                    APos.append((x,y-i))
                    wall[2]=True
                elif (x,y-i) in MPos:
                    wall[2]=True
                else:
                    APos.append((x,y-i))
            if y+i<=7 and not wall[3]:
                if (x,y+i) in OPos:
                    APos.append((x,y+i))
                    wall[3]=True
                elif (x,y+i) in MPos:
                    wall[3]=True
                else:
                    APos.append((x,y+i))
            if wall[0] and wall[1] and wall[2] and wall[3]:
                break
        return APos
                      
    def Bishop(MPos,OPos,x,y):
        APos=[]
        wall=[False,False,False,False]
        for i in range(1,8):
            if x-i>=0 and y-i>=0 and not wall[0]:
                if (x-i,y-i) in OPos:
                    APos.append((x-i,y-i))
                    wall[0]=True
                elif (x-i,y-i) in MPos:
                    wall[0]=True
                else:
                    APos.append((x-i,y-i))
            if x-i>=0 and y+i<=7 and not wall[1]:
                if (x-i,y+i) in OPos:
                    APos.append((x-i,y+i))
                    wall[1]=True
                elif (x-i,y+i) in MPos:
                    wall[1]=True
                else:
                    APos.append((x-i,y+i))
            if x+i<=7 and y-i>=0 and not wall[2]:
                if (x+i,y-i) in OPos:
                    APos.append((x+i,y-i))
                    wall[2]=True
                elif (x+i,y-i) in MPos:
                    wall[2]=True
                else:
                    APos.append((x+i,y-i))
            if x+i<=7 and y+i<=7 and not wall[3]:
                if (x+i,y+i) in OPos:
                    APos.append((x+i,y+i))
                    wall[3]=True
                elif (x+i,y+i) in MPos:
                    wall[3]=True
                else:
                    APos.append((x+i,y+i))
            if wall[0] and wall[1] and wall[2] and wall[3]:
                break
        return APos
            
    def Pawn(Name,OPos,x,y):
        APos=[]
        if Name=="Pawn_White":
            if (x-1,y) not in OPos:
                APos.append((x-1,y))
                if x==6 and (x-2,y) not in OPos:
                    APos.append((x-2,y))
            if (x-1,y-1) in OPos:
                APos.append((x-1,y-1))
            if (x-1,y+1) in OPos:
                APos.append((x-1,y+1))
            return APos
        else:
            if x==1 and (x-2,y) not in OPos:
                APos.append((x+2,y))
            if (x+1,y) not in OPos:
                APos.append((x+1,y))
            if (x+1,y-1) in OPos:
                APos.append((x+1,y-1))
            if (x+1,y+1) in OPos:
                APos.append((x+1,y+1))
            return APos
    AvPos=[]
    if name=="Rook_Black" or name=="Rook_White":
        AvPos=Rook(MyPos,OtherPos,x,y)
    if name=="Bishop_Black" or name=="Bishop_White":
        AvPos=Bishop(MyPos,OtherPos,x,y)
    if name=="Pawn_Black" or name=="Pawn_White":
        AvPos=Pawn(name,OtherPos,x,y)
    if name=="Queen_Black" or name=="Queen_White":
        AvPos=Rook(MyPos,OtherPos,x,y)+Bishop(MyPos,OtherPos,x,y)        
    if name=="King_Black" or name=="King_White":
          APos=[(x+1,y+1),(x+1,y),(x,y+1),(x-1,y-1),(x-1,y),(x,y-1),(x-1,y+1),(x+1,y-1)]
          for el in APos:
              if el[0]>=0 and el[1]<=7 and el[0]<=7 and el[1]>=0:
                  if name=="King_Black" and el in BlackPos or name=="King_White" and el in WhitePos:
                      continue
                  AvPos.append(el)
    if name=="Knite_Black" or name=="Knite_White":
        APos=[(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2)]
        for el in APos:
              if el[0]>=0 and el[1]<=7 and el[0]<=7 and el[1]>=0:
                  if name=="Knite_Black" and el in BlackPos or name=="Knite_White" and el in WhitePos:
                      continue
                  AvPos.append(el)


###################################             WINNER CODE                         ###################################
def WinnerWinner(text):
    img=pygame.image.load("{}.png".format(text))
    while True:
        pygame.time.delay(85)
        win.blit(img,(25,25))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    return False
                    
        pygame.display.update()

        
while True:
    
    BlackArmy=[Player(0,0,"Rook_Black"),Player(0,1,"Knite_Black"),Player(0,2,"Bishop_Black"),Player(0,3,"King_Black"),Player(0,4,"Queen_Black"),Player(0,5,"Bishop_Black"),Player(0,6,"Knite_Black"),Player(0,7,"Rook_Black"),Player(1,0,"Pawn_Black"),Player(1,1,"Pawn_Black"),Player(1,2,"Pawn_Black"),Player(1,3,"Pawn_Black"),Player(1,4,"Pawn_Black"),Player(1,5,"Pawn_Black"),Player(1,6,"Pawn_Black"),Player(1,7,"Pawn_Black")]
    WhiteArmy=[Player(7,0,"Rook_White"),Player(7,1,"Knite_White"),Player(7,2,"Bishop_White"),Player(7,3,"King_White"),Player(7,4,"Queen_White"),Player(7,5,"Bishop_White"),Player(7,6,"Knite_White"),Player(7,7,"Rook_White"),Player(6,0,"Pawn_White"),Player(6,1,"Pawn_White"),Player(6,2,"Pawn_White"),Player(6,3,"Pawn_White"),Player(6,4,"Pawn_White"),Player(6,5,"Pawn_White"),Player(6,6,"Pawn_White"),Player(6,7,"Pawn_White")]


    (x,y)=(4,4)
    ##########################      Main Loop       ########################
    run=True
    curpos=None
    while run:
        pygame.time.delay(100)
        clock.tick(20)
        pygame.draw.rect(win,Colour1,(0,0,650,650),10)
        pos=cent[x][y]
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    Colour2=(random.randint(50,200),random.randint(50,200),random.randint(50,200))
                
                if event.key==pygame.K_SPACE:
                    if not selected:
                        getPos()
                        curpos=(x,y)
                        if wturn and curpos in WhitePos:
                            availPos(WhiteArmy[WhitePos.index(curpos)].getName(),WhitePos,BlackPos,x,y)
                            selected=True
                        elif not wturn and curpos in BlackPos:
                            availPos(BlackArmy[BlackPos.index(curpos)].getName(),BlackPos,WhitePos,x,y)
                            selected=True
                    else:
                        newpos=(x,y)
                        
                        if newpos==curpos:
                            selected=False
                            AvPos = []
                        elif wturn:
                            if newpos in AvPos and newpos not in WhitePos:
                                WhiteArmy[WhitePos.index(curpos)].setPosition(x,y)
                                if newpos[0]==0 and WhiteArmy[WhitePos.index(curpos)].getName()=="Pawn_White":
                                    newName=PawnAtEnd("White")
                                    WhiteArmy[WhitePos.index(curpos)].setName(newName)
                                if newpos in BlackPos:
                                    if BlackArmy[BlackPos.index(newpos)].getName()=='King_Black':
                                       run= WinnerWinner("WHITEWIN")
                                       selected=False
                                       AvPos=[]
                                       continue
                                    BlackArmy.remove(BlackArmy[BlackPos.index(newpos)])
                                    
                                
                                selected=False
                                AvPos=[]
                                wturn=False
                                rotate()
                        else:
                            if newpos in AvPos and newpos not in BlackPos:
                                BlackArmy[BlackPos.index(curpos)].setPosition(x,y)
                                if newpos[0]==7 and BlackArmy[BlackPos.index(curpos)].getName()=="Pawn_Black":
                                    newName=PawnAtEnd("Black")
                                    BlackArmy[BlackPos.index(curpos)].setName(newName)
                                if newpos in WhitePos:
                                    if WhiteArmy[WhitePos.index(newpos)].getName()=='King_White':
                                       run= WinnerWinner("BLACKWIN")
                                    WhiteArmy.remove(WhiteArmy[WhitePos.index(newpos)])
                                    
                                
                                selected=False
                                AvPos=[]
                                wturn=True
                                rotate()
                        
                            
        keys=pygame.key.get_pressed()
        
        if wturn:
            if keys[pygame.K_LEFT] and y>0:
                y-=1
            elif keys[pygame.K_RIGHT] and y<7:
                y+=1
            if keys[pygame.K_UP] and x>0:
                x-=1
            elif keys[pygame.K_DOWN] and x<7:
                x+=1
        else:
            if keys[pygame.K_LEFT] and y<7:
                y+=1
            elif keys[pygame.K_RIGHT] and y>0:
                y-=1
            if keys[pygame.K_UP] and x<7:
                x+=1
            elif keys[pygame.K_DOWN] and x>0:
                x-=1
        
        posX=pos[0]-40
        posY=pos[1]-40
        reDrawWindow()

