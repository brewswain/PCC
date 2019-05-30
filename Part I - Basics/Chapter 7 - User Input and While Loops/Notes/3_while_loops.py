"""
Unlike a for loop, which takes a collection of items and executes a block 
of code once for each item in the collection, the while loop runs as long
as a certain condition is true.

You can use a while loop to count up through a series of numbers. For 
example, the following while loop counts from 1 to 5:
"""

# We set a value to start counting from.
current_number = 1

# The while loop is set to keep running as long as current_number's value is less than or equal to 5.
while current_number <= 5:
    # current_number's value is printed before it gets iterated.
    print(current_number)
# 1 is added to its value. Python repeats the loop until the condition returns False, ie current_number > 5
    current_number += 1


# Letting the User Choose When to Quit

"""
We can make the parrot program we wrote run as long sa the user wants
by putting most of the program inside a while loop. We'll define a 
Quit Value and then keep the program running as long as the user
has not entered the quit value.
"""

prompt = '\nTell me something, and I will repeat it back to you: '
prompt += "\nEnter 'quit' to end the program. "

# We set message as an empty string so Python has something to check the first time it reaches the while line.
message = ""

"""
while message != 'quit':
    message = input(prompt)
    print(message)
"""
# The program works well at this point, but it prints out the word 'quit' as if it were a message.

# We'll solve this with an if statement:
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
