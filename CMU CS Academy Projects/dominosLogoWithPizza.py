import cmu_graphics
from cmu_graphics import *

"""
Code Result: The Dominos Logo with a pizza
"""

# Draw a plain white background
Rect(0, 0, 400, 400, fill='white')

# Draw the blue side of the domino
RegularPolygon(150, 222, 55, 4, fill=rgb(11, 110, 143))
Circle(127, 222, 15, fill='white')
Circle(166, 222, 15, fill='white')

# Draw the red side of the domino
RegularPolygon(209, 163, 55, 4, fill=rgb(226, 23, 55))
Circle(209, 163, 15, fill='white')

# Draw the trademark symbol (TM)
Label('TM', 180, 272, fill=rgb(11, 110, 143), size=15)

# Draw Domino's label
Label("Domino's", 200, 343, fill=rgb(11, 110, 143), size=70, font='montserrat', bold=True)

# Draw the registered trademark symbol (®)
Circle(376, 329, 5, fill=None, border=rgb(11, 110, 143), borderWidth=1)
Label("R", 376, 329, size=6, fill=rgb(11, 110, 143))

# Draw a box that contains the pizza using lines
Line(270, 0, 270, 125, lineWidth=4)
Line(270, 125, 400, 125, lineWidth=4)
Line(400, 125, 400, 0, lineWidth=4)
Line(400, 0, 270, 0, lineWidth=4)

# Draw the pizza that is inside the box including the crust (assume cheese is ALREADY in the pizza)
Polygon(290, 10, 330, 115, 380, 10, fill=gradient(rgb(219, 162, 74), rgb(255, 241, 215), start='top'))
Line(292, 15, 378, 15, opacity=50, lineWidth=1)

# Draw the pizza toppings (Pepperoni, olives, peppers)
Circle(320, 32, 10, fill=gradient(rgb(181, 42, 4), rgb(225, 35, 1)))
Circle(332, 65, 10, fill=gradient(rgb(181, 42, 4), rgb(225, 35, 1)))
Circle(353, 24, 5, fill=gradient(rgb(181, 42, 4), rgb(225, 35, 1)))
Rect(340, 40, 15, 8, fill='green')
Rect(327, 85, 6, 12) 