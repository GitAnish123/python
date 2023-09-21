age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are to young to vote.")
    print("Please register as soon you turn 18 years old!")
# This is an 'if-else' statement. This is very useful.
# This is good for TWO results.

age = 21
# Determining the cost of a person to pay for entering an amusement park.
if age <= 12:
    print("Your admission fee is $59.99")
elif age <= 24:
    print("Your admission fee is $119.99")
elif age <= 70:
    print("Your admission fee is $349.99")
else:
    print("Your admission fee is $399.99")

print("Also, Parking fee is $25")
# This is the "if-elif-else" chain.

age = 39

if age < 10:
    price = 30
elif age < 20:
    price = 60
elif age < 50:
    price = 150
else:
    price = 255
print(f"Your admission is ${price}")
# This is a much consise way to do it.

# This code produces the same output as the previous example, but the purpose of the if-elif-else chain is narrower.
# You could add as many "elif" blocks or you can just add one 'elif' block.
# You don't need to always include the 'else' block. Here is an example of omiting an else block.

age = 39

if age < 10:
    price = 30
elif age < 20:
    price = 60
elif age < 50:
    price = 150
elif age >= 51:
    price = 255
print(f"Your admission is ${price}")

"""EXTRA       PRACTICE      !!!!!"""


# Imagine an alien got shot down
alien_color = 'green'
if alien_color == 'green':
    print("You earn 5 points!")

if alien_color != 'green':
    print("You lost 10 points!")
if alien_color == 'red':
    print("You lost 5 points!")

alien_color = 'green'
if alien_color == 'orange':
    print("You earned 5 points for shooting the alien!")
else:
    print("You earned 10 points for shooting a special alien!")

alien_color = ('yellow')
# The points are for shooting aliens

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earn 10 points!")
else: # If the alien is red???:
    print("You earn 15 points!")

persons_age = 50
# Stages of life examples

if persons_age < 2:
    print("You are a baby.")
elif persons_age < 4:
    print("You are a toddler.")
elif persons_age < 13:
    print("You are a kid.")
elif persons_age < 20:
    print("You are a teenager.")
elif persons_age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

favorite_fruits = ['strawberries','blackberries','bananas']

if 'bananas' in favorite_fruits:
    print("Bananas are one of my favorite fruits.")
if 'blueberries' in favorite_fruits:
    print("\nBlueberries are one of my favorite fruits.")
if 'strawberries' in favorite_fruits:
    print("\nStrawberries are one of my favorite fruits.")
if 'blackberries' in favorite_fruits:
    print("\nBlackberries are one of my favorite fruits.")
if 'watermelon' not in favorite_fruits:
    print("\nWatermelon is not one of my favorite fruits.")

# These are the practice examples of the topic we learned, 'if' statements



# --------------- PRACTICE IS OVER ------------------ #
"""   Real lesson now starts. Practice is over!!!    """



# Lets use the "int()" function while doing user input!" 
# For example, in an amusement park, we need to check if a person can ride a particular ride...


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")