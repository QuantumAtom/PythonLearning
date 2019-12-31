import unittest
from city_functions import location

class CityLocationsTest(unittest.TestCase):
    """This will test if the city and country combo work"""
    def test_city_locations(self):
        """Do city and country names work?"""
        locale = location('Chicago', 'USA')
        self.assertEqual(locale, 'Chicago, USA')
    
    def test_city_country_populations(self):
        """Do city, country, and population data work"""
        locale = location('Chicago', 'USA', 2716000)
        self.assertEqual(locale, 'Chicago, USA - population 2716000')

unittest.main()


