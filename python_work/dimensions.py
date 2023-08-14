dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
dimensions = (200, 50)
dimensions[0] = 250
print(dimensions)  # You can't modify tuples, so it will give an error if you print it.
dimensions.append(12,)
print(dimensions) # You can't append or insert tuples
dimensions = (200, 50)
del dimensions[1]
print(dimensions) # You can't delete tuples too!
dimension = (150,)  # This is for defining one value to create a tuple.
print(dimension)
dimensions = (200, 50)
for dimensionn in dimensions:
    print(dimensionn)
# We are just printing the dimenions using a "for" loop   
dimensions = (200, 50)
print("Original dimensions:")
for dimensionn in dimensions:
    print(dimensionn)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimensionn in dimensions:
    print(dimensionn)
# We can just change the values of the dimensions to make the values changed.
# This is practice from now on!!!!!
buffet_food_mondays = 'pizza','tacos','chicken sandwitch','fries','apple with cucumber'  # Original menu
for buffet_food_monday in buffet_food_mondays:
    print(buffet_food_monday)
buffet_food_mondays = 'pizza','pasta with meatballs','chicken sandwitch','fries','oranges' # Changed menu, made a new line.
for buffet_food_monday in buffet_food_mondays:
    print(buffet_food_monday)
buffet_food_mondays[2] = 'turkey corn dog'  # This will create a menu if uyou print it because you cannot modify a Tuple.
print(buffet_food_mondays)