"""
To exit a while loop immediately without running any remaining
code in the loop, regardless of the results of any conditional test,
use the break statement. The break statement directs the flow
of your program; you can use it to control which lines of code are
executed and which aren't, so the program only executes code that
you want it to, when you want it to.

We can stop the while loop in the below program by calling break
as soon as the user enters the 'quit' value.
"""

prompt = '\nPlease enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished.) "

# A while loop that tarts with while True will run forever unless it reaches a break statement.
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to  " + city.title() + '!')


"""
You can use the break statement in any of Python's loops. 
For example, you could use break to quit a for loop that's
working through a list or a dictionary.
"""
