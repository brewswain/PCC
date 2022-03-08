"""
An incredible amount of data is available in text files. text files can contain weather data,
traffic data, socioeconomic data, literary works, and more. Reading from a file is particularly
useful in data analysis applications, but it's also applicable to any situation in which you
want to analyze or modify information stored in a file. For example, you can write a program
that rteads in the contents of a text file and rewrites the file with formatting that allows
a browser to display it.

When you want ot work with the information in a text file, the first step is to read the file
into memory. You can read the entire contents of a file, yor you can work through the file
one line at a time.
"""

# Reading an Entire File

"""
To begin, we need a file with a few lines of text in it. Let's start with a file that contains
pi to 30 decimal places, with 10 decimal places per line:

=====================
|   # 3.1415926535  |
|   #   8979323846  |
|   #   2643383279  |
=====================

Here's a program that opens this file, reads it, and prints the contents of the file to the
screen:
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Please note that VSCode's internal terminal returns a FileNotFoundError, but it works using
# command prompt or git bash. I will hopefully get a fix for this, but in the mean time, this
# is posted here to remind me to use external terminals.


"""
To do any work with a file, even just printing its contents, you first need to open the file
to access it. The open() function needs one argument: the name of the file you want to open.
Python looks for this file in the directory where the program that's currently being executed
is stored. The open() function returns an object representing the file. 
Here, open('pi_digits.txt') returns an object representing pi_digits.txt. Python stores this
object in file_object, which we'll work with later in the program.

The keyword 'with' closdes the file once access to it is no longer needed. Notice how we call
open() in this program but not close(). You could open and close the file by calling open()
and close() but if a bug in your program prevents the close() statement from being executed,
the file may never close. This may seem trivial, but improperly closed files can cause data
loss or corruption. Also, if you close() too early in your program, you'll find yourself
trying to work with a closed file which leads to more errors.

Once we have a file object representing pi_digits.txt, we use the read() method in the second
line of our program to read the entire contents of the file and store it as one long string in 
contents. When we print the value of contents, we get the entire text file back:

=====================
|   # 3.1415926535  |
|   #   8979323846  |
|   #   2643383279  |
=====================

The only difference between this output and the original file is the extra blank line at the 
end of the output. The blank line appears because read() returns an empty string when it 
reaches the end of the file; this empty string shows up as a blank line. So, we use rstrip() 
in the print statement. This causes the output to match the contents of the original file exactly.
"""
