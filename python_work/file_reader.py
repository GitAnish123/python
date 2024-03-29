"""
Now that you've mastered the basic skills you need to write organized programs that are easy to use, 
it's time to think about making your programs even more relevant and usable. 
In this chapter, you'll learn to work with files so your programs can quickly analyze lots of data.
You'll learn to handle errors so your programs don't crash when they encounter unexpected situations. 
You'll learn about exceptions, 
which are special objects Python creates to manage errors that arise while a program is running. 
You'll also learn about the json module, 
which allows you to save user data so it isn't lost when your program stops running.
Learning to work with files and save data will make your programs easier for people to use. 
Users will be able to choose what data to enter and when to enter it. 
People will be able to run your program, do some work, and then close the program and pick up where they left off.
Learning to handle exceptions will help you deal with situations in which files don't exist and deal with other problems 
that can cause your programs to crash. 
This will make your programs more robust when they encounter bad data, 
whether it comes from innocent mistakes or from malicious attempts to break your programs. 
With the skills you'll learn in this chapter, you'll make your programs more applicable, usable, and stable.
"""



# Here is how to read from a file!
"""
An incredible amount of data is available in text files. 
Text files can contain weather data, traffic data, socioeconomic data, literary works, and more. 
Reading from a file is particularly useful in data analysis applications, 
but it's also applicable to any situation in which you want to analyze or modify information stored in a file. 
For example, you can write a program that reads in the contents of a text file and rewrites the file with formatting that 
allows a browser to display it.
When you want to work with the information in a text file, the first step is to read the file into memory. 
You can then work through all of the file's contents at once or work through the contents line by line.
"""



# Lets first find the path of a text file that is already created. (pi_digits.txt)  Then we can open, read, and print it!
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

"""
To work with the contents of a file, we need to tell Python the path to the file. 
A path is the exact location of a file or folder on a system. 
Python provides a module called pathlib that makes it easier to work with files and directories, 
no matter which operating system you or your program's users are working with. 
A module that provides specific functionality like this is often called a library, 
hence the name pathlib. We start by importing the Path class from pathlib. 
There's a lot you can do with a Path object that points to a file. 
For example, you can check that the file exists before working with it, 
read the file's contents, or write new data to the file. 
Here, we build a Path object representing the file pi_digits.txt, 
which we assign to the variable path ❶. 
Since this file is saved in the same directory as the .py file we're writing, 
the filename is all that Path needs to access the file. 
Once we have a Path object representing pi_digits.txt, 
we use the read_text() method to read the entire contents of the file ❷. 
The contents of the file are returned as a single string, which we assign to the variable contents. 
When we print the value of contents, we see the entire contents of the text file:
"""
# The only difference between this output and the original file is the extra blank line at the end of the output. 
# The blank line appears because...
# read_text() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line.
# We can remove the extra blank line by using rstrip() on the contents string:
# Python’s rstrip() method removes, or strips, any whitespace characters from the right side of a string. 
# Now the output matches the contents of the original file exactly:

from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

# We can strip the trailing newline character when we read the contents of the file. 
# We can do it by applying the rstrip() method immediately after calling read_text():
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)
"""
This line tells Python to call the read_text() method on the file we're working with. 
Then it applies the rstrip() method to the string that read_text() returns. 
The cleaned-up string is then assigned to the variable contents. This approach is called method chaining, 
and you'll see it used often in programming.
"""



"""
When you pass a simple filename like pi_digits.txt to Path, 
Python looks in the directory where the file that's currently being executed (that is, your .py program file) is stored.
Sometimes, depending on how you organize your work, the file you want to open won't be in the same directory as your 
program file. For example, you might store your program files in a folder called python_work; 
inside python_work, you might have another folder called text_files to distinguish your program files from the text files 
they're manipulating. 
Even though text_files is in python_work, just passing Path the name of a file in text_files won't work, 
because Python will only look in python_work and stop there; 
it won't go on and look in text_files. 
To get Python to open files from a directory other than the one where your program file is stored, 
you need to provide the correct path.
There are two main ways to specify paths in programming. 
A relative file path tells Python to look for a given location relative to the directory where the currently running 
program file is stored. Since text_files is inside python_work, 
we need to build a path that starts with the directory text_files, and ends with the filename. 
Here's how to build this path:
"""
#      path = Path('text_files/filename.txt')      #

"""
You can also tell Python exactly where the file is on your computer, 
regardless of where the program that's being executed is stored. 
This is called an absolute file path. You can use an absolute path if a relative path doesn't work. 
For instance, if you've put text_files in some folder other than python_work, 
then just passing Path the path 'text_files/filename.txt' won't work because Python will only look for that location 
inside python_work. You'll need to write out an absolute path to clarify where you want Python to look.
Absolute paths are usually longer than relative paths, because they start at your system's root folder:
Using absolute paths, you can read files from any location on your system. For now it's easiest to store files in the 
same directory as your program files, or in a folder such as text_files within the directory that stores your program 
files.
"""
#     path = Path('/users/anish/desktop/python_work/text_files/filename.text')      #




"""
When you're working with a file, you'll often want to examine each line of the file. 
You might be looking for certain information in the file, or you might want to modify the text in the file in some way.
For example, you might want to read through a file of weather data and work with any line that includes the word sunny in 
the description of that day's weather. In a news report, 
you might look for any line with the tag <headline> and rewrite that line with a specific kind of formatting.
You can use the splitlines() method to turn a long string into a set of lines, 
and then use a for loop to examine each line from a file, one at a time:
"""
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)

# Here is the actual list without looping:
print(lines)

"""
We start out by reading the entire contents of the file, as we did earlier ❶. 
If you're planning to work with the individual lines in a file, 
you don't need to strip any whitespace when reading the file. 
The splitlines() method returns a list of all lines in the file, and we assign this list to the variable lines ❷. 
We then loop over these lines and print each one. 
Since we haven't modified any of the lines, the output matches the original text file exactly.
"""



"""
After you've read the contents of a file into memory, 
you can do whatever you want with that data, so let's briefly explore the digits of pi. 
First, we'll attempt to build a single string containing all the digits in the file with no whitespace in it:
"""

from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)
print(len(pi_string))
"""
We start by reading the file and storing each line of digits in a list, just as we did in the previous example. 
We then create a variable, pi_string, to hold the digits of pi. 
We write a loop that adds each line of digits to pi_string ❶. 
We print this string, and also show how long the string is:
"""

# The variable pi_string contains the whitespace that was on the left side of the digits in each line, 
# but we can get rid of that by using lstrip() on each line:

from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))

# Now we have a string containing pi to 30 decimal places. 
# The string is 32 characters long because it also includes the leading 3 and a decimal point:
# When Python reads from a text file, it interprets all text in the file as a string. 
# If you read in a number and want to work with that value in a numerical context, 
# you’ll have to convert it to an integer using the int() function or a float using the float() function.



"""
So far, we've focused on analyzing a text file that contains only three lines, 
but the code in these examples would work just as well on much larger files. 
If we start with a text file that contains pi to 1,000,000 decimal places, 
instead of just 30, we can create a single string containing all these digits. 
We don't need to change our program at all, except to pass it a different file. 
We'll also print just the first 50 decimal places, so we don't have to watch a million digits scroll by in the terminal:
"""
from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

# The output shows that we do indeed have a string containing pi to 1,000,000 decimal places:
# Python has no inherent limit to how much data you can work with.
# You can work with as much data as your system’s memory can handle.



"""
I've always been curious to know if my birthday appears anywhere in the digits of pi. 
Let's use the program we just wrote to find out if someone's birthday appears anywhere in the first million digits of pi. 
We can do this by expressing each birthday as a string of digits and seeing if that string appears anywhere in pi_string:
"""

from pathlib import Path 
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

"""
My birthday does appear in the digits of pi! Once you've read from a file, 
you can analyze its contents in just about any way you can imagine.
"""










##  PRACTICE STARTS NOW ##
""" Practice is currently starting now"""











# Read and print a file's contents by finding the path of the file:
from pathlib import Path
path = Path('python_summary.txt')
contents = path.read_text()
print(contents)



# Creating a list that stores the file's contents and looping through the list:
from pathlib import Path
path = Path('python_summary.txt')
contents = path.read_text()
print(contents)
lines = contents.splitlines()
for line in lines:
    print(line)



# Replacing any word in a string with a different word using the "replace()" method:
from pathlib import Path
path = Path('python_summary.txt')
contents = path.read_text()
contents = contents.replace('python', 'javascript')
print(contents)



# Using simpliar code to make it more concise. (Remove the temperary variable, 'lines')
from pathlib import Path
path = Path('python_summary.txt')
contents = path.read_text()
print(contents)
for line in contents.splitlines():
    print(line)











# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """