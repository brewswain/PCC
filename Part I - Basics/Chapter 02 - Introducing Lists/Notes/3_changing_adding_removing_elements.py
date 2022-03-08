# Modifying Elements in a List

""" 
Most lists you create will be dynamic, meaning that you build a list then add and remove elements from it as your program runs its course.

The syntax for modifying an element is similar to the syntax for accessing an element in a list.
To change an element, use the name of the list followed by the index of the element you want to change, 
then provide the new value you want that item to have.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# Adding Elements to a List

"""
The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list,
the new element is added to the end of the list.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)


"""
append() makes it easy to build lists dynamically. For instance, you can use an empty list, then add items to it by using
append().
"""

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)


# Inserting Elements into a List

"""
You can add a new element at any position in your list by using the insert() method.
Specify the index of the new element, and its value.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removing Elements from a List

"""
If you know the position/index of the item that you want to remove, you can use the del statement.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method

"""
Sometimes you'll want to use the value of an item after you remove it from a list. the pop() method
removes the last item in a list, but lets you work with it after removal.

When you want to delete an item from a list and not use that item in any way, use the del statement.
When you want to use the item as you remove it, use pop()
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')


"""
pop() can be used to remove an item in any position by including the index in parentheses
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


# Removing an Item by Value

"""
If you only know the value of the item you want to remove, and not the position, then you can use the remove() method.
Just like with pop(), you can use the item that's being removed from a list.

The remove() method only deletes the first occurrence of the value you specify. If there's a possibility that the value
appears more than once in a list, a loop will be needed. 
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = ('ducati')
motorcycles.remove(too_expensive)
print(motorcycles)

print(' \nA ' + too_expensive.title() + ' is too expensive for me.')
