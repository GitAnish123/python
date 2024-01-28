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