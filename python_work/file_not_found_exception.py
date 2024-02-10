#  NOTE: THE FILE "story.txt" DOES NOT exist.




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