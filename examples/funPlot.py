from graphics import *
import math
import random
import time



def ptList(rangeNum,i):
    ptList = []
    t0 = time.clock()
    for item in rangeNum:
        temp = Point(450+(item**2)*math.cos(float(item+i/16*math.pi)),450+(item**2)*math.sin(float(item+i/16*math.pi)))
        ptList.append(temp)
    #print(i+1,": ",time.clock() - t0)
    return ptList

def floatRange(init, stop, increment):
    rangeList = []
    k = init
    for i in range(int(stop//increment)):
        rangeList.append(k)
        k += increment
        i += 1
    return rangeList

def toShape(ptList):
    spList = []
    for i in ptList:
        c = Circle(i,5)
        spList.append(c)
    return spList

def spiralDrawer(window, shapeRange):
    t0 = time.clock()
    j = 0
    listCol = ['red','green','blue','black','brown']
    for i in shapeRange:
        #i.setFill(listCol[random.randrange(len(listCol))])
        i.setFill(listCol[j%(len(listCol))])
        j+=1
        i.draw(window)
    #print("Drawing time: ",time.clock() - t0)

def despiral(window, shapeRange):
   for i in shapeRange:
        i.undraw()
        time.sleep(.025)
        i.draw(window)
           
def main():
    mw = GraphWin("Fun Plot",900,900)
    a = floatRange(0,50,.25)
    spiralList=[]
    for i in range(0,32):    
        b = toShape(ptList(a,i))
        spiralList.append(b)
        spiralDrawer(mw,b)
        #timer delay#
    i=0
    while mw.checkMouse()== None:
        print(i)
        for item in spiralList:
            despiral(mw,item)
        i+=1
    mw.getMouse()
    mw.close()        
    
main()
    
