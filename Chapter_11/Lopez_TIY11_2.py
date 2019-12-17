import unittest
import city_functions


class TestCityCountry(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city/country pairs like 'santiago'/'chile' work?"""
        city_country_formatted = city_functions.city_country_formatted('santiago', 'chile')
        self.assertEqual(city_country_formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does 'santiago', 'chile' , and 5000000 work?"""
        city_country_population_formatted = city_functions.city_country_formatted('santiago', 'chile', 5000000)
        self.assertEqual(city_country_population_formatted, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()

