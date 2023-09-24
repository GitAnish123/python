python = "pythons"
print(python.title())
print("\tpython")
print("Languages:\nPython\nC\nJavascript")
print("kishan,\nHow are you?\nHope you are good!")
print("Hello\n\tKishan, your cracked at\tFortnite!\nHope you win\tThe next game\nHave fun:)")
favorite_language = ' python p'
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language)
favorite_language = f"{favorite_language.lstrip()}"
nostarch_url = 'https://nostarch.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))
print(nostarch_url)
nostarch_url = f"{nostarch_url.removeprefix('https://')}"
print(nostarch_url)
message = input("Hello, security challenge, Type anything and I will continue the program running!")
print(message)
# That is how you do "input" and "output"
# You can also use a dictinary to store one kind of info for many objects!
# For example,
favorite_language = {
    'jen':'python',
    'sarah':'C',
    'edward':'rust',
    'phil':'python',
}
# To use this dictionary, given the name of a person who took the poll, you can easily look up their favorite language:

favorite_language = {
    'jen':'python',
    'sarah':'C',
    'edward':'rust',
    'phil':'python',
}
language = favorite_language['sarah'].title()
print(language)
""" That is how you can use a dictinary. """
# You can apply these situations for other key-values in dictinary's!
# Lets loop all the key-value pairs.
# For exaample...

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
""" Now lets loop only the keys"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
# Lets do an interesting example,


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
friends = ['sarah', 'phil']

for name in favorite_languages.keys():
   print(f"Hi {name.title()}.")
   if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Another example

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

""" You might want to return a result of looping in a particular order.
Just simply use the "sorted() function.""" 
"""For example"""


favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for filling out the poll.")
for name in sorted(favorite_languages.keys(), reverse=True):
        print(f"{name.title()}, thank you for filling out the poll.")
# I printed it in alphabetical order and reverse alphabetical order.

""" This is how you loop all the values in a dictinary using the...
values() function."""
# For example,

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# But if you want a unique code that has no repetition in it, you can use a set.
""" A set is a collection in which each item must be unique """
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# This is an example of how to build a set...
languages_in_a_set = {'python', 'rust', 'python', 'c'}
print(languages_in_a_set)
# What if you have more lists inside a dictinary:

# What if you have more lists?
""" Example??? """

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


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