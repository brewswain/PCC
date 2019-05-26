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
