"""
Let's use the program we just wrote to find out if someone's birthday
appears anywhere in the first million digits of pi. We can do this by 
expressing each birthday as a string of digits and seeing if that string 
appears anywhere in pi_string:
"""

filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


birthday = input("Enter your birthday in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi.")


"""
It turns out, my birthday does appear in the digits of pi! Once you've
read from a file, you can analyze its contents in just about any way
you can imagine.
"""
