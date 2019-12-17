import unittest

from day3.crossed_wires import find_closest_intersection, get_coordinates, find_min_intersection


class TestCrossedWires(unittest.TestCase):
    def test_find_closest_intersection(self):
        self.assertEqual(find_closest_intersection('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                                                   'U62,R66,U55,R34,D71,R55,D58,R83'), 159)
        self.assertEqual(find_closest_intersection('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                                                   'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'), 135)

    def test_get_coordinates_set(self):
        self.assertEqual(get_coordinates('R1,D2,R1,U2'), ({(1, 0), (1, -1), (1, -2), (2, -2), (2, -1), (2, 0)},
                                                          {(1, 0): 1, (1, -1): 2, (1, -2): 3, (2, -2): 4,
                                                           (2, -1): 5, (2, 0): 6}))
        self.assertEqual(get_coordinates('R1,D1,U1'), ({(1, 0), (1, -1)}, {(1, 0): 1, (1, -1): 2}))

    def test_find_min_intersection(self):
        self.assertEqual(find_min_intersection('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                                               'U62,R66,U55,R34,D71,R55,D58,R83'), 610)
        self.assertEqual(find_min_intersection('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                                               'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'), 410)
