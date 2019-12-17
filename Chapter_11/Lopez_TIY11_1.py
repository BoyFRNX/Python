import unittest
import city_functions


class TestCityCountry(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        """Do city/country pairs like 'santiago'/'chile' work?"""
        city_country_formatted = city_functions.city_country_formatted('santiago', 'chile')
        self.assertEqual(city_country_formatted, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
