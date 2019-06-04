"""
So far we've focused on analyzing a text file that contains only three lines,
but the code in these examples would work just as well on much larger files. 
If we start with a text file that contains pi to 1,000,000 decimal places
instead of just 30, we can create a single string containing all these digits.
We don't need to change our program at all except to pass it to a different 
file. We'll also print just the first 50 decimal places, so we don't have to 
watch a million digits scroll by in the terminal:
"""

filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


print(pi_string[:52] + "...")
print(len(pi_string))

"""
Python has no inherent limit to how much data you can work with; you can 
work with as much data as your system's memory can handle.
"""
