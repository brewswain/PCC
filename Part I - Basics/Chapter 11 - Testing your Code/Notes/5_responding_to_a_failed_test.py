"""
What do you do when a test fails. Assuming you're checking the right 
conditions, a passing test means the function is behaving correctly 
and a failing test means there's an error in the new code you wrote.
So when a test fails, don't change the test. Instead, fix the code
that caused the test to fail. Examine the changes you just made to
the function, and figure out how those changes broke the desired 
behaviour.

In this case, get_formatted_name() used to require only two parameters:
a first name and a last name. Now it requires a first name, middle name, 
and last name. Now it requires a first name, middle name, and last name.
The addition of that mandatory middle name parameter broke the desired
behaviour of get_formatted_name(). The best option here is to make the
middle name optional. Once we do, our test for names like Janis Joplin
should pass again, and we should be able to accept middle names as well.

Let's modify get_formatted_name() so middle names are optional, and then 
run the test case again. If it passes, we'll move on to making sure the
function handles middle names properly. To make middle names optional, 
we move the parameter 'middle' to the end of the parameter list in the
function definition(heehee the jokes write themselves) and give it an 
empty default value. We also add an if test that builds the full name
properly, depending on whether or not a middle name is provided:
"""

# full_name_function_pass.py


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()


"""
In this new version of get_formatted_name(), the middle name is optional.
If a middle name is passed to the function(if middle:), the full name will
contain a first, middle, and last name. Otherwise, the full name will consist 
of just a first and last name. Now the function should work for both kinds of 
names. To find out if the  function still works for names like Janis Joplin,
let's run test_name_function.py again:

=================================================
|   .                                           |
|   ------------------------------------------  |
|   Ran 1 test in 0.000s                        |
|                                               |
|   OK                                          |
=================================================

The test case passes now. This is ideal; this means the function works for names
like Janis Joplin again without us having to test the function manually. Fixing 
our function was easy because the failed test helped us identify the new code 
that broke existing behaviour.
"""
