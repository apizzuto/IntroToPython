'''
TITLE: Planetary Orbit Simulator 
AUTHOR: Alex Pizzuto & Connor Moore
DATE: 4/17/17
DESCRIPTION: Prompts the user to establish initial
conditions, then uses Euler's Method to trace planetary
orbits. Note, all astronomical units have been scaled such that
G=1 and masses are defined essentially in terms of solar masses. 
'''


import time
import math
import random
from graphics import *

frequency = 20

def planetCreator(mass, circle, vx, vy):
    #Given the planet parameters, returns planet as a dictionary
    colorList = ['red','yellow','green','purple','blue']
    color = colorList[random.randint(0,4)]
    pdict = {"M": mass, "C": circle,"V": (vx,vy),'F':None,"c": color}
    return pdict

def Window(x,y,name):
    #Sets up our graphics window
    win = GraphWin(name,x,y)
    win.setCoords(-1,-1,1,1)
    return win

def dualForce(body1, body2):
    #Establishes the force between two bodies (in scaled units)
    p1 = body1["C"].getCenter()
    p2 = body2["C"].getCenter()
    dist2 = (p1.getX()-p2.getX())**2+(p1.getY()-p2.getY())**2
    forcemag = body1['M']*body2['M']/dist2
    forcedir = math.atan2((p2.getY()-p1.getY()),(p2.getX()-p1.getX()))
    body1['F']=(forcemag, forcedir)
    body2['F']=(forcemag, forcedir+math.pi)
    return body1

def Velocity(body, interval):
    #Euler's Method be here
    vx = body['V'][0]+interval*body['F'][0]*math.cos(body['F'][1])/body['M']
    vy = body['V'][1]+interval*body['F'][0]*math.sin(body['F'][1])/body['M']
    body['V'] = (vx,vy)
    return body
    
def Position(body,interval,win):
    #Moves bodies for each iteration
    dot = Circle(body['C'].getCenter(),body['C'].getRadius()/10)
    dot.setFill(body['c'])
    dot.setOutline(body['c'])
    dot.draw(win)
    body["C"].move(body["V"][0]*interval,body["V"][1]*interval)
    return body

def Trajectory(body1, body2, win):
    #Concatenates the steps of Euler's Method
    interval = (1/frequency)**2
    flag = collisions(body1, body2)
    dualForce(body1, body2)
    Velocity(body1, interval)
    Velocity(body2, interval)
    Position(body1,interval,win)        
    Position(body2, interval,win)        
    flag = collisions(body1, body2)

def collisions(body1, body2):
    #if the objects touch, exit.
    p1 = body1['C'].getCenter()
    p2 = body2['C'].getCenter()
    r1 = body1['C'].getRadius()
    r2 = body2['C'].getRadius()
    dist2 = (p1.getX()-p2.getX())**2+(p1.getY()-p2.getY())**2
    flag = 1
    if math.sqrt(dist2) >= 1.15*(r1+r2):
        flag = 0
    return flag

def toofar(planet1,planet2):
    #If a planet is too far, exit
    flag = 0
    p1 = planet1["C"].getCenter()
    p2 = planet2["C"].getCenter()
    if math.fabs(p1.getX()) > 4 or math.fabs(p1.getY()) > 4:
        flag = 1
    elif math.fabs(p2.getX()) > 4 or math.fabs(p2.getY()) > 4:
        flag = 1
    return flag

def initialVel(x,y,win):
    #Define initial velocity from click
    p = win.getMouse()
    rawX = p.getX() - x
    rawY = p.getY() - y
    vx = rawX*8
    vy = rawY*8
    return vx,vy

def scene(win):
    #Initiaizes background, 30 stars placed and sized randomly
    win.setBackground("Midnight Blue")
    for i in range(30):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        star = Circle(Point(x,y),random.uniform(0.002,0.0055))
        star.setOutline('Snow')
        star.setFill('Snow')
        star.draw(win)
  
def main():
    w = Window(700,700,"Simulation Window")
    scene(w)
    num = int(input("How many planets would you like to simulate? "))
    sizeList = []
    for i in range(num):
        size = input("How large do you want planet " + str(i+1) +
                     "? (Enter h for huge, b for big, m for medium, s for small): ")
        while size != 1 and size != 2 and size !=3 and size !=10:
            if size.lower() == "b":
                size = 3
            elif size.lower() == "m":
                size = 2
            elif size.lower() == "s":
                size = 1
            elif size.lower() == "h":
                size = 10
            else:
                size = input("Not recognized, please input size again: ")
        sizeList.append(size)
    print("Now, refer to the graphics window for the rest of the directions.")
    message = "Click where you want planet 1"
    text = Text(Point(0,0.9),message)
    text.setSize(20)
    text.draw(w)
    planetList = []
    veclist = []
    for i in range(num):
        text.setText("Click where you want planet " +str(i+1))
        p = w.getMouse()
        x = p.getX()
        y = p.getY()
        text.setText("Now, click the direction you want planet "+str(i+1)+" to go." +
                     "\nThe farther from the planet you click, the faster it goes.")
        vx,vy = initialVel(x,y,w)
        planetList.append(planetCreator(15*sizeList[i],Circle(Point(x,y),0.01+0.01*sizeList[i]),vx,vy))
        planetList[i]["C"].setFill(planetList[i]['c'])
        planetList[i]["C"].setOutline(planetList[i]['c'])
        planetList[i]["C"].draw(w)
        p1 = vx/8 + x
        p2 = vy/8 + y
        vec = Line(Point(p1,p2),Point(x,y))                    
        veclist.append(vec)
        vec.draw(w)
    text.setText("Click to begin")
    w.getMouse()
    for i in veclist:
        i.undraw()
    text.undraw()
    flag = 0
    while flag==0:
        for i in range(len(planetList)):
            if flag > 0:
                break
            for j in range(i+1,len(planetList)):
                Trajectory(planetList[i],planetList[j],w)
                flag = flag + collisions(planetList[i],planetList[j])
                flag = flag + toofar(planetList[i], planetList[j])
                if flag > 0:
                    break
        time.sleep(0.005)
    print("Objects collided or are too far. Exiting.")
    
main()
