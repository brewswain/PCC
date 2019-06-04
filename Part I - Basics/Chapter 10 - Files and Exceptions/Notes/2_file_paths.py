"""
When you pass a simple filename like pi_digits.txt to the open() function
Python looks in the directory where the file that's currently being executed
is stored.

Sometimes, depending on how you organize your work, the file you want to open
won't be in the same directory as your program file. For example, you might store
your program files ina folder called python_work. Inside python_work, you might
have another folder called text_files to distinguish your program files from the
text files they're manipulating. Even thought text_files is in python_work, just
passing open() the name of a file in text_files won't work, because Python will
only look in python_work and stop there; it won't go on and look in text_files.

To get Python to open files from another directory other than the one where your
program file is stored, you need ot provide a file path, which tells Python to look
in a specific location on your system.

Because text_files is insside python_work, you could use a relative file path to
open a file from text_files, for example:
"""

# with open('Python_Crash_Course_WIP/Part I - Basics/Chapter 10 - Files and Exceptions\Notes/pi_digits.txt'):

"""
You can also tell Python exactly where the file  is on your computer regardless of
where the program that's being executed is stored. this is called an absolute
file path, you use an absolute path if a relative path doesn't work. For instance,
if you've put text_files in some folder other than python_work - say, a folder
called other_files - then just passing open(), the path 'text_files/filename.txt'
won't work because Python will only look for that location inside python_work.
You will need to write out a full path to clarify where you want Python to look.

Absolute paths are usually longe than relative paths, so it's helpful to store
them in a variable, and then pass that variable to open(). Using absolute paths,
you can read files from any location on your system. For now it's easiest to 
store files in the same directory as your program files, or ina  folder such
as text_files within the direectory that stores your program files.
"""
