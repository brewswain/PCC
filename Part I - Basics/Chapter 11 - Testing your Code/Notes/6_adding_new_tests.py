"""
Now that we know get_formatted_name() works for simple names again, let's write
a second test for people who include a middle name. We do this by adding another
method to the class NamesTestCase:
"""
import unittest

# This method to import from a differentfolder only works if there's an __init__.py in said folder
from tests.full_name_function_pass import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like Wolfgang Amadeus Mozart Work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()

"""
