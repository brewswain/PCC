import unittest
from city_functions import city_details


class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Does function work when population is withheld??"""
        formatted_details = city_details('tacarigua', 'trinidad')
        self.assertEqual(formatted_details, 'Tacarigua, Trinidad.')


unittest.main()
