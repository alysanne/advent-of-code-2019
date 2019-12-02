import unittest

from puzzles.day1.fuel_calc import fuel_for_mass, sum_fuel, calc_total_fuel


class TestFuelCalc(unittest.TestCase):
    def setUp(self):
        pass

    def test_fuel_for_mass(self):
        self.assertEqual(fuel_for_mass(12), 2)
        self.assertEqual(fuel_for_mass(14), 2)
        self.assertEqual(fuel_for_mass(1969), 654)
        self.assertEqual(fuel_for_mass(100756), 33583)

    def test_sum_fuel(self):
        self.assertEqual(sum_fuel([1, 2, 3]), 6)
        self.assertEqual(sum_fuel([12, 1, 24, 9]), 46)
        self.assertEqual(sum_fuel([3, 8, 2, 95]), 108)

    def test_calc_total_fuel(self):
        self.assertEqual(calc_total_fuel(-10), 0)
        self.assertEqual(calc_total_fuel(14), 2)
        self.assertEqual(calc_total_fuel(1969), 966)
        self.assertEqual(calc_total_fuel(100756), 50346)
