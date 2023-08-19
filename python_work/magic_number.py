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
    print("This is one of my top five favorite languages.")
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