"""
When you pass a list to a function, the function can modify the list.
Any changes made to the list inside the function's body are permanent,
allowing you to work efficiently even when you're dealing with large
amounts of data.

Consider a company that creates 3D printed models of designs that users 
submit. Designs that need to be printed are stored in a list, and after 
being printed they're moved to a separate list. The following code
accomplishes this without functions:
"""

# Start with designs that need need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)


# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


"""
This program starts with a list of designs that need to be printed and
an empty list called completed_models that each design will be moved to
after it has been printed. As long as designs remain in unprinted_designs,
the while loop simulates printing each design by removing a design from
the end of the list, storing it in current_design, and displaying a message
that the current design is being printed. 

It then adds the design to the list of the completed models. When the loop 
is finished running, a list of the designs that have been printed is displayed.

We can reorganise this code by writing two functions, each of which does one
specific job. Most of the code won't change, we're just making it more efficient.
The first function will handle printing the designs, and the second will summarise
the prints that have been made:
"""


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


"""
This program is easier to extend and maintain than the version without
functions. If we need  to print more designs later on, we can simply call
print_models() again. If we realise the printing code needs to be modified,
we can change the code once, and our changes will take place everywhere the 
function is called. This technique is more efficient than having to update
code separately in several places in the program.

This example also demonstrates the idea that every function should have one
specific job. The first function prints each design, and the second displays 
the completed models. This is more beneficial than using one function to do
both jobs. Remember that you can always call a function from another function, 
which can be helpful when splitting a complex task into a series of steps.
"""
