'''
TITLE: Ex-2.4.8.2
AUTHOR: Alex Pizzuto & Connor Moore
DATE: 4/12/17
DESCRIPTION: Faces Exercise
Loop to make six faces where the user clicks

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 4/12/17

'''
from graphics import *

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
    win = GraphWin('faces Exercise',300,300)
    win.yUp()
    text = Text(Point(win.getWidth()/2,250),'Click on the screen 6 times and see what happens')
    text.draw(win)
    for i in range(6):
        makeFace(win.getMouse(),win)
    win.promptClose(win.getWidth()/2, 20)
main()
