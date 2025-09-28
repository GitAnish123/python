import cmu_graphics
from cmu_graphics import *


"""
Code Result: Dynamic Paintbrush that draws on the screen while dragging on the mouse.
The faster you drag, the more red and bigger size, the slower you drag, the more blue and smaller size
"""




# Define my own clamp() function since clamp() is not built in
# Clamp is when if a number is too small, it sets to the minimum, if too big, sets to maximum
# If it is within range, it stays the same
# The clamp() function limits the number to stay within a certain range
# It prevents the brush from getting too big or small, and makes sure the color values are in RGB range always (0, 255)
# For example, in a vending machine, if it has snacks numbered 1-10, but you choose snack 12...
# it gives you the closest valid one, #10.
def clamp(value, minVal, maxVal):
    if value < minVal:
        return minVal
    elif value > maxVal:
        return maxVal
    else:
        return value


# Variables to track the previous mouse position
app.prevX = None
app.prevY = None


# Define the onMouseDrag function
def onMouseDrag(x, y):
    # Use previous coordinates to determine speed
    if app.prevX is not None and app.prevY is not None:
        dx = x - app.prevX
        dy = y - app.prevY
        speed = (dx**2 + dy**2) ** 0.5
        
        # Map speed to brush size (clamped between 2 and 30)
        brushSize = clamp(speed * 1.5, 2, 30)
        
        # Map speed to color (faster = redder, slower = bluer)
        red = clamp(int(speed*10), 0, 255)
        blue = 255-red
        
        
        # Draw a circle at current location with dynamic size and color
        Circle(x, y, brushSize, fill=rgb(red, 0, blue), opacity=70)
        
    # Update previous position
    app.prevX = x
    app.prevY = y


# Define the onMouseRelease function
def onMouseRelease(x, y):
    # Reset when the mouse is released
    app.prevX = None
    app.prevY = None