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
# For example...