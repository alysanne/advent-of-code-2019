import unittest

from day6.universal_orbit_map import checksum_orbits


class TestUniversalOrbitMap(unittest.TestCase):
    def test_checksum(self):
        self.assertEqual(checksum_orbits(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']), 42)
        self.assertEqual(checksum_orbits(['E)F', 'B)C', 'B)G', 'J)K', 'K)L', 'G)H', 'COM)B', 'D)E', 'D)I', 'E)J', 'C)D']), 42)









