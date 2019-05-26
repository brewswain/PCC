# Sorting a List Permanently With the sort() Method

"""
The sort() method changes the order of the list permanently. It stores the list in alphabetical order,
and can't be reverted to the original order. You can reverse this by passing the argumentreverse=True to the 
method, like this : sort(reverse=True)
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


# Sorting a List Temporarily With the sorted() Function

"""
To maintain the original order of a list but present it in a sorted order, you can use the sorted() function.
The sorted() function lets you display your list in a particular order, but doesn't affect the actual order of the list.
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# Printing a List in Reverse Order

"""
To reverse the original order of a list, you can use the reverse() method. 
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


# Finding the Length of a List

"""
You can easily find the length of a list by using the len() function. Python counts the items starting with one, so 
there is no off-by-one error possibility when determining the length of a list.
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
