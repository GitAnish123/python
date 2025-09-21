import cmu_graphics
from cmu_graphics import *
import random

app.background = 'black'

def makeStar(x, y):
    c = Star(x, y, 10, 5, fill='white')
    def onMousePress(x, y):
        c.centerX -= 1

makeStar(0, 0),
makeStar(100, 0),
makeStar(200, 0),
makeStar(300, 0),
makeStar(400, 0),
makeStar(0, 100),
makeStar(100, 100),
makeStar(200, 100),
makeStar(300, 100),
makeStar(400, 100),
makeStar(0, 200),
makeStar(100, 200),
makeStar(200, 200),
makeStar(300, 200),
makeStar(400, 200),
makeStar(0, 300),
makeStar(100, 300),
makeStar(200, 300),
makeStar(300, 300),
makeStar(400, 300),
makeStar(0, 400),
makeStar(100, 400),
makeStar(200, 400),
makeStar(300, 400),
makeStar(400, 400),

spaceship = Polygon(200, 180, 220, 220, 180, 220, fill='blue')
target = Circle(20, 20, 5, fill='yellow')
target2 = Circle(20, 20, 5, fill='brown')
target3 = Circle(0, 400, 5, fill='purple')
challengeTarget4 = Circle(random.randint(0, 400), random.randint(0, 400), random.randint(2, 10), fill='green')
laser = Line(0, 0, 0, 0, fill='red', visible=False)  # Serve this as a placeholder. It will be modified later (the coordinates)
points = Label(0, 30, 30, fill='orange', size=30, bold=True)
note = Label("Press any key to see the instructions", 90, 50, size=10, fill='white', bold=True)

def onStep():
    
    target.centerX -= 1
    if target.centerX < 20:
        target.centerX = 380
    
    target2.centerY += random.randint(1, 10)
    if target2.centerY > 380:
        target2.centerY = 20
        target2.centerX = random.randint(20, 380)
    
    target3.centerX += random.randint(1, 15)
    target3.centerY -= random.randint(1, 15)
    if target3.centerX > 380:
        target3.centerX = 0
    if target3.centerY < 20:
        target3.centerY = 400
    
    challengeTarget4.centerX += random.randint(-15, 15)
    challengeTarget4.centerY += random.randint(-15, 5)
    if challengeTarget4.centerX < 20:
        challengeTarget4.centerX = random.randint(0, 400)
    if challengeTarget4.centerY < 20:
        challengeTarget4.centerY = random.randint(0, 400)
    challengeTarget4.radius = random.randint(2, 10)
    
    if laser.visible:
        laser.x1 = spaceship.centerX
        laser.y1 = spaceship.centerY
        laser.x2 = spaceship.centerX
        laser.y2 = 0
    
    if laser.visible and laser.hitsShape(target):
        points.value += 1
        target.centerX = 380
    
    if laser.visible and laser.hitsShape(target2):
        points.value += 2
        target2.centerY = 20
        target2.centerX = random.randint(20, 380)
    
    if laser.visible and laser.hitsShape(target3):
        points.value += 3
        target2.centerY = 0
        target2.centerX = 400
    
    if laser.visible and laser.hitsShape(challengeTarget4):
        points.value += 5
        challengeTarget4.centerX = random.randint(0, 400)
        challengeTarget4.centerY = random.randint(0, 400)
        challengeTarget4.radius = random.randint(2, 10)
    
    if target.hitsShape(spaceship):
        Rect(0, 0, 399, 399, fill='red')
        Label('Game Over!', 200, 200, size=50)
        Label("The yellow ball hit you", 200, 310, size=20, fill='white')
        Label(points.value, 30, 30, size=30)
        app.stop()
            
    if target2.hitsShape(spaceship):
        Rect(0, 0, 399, 399, fill='red')
        Label('Game Over!', 200, 200, size=50)
        Label("The brown/red ball hit you", 200, 310, size=20, fill='white')
        Label(points.value, 30, 30, size=30)
        app.stop()

    if target3.hitsShape(spaceship):
        Rect(0, 0, 399, 399, fill='red')
        Label('Game Over!', 200, 200, size=50)
        Label("The purple ball hit you", 200, 310, size=20, fill='white')
        Label(points.value, 30, 30, size=30)
        app.stop()

def onKeyPress(key):
    Rect(0, 0, 399, 399, fill='lightBlue')
    Label("INSTRUCTIONS FOR THIS GAME: SPACESHIP EXPEDITION", 200, 100, fill='red', bold=True, size=12)
    Label("Toggle the mouse to move the spaceship left or right"
    ,200, 150)
    Label("Press any key to show this page, but it ends your game", 200, 180)
    Label("Be aware of the targets moving in different directions and speeds", 200, 210)
    Label("If the spaceship hits any of the targets (except the green one), the game ends", 200, 240,
    size=11)
    Label("To activate your laser, press the mousepad, and to hide it, release it",
    200, 270)
    Label("If your laser hits any of the targets, you earn points", 200, 300)
    Label("Yellow target: 1 point, Brown/Red: 2, Purple: 3,  Green: 5 (Bonus/Challenge)", 200, 330, size=11)
    Label("Have fun, good luck, & contact if any questions", 200, 360, size=17, bold=True)
    app.stop()
    
def onMousePress(x, y):
    laser.visible = True
    
def onMouseRelease(x, y):
    laser.visible = False

def onMouseMove(x, y):
    spaceship.centerX = x


cmu_graphics.run()