first_name = "anish"
last_name = "pasumarthi"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()}!")
message = f"hello, {full_name.title()}!"
print(message)





# In a function, you can return values to store for it later on!
# Lets do an example when we return a first and last name converting it into a neatly formatted name using "return"
# For example,

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('anish', 'pasumarthi')
print(musician)
# That is how you do a simple example of returning a function using "return".





# We can make an argument optional!
# For example, if we want to enter our first, middle, and last name, we can expand this code.
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# But middle names are not always needed!
# If you want to display your first and last name OR your first, middle, and last name, do this code!
# For example,

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
# That is an example of how you make an argument optional!



# You can also use "while" loops with functions
# Here is an example of a program that continuesly greets people
# For example, 
""" def get_formatted_name(first_name, last_name):
    ""Return a full name, neatly formatted.""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")  """


# The problem of the code is that, there is no quit condition, so it will keep on greeting people.
# Here is the better version that will apply quit conditions along with the simple examples that contains first & last names.
# For example,
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
# That is an example of while loops with functions
# Make sure when you do while loops, always make sure to apply a quit condition so it doesn't run forever!




##  PRACTICE STARTS NOW ##
""" Practice is currently starting now"""



def city_country(city, country):
    """Print the city along with its country."""
    functionobjective = f"{city}, {country}"
    return functionobjective 

formatted_country_and_city1 = city_country('Washington D.C', 'United States of America')
formatted_country_and_city2 = city_country('Cairo', 'Egypt')
formatted_country_and_city3 = city_country('New Delhi', 'India')
print(formatted_country_and_city1)
print(formatted_country_and_city2)
print(formatted_country_and_city3)



def make_album(artist_name, album_title):
    """Create a dictionary of the artist name and the album name."""
    make_album_dict = {'artist name': artist_name, 'album title': album_title}
    return make_album_dict

album1 = make_album('Taylor Swift', '2023 Album')
album2 = make_album('Justin Bieber', 'The kid laroi album')
album3 = make_album('Lil Mabu', 'Hard block blues 2021')
print(album1)
print(album2)
print(album3)



# Lets extend this code with an optional value
def make_album(artist_name, album_title, number_of_songs=None):
    """Create a dictionary of the artist name and the album name."""
    if number_of_songs:
        make_album_dict = {
            'artist name': artist_name, 
            'album title': album_title, 
            'number of songs': number_of_songs
        }
    else:
        make_album_dict = {'artist name': artist_name, 'album title': album_title}
    return make_album_dict

album1 = make_album('Taylor Swift', '2023 Album')
album2 = make_album('Justin Bieber', 'The kid laroi album', 4)
print(album1)
print(album2)




# Lets use a "while" loop so the user can quit whenever the user wants!
def make_album(artist_name, album_title):
    """Create a dictionary of the artist name and the album name."""
    make_album_dict = {'artist name': artist_name, 'album title': album_title}
    return make_album_dict

while True:
    print("\nHello, please enter the information we ask to create your album!")
    print("Enter 'quit' if you are finished.")
    artist_names = input("What is the artist's name?: ")
    if artist_names.lower() == 'quit':
        break
    album_titles = input("What is the album's name title?: ")
    if album_titles == 'quit':
        break
    album_info = make_album(artist_names, album_titles)
    print(album_info)

# These are some examples of "returning" specific values and using functions for more needs!




###### END OF PRACTICE #######
""" This is the end of practice"""