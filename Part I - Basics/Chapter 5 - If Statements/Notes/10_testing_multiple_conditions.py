"""
    The if-elif-else chain is powerful, but it's only appropriate to use when only one test is needed to pass.
Once Python passes one test, it skips the rest. This is useful, particular as it's efficient.
    However, there are situations where you would need to check all the conditions of interest. In these times,
you should use a chain of if statements without elif or else blocks. This technique makes sense when more than one 
condition could be True, and you wish o act on every True condition.
"""

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print('\nFinished making your pizza!')
