# You can return dictionaries inside of a function!
# For example:

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
# That is a simple example!


# You can also add more information like age, or occupation. You can add optional values so if you want you can include info
# Lets say for example, 'age'.
# For example,

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
# That is how you add multiple values and optional values.







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