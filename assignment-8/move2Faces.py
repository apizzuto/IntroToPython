'''
TITLE: Ex-2.4.8.3
AUTHOR: Alex Pizzuto & Connor Moore
DATE: 4/12/17
DESCRIPTION: Moving Faces Exercise

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 4/12/17

'''

from graphics import *

def moveAll(shapeList, dx, dy):
    ''' Move all shapes in shapeList by (dx, dy).'''    
    for shape in shapeList: 
        shape.move(dx, dy)

def makeFace(center, win):
    '''display face centered at center in window win.
    Return a list of the shapes in the face.
    '''
    
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)     # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    noseCorner1 = center.clone()
    noseCorner1.move(-5,-5)
    noseCorner2 = noseCorner1.clone()
    noseCorner2.move(10,0)
    noseCorner3 = noseCorner2.clone()
    noseCorner3.move(-5,10)
    noseVert = [noseCorner1,noseCorner2,noseCorner3]
    nose = Polygon(noseVert)
    nose.setFill('blue')
    nose.draw(win)
    

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, mouth, nose]

def main():
    win = GraphWin('Move Faces Exercise',300,300)
    win.yUp()
    text = Text(Point(win.getWidth()/2,250),"Click where you want two faces")
    text.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    text.undraw()
    face1 = makeFace(p1,win)
    face2 = makeFace(p2,win)
    mag = ((p1.getX()-p2.getX())**2+(p1.getY()-p2.getY())**2)**(1/2)
    dx = (p1.getX()-p2.getX())/mag
    dy = (p1.getY()-p2.getY())/mag
    for i in range(15):
        moveAll(face1,dx,dy)
        moveAll(face2,-dx,-dy)
        time.sleep(0.05)
    win.promptClose(win.getWidth()/2,50)
main()
