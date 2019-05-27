"""
Sometimes, you'll want to create a list of items that cannot change. Tuples allow you to
do just that. Python refers to values that cannot change as immutable, and an immutable
list is called a tuple.

A tuple looks just like a list except you use parentheses instead of square brackets.
Once you define a tuple, you can access individual elements by using each item's index.
"""

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250
# ^ The above causes a TypeError since we can't alter a tuple.


# Looping Through All Values in a Tuple

"""
You can loop over all the values in a tuple using a for loop, just as with a list
"""

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)


# Writing over a Tuple

"""
Although you can't modify a tuple, you can assign a new value to a variable that holds a tuple.
Therefore, if we wanted to change our dimensions, we would redefine the entire tuple.
"""

dimensions = (200, 40)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
