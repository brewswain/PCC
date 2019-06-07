"""
Let's write a short program that stores a set of numbers and another 
program that reads these numbers back into memory. The first program
will use json.dump() to store the numbers, and the second program 
will use json.load(). 

The json.dump() function takes two arguments: A piece of data to 
store and a file object it can use to store the data. Here's how 
you can use json.dump() to store a list of numbers:
"""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)


"""
We first import the json module and then create a list of numbers to
work with. At line 16 we choose a filename in which to store the list
of numbers. It's customary to use the file extension .json to indicate
that the data in the file is stored in the JSON format. Then we open 
the file in write mode, which allows json to write the data to the file 
in line 17. At line 18, we use the json.dump() function to store the 
list numbers in the file numbers.json.

This program has no output, but let's open the file numbers.json and 
look at it. The data is stored in a format that looks just like Python:

=============================
|   # [2, 3, 5, 7, 11, 13]  |
=============================

Now we'll write a program that uses json.load() to read the list back 
into memory:
"""

filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)

"""
At line 41 we make sure to read from the same file we wrote to. This
time when we open the file, we open it in read mode because Python 
only needs to read from the file(line 42). At line 43 we use the
json.load() function to load the information stored in numbers.json,
and we store it in the variable number. Finally, we print the recovered
list of numbers and see that it's the same list created in the earlier
program(line 12):

=============================
|   # [2, 3, 5, 7, 11, 13]  |
=============================

This is a simple way to share data between two programs.
"""
