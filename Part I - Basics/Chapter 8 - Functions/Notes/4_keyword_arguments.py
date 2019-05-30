"""
A keyword argument is a name-value pair that you pass to a function.
You directly associate the name and the value within the argument, 
so when you pass the argument to the function, there's no confusion.

Keyword arguments free you from the worry of correctly ordering 
your arguments in the function call, and they clarify the role of
each value in the function call.
"""


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')

"""
Then function hasn't changed. But when we call describe_pet(), we explicitly
tell Python which parameter each argument should be matched with. When Python
reads the function call, it know to store the argument 'hamster' in the 
parameter animal_type and the argument 'harry' in pet_name. The output 
correctly shows that we have a hamster named Harry.

The order of keyword arguments doesn't matter because Python knows where each 
value should go.
"""
