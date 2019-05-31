"""
Sometimes you won't know ahead of time how many arguments a function
needs to accept. Fortunately, Python allows a function to collect an
arbitrary number of arguments from the calling statement.

For example, consider a function that builds a pizza. It needs to 
accept a number of toppings, but you can't know ahead of time how many
toppings a person will want. AThe function in the following example has
one parameter, *toppings, but this parameter collects as many arguments
as the calling line provides:
"""


# def make_pizza(*toppings):
#     """Print the list of toppings requested."""
#     print(toppings)


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


"""
The asterisk in the parameter name *toppings tells Python to make an empty
tuple called toppings and pack whatever values it receives into this tuple.
The print statement in the function body produces output showing that 
Python can handle a function call with one value and a call with 3 values.

Note that Python packs the arguments into a tuple, even if the function 
receives only one value:
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')

Now, we can replace the print statement with a loop that runs through the 
list of toppings and describes the pizza being ordered:
"""


def make_pizza(*toppings):
    """Summarize the pizza we're about to make."""
    print("\nMaking a pizza with the following toppings:")

    for topping in toppings:
        print("- " + topping.title())


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
