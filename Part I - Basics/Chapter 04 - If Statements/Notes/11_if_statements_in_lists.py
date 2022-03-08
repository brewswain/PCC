"""
    The combination of if statements and lists, allows for interesting applications.
You can watch for special values that need to be treated differently from other values in the list.
You can manage changing conditions efficiently, such as the availability of specific items in a restaurant etc.
You can also begin to prove that your code works as you expct it to in all possible situations.
"""


# Checking For Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + '.')

print('\nFinished making your pizza!')


"""
The above program is simple, but what if the pizzeria runs out of green peppers? Here is where the if statement comes in.
"""


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')


# Checking That A List Is Not Empty


"""
Every list we've worked with so far has been done with the assumption that they contain at least one item in it. 
Soon, we'll let users provide the info that's stored in a list, so it doesn't make sense to assume that a list has any items in it each time a loop is run.
"""


requested_toppings = []

# When the name of a list is used in an if statement, Python returns True if the list contains at least one item, and False if it's empty.
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinished Making your pizza!')
# Since the list requested_toppings is empty, it fails the conditional test on line 43, causeing this else condition to execute.
else:
    print('Are you sure you want a plain pizza?')


# Using Multiple Lists

"""
You can use lists and if statements to make sure your input makes sense before you act on it.
Following the pizzeria example, let's watch out for unusual topping requests before we build a pizza.
"""

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'extra cheese', 'pepperoni', 'pineapple']
requested_toppings = ['mushrooms', 'bananas', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print('\nFinished making your pizza!')
