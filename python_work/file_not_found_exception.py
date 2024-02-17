#  NOTE: THE FILE "story.txt" and "siddartha.txt" DOES NOT exist.




# Handling missing files in file operations is crucial. 
# Whether due to location, misspelling, or non-existence, a try-except block is essential for managing such scenarios.
# For instance, attempting to read "alice.txt" exemplifies this need.

"""

from pathlib import Path

path = Path('story.txt')
contents = path.read_text(encoding='utf-8')

"""

# We're using read_text() differently.
# The encoding argument when default encoding mismatches the file's encoding, common with files from other systems.
# Python raises an exception when attempting to read from a missing file.


# Start at the traceback's end to identify the exception type. Note the FileNotFoundError raised.
# Look near the beginning for the error line. Begin handling from there.
# Try block catches FileNotFoundError.
# And it's executing matching except block for user-friendly error messages instead of tracebacks.

from pathlib import Path

path = Path('story.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

# Result is a friendly user message!
# The program has nothing more to do if the file doesn’t exist, so this is all the output we see. 
# Let’s build on this example and see how exception handling can help when you’re working with more than one file.
    



# We'll count words in "Alice in Wonderland" from Project Gutenberg. We use split() to break the text into words.
# This method splits a string based on whitespace. This helps count words effectively.

from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# We move "alice.txt" to the directory.
# We read "Alice in Wonderland" into a string, split it into words, and count using len(). 
# In the else block, we print the word count.
# This is a good approximation of the length of Alice in Wonderland.
    


# Let’s add more books to analyze. Before we do, let’s move the bulk of this program to a function called count_words(). 
# This will make it easier to run the analysis for multiple books:

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('alice.txt')
count_words(path)


# Code moved into count_words(), comments updated. Loop counts words in texts. 
# Filenames stored in list, count_words() called for each.

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)


# The names of the files are stored as simple strings. 
# Each string is then converted to a Path object ❶, before the call to count_words(). 
# The missing siddhartha.txt file has no effect on the rest of the program’s execution.
# Try-except blocks prevent tracebacks, letting program continue analyzing found texts. 
# FileNotFoundError handling enables analysis of all texts.
    



# In Python, handle exceptions with try and except blocks.
# For silent failure, use try and pass in the except block to continue program execution seamlessly.
def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass                              # Add the value to just pass! (This is a placeholder)
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# In this listing, using the pass statement in the except block allows the code to run without producing a ..... 
# traceback or any output when a FileNotFoundError occurs.
# The pass statement acts as a placeholder.
# It signifies the intentional choice to do nothing at a specific point in the program.
# It often indicates potential future actions.
        


# Deciding which errors to report and not:
"""
Consider user expectations when deciding to report errors or fail silently. 
If users anticipate specific results, inform them about missing data. 
Python's error-handling allows tailoring information sharing to improve usability as per user needs 
and program dependencies.
"""














##  PRACTICE STARTS NOW ##
""" Practice is currently starting now"""












# Using ValueError for addition solving
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")





# Addition calculator but with a different Exception that handles text instead of numbers.
while True:
    print("Give me two numbers and I will add them.\nEnter 'q' anytime to quit.")
    first_number_add = input("First number:  ")
    if first_number_add == 'q'.lower():
        break
    second_number_add = input("Second number:  ")
    if second_number_add == 'q'.lower():
        break
    try:
        total_sum = int(first_number_add) + int(second_number_add)
    except ValueError:
        print(f"Please enter a valid number!")
    else:
        print(f"Total sum: {total_sum}")





# Program that reads any amount of file's contents and using an exception to catch errors. 
# "cats.txt" and "dogs.txt" works but "hamsters.txt" doesn't work because it is in a different location.
from pathlib import Path 
filenames = [
             '/users/anish/desktop/python_work/python/python_work/cats.txt',
             '/users/anish/desktop/python_work/python/python_work/dogs.txt',
             '/users/anish/desktop/python_work/python/python_work/hamsters.txt'
    ]
for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"\nSorry, this file doesn't exist in this directory or isn't there at all!")
    else:
        print(f"\nReading the file...")
        print(f"{contents}")





# Program that reads any amount of file's contents and using an exception to catch errors. 
# "cats.txt" and "dogs.txt" works but "hamsters.txt" doesn't work because it is in a different location.
# THIS TIME, THE ERROR WILL BE SILENT, THERE WILL BE NO FRIENDLY MESSAGE OR TRACEBACK!
from pathlib import Path 
filenames = [
             '/users/anish/desktop/python_work/python/python_work/cats.txt',
             '/users/anish/desktop/python_work/python/python_work/dogs.txt',
             '/users/anish/desktop/python_work/python/python_work/hamsters.txt'
    ]
for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading the file...")
        print(f"{contents}")





# Using "count()" to count the amount of specifized characters are there in a file.
# If I want to find how many "the" are there, I can do "the " because it could be "they" or "there" so add a space.
# Here is an example:
from pathlib import Path
def count_characters(path_filename, keyword):
    """
    Count how many specified characters are in a file.
    Example:  count_characters(example.txt, an)
    Result:  4 
    """
    path = Path(path_filename)
    contents = path.read_text()
    keyword_counted = contents.count(keyword)
    return f"Amount: {keyword_counted}"

counting_in_little_women = count_characters('/users/anish/desktop/python_work/python/python_work/little_women.txt', 'an')
print(f"\n{counting_in_little_women}")


















# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """