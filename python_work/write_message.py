"""
One of the simplest ways to save data is to write it to a file. 
When you write text to a file, 
the output will still be available after you close the terminal containing your program's output. 
You can examine output after a program finishes running, and you can share the output files with others as well. 
You can also write programs that read the text back into memory and work with it again later.
"""

# Once you have a path defined, you can write to a file using the write_text() method.
# To see how this works, let’s write a simple message and store it in a file instead of printing it to the screen:
from pathlib import Path
path = Path('programming.txt')
path.write_text("I love programming.")