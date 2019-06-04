"""
When you're reading a file, you'll often want to examine each line of the file.
You might be looking for certain information in the file, or you might want to
modify the text in the file in some way. For example, you might want to read
through a file of weather data and work with any line that includes the word
'sunny' in the description of the day's weather. In a news report, you might
look for any line with the tag <headline> and rewrite that line with a
specific kind of formatting.

You can use a for loop on the file object to examine each line from a file
one at a time:
"""

filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)

"""
We store the name of the file we're reading from in the variable 'filename.'
This is a common convention when working with files. Because the variable
'filename' doesn't represent the actual file- It's just a string telling Python
where to find the file- you can easily swap out 'pi_digits.txt' for the name of
another file you want to work with. After we call open(), an object representing
fil and its contents is stored in the variable file-object.

We again use the with syntax to let Python open and close the file properly. To
examine the file's contents, we work through each line in the file by looping
over the file object. When we print each line, we find even more blank lines:

=====================
|   # 3.1415926535  |
|                   |
|                   |
|   # 8979323846    |
|                   |
|                   |
|   # 2643383279    |
=====================

These blank lines appear because an invisible newline character is at the end of
each line in the text file. The print statement adds its own newline each time we
call it, so we end up with two newline characters at the end of each line:
One from the file, and one from the print statement. Using rstrip() on each line
in the print statement eliminates these extra blank lines:
"""

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

"""
Now, the output matches the contents of the file once again.
"""
