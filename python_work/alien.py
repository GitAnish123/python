""" Consider a game featuring aliens that can have different colors and point values.
This simple dictionary stores information about a particular alien:"""
# For example, 

alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])


""" A dictionary in Python is a collection of key-value pairs.
Each key is connected to a value, and you can use a key to access the value associated with that key. 
A key's value can be a number, a string, a list, or even another dictionary. 
In fact, you can use any object that you can create in Python as a value in a dictionary."""

""" In Python, a dictionary is wrapped in braces ({})
with a series of key-value pairs inside the braces, as shown in the earlier example: """
# The simplest dictionary has one point value.
alien_0 = {'color': 'green'}

alien_0 = {'color': 'green'}
print(alien_0['color'])
# An example to access values in dictionary.
# Lets use a real-world situation.

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
# You can add key-value pairs,
# for example,

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# We do the "key" = "value" method.
# You can also add key-values by starting with an empty list

""" For example """
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# That is how you add the point values.
""" You can also modify point-values too! """
""" You basically replace the existing value with the new one! """
# For example,

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
# That is how you modify a dictinary.


""" For a more interesting example, let's track the position of an alien that can move at different speeds.
We'll store a value representing 
the alien's current speed and then use it to determine how far to the right the alien should move: """


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment


print(f"New position: {alien_0['x_position']}")

""" That is an excellent example!!! """

# You can remove key-values too!
# You can use the "del" statement to delete it permenently!
# If you want to use that key-value later on, use the "pop()" method.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# That is a really good example. To pop it...
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0.pop('points')
print(alien_0)

""" That is how you pop values. """



# You can use the "get()" method to retrieve values that don't exist in the key!
# This can be a common error,
""" alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points']) """
# That is an error, because "points" does not belong in that dictinary.
# You can use the "get()" method to make a second result!
# Assign a variable too it too!

# For example,
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
# You will get a message, that there is no value assigned!