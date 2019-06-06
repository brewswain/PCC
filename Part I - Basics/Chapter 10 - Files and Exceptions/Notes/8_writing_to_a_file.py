"""
One of the simplest ways to save data is to write it to a file. When you
write text to a file, the output will still be available after you close
the terminal containing your program's output. You can examine output
after a program finishes running, and you can share the output files with
others as well. You can also write programs that read the text back into
memory and work with it later.
"""

# Writing to An Empty File

"""
To write text to a file, you need to call open() with a second argument
telling Python that you want to write to the file. To see how this works,
let's write a simple message and store it in a file instead of printing
it to the screen:
"""

filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

"""
The call to open() has two arguments this time. The first argument is still
the name of the file we want to open. 

The second argument, 'w', tells Python that we want to open the file in 
write mode. You can open a file in read mode('r'), write mode('w'), 
append mode('a'), or a mode that allows you to read and write to the file('r+'). 

The open() function automatically creates the file you're writing to if it 
doesn't already exist. However, be careful opening a file in write mode('w')
because if the file does exist, Python will erase the file before returning the
file object.

At line 22, we use the write() method on the file object to write a string to the
file. this program has no terminal output, but if you open the file
programming.txt, you'll see one line:

============================
|   # I love programming.  |
============================

This file behaves like any other file on your computer. You can open it, write new
text in it, copy from it, paste to it, and so forth.

Python can only write strings to a text file. If you want to store numerical data
in a text file, you'll have to convert the data to string format first using the 
str() function.
"""
