add_library('minim')
minim = Minim(this)
import math
import time
import random

# jump

class Game:
    def __init__ (self,w,h,g):
        self.t=0
        self.x=0
        self.y=0
        self.w=w
        self.h=h
        self.g=g
        self.mImg = loadImage('marioCap.png')
        self.bImg = loadImage('bowserFace.png')
        self.bgSound = minim.loadFile('superMario.mp3')
        self.playSound(self.bgSound, 'once')
        self.platforms=[]
        self.lives=[]
        self.platforms.append(Platform(355,101,88,28,'platform.png')) # top platforms
        self.platforms.append(Platform(100,200,88,28,'platform.png')) # top platforms
        self.platforms.append(Platform(620,200,88,28,'platform.png')) # top platforms
        self.platforms.append(Platform(250,305,88,28,'platform.png')) # top platforms
        self.platforms.append(Platform(500,305,88,28,'platform.png')) # top platforms
        self.platforms.append(Platform(90,404,83,22,'platform3.png')) # bottom side platform
        self.platforms.append(Platform(630,404,83,22,'platform3.png')) # bottom side platform
        self.platforms.append(Platform(173,404,458,150,'platform2.png')) # bottom middle platform

    def display(self):
        image(self.mImg, 200, 500, 120, 80)  # marios cap image
        image(self.bImg, 400, 500, 80, 75) # bowsers face image
            
        for p in self.platforms:
            p.display()
            
        for l in self.lives:
            l.display()
            
    def playSound(self, sound, type):
        if type == 'once':
            sound.rewind()
            sound.play()
        else:
            sound.rewind()
            sound.loop()

class addLife:
    def __init__(self,x,y,r,g,hImg,w,h):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.hImg = loadImage(hImg) 
        self.w = w
        self.h = h   
        self.vy = 0.1
    
    def update(self):
        if self.y+self.r < self.g:
            self.vy+=0.05
            self.y+=self.vy
        else:
            self.vy=0
            self.y=self.g-self.r   
            
        if self.distance(bowser) < self.r+bowser.r: 
            if bowser.l >= 1:
                bowser.l -= 1
                game.lives.remove(self)
                del self
                
            if mario.l >= 1:
                mario.l -= 1
                game.lives.remove(self)
                del self
            
    def distance(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    
    def display(self):
        self.update()
        stroke(255,0,0)
        image(self.hImg, self.x, self.y,self.w,self.h)
        
class Platform:
    def __init__ (self,x,y,w,h,img):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.gImg=loadImage(img)
        
    def display(self):
        image(self.gImg,self.x-game.x,self.y-game.y,self.w,self.h,0,0,self.w,self.h)
              
class Creature:
    def __init__ (self,x,y,r,g,sImg,rImg,shImg,rF,w,h,l):
        self.x=x
        self.y=y
        self.r=r
        self.w=w
        self.h=h
        self.g=g
        self.vx=0
        self.vy=0
        self.dir=1
        self.rImg=loadImage(rImg)
        self.sImg=loadImage(sImg)
        self.shImg=loadImage(shImg)
        self.f=0
        self.rF=rF
        self.l = l
        
    def display(self):
        self.update()
        stroke(255,0,0)
        line(self.x-self.r-game.x,self.g-game.y,self.x+self.r-game.x,self.g-game.y)
        stroke(255)
        #ellipse(self.x,self.y,2*self.r,2*self.r)
        
        if isinstance(self, Mario):
            fill(255, 0, 0)
            rect(self.x - self.r - game.x, self.y - self.r - 20, 150, 10)
            fill(0, 255, 0)
            rect(self.x - self.r - game.x, self.y-self.r - 20, self.health, 10)
            image(loadImage('P1.png'), self.x - self.r - game.x, self.y - self.r + 87, 60,60)
            
        if isinstance(self, Bowser): 
            fill(255, 0, 0)
            rect(self.x - self.r - game.x, self.y-self.r-20, 150, 10) #red
            fill(0, 255, 0)
            rect(self.x - self.r - game.x, self.y-self.r-20, self.health, 10) #green
            image(loadImage('P2.png'), self.x - self.r - game.x + 20, self.y - self.r + 75, 50,50) 
            
        self.f=(self.f+0.1)%self.rF
        
        if self.vx>0:
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,int(self.f)*self.w,0,int(self.f)*self.w+self.w,self.h)
        elif self.vx<0:
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,int(self.f)*self.w+self.w,0,int(self.f)*self.w,self.h)
        else:
            if isinstance(self,Bowser): 
                if self.dir>0:
                    if self.shield:
                        image(self.shImg,self.x-54,self.y-48,100,100) 
                    else:                
                        image(self.sImg,self.x-self.r-game.x-25,self.y-self.r-game.y-25,self.w,self.h)
                else:
                    if self.shield:
                        image(self.shImg,self.x-54,self.y-48,100,100,100,0,0,100)
                    else:                
                        image(loadImage('bowserStand2.png'),self.x-self.r-game.x-25,self.y-self.r-game.y-25,self.w,self.h) #error
                                                
                        
            else: #  mario
                if self.dir>0:
                    if self.shield:
                        image(self.shImg,self.x-61,self.y-48,100,100)
                    else:                
                        image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h)
                else:
                    if self.shield:
                        image(self.shImg,self.x-58,self.y-50,100,100,100,0,0,100)
                    else:                
                        image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,self.w,0,0,self.h)
                  
class Mario(Creature):
    def __init__ (self,x,y,r,g,sImg,rImg,shImg,rF,w,h,l):
        Creature.__init__(self,x,y,r,g,sImg,rImg,shImg,rF,w,h,l)
        self.Keys={UP:False, LEFT:False, RIGHT:False, DOWN:False, SHIFT:False}
        self.jumpSound = minim.loadFile('jump.wav')
        self.health = 150
        self.shield = False
            
    def update(self):
        if self.y+self.r < self.g:
            self.vy+=0.1
            self.y+=self.vy
        else:
            self.vy=0
            self.y=self.g-self.r
    
        if self.Keys[RIGHT]:
            self.vx=7
            self.dir=1

        elif self.Keys[LEFT]: 
            self.vx=-7
            self.dir=-1
        else:
            self.vx=0
            
        if self.Keys[UP] and self.vy==0 :
            self.vy-=5
            self.y+=self.vy
            game.playSound(self.jumpSound, 'once')
        
        if self.Keys[DOWN] and self.vy==0 and self.vx == 0: # shield 
            self.shield=True
        else:
            self.shield=False
            
        if self.Keys[SHIFT]: # hit
            pass
            
        self.x+=self.vx
        
        if self.x-self.r<=0:
            self.x=self.r
            
        if self.distance(bowser) <= self.r+bowser.r:
            if bowser.y-bowser.r < self.y-self.r and bowser.vy > 0:
                if not self.shield:
                    self.health = max (0, self.health-2)
                    if self.health == 0:
                        mario.__init__(150,25,39,game.g,'marioStand.png','marioRun.png','marioShield.png',4,60,80,mario.l+1)
            elif mario.vy > 0:
                if not bowser.shield:
                    bowser.health = max (0,bowser.health-2)
    
                  
        for p in game.platforms:
            if (self.y+self.r < p.y or self.g==p.y) and p.x <= self.x <= p.x+p.w:
                self.g=p.y
                return
        self.g=game.g
    
        if self.y+mario.r==self.g:
            mario.__init__(150,25,39,game.g,'marioStand.png','marioRun.png','marioShield.png',4,60,80,mario.l+1)

    def distance(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

class Bowser(Creature):
    def __init__ (self,x,y,r,g,sImg,rImg,shImg,rF,w,h,l):
        Creature.__init__(self,x,y,r,g,sImg,rImg,shImg,rF,w,h,l)
        self.Keys={UP:False, LEFT:False, RIGHT:False, DOWN:False}
        self.jumpSound = minim.loadFile('bowserJump.mp3')
        self.health = 150
        self.shield = False

            
    def update(self):
        if self.y+self.r < self.g:
            self.vy+=0.1
            self.y+=self.vy
        else:
            self.vy=0
            self.y=self.g-self.r
    
        if self.Keys[RIGHT]:
            self.vx=7
            self.dir=1

        elif self.Keys[LEFT]: 
            self.vx=-7
            self.dir=-1
        else:
            self.vx=0
            
        if self.Keys[UP] and self.vy==0 :
            self.vy-=6
            self.y+=self.vy
            game.playSound(self.jumpSound, 'once')

        if self.Keys[DOWN] and self.vy==0 and self.vx == 0: # shield 
            self.shield=True
        else:
            self.shield=False
            
        self.x+=self.vx
        
        if self.x-self.r<=0:
            self.x=self.r
                      
        if self.health == 0: 
            bowser.__init__(650,25,33,game.g,'bowserStand.png','bowserRun.png','bowserShield.png',2,100,100,bowser.l+1)
                  
        for p in game.platforms:
            if (self.y+self.r < p.y or self.g==p.y) and p.x <= self.x <= p.x+p.w:
                self.g=p.y
                return
        self.g=game.g
    
        if self.y+bowser.r==self.g:
            bowser.__init__(650,25,33,game.g,'bowserStand.png','bowserRun.png', 'bowserShield.png',2,100,100,bowser.l+1)
        
    def distance(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

game=Game(800,600,900)
mario=Mario(140,25,39,game.g,'marioStand.png','marioRun.png','marioShield.png',4,60,80,0)
bowser=Bowser(680,25,33,game.g,'bowserStand.png','bowserRun.png', 'bowserShield.png',2,100,100,0)


global savedTime, totalTime, passedTime, sec, gameover, addlifetime, extralife
savedTime = 0
totalTime = 1000
sec = 300
gameover = False
extralife = None
addlifetime = random.randint(20,70)

def setup():
    size(game.w,game.h)
    background(0)
    stroke(255)
    
def draw():
    global savedTime, totalTime, passedTime, sec, gameover, addlifetime, extralife
    if sec >= 90:
        background(0)
        image(loadImage('firstDisplay.png'),0,0,800,600)
        sec-=1
    elif sec > 0 and sec < 90:
        background(0)
        image(loadImage('background.png'), 0, 0,800,600)
        if game.t != 0:
            if sec == (90-addlifetime) and len(game.lives) == 0:
                game.lives.append(addLife(random.randint(200,600),25,50,game.g,'health.png',50,50))
            textSize(28)
            text(game.t, 40,40) 
            myFont = createFont("prstartk.ttf", 32)
            textFont(myFont)
            fill(255)
            textSize(24)
            text("DEATHS:",250,500)
            text(mario.l,325,550)
            text(bowser.l,500,550)
        passedTime = millis() - savedTime
        if passedTime > totalTime:
            sec-=1
            game.t = str(sec//60)+':'
            if sec%60 < 10:
                game.t+='0'+str(sec%60)
            else:
                game.t+=str(sec%60)
            savedTime = millis()   
        game.display()
        mario.display()
        bowser.display()
        
    else:
        if gameover == False:
            background(23,25,35)
            playWinnerNoise()


def playWinnerNoise():
    global gameover
    if bowser.l > mario.l:
        image(loadImage('Player1Wins.png'),0,0,800,600)
        game.playSound(minim.loadFile('marioWin.mp3'), 'once')
    elif mario.l > bowser.l:
        image(loadImage('Player2Wins.png'),0,0,800,600)
        game.playSound(minim.loadFile('marioLose.mp3'), 'once')
    elif mario.l == bowser.l:
        image(loadImage('tieGame.png'),0,0,800,600)
        game.playSound(minim.loadFile('marioLose.mp3'), 'once')
    gameover=True

    
def keyPressed():
    # bowser
    if key == "'":
        bowser.Keys[RIGHT]=True
    elif key == "L" or key == "l":
        bowser.Keys[LEFT] = True
    elif key == "P" or key == "p":
        bowser.Keys[UP] = True
    elif key == ";":
        bowser.Keys[DOWN] = True

        
    # mario    
    if key == "D" or key == "d":
        mario.Keys[RIGHT]=True
    elif key == "A" or key == "a":
        mario.Keys[LEFT] = True
    elif key == "W" or key == "w":
        mario.Keys[UP] = True
    elif key == "S" or key == "s":
        mario.Keys[DOWN] = True
    
def keyReleased():
    # bowser
    if key == "'":
        bowser.Keys[RIGHT]= False
    elif key == "L" or key == "l":
        bowser.Keys[LEFT] = False
    elif key == "P" or key == "p":
        bowser.Keys[UP] = False
    elif key == ";":
        bowser.Keys[DOWN] = False
        
 # mario    
    if key == "D" or key == "d":
        mario.Keys[RIGHT]=False
    elif key == "A" or key == "a":
        mario.Keys[LEFT] = False
    elif key == "W" or key == "w":
        mario.Keys[UP] = False
    elif key == "S" or key == "s":
        mario.Keys[DOWN] = False
    
    
