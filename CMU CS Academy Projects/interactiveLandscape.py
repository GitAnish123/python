import cmu_graphics
from cmu_graphics import *


"""
Code Result: An interactive landscape that changes visually by mouse presses and releases
"""


# Draw the sky as a background
app.background = 'skyBlue'


# Draw The sun
sunPart = Circle(220,80,50, fill='yellow', opacity=40)
sun = Circle(220, 80, 30, fill=gradient('orange', 'red', start='top'))


# Draw The Moon 
moon = Circle(220,80,30, fill='white', visible=False)


# Draw the mountains
mountain = Polygon(400, 150, 300, 40, 160, 150, fill=gradient('deepSkyBlue', 'royalBlue', start='top'))
mountain2 = Polygon(0, 150, 140, 40, 280, 150,  fill=gradient('deepSkyBlue', 'royalBlue', start='top'))
moutainTop = Polygon(130, 50, 140, 40, 150, 50, fill='white')
mountainTop2 = Polygon(290, 50, 300, 40, 310, 50, fill='white')


# Draw the grassy land
grass = Rect(0, 150, 400, 250, fill=rgb(142, 252, 0))


# Draw the bushes
# Make a function to assist
def drawBush(LeftPartxCenter, LeftPartyCenter, radius, color):
    Circle(LeftPartxCenter, LeftPartyCenter, radius, fill=color)
    Circle(LeftPartxCenter+7, LeftPartyCenter-7, radius, fill=color)
    Circle(LeftPartxCenter+13, LeftPartyCenter+2, radius, fill=color)
    
drawBush(9, 143, 8, 'darkGreen')
drawBush(35, 143, 7, 'darkGreen')
drawBush(217, 143, 8, 'darkGreen')
drawBush(245, 143, 8, 'darkGreen')
drawBush(272, 143, 8, 'darkGreen')
drawBush(297, 143, 7, 'darkGreen')
drawBush(323, 143, 8, 'darkGreen')
drawBush(348, 143, 8, 'darkGreen')
drawBush(371, 143, 7, 'darkGreen')
drawBush(395, 143, 8, 'darkGreen')


# Draw the pathway
Circle(185, 325, 140, fill='saddleBrown', border='black', borderWidth=1)
grass2 = Oval(120, 298, 200, 240, fill=rgb(142, 252, 0))


# Write down the time period
currentTime = Label("Current Time: 7:55 AM", 88, 272, fill='black')


# Draw the isolated house
Polygon(124, 186, 209, 186, 209, 149, 170, 120, 124, 147, 124, 186, fill='lightPink')
Polygon(124, 147, 59, 114, 47, 145, 124, 186, fill='hotPink')
Polygon(58, 115, 109, 72, 176, 115, 124, 147, fill=gradient('crimson', 'crimson', 'orange', start='right-top'))
Polygon(167, 121, 173, 113, 216, 142, 209, 149, fill=gradient('crimson', 'orange', start='left'))
Rect(152, 160, 18, 25, fill='blue')
window = Polygon(63, 130, 78, 136, 74, 149, 57, 142)
window2 = Polygon(94, 158, 98, 146, 115, 155, 112, 167)


# Draw the tree
Line(23, 158, 13, 171, lineWidth=3)
Line(23, 158, 24, 173, lineWidth=3)
Line(23, 158, 33, 171, lineWidth=3)
Line(23, 158, 22, 93, lineWidth=10, fill='maroon')
Circle(21, 59, 50, fill='darkGreen')


# Draw the bush with flowers
# Make a function to assist
def drawCircleFlowerBush(x, y):
    Circle(x, y, 8, fill='darkGreen')

Line(50, 400, 50, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(60, 400, 60, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(70, 400, 70, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(80, 400, 80, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(90, 400, 90, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(100, 400, 100, 345, lineWidth=3, fill='limeGreen',rotateAngle=10)
Line(40, 400, 40, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(30, 400, 30, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(20, 400, 20, 345, lineWidth=3, fill='limeGreen', rotateAngle=10)
Line(50, 400, 50, 345, lineWidth=3,fill='limeGreen')
Line(60, 400, 60, 345, lineWidth=3, fill='limeGreen')
Line(70, 400, 70, 345, lineWidth=3, fill='limeGreen')
Line(80, 400, 80, 345, lineWidth=3, fill='limeGreen')
Line(90, 400, 90, 345, lineWidth=3, fill='limeGreen')
Line(100, 400, 100, 345, lineWidth=3, fill='limeGreen')
Line(40, 400, 40, 345, lineWidth=3, fill='limeGreen')
Line(30, 400, 30, 345, lineWidth=3, fill='limeGreen')
Line(20, 400, 20, 345, lineWidth=3, fill='limeGreen')
Line(40, 400, 30, 360, fill='darkGreen')
Line(50, 400, 70, 360, fill='darkGreen')
Line(60, 400, 50, 350, fill='darkGreen')
Line(75, 400, 85, 360, fill='darkGreen')

drawCircleFlowerBush(80, 375)
drawCircleFlowerBush(90, 375)
drawCircleFlowerBush(85, 385)
drawCircleFlowerBush(70, 375)
drawCircleFlowerBush(80, 375)
drawCircleFlowerBush(75, 385)
drawCircleFlowerBush(60, 375)
drawCircleFlowerBush(70, 375)
drawCircleFlowerBush(65, 385)
drawCircleFlowerBush(50, 375)
drawCircleFlowerBush(60, 375)
drawCircleFlowerBush(55, 385)
drawCircleFlowerBush(40, 375)
drawCircleFlowerBush(50, 375)
drawCircleFlowerBush(45, 385)
drawCircleFlowerBush(30, 375)
drawCircleFlowerBush(40, 375)
drawCircleFlowerBush(35, 385)
drawCircleFlowerBush(80, 385)
drawCircleFlowerBush(90, 385)
drawCircleFlowerBush(85, 395)
drawCircleFlowerBush(70, 385)
drawCircleFlowerBush(80, 385)
drawCircleFlowerBush(75, 395)
drawCircleFlowerBush(60, 385)
drawCircleFlowerBush(70, 385)
drawCircleFlowerBush(65, 395)
drawCircleFlowerBush(50, 385)
drawCircleFlowerBush(60, 385)
drawCircleFlowerBush(55, 395)
drawCircleFlowerBush(40, 385)
drawCircleFlowerBush(50, 385)
drawCircleFlowerBush(45, 395)
drawCircleFlowerBush(30, 385)
drawCircleFlowerBush(40, 385)
drawCircleFlowerBush(35, 395)
drawCircleFlowerBush(30, 395)
drawCircleFlowerBush(30, 385)
drawCircleFlowerBush(35, 395)
drawCircleFlowerBush(20, 395)
drawCircleFlowerBush(20, 385)
drawCircleFlowerBush(25, 395)
drawCircleFlowerBush(92, 395)
drawCircleFlowerBush(90, 385)
drawCircleFlowerBush(95, 395)
drawCircleFlowerBush(30, 395)
drawCircleFlowerBush(95, 375)
drawCircleFlowerBush(95, 380)
drawCircleFlowerBush(30, 395)


# Flower Petals
Star(30,360,12,5,roundness=60, fill='pink')
Star(50,350,12,5,roundness=60, fill='pink')
Star(70,360,12,5,roundness=60, fill='pink')
Star(85,360,12,5,roundness=60, fill='pink')
Circle(30,360,5, fill='yellow')
Circle(50,350,5, fill='yellow')
Circle(70,360,5, fill='yellow')
Circle(85,360,5, fill='yellow')


# Define the onMousePress function to apply mouse press actions
# Key part of the program
def onMousePress(mouseX, mouseY):
    sun.visible = False
    sunPart.visible = False
    moon.visible = True
    app.background = fill=rgb(4, 26, 64)
    window.fill = 'yellow'
    window2.fill = 'yellow'
    mountain.fill = 'grey'
    mountain2.fill = 'grey'
    grass.fill = rgb(11, 61, 46)
    grass2.fill = rgb(11, 61, 46)
    currentTime.value = "Current Time: 2:30 AM"
    currentTime.fill = 'white'


# Define the onMouseRelease function to apply mouse release actions
# Another key part of the program
def onMouseRelease(mouseX, mouseY):
    sun.visible = True
    sunPart.visible = True
    moon.visible = False
    app.background = 'skyBlue'
    window.fill = 'black'
    window2.fill = 'black'
    mountain.fill = gradient('deepSkyBlue', 'royalBlue', start='top')
    mountain2.fill = gradient('deepSkyBlue', 'royalBlue', start='top')
    grass.fill = rgb(142, 252, 0)
    grass2.fill = rgb(142, 252, 0)
    currentTime.value = "Current Time: 7:55 AM"
    currentTime.fill = 'black'

cmu_graphics.run()