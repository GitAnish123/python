players = ['charles','martina','michael','florence','eli']
print(players[0:3])
players = ['charles','martina','michael','florence','eli']
print(players[1:4])
players = ['charles','martina','michael','florence','eli']
print(players[2:4])
players = ['charles','martina','michael','florence','eli']
print(players[0:4])
players = ['charles','martina','michael','florence','eli']
print(players[-2:4])
players = ['charles','martina','michael','florence','eli']
print(players[:4])
players = ['charles','martina','michael','florence','eli']
print(players[-3:2])
players = ['charles','martina','michael','florence','eli']
print(players[:3])
players = ['charles','martina','michael','florence','eli']
print(players[:-3])
players = ['charles','martina','michael','florence','eli']
print(players[:2])
players = ['charles','martina','michael','florence','eli']
print(players[:-4])
players = ['charles','martina','michael','florence','eli']
print(players[2:])
players = ['charles','martina','michael','florence','eli']
print(players[3:])
players = ['charles','martina','michael','florence','eli']
print(players[1:])
players = ['charles','martina','michael','florence','eli']
print(players[0:])
players = ['charles','martina','michael','florence','eli']
print(players[4:])
players = ['charles','martina','michael','florence','eli']
print(players[-3:])
players = ['charles','martina','michael','florence','eli']
print(players[-1:])
players = ['charles','martina','michael','florence','eli']
print(players[-2:])
players = ['charles','martina','michael','florence','eli']
print(players[-4:])
players = ['charles','martina','michael','florence','eli']
print(players[-0:])
players = ['charles','martina','michael','florence','eli']
print(players[-3:])
# These are examples of how to slice your list.
# These tools could be very useful later on when you work with larger lists.
# There are couple syntaxes and you can do it on any index on any element.
# Make sure you don't forget "[]" this indicates a list or a list's index.
# Your lists should make sense and has all requirements, or else it won't work.
# Your lists should also follow some grammer. In these examples, I did not do any grammer work.
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players in my team:")
for player in players[:3]:
    print(player.title())
players = ['charles','martina','michael','florence','eli']
print("Here are my last two players in my team:")
for player in players[3:5]:
    print(player.title())
    print(f"{player.title()}, you are our OG people in the league. Welcome to the team and please help me teach the others!")
# These are examples of slicing a "for" loop.
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# This is the easiest way how you copy a list.
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]  # There is colon and brackets, [:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# We just appended new items into the two lists.
# This will prove we actually have two different lists.
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods  #There is no colon and brackets. [:] 
my_foods.append('canoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
# This is another example of a simple unpredictable error.
# Make sure you keep the colon + the brackets at the end to make a spare copy.
# In this example you made 'my_foods = friend_foods' so now they will associate with each other.
# This is not what we wanted.
# Make sure you be careful and don't do any simple errors.
# This is practice from now on!!!!!
dancers_and_singers = ['justin','olivia','ellie','addie','bristol','zoe','natalie','austin','charlotte']
print("\nThe first three dancers in my list are:")
print(dancers_and_singers[0:3])
print("\nThe next three dancers in my list are:")
print(dancers_and_singers[3:6])
print("\nThe last three dancers in my list are:")
print(dancers_and_singers[6:9])
# I am slicing lists by doing a real world situation.
my_pizza = ['cheese pizza','vegetable pizza','chicken pizza']
friend_pizza = my_pizza[:]
my_pizza.append('pepperoni pizza')
friend_pizza.append('sausage pizza')
print("\nMy favorite pizzas are:")
for my_pizzas in my_pizza[0:]:
    print(my_pizzas)
print("\nMy friend's favorite pizzas are:")
for friend_pizzas in friend_pizza[0:]:
    print(friend_pizzas)
# This is copying lists by using for loops and slices.
# This is also a good way to copy and print big lists.
dancers_and_singers = ['justin','olivia','ellie','addie','bristol','zoe','natalie','austin','charlotte']
print("\nThe first three dancers in my list are:")
for dancer_and_singer in dancers_and_singers[0:3]:
    print(dancer_and_singer)
print("\nThe next three dancers in my list are:")
for dancer_and_singer in dancers_and_singers[3:6]:
    print(dancer_and_singer)
print("\nThe last three dancers in my list are:")
for dancer_and_singer in dancers_and_singers[6:9]:
    print(dancer_and_singer)
print("\nThe best dancer in the list is:")
print(dancers_and_singers[2].title())
# I just did this again but I added the "for" loop
# This is also a very interesting and a useful way for longer lists.
# Make sure you keep this one in mind.

# ------------- PRACTICE IS OVER ---------------- #
""" Practice is now currently over! """
""" Real lessons now continues... """

# Instead of keeping a dictinary in a list, you could keep a list in a dictinary.
# For example...

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

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






# In functions, you can pass an arbitrary number of arguments. (Learn more in notes)
# Here is a simple example,

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# We can use a asterisk to make a tuple with all the values stored inside.


# Instead, we could replace the "print()" call with a loop that runs through all the values in the tuple
# That will make our code much better. For example:

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# That is an example of how you do it.



# Additionally, you can also mix positional and arbitrary arguments. The normal arguments should come first, then arbitrary.
# Here is an example:

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# That is a basic understanding and you can understand it more if you look at the program closely.







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