"""
Lists are ideal for storing sets of numbers, and Python provides a number of tools
to help work with lists of numbers. Once you understand how to use these tools effectively,
your code will work well even when your lists contain millions of items.
"""

# Using the range() Function

for value in range(1, 5):
    print(value)

"""
Although the code above looks like it should print the numbers 1 to 5, it doesn't print the number 5. 
The range() function causes Python to start counting at the first value you give it, and it stops when
it reaches the second value you provide. Since it stops at the second value, you output will never contain it.
Therefore, To print to 5, you'd use: 
for value in range(1,6)
"""


# Using range() to Make a List of Numbers

"""
If you want to make a list of numbers, you can convert the results of range() directly into a list using the
list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.
"""

numbers = list(range(1, 6))
print(numbers)

"""
We cam also use the range() function to tell Python to skip numbers in a given range. The program seen below demonstrates
how to list the even numbers between  and 10.

The range() function starts with the value 2 and then adds 2 to that value. It then adds 2 repeatedly, until it reaches or passes
the end value, 11, and produces this result:
"""

even_numbers = list(range(2, 11, 2))
print(even_numbers)


"""
You can create almost any set of numbers you want to, using the range() function. For example, consider how you might make a list
of the first 10 square numbers(the square of each integer of 1 through 10) . In Python, two asterisks(**) represent exponents. 
Here's how you might put the first 10 square numbers into a list:
"""

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


"""
To write the above more concisely, omit the temporary variable square and append each new value directly to the list.
"""

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

"""
You can use either of these two approaches when you're making more complex lists. Sometimes using a temporary variable
makes your code easier to read; other times it makes the code unnecessarily long. Focus on writing code that you understand
clearly first, which does what you want it to do. Then, look for more efficient approaches as you review your code.
"""
