import unittest
from city_functions import get_location_name

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do names like Santiago, Chile work?"""
        name = get_location_name('santiago', 'chile')
        self.assertEqual(name, 'Santiago, Chile - population size unknown')

    def test_city_country_population(self):
        """Do cities with populations work?"""
        name = get_location_name('santiago', 'chile', 5000000)
        self.assertEqual(name, 'Santiago, Chile - population 5000000')

unittest.main()