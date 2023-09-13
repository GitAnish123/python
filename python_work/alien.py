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

# ------------ PRACTICE ------------------- #


my_friend = {'first_name':'rithin', 'last_name':'nallathambi', 'age':12, 'city':'fort mill'}
print(my_friend)

print(my_friend['first_name'].title())
print(my_friend['last_name'].title())
print(my_friend['age'])
print(my_friend['city'].title())

favorite_numbers = {
    'aja':3, 
    'miraj':'123', 
    'peter':43, 
    'susan':98, 
    'abraham':12,
}


aja_poll = favorite_numbers['aja']
print(f"Aja's favorite number is {aja_poll}")
miraj_poll = favorite_numbers['miraj']
print(f"Miraj's favorite number is {miraj_poll}")
peter_poll = favorite_numbers['peter']

print(f"Peter's favorite number is {peter_poll}")
susan_poll = favorite_numbers['susan']
print(f"Susan's favorite number is {susan_poll}")
abraham_poll = favorite_numbers['abraham']
print(f"Abraham's favorite number is {abraham_poll}")


glossary_top_3_words = {
    'key':'The name of the value.', 
    'value':'The value of the key', 
    'key-value':'The key and the value combined.',
}
print(f"\nThe term 'key' means, {glossary_top_3_words['key']}")
print(f"\nThe term 'value' means, {glossary_top_3_words['value']}")
print(f"\nThe term 'key-value' means, {glossary_top_3_words['key-value']}")

# Make sure to practice how to modify, add, and remove elements in dictinary. Practice everything you learned so far.
# glossary, (edited)


glossary_top_3_words = {
    'key':'The name of the value.', 
    'value':'The value of the key', 
    'key-value':'The key and the value combined.',
}


for word in glossary_top_3_words.keys():
    print(word)
for word in glossary_top_3_words.values():
    print(word)
for word in glossary_top_3_words.items():
    print(word)
# I'm expirenmenting of all the printed keys, values, and key-values.



glossary_top_5_words = {
    'key':'The name of the value.', 
    'value':'The value of the key', 
    'key-value':'The key and the value combined.',
    'set' : 'a collection in which each item must be unique',
    'looping':'repeating something over and over until a particular condition is satisfied',
}

for word in glossary_top_5_words.keys():
    print(word)
for word in glossary_top_5_words.values():
    print(word)
for word in glossary_top_5_words.items():
    print(word)
    

favorite_major_rivers = {
    'nile':'egypt',
    'amazon':'peru',
    'missisipi':'united states'
}

for river_1, river_2 in favorite_major_rivers.items():
    print(f"\n{river_1.title()} runs through {river_2.title()}.")
print("\nThese rivers belong into different continents.")

for river_1 in favorite_major_rivers.keys():
    print(river_1.title())
for river_2 in favorite_major_rivers.values():
    print(river_2.title())

favorite_languages_practice = {
    'athena' : 'python',
    'olivia' : 'c',
    'bryson' : 'javascript',
    'ellie'  : 'python',
    'jackson' : 'javascript',
}


random_people_i_know = ['athena','kendall','olivia','charlotte','austin','ellie','sam','ahaan']
for people in random_people_i_know:
    if people in favorite_languages_practice:
        print(f"\n{people.title()}, thank you for taking the poll!")
    elif people not in favorite_languages_practice:
        print(f"{people.title()}, please take the poll")


# --------- PRACTICE IS OVER, NOW WE ARE MOVING ON TO NEXT LESSON!!! -------------- #

""" Practice is over """


""" Sometimes you'll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary.
This is called nesting. 
Lets nest some dictinaries inside a list."""
# For example,

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Here is a more interesting example. Try to figure it out!


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"\nTotal number of aliens: {len(aliens)}")

# Lets say you want the aliens to change.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"\nTotal number of aliens: {len(aliens)}")

# Another example,

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"\nTotal number of aliens: {len(aliens)}")

""" Lets add two 'for' loops"""

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[3:5]:
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"\nTotal number of aliens: {len(aliens)}")


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
print(alien_0['points'].title())
print(alien_0['condition'].title())

if alien_0['condition'] == 'weak':
    print("Alien 0 will officially be dead in 12 hours!")
else:
    print("Watch out, the alien is going to attack!")

""" As you can see, I extended it a little bit."""



###### END OF PRACTICE #######
""" This is the end of practice"""