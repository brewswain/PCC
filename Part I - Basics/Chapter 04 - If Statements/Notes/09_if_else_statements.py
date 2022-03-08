"""    
    There are many cases in which you'd want to take an action when a conditional test passes, and a different action in all other cases. 
During these situations, the if-else syntax is very useful. 

    The else statement allows you to set a block of options that are executed when the conditional test fails.
"""

age = 17

if age >= 18:
    print('You are old enough to vote!')
    print('have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')


# if-elif-else chain

"""
    There are many times where you'll need to test more than two possible situations, which is where if-elif-else syntax comes in.
Python executes only one block in an if-elif-else chain. It runs each conditional test in order until one passes. When a test passes, the code following that test is executed and python skips the rest of the tests.
The following example  considers an amusement park that charges different rates for different age groups.
    There's no limit to the amount of elif blocks that you can use in your code. If the amusement park were to implement a discount for seniors, you could add another test to see
whether someone qualifies for the senior discount.
"""

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print('Your admission cost is $' + str(price) + '.')


# Omitting the else Block

"""
    Python doesn't require an else block at the end of an if-elif chain. Sometimes an else block is useful; 
sometimes it's clearer to use an additional elif statement that catches the condition of interest.
    The else block is a catchall statement. It matches any condition that wasn't matched by a specific if/elif test,
which can potentially include invalid or even malicious data.
    If you have a specific final condition you're testing for, using a final elif block and omitting the else block will 
provide extra confidence that your code will only run under the correct circumstances.
"""

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print('Your admission cost is $' + str(price) + '.')
