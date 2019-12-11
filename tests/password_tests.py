import unittest

from day4.password import calc_possible_passwords, check_if_valid


class TestPassword(unittest.TestCase):
    def test_calc_possible_passwords(self):
        self.assertEqual(calc_possible_passwords(236791, 236799), 1)

    def test_check_if_valid(self):
        self.assertEqual(check_if_valid('112233'), True)
        self.assertEqual(check_if_valid('123444'), False)
        self.assertEqual(check_if_valid('111122'), True)
        self.assertEqual(check_if_valid('135679'), False)
        self.assertEqual(check_if_valid('223450'), False)
        self.assertEqual(check_if_valid('123789'), False)
