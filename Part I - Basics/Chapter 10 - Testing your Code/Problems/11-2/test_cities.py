import unittest
from city_functions import city_details


class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Does ('tacarigua', 'trinidad') work?"""
        formatted_details = city_details('tacarigua', 'trinidad')
        self.assertEqual(formatted_details, 'Tacarigua, Trinidad.')

    def test_city_country_population(self):
        """Does function work when population is included?"""
        formatted_details = city_details('tacarigua', 'trinidad', 5)
        self.assertEqual(formatted_details,
                         'Tacarigua, Trinidad.\nPopulation: 5')


unittest.main()
