# Testing numerical expressions are pretty straightforward:
# For example,

age = 18
print(age == 18)
# You can also test numerical expressions that are not equal.

age = 18
print(age != 18)
# That is another example of testing numerical expressions.
# You can also use an "if" statement to check too!
# For example,

answer = 42                          # There will be no result because the answer is correct.
if answer != 42:
    print("That is not the correct answer, please try again!")

#  ANOTHER EXAMPLE #

correct_answer = 20
if answer == 20:
    print("That is the correct answer!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # Every inequality should be correct if you are using the 'and' keyword.
# The second one is incorrect so the entire thing is incorrect even though the first one is correct. It will mark as False.

age_0 = 22
age_3 = 24
print(age_0 >= 21) and (age_3 >= 21)
# The first and second one is correct and matches the operations. So it will mark as True.
# You also can wrap paranthesis around the inequalities to make it easier to read. It won't affect anything.

ages_0 = 22
ages_1 = 18
print(ages_0 >= 21 or ages_1 >= 21)
# The keyword "or" can also be used in multiple conditions. Either one or both has to be correct to mark it as True.
# If none are correct, it will be marked as "False"
# Another example,

ages_3 = 15
ages_1 = 18
print(ages_1 >= 21 or ages_3 >= 21)  # This example, none of the inequalities are correct, so it will be "False"
# That is how you can compare multiple conditions.

# Lets try the modulo operator:
# It will always return the remainder of the numbers!
print(4%3)
print(4%2)
print(7%3)

# --------PRACTICE--------------

friends1_age = 14
if friends1_age < 18:
    print("I'm still not an adult.")  # True
friends2_age = 21
if friends1_age > friends2_age:
    print("Haha!!!, i'm older than you!") #False

future_driver_age = 18
if future_driver_age >= 18:
    print("You are old enough to drive!") # True
number = 2
print(number == 5) # False
main_number = 21
if main_number != 21:
    print("This is the wrong answer, please try again!")  # True

number_of_shirts_in_Europe = 2_000_000_000_000_000_000_000_000
if number_of_shirts_in_Europe <= 5_000_000_000_000_000_000_000_000_000_000_000_000_000:
    print("Europe has less clothing than the USA.") # True
print(100 < 201 and 202 >= 208)  # False
print(9203 <= 21 or 382214823 == 382214823) # True
top5_coding_languages = ['Javascript','C','C++','Python','Lua']
print('Javascript' in top5_coding_languages)  # True
print('SQL' in top5_coding_languages)  # False

top5_coding_languages = ['Javascript','C','C++','Python','Lua']
if 'HTML' not in top5_coding_languages:
    print("This is not my top five coding languages.")
top5_coding_languages = ['Javascript','C','C++','Python','Lua']
if 'Javascript' in top5_coding_languages:
    print(f"{top5_coding_languages[0].title()} is one of my top five favorite languages.")
# This is examples of conditional testing.

NBA_sport = 'basketball'

# NBA sport stands for: ()
print(NBA_sport == 'soccer')  # I predict, false
# Hmm for the next one it is about 'cakes'
print(NBA_sport == 'cakes')  
# I predict, false

# NBA sport equals ???
# For the next one, it is about sports!
print(NBA_sport.title() == 'Basketball') # I predict "True"

for sports in NBA_sport:
    print(NBA_sport)
    if NBA_sport == 'basketball':
        print(f"{NBA_sport.title()}, True")
    else:
        print("That is the wrong answer, please try again!")

# Based on the results, the answer is "true"

NBA_sport = 'soccer'
print(NBA_sport == 'Soccer') # I predict false
NBA_sport = 'NBA'
print(NBA_sport.lower() == 'nba')  # I predict "True"

NBA_sport = 'football'
print(NBA_sport == NBA_sport)  

# I predict true because it is the same variable and has the same values.


NBA_sport = 'hockey'
print(NBA_sport == 'hockeys')  # I predict False

print(NBA_sport == 'hockey')  # I predict "True"
# We are doing conditional testing.
NBA_sport = 'baseball'

print(NBA_sport.upper() == 'BASEbALL')
# I did 5 examples of True and False.
path = 'stone path'

print(path != 'upper path')
# True
elevator_1stFloor_button = 'Two'
if elevator_1stFloor_button == 'Two':
    print("No!!!, we are in the wrong floor by mistake.")
# In this example, the result was printed, so it is, True

NBA_sport = 'NBA'
print(NBA_sport.lower() == 'nba')
# True
print(NBA_sport.lower() == 'NBA')
# False



# Lets use the modulo operator in a example.
# For example, we can use it to determine if a number is even or odd. Lets add user input to make things interesting!

even_or_odd_number = input("Enter a number and I will determine if that number is even or odd: ")
even_or_odd_number = int(even_or_odd_number)
if even_or_odd_number % 2 == 0:
    print(f"The number {even_or_odd_number} is even.")
else:
    print(f"The number {even_or_odd_number} is odd.")

rental_car = input("What kind of rental car you need?")
rental_car = f"Let me see if I could find you a {rental_car}"
car = input(rental_car)


dining = input("How many people you have in your dinner group?")
dining = int(dining)

if dining >= 8:
   print("You would have to wait for some time to get a table.")
else:
    print("All right, your all set!")


determine_number = input("Enter a number and I will determine if it is a multiple of 10.")
number = int(determine_number)

if number % 10 == 0:
    print(f"The number, {number} is a multiple of 10!")
else:
    print(f"The number, {number} is NOT a multiple of 10!")


# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """


# Lets do our first example of while loops.
# print numbers from 1-5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1



# Now lets use the continue statement to print only odd numbers from 1-10
# For example:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

# Try to avoid infinite loops.
# "Check notes for more information"
# Here is an example of an infinite loop you should avoid.
# This loop runs forever!
""" x = 1
while x <= 5:
    print(x) """





# ----------- PRACTICE -------------- #
""" Practice now begins """


pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

message = ""
while message != "quit":
    message = input(pizza_prompt)
    
    if message != "quit":
        print(f"We are adding {message}")


# 2nd example
movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
while True:
    themovie = input(movie_tickets)
    if themovie == "finished":
        break
    else:
        themovie = int(themovie)
        if themovie <= 3:
            print("It is free to enter.")
        elif themovie <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")

# While conditioning examples
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

message = ""
while message != "quit":
    message = input(pizza_prompt)
    
    if message != "quit":
        print(f"We are adding {message}")


movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
message = ""
while message != "finished":
    message = input(movie_tickets)
    
    if message != "finished":
        message = int(message)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")


# Flag examples
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

active = True
while active:
    message = input(pizza_prompt)
    if message == "quit":
        active = False
    else:
        print(f"We are adding {message}")

movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
active = True
while active:
    message = input(movie_tickets)
    if message == "finished":
        active = False
    else:
        message = int(message)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")
        



# while "True" with a break value.
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "
while True:
    message = input(pizza_prompt)
    if message == "quit":
        break
    else:
        print(f"We are adding {message}")

movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
while True:
    message = input(movie_tickets)
    if message == "finished":
        break
    else:
        message = int(themovie)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")


# Here is a infinite loop!!!
while 1 == 1:
    print(True)



# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """