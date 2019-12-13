import io
import sys
import unittest

from unittest.mock import patch

from day5.air_conditioner import process_intcode


class TestAirConditioner(unittest.TestCase):
    def test_process_intcode(self):
        self.assertEqual(process_intcode([1002, 4, 3, 4, 33], 1), [1002, 4, 3, 4, 99])
        self.assertEqual(process_intcode([1101, 100, -1, 4, 0], 1), [1101, 100, -1, 4, 99])

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_io(self):
        process_intcode([3, 0, 4, 0, 99], 1)
        self.assertEqual(sys.stdout.getvalue().strip(), '1')

    @patch('sys.stdout', new=io.StringIO())
    def test_process_intcode_io_mode(self):
        process_intcode([3, 1, 104, 2, 99], 1)
        self.assertEqual(sys.stdout.getvalue().strip(), '2')
