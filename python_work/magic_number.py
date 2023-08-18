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