"""
When you start to use function, don't be surprised if you encounter
errors about unmatched arguments. Unmatched arguments occur when
you provide fewer or more arguments than a function needs to do
its work.

For example, here's what happens if we try to call describe_pet()
with no arguments:

def describe_pet(pet_name, animal_type='dog'):
    # Display information about a pet.
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet()



Python recognizes that some information is missing from the function
call, and the traceback tells us:
"TypeError: describe_pet() missing 2 required positional arguments: 
'animal_type' and 'pet_name'."

Python is helpful in that it reads the function's code for us and tells
us the names of the arguments ywe need to provide, thus providing
further motivation to give your variables and functions descriptive names.
This will help Python's error messages be more useful to both you and 
whoever might use your code.
"""
