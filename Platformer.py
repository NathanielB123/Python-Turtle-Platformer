import turtle
import time
import random
import sys

turtle.bgcolor("Light Blue")
Turtle1 = turtle.Turtle()
Turtle1.ht()
screenr = turtle.Screen()
Laser = []
Coin = 0
CoinX = 0
CoinY = 0
COINHIT = 0

global Keypress
Keypress = ""
XPos = 0
YPos = 100
XVel = 0
YVel = 0

Turtle0 = turtle.Turtle()
Turtle0.ht()
Turtle0.speed(500)
Turtle0.penup()

Turtle0.clear()
turtle.bgcolor("Light Blue")

Turtle0.goto(-100,0)
Turtle0.write("Arrow keys or WASD to move.")
Turtle0.goto(-100,-20)
Turtle0.write("Collect coins, avoid lasers, do not fall off")
Turtle0.goto(-100,-40)
time.sleep(3)
Turtle0.clear()

Turtle0.goto(0,0)
Turtle0.speed(100)

def start123():#this sub routine draws the number 3 in red
    Turtle0.penup()
    Turtle0.color("red")#this changes the colour of the pen
    Turtle0.left(90)
    Turtle0.forward(20)
    Turtle0.pendown()
    Turtle0.begin_fill()
    Turtle0.right(90)
    Turtle0.forward(70)
    Turtle0.left(90)
    Turtle0.forward(40)
    Turtle0.left(90)
    Turtle0.forward(70)
    Turtle0.right(90)
    Turtle0.forward(20)
    Turtle0.right(90)
    Turtle0.forward(70)
    Turtle0.left(90)
    Turtle0.forward(40)
    Turtle0.left(90)
    Turtle0.forward(70)
    Turtle0.right(90)
    Turtle0.forward(20)
    Turtle0.right(90)
    Turtle0.forward(90)
    Turtle0.right(90)
    Turtle0.forward(140)
    Turtle0.right(90)
    Turtle0.forward(100)
    Turtle0.end_fill()

start123()#this calls the sub routine
time.sleep(1)
Turtle0.clear()#this clears the number

def start2():#this sub routine draws the number 2 in orange
    Turtle0.begin_fill()
    Turtle0.color("orange")#this changes the colour of the pen)#this changes the speed of the pen
    Turtle0.left(90)
    Turtle0.forward(20)
    Turtle0.right(90)
    Turtle0.forward(70)
    Turtle0.left(90)
    Turtle0.forward(40)
    Turtle0.left(90)
    Turtle0.forward(70)
    Turtle0.right(90)
    Turtle0.forward(20)
    Turtle0.right(90)
    Turtle0.forward(90)
    Turtle0.right(90)
    Turtle0.forward(80)
    Turtle0.right(90)
    Turtle0.forward(70)
    Turtle0.left(90)
    Turtle0.forward(40)
    Turtle0.left(90)
    Turtle0.forward(70)
    Turtle0.right(90)
    Turtle0.forward(20)
    Turtle0.right(90)
    Turtle0.forward(90)
    Turtle0.right(90)
    Turtle0.forward(70)
    Turtle0.end_fill()
    
start2()#this calls the sub routine
time.sleep(1)
Turtle0.clear()

def start1 ():
    Turtle0.begin_fill()
    Turtle0.color("green")            
    Turtle0.right(180)
    Turtle0.forward(100)
    Turtle0.right(90)
    Turtle0.forward(20)
    Turtle0.right(90)
    Turtle0.forward(100)
    Turtle0.right(90)
    Turtle0.forward(20)
    Turtle0.end_fill()
    
start1()
time.sleep(1)
Turtle0.clear()

def GetInput():
    global Keypress
    Keypress = ""
    screenr.onkeypress(LEFT,"Left") # how to get input
    screenr.onkeypress(RIGHT,"Right")
    screenr.onkeypress(UP,"Up")
    screenr.onkeypress(LEFT,"a") # how to get input
    screenr.onkeypress(RIGHT,"d")
    screenr.onkeypress(UP,"w")
    screenr.onkeypress(UP,"space")
    time.sleep(0.05)

def UP():
    global Keypress
    Keypress = Keypress+"U"
    if Keypress == "UU":
        Keypress = "U"
    if Keypress =="LUU":
        Keypress = "LU"
    if Keypress == "RUU":
        Keypress = "RU"

def RIGHT():
    global Keypress
    Keypress = "R"

def LEFT():
    global Keypress
    Keypress = "L"
    
    
def DrawCharacter():
    turtle.tracer(0, 0)
    screenr.clear()
    DrawRectangle(-25,-25,25,25,"Blue")

def DrawLevel(XPos,YPos,Laser,Coin,CoinX,CoinY):
    turtle.bgcolor("Light Blue")
    DrawRectangle(-100-XPos,-300-YPos,100-XPos,-200-YPos,"Green")
    DrawRectangle(-400-XPos,-300-YPos,-200-XPos,-200-YPos,"Green")
    DrawRectangle(400-XPos,-300-YPos,200-XPos,-200-YPos,"Green")
    DrawRectangle(-1000-XPos,-1000-YPos,1000-XPos,-1500-YPos,"Red")
    if not Coin == 0:
        COINHIT = DrawRectangle(CoinX-XPos,CoinY-YPos,CoinX+25-XPos,CoinY+25-YPos,"Yellow")
    else:
        COINHIT = 0
    i = 0
    while i < len(Laser):
        DrawRectangle(Laser[i]-XPos,Laser[i+1]-YPos,Laser[i]-XPos+30,Laser[i+1]-YPos+2,"Red")
        i += 2
    if YPos < -1000:
        sys.exit()
    turtle.update()
    return(COINHIT)
        
def DrawRectangle(X,Y,X2,Y2,C):
    Turtle1.color(C)
    Turtle1.speed(0)
    turtle.delay(0)
    Turtle1.ht()
    Turtle1.penup()
    Turtle1.begin_fill()
    Turtle1.goto(X,Y)
    Turtle1.pendown()
    Turtle1.goto(X2,Y)
    Turtle1.goto(X2,Y2)
    Turtle1.goto(X,Y2)
    Turtle1.goto(X,Y)
    Turtle1.end_fill()
    if C == "Red" and round(X/50)*50 == 0 and round(Y/50)*50 == 0:
        sys.exit()
    if C == "Red" and round(X2/50)*50 == 0 and round(Y2/50)*50 == 0:
        sys.exit()
    if C == "Yellow" and round(X/50)*50 == 0 and round(Y/50)*50 == 0:
        COINHIT = 1
    elif C == "Yellow" and round(X2/50)*50 == 0 and round(Y2/50)*50 == 0:
        COINHIT = 1
    else:
        COINHIT = 0
    return(COINHIT)
def RunPhysics(XPos,YPos,XVel,YVel,Laser,Coin,CoinX,CoinY):
    global Keypress

    i = 0
    while i < len(Laser):
        i += 2
    YPos += YVel
    
    if YPos > - 175 or (XPos > 125 and XPos < 175) or XPos > 425 or (XPos < -125 and XPos > -175) or XPos < -425 or YPos < -225:
        YVel -=  5
    else:
        YVel = 0
        YPos = -176
        if Keypress == "U" or Keypress == "RU" or Keypress == "LU":
            YVel = 40
            YPos+YVel

    if "R" in Keypress:
        XVel = 50
    
    if "L" in Keypress:
        XVel = -50

    XVel = XVel*0.6

    XPos += XVel

    if random.randint(0,10) == 1 and Coin == 0:
        CoinX = random.randint(-400,400)
        CoinY = random.randint(-100,0)

        Coin = 1

    if (Laser == [] or random.randint(0,10)) == 1 and len(Laser) < 8 :
        Laser.append(-1000)
        Laser.append(YPos + random.randint(-100,100))
                  
    i = 0
    LaserOld = Laser
    Laser = []
    while i < len(LaserOld):
        Laser.append(LaserOld[i]+30)
        i+=1
        Laser.append(LaserOld[i])
        i+=1

    if Laser[0] > 1000:
        Laser.pop(0)
        Laser.pop(0)
    

    return(XPos,YPos,XVel,YVel,Laser,Coin,CoinX,CoinY)
score = 0
while 1 == 1:
    screenr.listen()
    GetInput()
    DrawCharacter()
    COINHIT = DrawLevel(XPos,YPos,Laser,Coin,CoinX,CoinY)
    if COINHIT == 1:
        print("Coin collected!")
        score+=10
        print("Score:",score)
        Coin = 0
    (XPos,YPos,XVel,YVel,Laser,Coin,CoinX,CoinY) = RunPhysics(XPos,YPos,XVel,YVel,Laser,Coin,CoinX,CoinY)


    
    
