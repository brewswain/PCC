"""
A few python functions are specific to lists of numbers. for example, you can easily find the minimum, maximum,
and sum of a list of numbers:
"""

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))
print(max(digits))
print(sum(digits))


# List Comprehensions

"""
The approach described in file 3_making_numerical_lists.py for generating the list squares consisted of using three 
or four lines of code. A List Comprehension allows you to generate this same list in just one line of code. 

A list comprehension combines the for loop and he creation of new elements into one line, and automatically appends
each new  element.
The following example builds the same list of square numbers you saw earlier, but uses a list comprehension:
"""

squares = [value**2 for value in range(1, 11)]
print(squares)

"""
To use this syntax, begin with a descriptive name for the list(in this case, squares). 
Next, open a set of square brackets and define the expression for the values you want to store in the new list.
In the above, the expression is 'value**2', which raises the value to the second power. 
Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets.
Notice that no colon is used at the end of the for statement.
"""
