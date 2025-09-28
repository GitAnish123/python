import cmu_graphics
from cmu_graphics import *





"""
Code Result: A soccer video game that changes based on mouse events and more
"""


# Draw the sky as a background
app.background = rgb(135, 206, 235)


# Draw the grass
Rect(0, 375, 400, 25, fill=rgb(34, 139, 34))


# Draw Soccer Ball Pentagon Patterns using a function
def drawPentagonPattern(x, y, rotate=0):
    if rotate != 0:
        return RegularPolygon(x, y, 12, 5, fill='black', rotateAngle=rotate)
    else:
        return RegularPolygon(x, y, 12, 5, fill='black')


# Create a soccer ball function that will make a soccer ball
# It contains the helper function for the patterns on the soccer ball
def drawSoccerBall(x, y):
    ball = Group(
        Circle(x, y, 50, fill='white', border='black', borderWidth=2),
        drawPentagonPattern(x, y-25, 180),
        drawPentagonPattern(x+27, y+3, -15),
        drawPentagonPattern(x-28, y+3, 15),
        drawPentagonPattern(x-15, y+32, 15),
        drawPentagonPattern(x+15, y+31, -15),
        drawPentagonPattern(x-3, y+1),
    )
    return ball
    
gameBall = drawSoccerBall(125, 330)


# Draw more visual elements
sun = Circle(400, 0, 50, fill=gradient('orange', 'red', start='top'), visible=False)
bird = Group(
    Oval(100, 100, 28, 10, fill='black'),
    Polygon(90, 95, 75, 70, 85, 85, 90, 95, fill='black'),
    Polygon(110, 95, 125, 115, 115, 100, 110, 95, fill='black'),
    Polygon(87, 100, 80, 97, 80, 103, fill='black'),
    Circle(114, 98, 3, fill='black'),
    )

bird.visible = False
goals = Label("Goals:      ", 59, 35, visible=False, bold=True, fill='yellow', size=25)
goalPoints = Label(0, 90, 35, visible=False, bold=True, fill='yellow', size=25)


# Label the "You Scored" celebration
celebration = Label("", 210, 25, bold=True, size=25, visible=False)


# Draw the soccer goal post
Line(384, 118, 400, 118, fill='white', lineWidth=4)
Line(400, 118, 400, 375,fill='white', lineWidth=4)
Line(384, 375, 400, 375, fill='white', lineWidth=4)


# Create the Soccer Ball Kick video game logo/title/instructions (all in one group)
gameGroupOverview = Group(
    drawSoccerBall(330, 20),
    Label("Soccer Ball Kick Simulator -- Video Game", 130, 20, bold=True, size=12),
    Line(0, 72, 400, 72, lineWidth=1, opacity=50),
    Label("Instructions: Use the mouse to play the simulator", 138, 53, fill='red', 
        bold=True, size=11),
    )


# Draw the person
person = Group(
    Rect(36, 251, 37, 59, fill='red'),
    Circle(55, 234, 25, fill=rgb(232, 190, 172)),
    Label('45', 56, 281, bold=True, size=25),
    Line(73, 281, 94, 288, fill=rgb(232, 190, 172)),
    Line(34, 281, 55, 288, fill=rgb(232, 190, 172)),
    Line(47, 310, 47, 375, fill=rgb(232, 190, 172)),
    Line(61, 310, 61, 375, fill=rgb(232, 190, 172)),
    )


# More instructions
screenHide = Rect(0, 0, 400, 400, fill='blue', visible=True)
startInstruction = Label("Press the 'enter' key to start the game.", 200, 200, visible = True,
    size=20, fill='darkRed', bold=True)
startInstruction2 = Label("DO NOT MOVE THE MOUSE OR PRESS ANYTHING", 200, 250, fill='darkRed', bold=True, size=15)
def onKeyPress(key):
    if key == 'enter':
        screenHide.visible = False
        startInstruction.visible = False
        startInstruction2.visible = False
    

# Define the onMouseMove function to enable mouse move events
def onMouseMove(mouseX, mouseY):
    person.centerX = mouseX
    if gameGroupOverview.visible:
        gameGroupOverview.visible = False
    gameBall.centerX = mouseX+64
    while person.centerX >= 200:
        if person.centerX >= 200:
            gameBall.centerX -= 10
            person.centerX -= 10
        else:
            person.centerX = mouseX
            gameBall.centerX = mouseX+64
    sun.visible = True
    bird.visible = True
    celebration.visible = False
    goalPoints.visible = True
    goals.visible = True


# Define the onMousePress function to enable mouse press events
def onMousePress(mouseX, mouseY):
    if gameGroupOverview.visible:
        gameGroupOverview.visible = False
    gameBall.centerX = 350
    celebration.visible = True
    celebration.value = 'Kicking the ball..'


# Define the onMouseRelease function to enable mouse release events
def onMouseRelease(mouseX, mouseY):
    celebration.visible = True
    celebration.value = 'You scored!!  :)'
    goalPoints.value += 1
    if goalPoints.value % 5 == 0 and goalPoints.value != 0:
        if (goalPoints.value // 5) % 2 == 1:
            app.background = rgb(43, 47, 119)
            sun.fill = 'white'
        else:
            app.background = rgb(135, 206, 235)
            sun.fill = gradient('orange', 'red', start='top')


cmu_graphics.run()