for value in range(1,6):
    print(value)
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
# This is a list comprehension of finding the squares of 1-10!
# This is complex but it will take 1-2 lines of code
# Try it!, code is in next line
squares = [value **2 for value in range(1,11)]
print(squares)
one_million = list(range(1,1_000_001))
print(one_million)
for value in range(1,21):
 print(value)
one_million_list = list(range(1,1000001))
print(one_million_list)
print(min(one_million_list))
print(max(one_million_list))
print(sum(one_million_list))
# These are all simple statical questions
odd_numbers = list(range(1,22,2))
print(odd_numbers)
# Odd numbers from 1-20
for value in range(1,22,2):
   print(value)
counting_by_threes = list(range(3,31,3))
print(counting_by_threes)
for value in range(3,31,3):
   print(value)
cubes = []
for value in range(1,16):
   cube = value**3
   cubes.append(cube)
print(cubes)
# These are the cubes from 1-15. You have to use (**) to indicate an exponent.
# cubes means a value to the power of three
cubes_list_comprehensions = [value**3 for value in range(1,11)]
print(cubes_list_comprehensions)
# This is a list comprehension. This is a simple but complex way to write code
# This is very useful later on and if you practice, you can create your own list comprehension.
for value in range(1,1_000_001):
   print(value)
# This is values from 1-1000000 but not in a list.
# Values and examples are expected to change!