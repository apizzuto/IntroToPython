'''
TITLE: Final Exam Graphics Extra Credit
AUTHOR: Alex Pizzuto
DATE: 5/1/17
DESCRIPTION: Fun Picture

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 5/1/17

'''
from graphics import *
colorList = ['red','blue','orange','pink']
win = GraphWin("Nested Circles and Squares",500,500)
win.setCoords(-1,-1,1,1)
basis = 1
shapeList = []
for i in range(30):
    shapeList.append(Circle(Point(0,0),basis))
    shapeList.append(Rectangle(Point(-(1/(2**(1/2)))*basis,(1/(2**(1/2)))*basis),Point((1/(2**(1/2)))*basis,-(1/(2**(1/2)))*basis)))
    basis = basis*(1/(2**(1/2)))
for i in range(30):
    shapeList[i].setFill(colorList[i%4])
    shapeList[i].draw(win)
