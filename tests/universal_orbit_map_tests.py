import unittest

from day6.universal_orbit_map import checksum_orbits, calculate_distance


class TestUniversalOrbitMap(unittest.TestCase):
    def test_checksum(self):
        self.assertEqual(checksum_orbits(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']), 42)
        self.assertEqual(checksum_orbits(['E)F', 'B)C', 'B)G', 'J)K', 'K)L', 'G)H', 'COM)B', 'D)E', 'D)I', 'E)J', 'C)D']), 42)

    def test_calculate_distance(self):
        self.assertEqual(calculate_distance(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']), 4)
        self.assertEqual(calculate_distance(['E)F', 'B)C', 'I)SAN', 'B)G', 'J)K', 'K)YOU', 'K)L', 'G)H', 'COM)B', 'D)E', 'D)I', 'E)J', 'C)D']), 4)
