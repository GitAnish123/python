# Importing
from random import randint, choice
from cmu_graphics import *


# Game Materials/Tools
player = Rect(180, 350, 40, 40)
target = Circle(200, 0, 20, fill='blue')
gameOver = False
score = Label(0, 10, 10, size=20)
modulo = 0
x = 0
speed = 5
playerSpeed = 20

# Player movements
def movePlayer(key):
    global modulo
    global x
    global speed
    global playerSpeed
    if key == 'left':
        player.left -= playerSpeed
    elif key == 'right':
        player.right += playerSpeed
    elif key == 's':
        speed += 1
    elif key == 'p':
        playerSpeed += 1
    else:
        resetTarget() # Admin hack (resets the ball infinetely)
        target2 = Circle(randint(0, 400), randint(0, 400), 20, fill='blue')
        modulo += 1
        if modulo % 100 == 0:
            x += 1
            if x >= 20:
                app.showMessage(f'HAPPY {100*x}:\n You BEAT the game:   ALL OBJECTS FILLED;' 
                ' PROJECTILES CLEAR;   EVERYTHING FILLED 100%')
            else:
                app.showMessage(f'HAPPY {100*x}')
            

# Reset Target
def resetTarget():
    target.centerX = randint(20, 380)
    target.centerY = 0
    target.fill = choice(['blue', 'red']) # Blue is good

# Key press condition
def onKeyPress(key):
    if not gameOver:
        movePlayer(key)

# Game loop
def onStep():
    global gameOver
    global modulo
    if not gameOver:
        target.centerY += speed
        if target.hitsShape(player):
            if target.fill == 'blue':
                score.value += 1
                resetTarget()
            else:
                gameOver = True
                Label('Wrong Color! Game Over!', 200, 200, size=20, fill='red')
        elif target.top > 400:
            resetTarget()


# Run the app
app.run()