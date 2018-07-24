'''
TITLE: Ex-2.4.5.1
AUTHOR: Alex Pizzuto & Connor Moore
DATE: 4/12/17
DESCRIPTION: Scene Exercise

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 4/12/17

'''
from graphics import *

win = GraphWin("Alex and Connor's pretty picture", 500,400)
win.yUp()
win.setBackground('blue')
grass = Rectangle(Point(0,0),Point(500,125))
grass.setFill('green')
house = Rectangle(Point(25,125),Point(150,275))
house.setFill('brown')
grass.draw(win)
house.draw(win)
vertices = [Point(25,275),Point(150,275),Point(87.5,340)]
roof = Polygon(vertices)
roof.setFill('red')
roof.draw(win)
door = Rectangle(Point(65,125),Point(110,200))
door.setFill('black')
window1 = Rectangle(Point(50,225),Point(75,250))
window1.setFill('white')
window2 = Rectangle(Point(100,225),Point(125,250))
window2.setFill('white')
door.draw(win)
window1.draw(win)
window2.draw(win)
sun = Circle(Point(400,325),50)
sun.setFill('yellow')
sun.draw(win)
