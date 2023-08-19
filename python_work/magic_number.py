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