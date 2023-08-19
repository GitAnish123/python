# Toppings requested
# using SIGN: != 
# This sign means: not equal to opperator
# This is an example...
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies, this is not the topping the person wants.")

ice_cream_topping = 'chocolate chips'
if ice_cream_topping == 'chocolate chips':
    print("This is the right topping for the customer!")

# This sign means: equal to the operator.
# We used this example in a real life situation using an "if" statement.
# You can do this instead of manually checking if a value is equal to the other one.

requested_toppings = ['mushrooms','onions','pineapples']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
# We can see if any item is there in a list by using this way.
# We also checked if pepperoni is not in the list. Python said false, so pepperoni is not in the list
# You can check if values is in lists using the "if" statement, and this is checking if a value is not in a list. (1)

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
# In this example, any element in the variable (user) will get the message. Otherwise they won't.
# This is an example of how to see if a value is in a list using the 'if' statement. (2)

banned_users = ['andrew','carolina','david']
if 'andrew' in banned_users:
    print("You are a banned user, go away!")
# If the value "andrew" is in the list, it will print the message. It's because the "if" statement stated that.

# As you learn, you might come across boolean expressions. This is another name of conditional testing.
# A boolean value is either "True" or "False"
# Boolean values are often used to keep track of certain conditions
# For example,
game_active = True
can_edit = False
# Boolean values provide an efficient way to track the state of a program

# -------PRACTICE----------------

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
    print("This is one of my top five favorite languages.")
# This is examples of conditional testing.