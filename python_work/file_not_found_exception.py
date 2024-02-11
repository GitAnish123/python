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