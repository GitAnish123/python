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
print(dancers_and_singers[1].title())
# I just did this again but I added the "for" loop
# This is also a very interesting and a useful way for longer lists.
# Make sure you keep this one in mind.