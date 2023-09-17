aliens = ('bob','jon','ben')
for alien in aliens:
    print(alien.title())
aliens = ('bob','jon','ben')

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