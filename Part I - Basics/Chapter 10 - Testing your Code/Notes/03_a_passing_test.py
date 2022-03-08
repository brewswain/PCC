"""
The syntax for setting up a test case takes some getting used to, but once 
you've set up the test case it's straightforward to add more unit tests for
your functions. To write a test case for a function, import the unittest
module and the function you want to test. Then, create a class that inherits
from unittest.TestCase, and write a series of methods to test different 
aspects of your function's behaviour.

Here's a test case with one method that verifies that the function 
get_formatted_name() - Located in 1_testing_a_function.py, works correctly 
when given a first and last name:
"""

import unittest
from tests.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()


"""
First we import unittest and the function we want to test, get_formatted_name().
At line 18, we create a class called NamesTestCase, which will contain a series of
unit tests for get_formatted_name() . You can name the class anything you want, 
but it's best to call it something related to the function you're about to test and
use the word Test in the class name. This class MUST inherit from the class 
'unittest.TestCase' so Python knows how to run the tests you write.

NamesTestCase contains a single method that tests one aspect of get_formatted_name().
We call this method test_first_last_name() because we're verifying that names with
only a first and last name are formatted correctly.  Any method that starts with
'test_' will be run automatically when we run this program. Within this test method,
we call the function we want to test and store a return value that we're interested 
in testing. In this example we call get_formatted_name() with the arguments 'janis'
and 'joplin', and store the result in formatted_name(line 23).

At line 24, we use one of unittest's most useful features: An assert method. Assert
methods verify that a result you received matches the result you expected to receive.
In this case, because we know get_formatted_name() is supposed to return a 
capitalized, properly spaced full name, we expect the value in formatted_name to be
'Janis Joplin'. To check if this is true, we use unittest's assertEqual() method and 
pass it formatted_name and 'Janis Joplin'. 

The line "self.assertEqual(formatted_name, 'Janis Joplin')" says, "Compare the value 
in formatted_name to the string 'Janis Joplin'. If they are equal as expected, fine. 
But if they don't match, let me know."

The line unittest.main() tells Python to run the tests in this file. When we run this
program, we get the following output:

=================================================
|   .                                           |
|   ------------------------------------------  |
|   Ran 1 test in 0.000s                        |
|                                               |
|   OK                                          |
=================================================

The dot on the first line of output tells us that a single test passed. The next line
tells us that Python ran one test, and it took less than 0.001 seconds to run. The
final OK tells us that all unit tests in the test case passed.

This output indicates that the function get_formatted_name() will always work for names
that have a first and last name unless we modify the function. When we modify 
get_formatted_name(), we can run this test again. If the test case passes, we know the 
function will still work for names like Janis joplin.
"""
