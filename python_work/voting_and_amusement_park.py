age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are to young to vote.")
    print("Please register as soon you turn 18 years old!")
# This is an 'if-else' statement. This is very useful.
# This is good for TWO results.

age = 21
# Determining the cost of a person to pay for entering an amusement park.
if age <= 12:
    print("Your admission fee is $59.99")
elif age <= 24:
    print("Your admission fee is $119.99")
elif age <= 70:
    print("Your admission fee is $349.99")
else:
    print("Your admission fee is $399.99")

print("Also, Parking fee is $25")
# This is the "if-elif-else" chain.

age = 39

if age < 10:
    price = 30
elif age < 20:
    price = 60
elif age < 50:
    price = 150
else:
    price = 255
print(f"Your admission is ${price}")
# This is a much consise way to do it.

# This code produces the same output as the previous example, but the purpose of the if-elif-else chain is narrower.
# You could add as many "elif" blocks or you can just add one 'elif' block.
# You don't need to always include the 'else' block. Here is an example of omiting an else block.

age = 39

if age < 10:
    price = 30
elif age < 20:
    price = 60
elif age < 50:
    price = 150
elif age >= 51:
    price = 255
print(f"Your admission is ${price}")

