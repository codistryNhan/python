import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
  def test_city_country(self):
    """Does 'San Francisco USA' work?"""
    city_country_name = city_country('san francisco', 'usa')
    self.assertEqual(city_country_name, 'San Francisco, Usa')

  def test_city_country_population(self):
    """Does 'Dallas, USA  800000' work?"""
    city_country_population = city_country('dallas','usa', '800000')
    self.assertEqual(city_country_population, 'Dallas, Usa - population 800000')

unittest.main() 
