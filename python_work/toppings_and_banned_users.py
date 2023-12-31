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


requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# This is how you check multiple conditions.

# Sometimes you can't always check single conditions, so you have to use the seires of...
# independent "if" statements.
# For example, here is what happens if you use the "if-elif-else" chain in this situation.

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza")
# Python will execute only the first test that passes.


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
    print(f"{top5_coding_languages[0].title()} is one of my top five favorite languages.")
# This is examples of conditional testing.

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

# You can combine "lists" with "if" statements!!!
# For example, add a 'for' loop.



# This is a basic "for" loop you should already know from last unit!
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    # Print the requested toppings along with the pizza.
    # using an "f" string!!!
    print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")



# Lets say, for example the pizza place runs out of green peppers.
# We can use a "if" statement to handle this situation appropriatly.
# For example,

# (Lets do it step by step)
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        # We are using the "green peppers" as the "what if" question!:
        print("Sorry, we are currently out of green peppers. Come back later for some.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")


# This is an example of how, "for" loops and lists interact with "if" statements.
# So this is an example of how we handle this situation appropriatly.


print("Examples")
"""             MORE CODING           """
print("More coding coming soon!")



# So far: we've assumed that each list has at least one item in it.
# BUT, what if there is none and you want to test if they are.
# In this situation, it’s useful to check whether a list is empty before running a for loop.

# for example,



requested_toppings = [] # There is no toppings in this example.

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_toppings}")
# This is when the condition is "True"
else:
    print("Are you sure you want a plain pizza.")
# This is when the condition is "False"
# The quick check of what we did is the "if" statement



# This is a real world situation of what happens if a customer asks toppings when a pizzeria doesn't have.
available_toppings = ['mushrooms', 'olives', 'green peppers',
                       'pepperoni', 'pineapple', 'extra cheese']
# This is all the available toppings
# This is the toppings they only have.
requested_toppings = ['mushrooms','french fries','extra cheese']
# This is the requested toppings one customer asked.


for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

# This is a really good real-world situation example.
# This also has a decent amount of lines.

"""   PRACTICE     """


usernames = ['jane910','pasuar589','ad@msheey55','admin','coNtracTor1092']
# Remember, from now on, this is only practice.

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to hear our weekly report?")
    else:
        print(f"Thank you for logging in {username.title()}.")
print("\nThank you everyone for logging in and have a really nice day!")
# This repeats forever in the building for the next century!


# Now lets see if we have any users this month.
# We can do an "if" test to see!
# For example,


usernames = []
""" We begin with an empty list. """

if usernames:
    for username in usernames:
        print(f"Hello, {username.title()}, i'm glad to see you today!")
else:
    print("We need to find some new users!")

# This is how we test.
# In this case, the list is empty, so this company needs more users.

# Lets do another real-world situation.
# In this case, lets say that the company found some users, and they need to create a username.
""" But the users can not take the same existing usernames. """
# For example,

current_users = ['jane910','pasuar589','ad@msheey55','admin','coNtracTor1092']
new_users = ['leonlove561','olivi@Simmons1012','bRadYcoW911#','ad@msheey55','charlotte0300!']
# These are the list of the existing users and the new users.
# The new users are requesting to submit their new usernames...
for new_user in new_users:
    if new_user in current_users:
        print("Sorry, this username has already been taken. Please put another.")
    else:
        print("Your username is all set! You may now start the current project happening now.")

# This is how we test to see if a username is available
""" This is a useful...
test to do conditional testing!"""


""" Make sure to style your statements """
# The only recommendation is styling conditional tests is to use a single space around comparison operators.
# such as ==, >=, and <=
# spacing does not affect the code, it just makes it easier to read.

""" MAKE SURE YOU DO THIS PROPERLY. """
# You can also loop all key-value pairs in a dictinary.
# For example,
# This is the original dictinary.
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# Now lets loop all the key-values!
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")





""" ---------- PRACTICE # """ # IS OVER





# Lets say if you want to nest a dictinary inside a dictinary???
# For a real-world situation, lets say if you have 2 users with different amounts of information
""" This way will...
handle this situation appropriatly."""
# For example,


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
    full_name = f"{user_info['first']}  {user_info['last']}"
    location = user_info['location']
    print(f"\tFirst name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
# That is an example.


#---- PRACTICE ----------#



friend_1 = {'first_name': 'rithin', 'last_name': 'nallathambi', 'hobby': 'basketball'}
friend_2 = {'first_name': 'leon', 'last_name:': 'sarey', 'hobby': 'football'}
friend_3 = {'first_name': 'nakulan', 'last_name': 'punniyamorthy', 'hobby': 'video games'}
peoples = [friend_1, friend_2, friend_3]

for friend in peoples:
    print(friend)

friend_1 = {
            'first_name': 'rithin', 
            'last_name': 'nallathambi', 
            'hobby': 'basketball',
        }
friend_2 = {   
            'first_name': 'leon', 
            'last_name': 'sarey', 
            'hobby': 'football',
        }
friend_3 = {
            'first_name': 'nakulan', 
            'last_name': 'punniyamorthy', 
            'hobby': 'video games',
        }
peoples = [friend_1, friend_2, friend_3]

for friend in peoples:
    print(f"\nFirst name: {friend['first_name'].title()}")
    print(f"Last name: {friend['last_name'].title()}")
    full_name = f"{friend['first_name']} {friend['last_name']}"
    print(f"Full name: {full_name.title()}")
    print(f"Hobby: {friend['hobby'].title()}")

pet_1 = {'animal': 'dog',
         'gender': 'female',
         'name': 'daisy'
}
pet_2 = {'animal': 'cat',
         'gender': 'female',
         'name': 'bella'
}
pet_3 = {'animal': 'dog',
         'gender': 'male',
         'name': 'nabo'
}
pet_4 = {'animal': 'snake',
         'gender': 'male',
         'name': 'richard'
}
pet_5 = {'animal': 'fish',
         'gender': 'female',
         'name': 'goldie'
}


my_pets = [pet_1, pet_2, pet_3, pet_4, pet_5]
print(my_pets)
for pet in my_pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Gender: {pet['gender'].title()}")
    print(f"Name: {pet['name'].title()}")




favorite_places = {
    'sarthak': ['disney world','eiffel tower','adventure air sports'],
    'lyonkesh': ['carowinds'],
    'renier': ['golden gate bridge','legoland'],
}
for name, place in favorite_places.items():
    print(f"\n{name.title()}'s favorite place(s) are:")
    for location in place:
        print(f"\t{location.title()}")



favorite_numbers = {
    'aja':[3,199,12], 
    'miraj':[69,1,78,25,88,94,31,101,609],
    'peter':[43,9923213],
    'susan':[98,1000,81,86,89,102,9013,37248,3421401],
    'abraham':[12,911,2,46,13,29],
}
for person, number in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for numerical in number:
        print(f"\t{numerical}")


cities = {
    'fort_mill': {
        'country': 'United States Of America',
        'population': 'about 34_000 in 2023',
        'fun_fact': 'Fort Mill has a rising, complex district of schools.',
    },
    
    'hong_kong': {
        'country': 'china',
        'population': 'about 7_500_000 in 2023',
        'fun_fact': 'It is one of the most densely poplulated cities in the world in 2023!'
    },

    'istanbul': {
        'country': 'turkey',
        'population': 'about 16_000_000 in 2023',
        'fun_fact': 'It is the only transcontinental city in the world in 2022'
    },


}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {city_info['country'].title()}")
    print(f"Population: {city_info['population'].title()}")
    
    fun_fact_city = city_info['fun_fact']
    print(f"Fun fact: {fun_fact_city.title()}")

# Let me extend a little bit to an aliens example...
# I am doing it because to learn how to extend.
# This is the first example...

alien_0 = {'color':'green', 'points':5, 'condition':'weak'}
print(alien_0['color'].title())
print(alien_0['points'])
print(alien_0['condition'].title())

if alien_0['condition'] == 'weak':
    print("Alien 0 will officially be dead in 12 hours!")
else:
    print("Watch out, the alien is going to attack!")

""" As you can see, I extended it a little bit."""



###### END OF PRACTICE #######
""" This is the end of practice"""



# You can move values from one list to another using a "while" loop!
# For example,



# Start with users that need to be verified,
#  and an empty list to hold confirmed users.

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("The following users have been confirmed: ")
for cUrReNt_UsEr in confirmed_users:
    print(cUrReNt_UsEr.title())

# With that, you can do that to any kind of situation
# You can use the input function with "while" loops

# Since the user "candance", was last, it is first in the new lists!

# You can apply this situation to harder concepts like dictionaries
# Dictionaries allow you to connect information
# This is much more complicated.






##  PRACTICE STARTS NOW ##
""" Practice is currently starting now"""




# using "while" loops with lists
sandwich_orders = ['tuna sandwich', 'potato sandwich', 'cheese sandwich', 'peanut-butter sandwich', 'chicken sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    finished_sandwiches.append(sandwiches)
    print(f"\nI am working on your {sandwiches}")

print("Here are the sandwiches completed: ")
for sandwich in finished_sandwiches:
    print(sandwich)



# using "while" loops to remove certain kinds of elements
sandwich_orders = ['tuna sandwich', 'pastrami', 'potato sandwich', 'cheese sandwich', 'pastrami', 'peanut-butter sandwich', 'chicken sandwich', 'pastrami']
finished_sandwiches = []

print("We're extremely sorry, we ran out of pastrami sandwiches!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    finished_sandwiches.append(sandwiches)
    print(f"\nI am working on your {sandwiches}")

print("Here are the sandwiches completed: ")
for sandwich in finished_sandwiches:
    print(sandwich)



# using "while" loops with dictionaries
vacation = {}
vacation_active = True

while vacation_active:
    name = input("What is your name?  ")
    poll = input("If you would visit anywhere in the world, where would you go?  ")
    vacation[name] = poll

    respond_again = input("Is there anybody else to respond (yes, no)?  ")
    if respond_again != "yes":
        vacation_active = False

print(" --- Poll Results --- ")
for name, poll in vacation.items():
    print(f"{name.title()} will want to visit {poll.title()}")





# If you want to add more user input about asking more info...
vacation = {}
vacation_active = True

while vacation_active:
    name = input("What is your name?  ")
    age = input("What is your age? ")
    age = int(age)
    location = input("Where do you currently live?  ")
    poll = input("If you would visit anywhere in the world, where would you go?  ")
    vacation[name] = {
        "age": age,
        "location": location,
        "poll": poll,
    }

    respond_again = input("Is there anybody else to respond (yes, no)?  ")
    if respond_again != "yes":
        vacation_active = False

print(" --- Poll Results --- ")
for name, info in vacation.items():
    print(f"{name.title()} will want to visit {info['poll'].title()}")
    print(f"{name.title()} is {info['age']} years old and lives in {info['location'].title()}")





# Lets do the code but lets use the break statement. (Lets do the unique and long example)
vacation = {}

while True:
    name = input("What is your name?  ")
    age = input("What is your age? ")
    age = int(age)
    location = input("Where do you currently live?  ")
    poll = input("If you would visit anywhere in the world, where would you go?  ")
    vacation[name] = {
        "age": age,
        "location": location,
        "poll": poll,
    }

    respond_again = input("Is there anybody else to respond (yes, no)?  ")
    if respond_again != "yes":
        break

print(" --- Poll Results --- ")
for name, info in vacation.items():
    print(f"{name.title()} will want to visit {info['poll'].title()}")
    print(f"{name.title()} is {info['age']} years old and lives in {info['location'].title()}")



###### END OF PRACTICE #######
""" This is the end of practice"""




# In functions, you might want to accept an arbitrary amount of arguments but you don't know what infomation to pass.
# You can do keyword with key-value arguments to make that happen by storing and collecting information.
# For example...

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# Learn more in the notes.
# That is a short example of key-value keyword arguments.






##  PRACTICE STARTS NOW ##
""" Practice is currently starting now"""






# Arbitrary arguments only
def sandwich_order(*items_on_a_sandwich):
    """Describe a sandwich order including items in a sandwich like toppings."""
    print("\nThe following items on a sandwich are requested:")
    for item in items_on_a_sandwich:
        print(f"-- {item}")

sandwich_order('extra cheese', 'green peppers', 'broccoli', 'tomatoes')
sandwich_order('chili', 'red peppers', 'garlic', 'spicy salsa', 'BBQ sauses')
sandwich_order('olives', 'mushrooms')
sandwich_order('lettuce')



# Calling key-value pairs by doing keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

anish_profile = build_profile('Anish', 'Pasumarthi',
                              location='Fort Mill',
                              hobby='basketball',
                              favorite_food='pizza',
                              favorite_color='blue',
)
print(anish_profile)



# Writing functions with extra info, with normal arguments, with key-value pairs that is positional and keyword arguments.
def build_car(manufacturer, model_name, **extra_information):
    """
    Build your own car with at least 2 pieces of information below with any other added information.
    Store results in a dictionary with all pieces of information.
    """
    extra_information['manufacturer'] = manufacturer
    extra_information['model name'] = model_name
    return extra_information

car = build_car('Tesla', 'Tesla Model Y', color='light blue', age='5 months', drive_itself=True)
print(car)







###### END OF PRACTICE #######
""" This is the end of practice"""