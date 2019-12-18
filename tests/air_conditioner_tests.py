import io
import sys
import unittest

from unittest.mock import patch

from puzzles.day5.air_conditioner import process_intcode


class TestAirConditioner(unittest.TestCase):
    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_io(self):
        process_intcode([3, 0, 4, 0, 99], 1)
        self.assertEqual(sys.stdout.getvalue().strip(), '1')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_io_mode(self):
        process_intcode([3, 1, 104, 2, 99], 1)
        self.assertEqual(sys.stdout.getvalue().strip(), '2')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_true_comparisons_position_mode(self):
        process_intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8)
        self.assertEqual(sys.stdout.getvalue().strip(), '1')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_false_comparisons_position_mode(self):
        process_intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 13)
        self.assertEqual(sys.stdout.getvalue().strip(), '0')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_true_comparisons_immediate_mode(self):
        process_intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8)
        self.assertEqual(sys.stdout.getvalue().strip(), '1')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_false_comparisons_immediate_mode(self):
        process_intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], 11)
        self.assertEqual(sys.stdout.getvalue().strip(), '0')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_true_jump_position_mode(self):
        process_intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0)
        self.assertEqual(sys.stdout.getvalue().strip(), '0')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_false_jump_immediate_mode(self):
        process_intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 3)
        self.assertEqual(sys.stdout.getvalue().strip(), '1')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_long_input_1(self):
        process_intcode([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 3)
        self.assertEqual(sys.stdout.getvalue().strip(), '999')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_long_input_2(self):
        process_intcode([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8)
        self.assertEqual(sys.stdout.getvalue().strip(), '1000')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_long_input_3(self):
        process_intcode([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 21)
        self.assertEqual(sys.stdout.getvalue().strip(), '1001')
