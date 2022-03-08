"""
What does a filing test look like? Let's modify get_formatted_name() so
it can handle middle names, but we'll do so in a way that breaks the
function for names with just a first and last name, like Janis Joplin.

Here's a new version of get_formatted_name() that requires a middle
name argument:
"""


def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()


"""
This version should work for people with middle names, but when we test
it, we see that we've broken the function for people with just a first
and last name. This time, running the file test_name_function.py
gives this output:

=======================================================================================
|   E                                                                                 |
|=====================================================================================|
|   ERROR: test_first_last_name (__main__.NamesTestCase)                              |
|   Do names like 'Janis Joplin' work?                                                |
|-------------------------------------------------------------------------------------|                                                        |
|   Traceback (most recent call last):                                                |
|   (TypeError: get_formatted_name() missing 1 required positional argument: 'last')  |                      |
|-------------------------------------------------------------------------------------|
|   Ran 1 test in 0.001s                                                              |
|                                                                                     |
|   FAILED (errors=1)                                                                 |
=======================================================================================

There's a lot of information here because there's a lot you might need
to know when a test fails. The first item in the output is a single 'E'
which tells us one unit test in the test case resulted in an error. 
Next, we see that test_first_last_name3() in NamesTestCase caused an
error(line 26).

Knowing which test failed is critical when your test case contains many 
unit tests. At line 29 we see a standard traceback, which reports that
the function call get_formatted_name('janis', 'joplin') no longer works
because it's missing a required positional argument.

We also see that one test was run(line32). Finally, we see an additional 
message that the overall test case failed and that one error occurred
when running the test case(line 33). This information appears at the end
of the output so you see it right away; you don't want to scroll up through
a long output listing to find out how many tests failed.
"""
