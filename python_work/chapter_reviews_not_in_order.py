aliens = ['bob','jon','ben']
for alien in aliens:
    print(alien.title())
aliens = ['bob','jon','ben']

alien_game_name = 'alien war'

for alien in aliens:
    print(f"{alien.title()} is one of the three deadliest aliens in this game.")
    print(f"If you lose to {alien.title()}, we all can understand why!\n")
print(f"Make sure you try hard to win against these aliens to beat {alien_game_name.upper()}!!!\n")

for value in range(1,1_001):
    print(value)

five_thousand = list(range(1,5_000)) # range() and list() are all functions
# Make result into list and there should be a variable.
print(five_thousand)

skipping_and_counting_by_fours = list(range(4,101,4))   # Counting evenly by 4s
print(skipping_and_counting_by_fours)
squares = []

for value in range(1,101):
    square = value**2
    squares.append(square)
    # squaring numbers from one to hundred by doing the "for" loop
# We multiply every value to the power of 2.

print(squares)
# printing squares from one to one_hundred
scores_on_math_test_1stSemester = (82,94,100,98,99,99,91,92,92,91,83,79,100,94,92,99,80,95,93,91,82,71,74,70,74,77,97,90)

print(min(scores_on_math_test_1stSemester))
print(max(scores_on_math_test_1stSemester))
print(sum(scores_on_math_test_1stSemester))
print(len(scores_on_math_test_1stSemester))
# Simple statical problems
# Lets find average of all scores using the data we have!
print(2479/28)
# The average equals about "89"

estimate_average_of_all_scores = 89
print(estimate_average_of_all_scores)
squares = [value**2 for value in range(1,101)]
print(squares)  # Easiest way to print the squares or any other one. (This is a comprehension list)

aliens = ('bob','jon','ben')
print(aliens[-2:2])
# Example of slicing a list
level_one_all_aliens = ['peter','joseph','bristol','parker','ben','juice','sophia','isabella','bob','jon','charlotte']
# These are all the aliens in ALIEN WAR

print("These are the names of the first five aliens in this level")
for level_one_all_alien in level_one_all_aliens[:5]:
    print(level_one_all_alien.title())
# printed first five aliens

print("These are the names of the rest of the aliens in this level")
for level_one_all_alien in level_one_all_aliens[5:11]:
    print(level_one_all_alien.title())
    print(f"{level_one_all_alien.title()}, you are the last but not the weakest!\n")
# printed last six lines + xtra msg

my_books = ['percy jackson','diary of a wimpy kid','the BFG','story thieves']
# List of books a kid has in his house
brothers_books = my_books[:]
# List of books of the kid's brother has in his house
# We added a copy of that list and added a slice to not SYNC the list.

print(my_books)
print(brothers_books)
my_books.append('two degrees')
brothers_books.insert(4, 'across the desert')
print(my_books)
print(brothers_books)
# Lets see what happens if you don't add a slice.

my_books = ['percy jackson','diary of a wimpy kid','the BFG','story thieves']
brothers_books = my_books
my_books.insert(4, 'two degrees')
brothers_books.append('across the desert')
print(my_books)
print(brothers_books)
# This is different, the two lists SYNC with each other and they will associate with every modify, adding, and removing.

my_houses_size = (3102, 2948, 7056)
for my_house_size in my_houses_size:
    print(my_house_size)
#   OR   #
my_houses_size = (3102, 2948, 7056)
print(my_houses_size[0])
print(my_houses_size[1])
print(my_houses_size[2])

print(my_houses_size)  # This is in a "list" format
# You cannot modify, add, or remove elements in a Tuple, but instead you can...

my_houses_size = (3102, 2948, 7056)
print("Original Dimensions:")
print(my_houses_size)
my_houses_size = (3103, 2951, 7040) # Typing errors
print("\nModified Dimensions:")
print(my_houses_size) # I just changed the value, and this can never be illigal in Python.

first_name = 'anish'
last_name = 'pasumarthi'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
greeting = f"Hello, {full_name.title()}"
print(greeting)
# printing a greeting using first + last names.
print(f"Hello,\nI want to guess your name because I think...\tI forgot it!\n\tIs your name {full_name.title()}???")

favorite_food = '   pizza'
print(favorite_food)
print(favorite_food.lstrip())  # You can also do "rstrip()" to strip right side and "strip()" to strip both sides.
amazon_url = 'https://www.amazon.com'
print(amazon_url.removeprefix('https://www.'))
simple_url = f"{amazon_url.removeprefix('https://www.')}"
print(simple_url)
favorite_food_noError = f"{favorite_food.lstrip()}"   # Making values permenanyt instead of temperary use.
print(favorite_food_noError)
# Use double quotation marks if you are using appostrophies.

print(2+5)
print(2-91/4*91)
print(2.0*8.1)
print(2**5)

MAX_CONNECTIONS = '40_000 a time'
print(MAX_CONNECTIONS)
x,y,z = 3,10,3
print(x)
print(z)
print(y)
# This line is a comment


board_games = ['monopoly','sequence','the game of life','chutes and ladders']  # (lists)
print(board_games)
print(board_games[0])
print(board_games[-2])
print(board_games[3].title())
print(f"My favorite board game when I was a little boy was {board_games[-2].title()}.")
board_games = ['monopoly','sequence','the game of life','chutes and ladders']


board_games[1] = 'uno'
# This is modifing a list
print(board_games)
board_games = ['monopoly','sequence','the game of life','chutes and ladders']
board_games.append('risk')  # We are now adding elements in a list
print(board_games)
board_games.insert(4, 'chess')
print(board_games)


# Lets now remove elements in a list!
del board_games[-3]
print(board_games)
popped_game = board_games.pop()
print(board_games)
print(popped_game)

my_own_popped_game = board_games.pop(1)
print(board_games)
print(my_own_popped_game)  # We are popping elements, now lets use them in a sentence.
print(f"\nI really hate {my_own_popped_game.title()} and {popped_game.title()},\n\t so now I don't play them any more.")

board_games.remove('chess')
print(board_games)
board_games = ['monopoly','sequence','the game of life','chutes and ladders']  # (lists)
board_games.sort()
print(board_games)
board_games.sort(reverse=True)
print(board_games)
# sorting out the board games in alphebetical order

# now I use the "sorted()" function to sort!

board_games = ['monopoly','sequence','the game of life','chutes and ladders']  # (lists)
print("\nHere is the original list:")
print(board_games)
print("\nHere is the sorted list:")
print(sorted(board_games))
print("\nHere is the reverse of the sorted list:")
print(sorted(board_games, reverse=True))
board_games = ['monopoly','sequence','the game of life','chutes and ladders']  # (lists)

board_games.reverse()
print(board_games)
# We reversed the list completely
print(len(board_games))

# Make sure you know the "len()" function
# Make sure to know the Zen of Python
# If you type in the terminal "import this" you will see the poem
# Make your code easy as possible
# Make sure to style your code always.


""" An if statement is a programming conditional statement that allows a program to make decisions """
# Lets do a simple example.

cars = ['audi','bmw','subaru','toyota']
# We have to 'case' these cars, because we need proper grammer.
""" For example """
car = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# We added the 'for' loop first, to seperate the list. Next we did an 'if' statement, if it's True, it will do an action.
# If it is false, it will do a seperate action too!

""" At the heart of every if statement is an expression - 
          that can be evaluated as True or False and is called a conditional test. """

# If it's true, Python executes the code. If false, Python ignores the code.
# For example, 

car1 = 'audi'
car2 = 'bmw'
car3 = 'subaru'
car4 = 'toyota'


car2 = 'bmw'
print(car2 == 'bmw')


car2 = 'bmw'
print(car1 == car2)
print(car2 == 'audi')


# Python is also case sensitive too
car3 = 'subaru'
print(car3 == 'Subaru')

""" instead... """

car3 = 'subaru'
print(car3.title() == 'Subaru')
# also you can use the inquality sign (!=)

car4 = 'toyota'
print(car4 != 'audi')

# This is a true test!
# You also can set a real life situation, like if a person did not order a topping...


requested_topping38193173 = 'anchovies'
print(requested_topping38193173)
if requested_topping38193173 == 'anchovies':
    print("This is the right customer, you may give him the topping!")
# Lets do another example...


requested_topping38193173 = 'anchovies'
print(requested_topping38193173)
if requested_topping38193173 != 'yellow peppers':
    print("Hold the yellow peppers, this is the wrong customer!")

# Numerical expressions are very important too!
# Tesing numerical expressions are pretty straightforword!

age102123874956478562846123940123840123675294 = 291
print(age102123874956478562846123940123840123675294 == 291)
# Python returns 'true'
print(age102123874956478562846123940123840123675294 != age102123874956478562846123940123840123675294)
# Python returns 'false'


math_homework_answer782 = '21'
if math_homework_answer782 != '78':
    print("This is the wrong answer, please try again!")

# Lets do another example!
math_homework_answer781 = 56
if math_homework_answer781 == 56:
    print("You are correct!")
# Lets see an examples with 'comparsion operators'


age102123287956478562916123940123840123670000 = 99
print(age102123287956478562916123940123840123670000 < 100)

age102123287956478562916123940123840123670000 = 99
print(age102123287956478562916123940123840123670000 > 100)

age102123287956478562916123940123840123670000 = 99
print(age102123287956478562916123940123840123670000 <= 100)

age102123287956478562916123940123840123670000 = 99
print(age102123287956478562916123940123840123670000 >= 100)

""" Sometimes you might want to check multiple conditions. """
# We can use "and" and "or"
# For example...


print(age102123287956478562916123940123840123670000 < 99 and age102123287956478562916123940123840123670000 > 99)
print(age102123287956478562916123940123840123670000 == 99 and age102123287956478562916123940123840123670000 > 81)
print(age102123287956478562916123940123840123670000 > 100 or age102123287956478562916123940123840123670000 >= 109)
print(age102123287956478562916123940123840123670000 < 109 or age102123287956478562916123940123840123670000 < 91)
# You also can use parenthesis to make iot easier to read.
# For example,
print(age102123287956478562916123940123840123670000 < 100) and (age102123287956478562916123940123840123670000 <= 100)
""" this gives the same result too! """


# Sometimes you need to know if an item is in a list!
# We could use 'in' to check.
# For example...

requested_toppings = ['mushrooms','olives','pepperoni']


""" Using the elements in the lists... """
print('mushrooms' in requested_toppings)
print('tomatoes' in requested_toppings)
print('pepperoni' in requested_toppings)
# Lets use an 'if' statement to check too!.


banned_users = ['andrew','carolina','david']
user = 'marie'
# use the keyword, "not in"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish!")

""" OR  """

banned_users = ['andrew','carolina','david']
print(banned_users)
if 'andrew' in banned_users:
    print(f"{banned_users[0].title()}, you can not enter because you are banned!")
# Boolean expressions are another name of conditional testing. The values are either "true" or 'false'
# For example,

game_active = True
can_edit = False

# Since we know about conditional testing, we can move on to 'if' statements.
# There are several kinds of "if" statements.
# Here is an example of an easiest one!

age192901223331291032913382139218732431473621452 = 19
if age192901223331291032913382139218732431473621452 >= 18:
    print("You are old enough to vote!")
""" This is an example of voting. As a fact, you cannot vote unless if you are 18 years or above."""
# This is similar to conditional testing
# If test passes, it executes. if not, it will be ignored.
# Add as many lines as you want
# Another example using "if" and "else"

age832183794762859 = 17
if age832183794762859 >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    # This is an 'else' statement. It will be used if the 'if' statement did not pass!
    print("Sorry you are young to vote!")
    print("Please register to vote as soon you turn 18.")
# This is used to test "two" situations

""" Sometimes you might need to test more than two situations. """
""" You can use an (if, elif, else) chain."""
# elif stands for --- else if
# for example...

age9999912939281 = 12
if age9999912939281 < 4:
    print("Your admission is $5")
elif age9999912939281 < 18:
    print("Your admission is $20")
elif age9999912939281 < 36:
    print("Your admission is $40")
else:
    print("Your admission is $100")
print("Parking tickets are $15 extra")

# This is an amusement park entry pricing.
# You can keep how many "elif" blocks or just one elif block.
# Another easier example,

age9999912939281 = 12
if age9999912939281 < 4:
    price = 10
elif age9999912939281 < 16:
    price = 40
elif age9999912939281 < 40:
    price = 100
else:
    price = 150
print(f"Your admission is ${price}.")

# You don't always have to include the "else" block.
""" you can remove the else block if you want and if it's appropriate! """
""" for example, """

age9999912939281 = 12
if age9999912939281 < 4:
    price = 20
elif age9999912939281 < 16:
    price = 80
elif age9999912939281 < 40:
    price = 200
elif age9999912939281 >= 40:
    price = 250

print(f"Your admission is ${price}.")

""" This is how you do it! """
""" Sometimes it is not appropriate to use the (if, elif, else) chain when you are testing multiple conditions. """
# For example, lets see if we have items in a list using the 'if' statement.

requested_toppings2 = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings2:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings2:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings2:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# This is a great way to check if an item is in a list or not. 
# But this code will not work properly if we use an (if, elif, else) chain.
""" For example,"""


requested_toppings2 = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings2:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings2:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings2:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

""" The reason it is not working because the "if mushrooms" one is already executed and Python doesn't check any more
code after when a code is executed. """

# Now lets learn to use "if" statements in lists!!!
# Below, is a code that is pretty straightforward.
requested_toppings3 = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings3:
    print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

""" What if the pizzeria runs out of green peppers???
An 'if' statement will handle this situation appropriatly. """


requested_toppings3 = ['mushrooms','green peppers','extra cheese']
print(requested_toppings3)

for requested_topping in requested_toppings3:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")
# This is a great way to handle these cases effientily.
# Lets say if somebody doesn't want toppings
""" We can ask if they wan't a plain pizza. """
requested_toppings4 = []
if requested_toppings4:
    for requested_topping in requested_toppings4:
        print(f"Adding {requested_toppings4}")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# What we did is we put an empty list
# Next, instead of jumping into a "for" loop, we did a quick test first. (If there is any toppings...)
""" When the name of the list is used by an 'if' statement, Python returns 'True'.
An empty list evaluates to 'False'. """

# If "requested_topping4" passes the test, we run the same loop as the previous examples.
# Otherwise, we ask the customer if he wants a plain pizza.

""" People can ask for anything!!!, especially when it comes to pizza. """
""" What if a customer asks for french fries????? """
# We have to add a list of the toppings avaliable so the code will check against the list of toppings available.
# After when it is checked, it will tell if a pizzeria doesn't have the requested_toppings.
""" For example... """

available_toppings = ['mushrooms','olives','green peppers','pepperoni','extra cheese']
requested_toppings5 = ['mushrooms','french fries','extra cheese']
print(available_toppings)
print(requested_toppings5)

for requested_topping in requested_toppings5:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}")
print("\nFinished making your pizza!")

# We first added a list of the requested_toppings and the available_toppings.
""" Next, we did a loop to seperate the toppings and did an 'if' statement to check if any requested_toppings is
inside the list of available_toppings. """
# if the elements are matching in both lists, it will add that topping.
# if the test did not pass, it will print a statement that the topping is not available.


""" Make sure to style your statements """
# The only recommendation is styling conditional tests is to use a single space around comparison operators.
# such as ==, >=, and <=
# spacing does not affect the code, it just makes it easier to read.

""" MAKE SURE YOU DO THIS PROPERLY. """

""" Now moving on to chapter 6 in python. """

# Dictinoary's allow python to connect infortmation
# Here is a simple example

alien_0 = {"color":"green", "points":5}
# That is the dictionary's key-values
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
# we printed the key!
# another example,


alien_0 = {'color':'green', 'points':5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# To add key-values...
alien_0 = {'color':'green', 'points':5}
print(alien_0)
print("...")

alien_0['x_position'] = 0
alien_0['y_postition'] = 2
print(alien_0)
# Add from an empty list!

alien_0 = {}
alien_0['x_position'] = 15
alien_0['y_postition'] = 1000
print(alien_0)



# modifying dictionaries...
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# Interesting example

alien_0 = {'x_position': 2, 'y_position': '27', 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Here is the part...
if alien_0['speed'] == 'slow':
    x_increase = 1.2
elif alien_0['speed'] == 'medium':
    x_increase = 2.4
else:
    x_increase = 3.6


alien_0resultposition = alien_0['x_position'] + x_increase
print(f"New position: {alien_0resultposition}")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# You can list a dictinary in a different format
# for example,

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ellie': 'javascript',
    'edward': 'rust',
    'phil': 'python'
}
# Lets do an example



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ellie': 'javascript',
    'edward': 'rust',
    'phil': 'python'
}

language3 = favorite_languages['ellie']
language1 = favorite_languages['jen']
print(f"Ellie's favorite language is {language3.title()}!")
print(f"Jen's favorite language is {language1.title()}!")

# Normally, if you print the wrong key-value, you get an error
# If you use the "get()" method, you can change that.
# For example,


alien_0 = {'color': 'green', 'speed': 'slow'}
error_point_value = alien_0.get('points', 'No point value assigned.')
print(error_point_value)
# You should not get the corrsuponding value!

""" Now lets learn how to loop a dictionary. """
# One case is if you want to loop the key and the value.
# For example,

animals = {
    'common_pet1': 'dog',
    'wild cat':'tiger',
    'common_pet2': 'cat',
    'air_pet': 'bird',
    'water_pet': 'fish',
}

for key, value in animals.items():
    print(f"\nCategory: {key}")
    print(f"Animal: {value}")

# We printed the key and the value including looping.
# Now lets loop only the keys.
# We'll do a couple of examples this time...
# For example,


animals = {
    'common_pet1': 'dog',
    'wild cat':'tiger',
    'common_pet2': 'cat',
    'air_pet': 'bird',
    'water_pet': 'fish',
}
for category in animals.keys(): 
# you don't have to add the ".keys()" it is optional!
    print(f"\n{category}")

# Lets do another example...



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ellie': 'javascript',
    'edward': 'rust',
    'phil': 'python'
}
friends = ['phil','ellie']
for name in favorite_languages.keys():
    print(f"\nHi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# Lets check if another friend, olivia, did the favorite_languages poll.
# for example, (use the "keys()" method!)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ellie': 'javascript',
    'edward': 'rust',
    'phil': 'python'
}
if 'olivia' not in favorite_languages.keys():
    print("Olivia, please take our poll!")

# You can also sort your dictionaries using the "keys()" method!
""" For example, """

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ellie': 'javascript',
    'edward': 'rust',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll!")

# Lastly, lets now learn how to loop only the values.
# Use the "values()" method!
# for example...

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ellie': 'javascript',
    'edward': 'rust',
    'phil': 'python'
}
print(f"The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# This will be ok for a small set of values, but if it is a bigger set, you may not want repeatition.
# You can use a set.
# A set is a collection in which each item should be unique.
""" here is how you build a set
languages = {'python','rust','c'}   """
# That is an example shown above!

# Here is an example of how to do this with a set!
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ellie': 'javascript',
    'edward': 'rust',
    'phil': 'python'
}
print(f"The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Now we have all unique values and you can use 'sets' anytime when it is approproiate.

# Now we are now currently in the NESTING unit in chapter 6!
# Lets learn how to keep dictionaries in a list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Lets do a more realistic example
# for example,

# Empty list for storing aliens
aliens = []
for alien_number in range(30):
    # Make 30 green aliens
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)
# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# Print how many aliens are there
print(f"Total amount of aliens: {len(aliens)}")

# Lets do another interesting example.
# Lets extend this code

aliens = []
for alien_number in range(30):
    # Make 30 green aliens
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        # Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# Print how many aliens are there
print(f"Total amount of aliens: {len(aliens)}")

# Lets expand this code one more time. This time, things get interesting.
# For example,

aliens = []
for alien_number in range(30):
    # Make 30 green aliens
    new_alien = {
        'color': 'green', 
        'points': 5,
        'speed': 'medium',
    }
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
for alien in aliens[3:5]:
    alien['color'] = 'red'
    alien['speed'] = 'fast'
    alien['points'] = 15
    # This is the most hardest alien to defeat!
# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# Print how many aliens are there
print(f"Total amount of aliens: {len(aliens)}")

""" This is a pretty wild example! """

# Now lets learn to nest lists in dictionaries.
# Here is a simple example,


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}- crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# Again, this is a simple pizzeria example
# Here is a little more complex example.

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['C'],
    'ellie': ['javascript', 'lua'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language(s) are:")
    for language in languages:
        print(language.title())
print("As for the information shown above, Python and Rust are the two favorable languages in the poll!")

# That is a little complex example, but you should understand it by looking at it step by step.
# Finally, the last topic is how to nest a dictionary inside another dictionary!!!
# Here is one example of how you do it. Things get really complex and difficult.
# For example, lets print two new-coming users and print some basic information about them


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    print(f"First name: {user_info['first'].title()}")
    print(f"Last name: {user_info['last'].title()}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    print(f"\tFull name: {full_name}")
    print(f"Location: {user_info['location'].title()}")


# That is one complex way to representing a tutorial of nesting a dictionary inside another one.






# Lets learn about user input!
# This will make your code exciting and good!
# Lets do a copycat program...
# For example...
prompt1 = input("Tell me something and I will repeat it back to you!: ")
print(prompt1)




# We can also use the variable you assigned to the prompt
# The value use used for the user input at the previous program is the value of the "prompt1"!
# Here is an example of how to use it.


prompt2 = input("Please enter your name: ")
print(f"\tHello {prompt2}")





# You can add multiple lines to your user input, but the last line will do the actual input:
# For example...



prompt3_0 = "If you share your name, we can personalize the messages you see!"
prompt3_0 += "\nWhat is your first name? "
full_prompt_3 = input(prompt3_0)
print(f"Hello, {full_prompt_3}")





# If you want to add multiple lines with MULTIPLE INPUTS...
# Here is an example... (use the amount of input functions for number of inputs)


prompt3_5 = input("If you share your name, we can personalize the messages you see. Type anything to continue!")
prompt3_8 = input("What is your first name? ")
print(f"Hello, {prompt3_8}")





""" The input function takes every user input as a string. If you enter a number, suppose 5. 
The function will be taking that number as this: '5'  """
# So if you are working with numbers, you can use the "int()" function to convert the string into an integer!!!
# Here is an example of how the input function handles numbers!!! For example,




age = input("How old are you? ")
print(age)
# This will work ok but if you compare it to a number using a comparsion operator, you will get an error
# If you want to physically change an "str" number into a normal number that python understands, use the int function.
# Here is a following example,

age = input("How old are you")
age = int(age)
print(age >= 18)
# This will be marked as True or False depending on the age you entered.
""" This will work, but if you omit the second line, this code will not work at all as it will say it can't compare
str and int  """





# Here is a other example involving numbers and the "input()" function.
# We need to determine if a person can go on a specific ride...
height = input("How tall are you, in inches")
height = int(height)
if height >= 48:
    print("You are tall enough to go on the ride!")
else:
    print("Sorry, you can ride when you get taller.")





# Lastly, you can use the modulo operator to find the remainders of a pair of numbers.
# Remember, it won't give you the quotient, it will give you the remainder.
# Here are some examples of how to use it!
print(4%3)
print(5%9)
print(10%2)
print(1%1)
print(0%6)
print(5%2)




# Lets use it on an actual program of determining a number is even or odd...
# For example...
even_or_odd = input("Enter a number and I will determine if that number is even or odd:  ")
number = int(even_or_odd)
if number % 2 == 0:
    print("The number you entered is even!")
else:
    print("The number you entered is odd!")





# Lets learn about "while" loops
# These loops run forever if the condition is True and until the condition is False
# Learn more about it in my notes...
# Here is a basic example of a "while" loops program...

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# This program just basically prints numbers from 1-5
# while conditioning makes the numbers generate until numbers reach 5 and it prints that last number
# The current_number will also increase by 1




# Here is some examples of a copycat program but you can let the user choose when to quit:
# There are 3 examples
# The first one is pretty straightforward
# The second one has a flag and that flag will make the code run until when the flag is set to False. see notes for more...
# The third one uses the "break" statement and it will use the loop, "while True". To stop it, we use the "break" statement
# See notes for any of the information!!!
# Below is the first example...





# while loops conditioning
prompt4 = "Tell me something and I will repeat it back to you."
prompt4 += "\nEnter 'quit' to stop the program."
setofquotes = ""
while setofquotes != "quit":
    setofquotes = input(prompt4)
    if setofquotes != "quit":
        print(setofquotes)




# flag example
prompt4_3 = "Tell me something and I will repeat it back to you."
prompt4_3 += "\nEnter 'quit' to stop the program."
code_active = True
while code_active:
    quotes = input(prompt4_3)
    if quotes == "quit":
        code_active = False
    else:
        print(quotes)




# using the break statement
prompt4_7 = "Tell me something and I will repeat it back to you."
prompt4_7 += "\nEnter 'quit' to stop the program."
while True:
    quotes = input(prompt4_7)
    if quotes == "quit":
        break
    else:
        print(quotes)




# You can do any kind of example you want.
# Here is a different kind of example...
prompt5 = "\nEnter a name of a city you visited"
prompt5 += "\nEnter 'quit' when you are completely finished: "
while True:
    quotes = input(prompt5)
    if quotes == "quit":
        break
    else:
        print(f"I would like to visit {quotes.title()}")




# Lets use the "continue" statement in this example
# We can do an example printing the odd numbers from 1-10.
# For example,
secondnumber = 0
while secondnumber <= 10:
    secondnumber += 1
    if secondnumber % 2 == 0:
        continue
    else:
        print(secondnumber)





# Make sure to avoid infinite loops
# These loops will always run forever and never stop
# Every programmer writes these loops by accident
# Here is an example of an infinite loop...
""" 
x = 1
while x <= 5:
    print(x)
"""
# (I just put the loop on the comment so it won't affect the rest of the code)



# Lets use "while" loops in lists & dictionaries
# An example is when you want to move items from one list to another
# Lets do one example when we move some uncomfired users to a list of comfirmed users...
# For example,
unconfirmed_users = ['alice', 'joey', 'elsa']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print(f"\nThe following users have been verifyed: ")
for user in confirmed_users:
    print(user.title())
# We basically moved the people from the unconfirmed list to the confirmed list




# If you want to remove specific elements from a list, you can use the "remove()" method!
# For example, lets remove all of the elements, cat
pets = ['dog', 'cat', 'parrot', 'dog', 'cat', 'rabbit', 'cat', 'dog', 'dog', 'cat', 'parrot', 'fish', 'rabbit', 'cat', 'dog']
while 'cat' in pets:
    pets.remove('cat')    # This should successfully remove all of the 'cat' from the list, "pets"




# Finally, to finish "while" loops and user input, we can use this information in dictionaries!!!
# Lets make a poll about which mountain you want to visit later in life and make other people respond and poll results
responses = {}
polling_active = True
while polling_active:
    promptNAME = input("What is your name?: ")
    promptRESPONSE = input("What mountain would you like to climb someday?: ")
    responses[promptNAME] = promptRESPONSE
    respond_again = input("Do you want to respond again?: ")
    if respond_again != "yes":
        polling_active = False
print("---Poll Results---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb the mountain, {response.title()}")




# That is an example of how to use "while" loops in a dictionary.
# Lets add a little more user input:
responses = {}
polling_active = True
while polling_active:
    promptNAME = input("What is your name?: ")
    promptAGE = input("What is your age?: ")
    promptAGE = int(promptAGE)
    promptLOCATION = input("Where do you currently live?: ")
    promptRESPONSE = input("What mountain would you like to climb someday?: ")
    responses[promptNAME] = {
        "promptAGE": promptAGE,
        "promptLOCATION": promptLOCATION,
        "promptRESPONSE": promptRESPONSE,
    }
    respond_again = input("Do you want to respond again?: ")
    if respond_again != "yes":
        polling_active = False
print("---Poll Results---")
for name, info in responses.items():
    print(f"{promptNAME.title()} would like to climb the mountain, {info['promptRESPONSE'].title()}")
    print(f"Here is some background information about the person:  He is {info['promptAGE']} years old and lives in {info['promptLOCATION'].title()}")
# These are some examples of how to apply your skills to harder topics.







# Lets learn about functions!
# These blocks of code will make your coding easier and simple to understand. More explainations throughout will be in notes.



# Lets define a simple function.
# When you define, you are creating a function that is desired to do a specific job.
# For example,

def greet_user():     # Defining the function, no extra info provided inside parenthesis.
    """Display a simple greeting"""    # Displaying a docstring to explain the function's purpose.
    print("Hello")   # This is what the function does.
greet_user()  # Now I am calling the function. It will now do the specifc job when it is runned.


# Now lets keep some information so we can use it for be effiective. That is the parameter, The value that is expected.
def greet_user(username):  # Kept information, that is the parameter.
    """Display a simple greeting"""
    print(f"Hello, {username.title()}")   # Greeting the user by its name
greet_user('Anish')  # Calling the function but creating an argument. This is what me or the user enters to call.


# If you want to keep more parameters and calling a function with two or more arguments with just that, that is called...
# Postitional arguments!!!
# For example,

def describe_pet(animal_type, pet_name):  # Multiple parameters means more information!
    """Display information about a pet."""
    print(f"I have an {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')  # Keep it in the same order. That is called postitional arguments. Keeping it in the...
# Order of the parameters.


# You can also do multiple function calls at a time!
# For example,

def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print(f"I have an {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')  # One function call
describe_pet('dog', 'willie') # Another function call


# In postitional arguments, when you call the function, keep the same order as the parameters or otherwise the code won't...
# function properly as you expect.
# For example,

def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print(f"I have an {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry', 'hamster')  # Reversed order. Output will be different and silly!


# To avoid this, use another type of arguments and that is keyword arguments. That comes in key-value pairs so no confusion.
# For example,

def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print(f"I have an {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry') # So now there is no need of ordering. You can do the other way around.


# If you use a argument more often for the parameter, use a default value so you don't have to provide it every time.
# This can help you simplify and make your code faster and easier to understand.
# Default values should always be placed at the last, after the original parameters.
# For example,

def describe_pet(animal_type, pet_name='harry'):    # Now you don't have to keep the pet name, harry! 
    """Display information about a pet."""
    print(f"I have an {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster') or describe_pet(animal_type='hamster')  # It doesn't matter which option you choose, same output.
# If you want to keep a different value, just call the function as usual for the "pet_name" and the "animal_type".


# For equivalent arguments, you can call a function however you like.
# Consider the following function definition:   def describe_pet(pet_name, animal_type='dog'):
# All the following function calls will work for this function:

# A dog named Willie.
""" describe_pet('willie')
describe_pet(pet_name='willie') """

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Avoid argument error's by keeping less or more arguments than the function expects you to keep.


# You don't always have to display the output directly like always.
# A "return" statement takes a value from inside a function and sends it back to the line that called the function.
# You need to assign a variable when you want to call a function that contains the "return" statement. 
# Here is a simple example of how return statments can be useful instead of a print statement. For example,

def get_formatted_name(first_name, last_name):
    """Display a full, neat formatted name.""" 
    full_name = f"{first_name} {last_name}"  # Assigning "full_name" to the two parameters of first & last names.
    return full_name   # Returning the specific value
my_name = get_formatted_name('Anish', 'Pasumarthi')  # Assigning the function call to a variable to use it in later use.
print(my_name)  # Print the variable to display the output.


# Lets do another example...
def get_formatted_name(first_name, middle_name, last_name):  # Created a new parameter
    """Display a full, neat formatted name.""" 
    full_name = f"{first_name} {middle_name} {last_name}"  # Added "middle_name" to include more information
    return full_name   
my_name = get_formatted_name('Anish', 'Ram', 'Pasumarthi') # Assigning function call to a variable to use it in later use.
print(my_name)


# The problem is not everybody doesn't have middle names. We can create an optional value to make 'middle_name' optional.
# For example, apply your skills you know:

def get_formatted_name(first_name, last_name, middle_name=None): # Applyed a placeholder so it has no value if left alone.
    """Display a full, neat formatted name.""" 
    if middle_name:   # If there is a middle name...  # If "middle_name" does not equal 'None'.
        full_name = f"{first_name} {middle_name} {last_name}"  # If there is a middle name, this is the value!
    else:  # If there is no middle name applied as an argument.
        full_name = f"{first_name} {last_name}"  # This is the value without the middle name included.
    return full_name     # Returning the value
my_name = get_formatted_name('Anish', 'Pasumarthi', 'Ram')  # Middle name should be placed in the last in this case 
print(my_name)
my_name = get_formatted_name('Anish', 'Pasumarthi')  # Only first & last name are only there in the arguments.
print(my_name)


# You can also use the "return" statement to return a dictionary! Here is an example that involves full names.
def build_person(first_name, last_name):
    """Display a dictionary containing a full name."""    
    full_name = {'first': first_name, 'last': last_name}   # Building a dictionary containing the parameters.
    return full_name   # Returning the dictionary
me = build_person('Anish', 'Pasumarthi')         # Providing the arguments
print(me)    # Printing variable containing the values and dictionary


# Lets say if you want to create optional values to add in your dictionary...
# Here is a simple transaction and movement of how. For example,

def build_person(first_name, last_name, middle_name=None):
    """Display a dictionary containing a full name."""    
    full_name = {'first': first_name, 'last': last_name}  
    if middle_name:   # Creating an "if" conditioning statement
        full_name['middle'] = middle_name   # Adding the "middle name" value if desired
    return full_name  # Returning whatever value you called for the function.
me = build_person('Anish', 'Pasumarthi', 'Ram')         
print(me)


# You also can inplument "while" loops with functions!
# This can help make the experience it user friendly and intresting.
# Here is an example to make a loop that allows users to quit whenever the user wants to!

def get_formatted_name(first_name, last_name):     # Defining the function and the job performing.
    """Display a full, neat formatted name.""" 
    full_name = f"{first_name} {last_name}"
    return full_name    # Returning the value from the "while" loop after defining.
while True:    #     "while" loop
    print(f"Please enter your first and last names to get a neatly formatted full name. Enter 'quit' to quit anytime.")
    first = input("What is your first name? ")   # First user input question
    if first.lower() == 'quit':    # Defining quit value
        break
    last = input("What is your last name? ")    # Other user input question
    if last.lower() == 'quit':    # Defining quit value
        break
    formatted_name = get_formatted_name(first, last)   # Creating a variable and calling the function in the loop
    print(formatted_name)   # Printing the value


# You can pass a list instead of only passing normal values.
# These can make your code effitient and quick to understand.
# You will apply lists to the code. Here is a simple example to demonstrate:

def greet_users(names):   # Defining the function
    """Greet users by its name individually in a list."""
    for name in names:    # Creating a "for" loop to access all the values in the list
        print(f"Hello, {name.title()}")   # Greeting each user in the list by saying "hello"
usernames = ['anish', 'kishan', 'sudha', 'chandra']   # List of names. Creating a list.
greet_users(usernames)    # Applying the list for the argument in the function call.


# You also can modify a list in a function. Here is an example that involves two functions that each does specific job(s).
# This contains two lists and one list of elements will be transferred into the other list with no elements inside.
# For example...

def print_and_transfer_models(unprinted_models, completed_models): # Prints the models and transferrs to completed list (1st)
    """
    Stimulate printing each design in the unprinted models list and move them into the completed models list. 
    Prints every element in the list and moves every element in the completed models list.
    """
    while unprinted_models: # There is a "while" loop in display. While there is elements in the list, "unprinted_models"...
        current_design = unprinted_models.pop()    # Pop every item in the list
        print(f"Printing design: {current_design}")   # Use the popped variable, use it to print a statement
        completed_models.append(current_design)  # Move the variable to the completed list. Repeat the same for all elements.
def show_completed_models(completed_models):  # Shows all the printed models in the completed list  (2nd function)
    """Display the completed models and print them for display! Print every element in the final, completed list."""
    print("The following models have been printed:")    # Print a statement
    for model in completed_models:    # Use a "for" loop
        print(model)   # Prints every model in the completed list
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']  # First list    (Full)  (Starting list)
completed_models = []   # Second list     (Empty)  (Complete list)
print_and_transfer_models(unprinted_designs, completed_models)    # Plugging it for the lists
show_completed_models(completed_models)    # Plugging it for the list


# If you don't want a list to be modified, (Like elements in a list being transferred to another list) create a copy!
# Lets do the same example but when we call the first function, we can add a copy for the "unprinted_designs".
# This copy will prevent the values in the list from being modified. It will create a copy and move the elements to the...
# completed list
# As a result, both lists will have the same elements inside because we are creating a copy to prevent it from modifying.
# For example, lets provide the correct demonstration:

def print_and_transfer_models(unprinted_models, completed_models): 
    """
    Stimulate printing each design in the unprinted models list and move them into the completed models list. 
    Prints every element in the list and moves every element in the completed models list.
    """
    while unprinted_models: 
        current_design = unprinted_models.pop()    
        print(f"Printing design: {current_design}")   
        completed_models.append(current_design)  
def show_completed_models(completed_models):  
    """Display the completed models and print them for display! Print every element in the final, completed list."""
    print("The following models have been printed:")    
    for model in completed_models:   
        print(model)  
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']  
completed_models = []   
print_and_transfer_models(unprinted_designs[:], completed_models)    # Creating a copy by doing this, "[:]".
show_completed_models(completed_models)
# Both lists will have the same elements inside and will be filled with the three elements for each one. Look at the output.


# Sometimes you won’t know ahead of time how many arguments a function needs to accept.
# Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.
# Here is an example that involves pizza:

def make_pizza(*toppings):   # One arbitrary argument called "toppings" that contains a tuple of all the toppings inside.
    """Print the list of toppings that have been requested.""" 
    print(toppings)   # Prints the tuple that contains the values. (toppings)
make_pizza('pepperoni')  # Contains a tuple that holds the topping, 'pepperoni', and prints the entire tuple.
make_pizza('mushrooms', 'green peppers', 'extra cheese')  # Contains a tuple that holds the toppings and prints the tuple.


# Instead we can replace the print value with the "for" loop that runs through all the values in the tuple.
# For example:

def make_pizza(*toppings):
    """Summerize a pizza that is being ordered."""
    print("Here are the toppings being requested on the pizza:")  # Message
    for topping in toppings:   #   "for" loop
        print(f"--{topping}")   # Prints every value in the tuple, "toppings"
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Learn to mix positional and arbitrary arguments. If you want a function to accept several different kinds of arguments, 
# the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.
# Here is an example:

def make_pizza(size, *toppings): # Two parameters. The first one will be the size of the pizza and the rest are in the tuple.
    """Summerize a pizza that is being ordered."""
    print(f"Making a {size}-inch pizza with the following toppings:") # Inplumenting the "size" parameter to the sentence.
    for topping in toppings:   # A "for" loop being activated
        print(f"--{topping}")  # Prints the remaining arguments that are in the tuple and prints each value inside.
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Now lets learn how to mix keyword arguments and arbitrary arguments. Sometimes you’ll want to accept an arbitrary number...
# of arguments, but you won’t know ahead of time what kind of information will be passed to the function.
# In this case, you can write functions that accept as many key-value pairs as the calling statement provides.
# Here is an example:

def build_person(first_name, last_name, **user_info): # The double astericks store the remaining arguments in a dictionary...
# that is named, "user_info". The first two parameters will not be in the dictionary, so we have to add them seperatly.
    """Describe and model a specific person by formatting a dictionary."""
    user_info['first_name'] = first_name  # Adding the first name to the dictionary
    user_info['last_name'] = last_name    # Adding the last name to the dictionary
    return user_info  # Returning the complete dictionary of all the information of one person that is provided.
my_person = build_person('Anish', 'Pasumarthi', location='Fort Mill', age=13, occupation='Doctor', hobby='basketball')
print(my_person) # Created a varibale to hold the function and it's arguments above, this line is for printing the variable.


# Now lets learn how to store your functions in modules! 
# A module is a file ending in .py that contains the code you want to import into your program. 
# An import statement tells Python to make the code in a module available in the currently running program file.
# Here is an example of how to import an entire module...

import printing_models    # Importing an example file that ends with ".py" in this directory.
printing_models.print_models(unprinted_designs, completed_models)  # Using that import to use a function
printing_models.show_completed_models(completed_models)  # Using another function.
# With that, we can use functions from another file in the same directory!


# Here is an example of how to import specific functions in a module.

from printing_models import print_models   # Importing a function using the "from" keyword
print_models(unprinted_designs, completed_models)   # Using the function directly
# We also can import many functions in a module at one time! For example,

from printing_models import print_models, show_completed_models   # Importing two/many functions!
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# We also can give a function a nickname, (alias). That will make your function calling much easier. For example:
from printing_models import print_models as pm   # Giving a nickname
pm(unprinted_designs, completed_models)  # Using the alias
show_completed_models(completed_models)  # We also can give this function an alias if we want or desired to.


# In the same way, we can give a module an alias. Here is an example...

import printing_models as p    # Giving the function an alias
p.print_models(unprinted_designs, completed_models)
p.show_completed_models(completed_models)


# You also can import all the functions in one module by using an asterick. For example,

from printing_models import *  
# Importing all the functions in the module in the line above. This is not recommended for larger modules you haven't wrote.
print_models(unprinted_designs, completed_models)  # Using one of the functions
show_completed_models(completed_models)  # Using another function.
# These are some ways to store your functions in modules, use them, and give them nicknames to call/use them easier.


# Here are some tips to style your functions:
"""
You need to keep a few details in mind when you're styling functions. Functions should have descriptive names, 
and these names should use lowercase letters and underscores. Descriptive names help you and others understand what your 
code is trying to do. Module names should use these conventions as well. Every function should have a comment that explains 
concisely what the function does. This comment should appear immediately after the function definition and use the docstring 
format. In a well-documented function, other programmers can use the function by reading only the description in the 
docstring. They should be able to trust that the code works as described, and as long as they know the name of the function, 
the arguments it needs, and the kind of value it returns, they should be able to use it in their programs.
If you specify a default value for a parameter, no spaces should be used on either side of the equal sign: The same 
convention should be used for keyword arguments in function calls:

def function_name(parameter_0, parameter_1='default value')
function_name(value_0, parameter_1='value')

PEP 8 (https://www.python.org/dev/peps/pep-0008) 
recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window. 
If a set of parameters causes a function's definition to be longer than 79 characters, press ENTER after the opening 
parenthesis on the definition line. On the next line, press the TAB key twice to separate the list of arguments from the 
body of the function, which will only be indented one level. Most editors automatically line up any additional lines of 
arguments to match the indentation you have established on the first line:

def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...

If your program or module has more than one function, you can separate each by two blank lines to make it easier to see 
where one function ends and the next one begins. All import statements should be written at the beginning of a file. 
The only exception is if you use comments at the beginning of your file to describe the overall program.
"""
# These are some tips & guidelines followed with examples to style your functions efficiently and as advanced as it will be.











# Lets learn about classes
"""
Object-oriented programming (OOP) is one of the most effective approaches to writing software. 
In object-oriented programming, you write classes that represent real-world things and situations, 
and you create objects based on these classes. 
When you write a class, you define the general behavior that a whole category of objects can have. 
When you create individual objects from the class, each object is automatically equipped with the general behavior; 
you can then give each object whatever unique traits you desire. 
You'll be amazed how well real-world situations can be modeled with object-oriented programming.
Making an object from a class is called instantiation, and you work with instances of a class. 
In this chapter you'll write classes and create instances of those classes. 
You'll specify the kind of information that can be stored in instances, 
and you'll define actions that can be taken with these instances. 
You'll also write classes that extend the functionality of existing classes, 
so similar classes can share common functionality, and you can do more with less code. 
You'll store your classes in modules and import classes written by other programmers into your own program files.
Learning about object-oriented programming will help you see the world as a programmer does. 
It'll help you understand your code—not just what's happening line by line, 
but also the bigger concepts behind it. Knowing the logic behind classes will train you to think logically, 
so you can write programs that effectively address almost any problem you encounter.
Classes also make life easier for you and the other programmers you'll work with as you take on increasingly complex 
challenges. When you and other programmers write code based on the same kind of logic, 
you'll be able to understand each other's work. Your programs will make sense to the people you work with, 
allowing everyone to accomplish more.
"""

# Lets create and use a class
"""
You can model almost anything using classes. 
Let's start by writing a simple class, Dog, that represents a dog—not one dog in particular, but any dog. 
What do we know about most pet dogs? Well, they all have a name and an age. 
We also know that most dogs sit and roll over. 
Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go in our Dog class 
because they're common to most dogs. This class will tell Python how to make an object representing a dog. 
After our class is written, we'll use it to make individual instances, each of which represents one specific dog.
"""
# Each instance created from the Dog class will store a name and an age.
# We’ll give each dog the ability to sit() and roll_over()
# Here is a simple example:

class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Stimulate sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Stimulate a dog rolling over."""
        print(f"{self.name} rolled over.")

"""
We first define a class called Dog ❶. 
By convention, capitalized names refer to classes in Python. 
There are no parentheses in the class definition because we're creating this class from scratch.
We then write a docstring describing what this class does.
A function that's part of a class is a method. 
Everything you learned about functions applies to methods as well; 
the only practical difference for now is the way we'll call methods. 
The __init__() method ❷ is a special method that Python runs automatically whenever we create a new instance based 
on the Dog class. 
This method has two leading underscores and two trailing underscores, 
a convention that helps prevent Python's default method names from conflicting with your method names. 
Make sure to use two underscores on each side of __init__(). If you use just one on each side, 
the method won't be called automatically when you use your class, 
which can result in errors that are difficult to identify. We define the __init__() method to have three parameters: 
self, name, and age. The self parameter is required in the method definition, 
and it must come first, before the other parameters. 
It must be included in the definition because when Python calls this method later (to create an instance of Dog), 
the method call will automatically pass the self argument. 
Every method call associated with an instance automatically passes self, 
which is a reference to the instance itself; 
it gives the individual instance access to the attributes and methods in the class. 
When we make an instance of Dog, Python will call the __init__() method from the Dog class. 
We'll pass Dog() a name and an age as arguments; self is passed automatically, 
so we don't need to pass it. Whenever we want to make an instance from the Dog class, 
we'll provide values for only the last two parameters, name and age. The two variables defined in the body of the 
__init__() method each have the prefix self ❸. 
Any variable prefixed with self is available to every method in the class, 
and we'll also be able to access these variables through any instance created from the class. 
The line self.name = name takes the value associated with the parameter name and assigns it to the variable name, 
which is then attached to the instance being created. The same process happens with self.age = age. 
Variables that are accessible through instances like this are called attributes. The Dog class has two other 
methods defined: sit() and roll_over() ❹. Because these methods don't need additional information to run, 
we just define them to have one parameter, self. The instances we create later will have access to these methods. 
In other words, they'll be able to sit and roll over. For now, sit() and roll_over() don't do much. 
They simply print a message saying the dog is sitting or rolling over. 
But the concept can be extended to realistic situations: 
if this class were part of a computer game, these methods would contain code to make an animated dog sit and roll over. 
If this class was written to control a robot, 
these methods would direct movements that cause a robotic dog to sit and roll over.
"""



# We can make an instance/object from a class.
# Think of a class as a set of instructions for how to make an instance. 
# The Dog class is a set of instructions that tells Python how to make individual instances representing specific dogs.
# Let’s make an instance representing a specific dog:

class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Stimulate sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Stimulate a dog rolling over."""
        print(f"{self.name} rolled over.")

my_dog = Dog('Willie', 6)  # creating instance

print(f"My dog's name is {my_dog.name}.")   # Using attribute
print(f"My dog is {my_dog.age} years old.")  # Using attribute
"""
The Dog class we're using here is the one we just wrote in the previous example. 
Here, we tell Python to create a dog whose name is 'Willie' and whose age is 6 ❶. 
When Python reads this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6. 
The __init__() method creates an instance representing this particular dog and sets the name and age attributes using 
the values we provided. Python then returns an instance representing this dog. 
We assign that instance to the variable my_dog. 
The naming convention is helpful here; we can usually assume that a capitalized name like Dog refers to a class, 
and a lowercase name like my_dog refers to a single instance created from a class.
"""



# You can access attributes from an instance by using dot notation.
print(my_dog.name)
print(my_dog.age)
# Dot notation is used often in Python and demonstrates how it works and is crucial.



# You can use dot notation to call methods from an instance.
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Stimulate sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Stimulate a dog rolling over."""
        print(f"{self.name} rolled over.")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
"""
To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, 
separated by a dot. When Python reads my_dog.sit(), 
it looks for the method sit() in the class Dog and runs that code. 
Python interprets the line my_dog.roll_over() in the same way. Now Willie does what we tell him to.
"""



# You can call as many instances as you need.
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Stimulate sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Stimulate a dog rolling over."""
        print(f"{self.name} rolled over.")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
"""
Even if we used the same name and age for the second dog, 
Python would still create a separate instance from the Dog class. 
You can make as many instances from one class as you need, 
as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.
Each dog is a separate instance with its own set of attributes, capable of the same set of actions
"""



"""
You can use classes to represent many real-world situations. 
Once you write a class, you'll spend most of your time working with instances created from that class. 
One of the first tasks you'll want to do is modify the attributes associated with a particular instance. 
You can modify the attributes of an instance directly or write methods that update attributes in specific ways.
"""
# Lets create a new class that is a class car:

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

"""
In the Car class, we define the __init__() method with the self parameter first ❶, just like we did with the Dog class. 
We also give it three other parameters: make, model, and year. 
The __init__() method takes in these parameters and assigns them to the attributes that will be associated with instances 
made from this class. When we make a new Car instance, we'll need to specify a make, model, and year for our instance.
We define a method called get_descriptive_name() ❷ that puts a car's year, make, and model into one string neatly 
describing the car. This will spare us from having to print each attribute's value individually. 
To work with the attribute values in this method, we use self.make, self.model, and self.year. Outside of the class, 
we make an instance from the Car class and assign it to the variable my_new_car ❸. 
Then we call get_descriptive_name() to show what kind of car we have. 
To make the class more interesting, let's add an attribute that changes over time. 
We'll add an attribute that stores the car's overall mileage.
"""



# You can set a default value for an attribute to use it for an instance.
# It can be defined in the "__init__()" method. Lets create a default value called "odometer_reading" that value is 0.
# We also add a method that reads the car's mileage:

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""
This time, when Python calls the __init__() method to create a new instance, it stores the make, model, and year values 
as attributes, like it did in the previous example.  Then Python creates a new attribute called odometer_reading and sets 
its initial value to 0 ❶.  We also have a new method called read_odometer() that makes it easy to read a car's mileage. 
Our car starts with a mileage of 0.
Not many cars are sold with exactly 0 miles on the odometer, so we need a way to change the value of this attribute.
"""



# You can modify attribute values by modifying them directly. This is the simplest way!
class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# We use dot notation to access the car's odometer_reading attribute, and set its value directly. 
# This line tells Python to take the instance my_new_car, and sets the value of that attribute to 23



# You can modify an attribute value through a method.
# Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.
# Lets also add some logic so nobody can roll back the odometer to a less value than the existing value.

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Stimulate updating the car's odometer and telling the final mileage of the car.
        Make sure that odometer cannot roll back after updating.
        """        
        if mileage >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = self.odometer_reading + mileage

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)   # Updates to 23
my_new_car.read_odometer()    # Reads the odometer
my_new_car.update_odometer(0)    # Prints a message that cannot roll back the odometer

"""
The only modification to Car is the addition of update_odometer(). 
This method takes in a mileage value and assigns it to self.odometer_reading. 
Using the my_new_car instance, we call update_odometer() with 23 as an argument ❶. 
This sets the odometer reading to 23, and read_odometer() prints the reading. 
Now update_odometer() checks that the new reading makes sense before modifying the attribute. 
If the value provided for mileage is greater than or equal to the existing mileage, self.odometer_reading, 
you can update the odometer reading to the new mileage ❶. 
If the new mileage is less than the existing mileage, you'll get a warning that you can't roll back an odometer ❷.
"""



# You can increment the value by using a method as well. Same logic goes for decreasing.
class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Stimulate updating the car's odometer and telling the final mileage of the car.
        Make sure that odometer cannot roll back after updating.
        """
        if mileage >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = self.odometer_reading + mileage
    
    def increment_odometer(self, miles):
        """Increment the car's odometer. Make sure to apply the logic of not rolling back the odometer."""
        if miles >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

"""
The new method increment_odometer() takes in a number of miles, and adds this value to self.odometer_reading.
We set its odometer to 23,500 by calling update_odometer() and passing it 23_500 ❷. 
Finally, we call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and 
registering it.
"""



# You can also use inheritence in classes. Here is some more:
"""
You don't always have to start from scratch when writing a class. 
If the class you're writing is a specialized version of another class you wrote, you can use inheritance. 
When one class inherits from another, it takes on the attributes and methods of the first class. 
The original class is called the parent class, and the new class is the child class. 
The child class can inherit any or all of the attributes and methods of its parent class, 
but it's also free to define new attributes and methods of its own. 
When you're writing a new class based on an existing class, you'll often want to call the __init__() method from the 
parent class. 
This will initialize any attributes that were defined in the parent __init__() method and make them available in the 
child class. As an example, let's model an electric car. An electric car is just a specific kind of car, 
so we can base our new ElectricCar class on the Car class we wrote earlier. 
Then we'll only have to write code for the attributes and behaviors specific to electric cars. 
Let's start by making a simple version of the ElectricCar class, which does everything the Car class does:
"""

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Stimulate updating the car's odometer and telling the final mileage of the car.
        Make sure that odometer cannot roll back after updating.
        """
        if mileage >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = self.odometer_reading + mileage
    
    def increment_odometer(self, miles):
        """Increment the car's odometer. Make sure to apply the logic of not rolling back the odometer."""
        if miles >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles

class ElectricCar(Car):
    """Similar characteristics to a car, but specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.get_descriptive_name()

"""
We start with Car ❶. 
When you create a child class, the parent class must be part of the current file and must appear before the child class 
in the file. We then define the child class, ElectricCar ❷. 
The name of the parent class must be included in parentheses in the definition of a child class. The __init__() method 
takes in the information required to make a Car instance ❸. The super() function ❹ is a special function that allows you 
to call a method from the parent class. 
This line tells Python to call the __init__() method from Car, 
which gives an ElectricCar instance all the attributes defined in that method. 
The name super comes from a convention of calling the parent class a superclass and the child class a subclass. 
We test whether inheritance is working properly by trying to create an electric car with the same kind of information 
we'd provide when making a regular car. 
We make an instance of the ElectricCar class and assign it to my_leaf ❺. 
This line calls the __init__() method defined in ElectricCar,
which in turn tells Python to call the __init__() method defined in the parent class Car. 
We provide the arguments 'nissan', 'leaf', and 2024. Aside from __init__(), there are no attributes or methods yet that 
are SPECIFIC to an electric car. At this point we're just making sure the electric car has the appropriate Car behaviors.
The ElectricCar instance works just like an instance of Car, 
so now we can begin defining attributes and methods specific to electric cars.
"""



# You can define attributes and methods for a child class after creating the child class __init__ method.
# Once you have a child class that inherits from a parent class, ...
# you can add any new attributes and methods necessary to differentiate the child class from the parent class.
# Lets create two attributes and methods for the child class ONLY!

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Stimulate updating the car's odometer and telling the final mileage of the car.
        Make sure that odometer cannot roll back after updating.
        """
        if mileage >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = self.odometer_reading + mileage
    
    def increment_odometer(self, miles):
        """Increment the car's odometer. Make sure to apply the logic of not rolling back the odometer."""
        if miles >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles

class ElectricCar(Car):
    """Similar characteristics to a car, but specific to electric vehicles."""

    def __init__(self, make, model, year, charging_time):
        super().__init__(make, model, year)
        self.battery = 40
        self.charging_time = charging_time
    
    def describe_battery(self):
        """Print a statement that describes the battery size."""
        print(f"This car has a {self.battery}-kWh battery.")
    
    def provide_charging_time(self):
        """Print a statement that provides the charge time, in minutes."""
        print(f"The charge time is {self.charging_time} minutes.")

my_leaf = ElectricCar('nissan', 'leaf', 2024, 450)
my_leaf.get_descriptive_name()
my_leaf.describe_battery()
my_leaf.provide_charging_time()

"""
These attributes will be associated with all instances created from the ElectricCar class 
but won't be associated with any instances of Car. 
We also add a method called describe_battery() and provide_charging_time() that prints information about the battery ❷.
There's no limit to how much you can specialize the ElectricCar class. 
You can add as many attributes and methods as you need to model an electric car to whatever degree of accuracy you need. 
An attribute or method that could belong to any car, rather than one that's specific to an electric car, 
should be added to the Car class instead of the ElectricCar class. 
Then anyone who uses the Car class will have that functionality available as well, 
and the ElectricCar class will only contain code for the information and behavior specific to electric vehicles.
"""



# You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.
# You define a method in the child class with the same name as the method you want to override in the parent class.
# Say the class Car had a method called fill_gas_tank(). In the electric car class, we'll modify it because...
# electric cars don't have fuel tanks and don't store gas.

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Stimulate updating the car's odometer and telling the final mileage of the car.
        Make sure that odometer cannot roll back after updating.
        """
        if mileage >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = self.odometer_reading + mileage
    
    def increment_odometer(self, miles):
        """Increment the car's odometer. Make sure to apply the logic of not rolling back the odometer."""
        if miles >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Stimulate filling a gas tank for a car."""
        print("Gas is filled, car is ready to drive.")

class ElectricCar(Car):
    """Similar characteristics to a car, but specific to electric vehicles."""

    def __init__(self, make, model, year, charging_time):
        super().__init__(make, model, year)
        self.battery = 40
        self.charging_time = charging_time
    
    def describe_battery(self):
        """Print a statement that describes the battery size."""
        print(f"This car has a {self.battery}-kWh battery.")
    
    def provide_charging_time(self):
        """Print a statement that provides the charge time, in minutes."""
        print(f"The charge time is {self.charging_time} minutes.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024, 450)
my_leaf.get_descriptive_name()
my_leaf.describe_battery()
my_leaf.provide_charging_time()

"""
Now if someone tries to call fill_gas_tank() with an electric car, 
Python will ignore the method fill_gas_tank() in Car and run this code instead. 
When you use inheritance, you can make your child classes retain what you need and override anything 
you don't need from the parent class.
"""



"""
When modeling something from the real world in code, you may find that you're adding more and more detail to a class. 
You'll find that you have a growing list of attributes and methods and that your files are becoming lengthy. 
In these situations, you might recognize that part of one class can be written as a separate class. 
You can break your large class into smaller classes that work together; this approach is called composition.
For example, if we continue adding detail to the ElectricCar class, we might notice that we're adding many attributes and 
methods specific to the car's battery. When we see this happening, we can stop and move those attributes and methods 
to a separate class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:
"""
# There are many ways to do it, here is one example using a default value:

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Stimulate updating the car's odometer and telling the final mileage of the car.
        Make sure that odometer cannot roll back after updating.
        """
        if mileage >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = self.odometer_reading + mileage
    
    def increment_odometer(self, miles):
        """Increment the car's odometer. Make sure to apply the logic of not rolling back the odometer."""
        if miles >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Stimulate filling a gas tank for a car."""
        print("Gas is filled, car is ready to drive.")


class Battery:
    """Modeling a battery for electric car use."""

    def __init__(self, battery=40):
        """Initialize the battery attribute."""
        self.battery = battery
    
    def describe_battery(self):
        """Print a statement that describes the battery size."""
        print(f"This car has a {self.battery}-kWh battery.")

# Create an instance to use as an attribute
my_battery = Battery(40)


class ElectricCar(Car):
    """Similar characteristics to a car, but specific to electric vehicles."""

    def __init__(self, make, model, year, charging_time):
        """Initialize child class attributes."""
        super().__init__(make, model, year)
        self.charging_time = charging_time
        self.battery = my_battery   # Using the instance as the attribte
    
    def provide_charging_time(self):
        """Print a statement that provides the charge time, in minutes."""
        print(f"The charge time is {self.charging_time} minutes.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024, 450)
my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()   # Accessing method
my_leaf.provide_charging_time()

"""
We define a new class called Battery that doesn't inherit from any other class. 
The __init__() method ❶ has one parameter, battery_size, in addition to self. 
This is an optional parameter that sets the battery's size to 40 if no value is provided. 
The method describe_battery() has been moved to this class as well ❷. 
In the ElectricCar class, we now add an attribute called self.battery ❸. 
This line tells Python to create a new instance of Battery (with a default size of 40, 
because we're not specifying a value) and assign that instance to the attribute self.battery. 
This will happen every time the __init__() method is called; 
any ElectricCar instance will now have a Battery instance created automatically. 
We create an electric car and assign it to the variable my_leaf. When we want to describe the battery, 
we need to work through the car's battery attribute: 
This line tells Python to look at the instance my_leaf, find its battery attribute, 
and call the method describe_battery() that's associated with the Battery instance assigned to the attribute.
The output is identical to what we saw previously.
"""

# This looks like a lot of extra work.
# But now we can describe the battery in as much detail as we want without cluttering the ElectricCar class. 
# Let’s add another method to Battery that reports the range of the car based on the battery size:

class Car:
    """A simple attempt to represent and model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a statement that prints the full name of a car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that tells the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Stimulate updating the car's odometer and telling the final mileage of the car.
        Make sure that odometer cannot roll back after updating.
        """
        if mileage >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = self.odometer_reading + mileage
    
    def increment_odometer(self, miles):
        """Increment the car's odometer. Make sure to apply the logic of not rolling back the odometer."""
        if miles >= self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Stimulate filling a gas tank for a car."""
        print("Gas is filled, car is ready to drive.")


class Battery:
    """Modeling a battery for electric car use."""

    def __init__(self, battery_size=40):
        """Initialize the battery attribute."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement that describes the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Similar characteristics to a car, but specific to electric vehicles."""

    def __init__(self, make, model, year, charging_time):
        """Initialize child class attributes."""
        super().__init__(make, model, year)
        self.charging_time = charging_time
        self.battery = Battery()   # Using the instance as the attribte
    
    def provide_charging_time(self):
        """Print a statement that provides the charge time, in minutes."""
        print(f"The charge time is {self.charging_time} minutes.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024, 450)
my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()   # Accessing method
my_leaf.provide_charging_time()
my_leaf.battery.get_range()

"""
The new method get_range() performs some simple analysis. 
If the battery's capacity is 40 kWh, get_range() sets the range to 150 miles, and if the capacity is 65 kWh, 
it sets the range to 225 miles. It then reports this value. When we want to use this method, 
we again have to call it through the car's battery attribute.
The output tells us the range of the car based on its battery size.
"""



# Here is some tips to Model Real-World Objects
"""
Modeling electric cars raises questions about associating the get_range() method. 
For a single car, linking it to the Battery class is fine. 
Yet, for a manufacturer's lineup, it might be better in the ElectricCar class. 
Another option is keeping the link with the battery but using a parameter like car_model. 
This growth stage involves thinking beyond syntax, focusing on real-world representation. 
Embrace the learning process, even if it means revising classes and trying different approaches.
"""



# You can import classes as well instead of functions.
"""
As you add more functionality to your classes, 
your files can get long, even when you use inheritance and composition properly. 
In keeping with the overall philosophy of Python, you'll want to keep your files as uncluttered as possible. 
To help, Python lets you store classes in modules and then import the classes you need into your main program.
"""
# Lets import an example file that ends with ".py" in this directory.
# This restaurant.py module has already one class that is stored.
# Here is how you import a single class from the "restaurant" module and importing the entire class of Restaurant.
# Remember, it has to be in the same directory:

from restaurant import Restaurant
favorite_restaurant = Restaurant('chick-fil-a', 'chicken sandwiches')
favorite_restaurant.describe_restaurant()
favorite_restaurant.set_number_served(100)