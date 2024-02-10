"""
Python uses special objects called exceptions to manage errors that arise during a program's execution. 
Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. 
If you write code that handles the exception, the program will continue running. 
If you don't handle the exception, the program will halt and show a traceback, 
which includes a report of the exception that was raised.
Exceptions are handled with try-except blocks. 
A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised. 
When you use try-except blocks, your programs will continue running even if things start to go wrong. 
Instead of tracebacks, which can be confusing for users to read, 
users will see friendly error messages that you've written.
"""
# Let’s look at a simple error that causes Python to raise an exception. 
# You probably know that it’s impossible to divide a number by zero, but let’s ask Python to do it anyway:
# This will be in a "comments" form so the rest of the code will excecute properly:

"""  print(5/0)  """

# Python can’t do this, so we get a traceback:

"""
Traceback (most recent call last):
  File "division_calculator.py", line 1, in <module>
    print(5/0)
          ~^~
ZeroDivisionError: division by zero
"""

"""
The error reported in the traceback, ZeroDivisionError, is an exception object ❶. 
Python creates this kind of object in response to a situation where it can't do what we ask it to. 
When this happens, Python stops the program and tells us the kind of exception that was raised. 
We can use this information to modify our program. 
We'll tell Python what to do when this kind of exception occurs; that way, if it happens again, we'll be prepared.
"""

# When you think an error may occur, you can write a try-except block to handle the exception that might be raised. 
# You tell Python to try running some code, and you tell it what to do. 
# That is only if the code results in a particular kind of exception.
# Here’s what a try-except block for handling the ZeroDivisionError exception looks like:

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
We put print(5/0), the line that caused the error, inside a try block. 
If the code in a try block works, Python skips over the except block. 
If the code in the try block causes an error, 
Python looks for an except block whose error matches the one that was raised, and runs the code in that block.
In this example, the code in the try block produces a ZeroDivisionError, 
so Python looks for an except block telling it how to respond. 
Python then runs the code in that block, and the user sees a friendly error message instead of a traceback:
"""

# If more code followed the try-except block, the program would continue running.
# This is because we told Python how to handle the error. 
# Let’s look at an example where catching an error can allow a program to continue running.




# Handling errors correctly is especially important when the program has more work to do after the error occurs. 
# This happens often in programs that prompt users for input. 
# If the program responds to invalid input appropriately, it can prompt for more valid input instead of crashing.
# Let’s create a simple calculator that does only division:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

"""
This program prompts the user to input a first_number ❶ and, if the user does not enter q to quit, a second_number ❷. 
We then divide these two numbers to get an answer ❸. 
This program does nothing to handle errors, so asking it to divide by zero causes it to crash:
"""

"""
Example Result of code:


Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
Traceback (most recent call last):
  File "division_calculator.py", line 11, in <module>
    answer = int(first_number) / int(second_number)
             ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
ZeroDivisionError: division by zero
"""

"""
It's bad that the program crashed, but it's also not a good idea to let users see tracebacks. 
Nontechnical users will be confused by them, and in a malicious setting, 
attackers will learn more than you want them to. 
For example, they'll know the name of your program file, and they'll see a part of your code that isn't working properly. 
A skilled attacker can sometimes use this information to determine which kind of attacks to use against your code.
"""



"""
We can make this program more error resistant by wrapping the line that might produce errors in a try-except block. 
The error occurs on the line that performs the division, so that's where we'll put the try-except block. 
This example also includes an else block. 
Any code that depends on the try block executing successfully goes in the else block:
"""


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
      answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
      print("You can't divide by 0!")
    else:
      print(answer)

"""
We ask Python to try to complete the division operation in a try block ❶, 
which includes only the code that might cause an error. 
Any code that depends on the try block succeeding is added to the else block. In this case, 
if the division operation is successful, we use the else block to print the result ❸.
The except block tells Python how to respond when a ZeroDivisionError arises ❷. 
If the try block doesn't succeed because of a division-by-zero error, 
we print a friendly message telling the user how to avoid this kind of error. 
The program continues to run, and the user never sees a traceback:
"""

"""
The only code that should go in a try block is code that might cause an exception to be raised. 
Sometimes you'll have additional code that should run only if the try block was successful; 
this code goes in the else block. 
The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block.
By anticipating likely sources of errors, 
you can write robust programs that continue to run even when they encounter invalid data and missing resources. 
Your code will be resistant to innocent user mistakes and malicious attacks.
"""