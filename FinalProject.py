'''
TITLE: Ex-2.4.8.1
AUTHOR: Alex Pizzuto & Connor Moore
DATE: 4/12/17
DESCRIPTION: Nose in Face Exercise

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 4/12/17

'''
from graphics import *
from math import *

def force(circ1, circ2):
    p1 = mass1.getCenter()
    p2 = mass2.getCenter()
    dist2 = (p1.getX()-p2.getX())**2+(p1.getY()-p2.getY())**2
    forcemag = 1/dist2
    forcedir = math.atan((p2.getY()-p1.getY())/(p2.getX()-p1.getX()))
    return (forcemag, forcedir, -forcedir)

def makePlanet():
    p1 = win.getMouse()
    circ = Circle(p1, 25)
    vel

    return (circ, mass, vel)
                    

