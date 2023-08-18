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