# -*- coding: utf-8 -*-
from challenge.grid import Position

import unittest


class PositionTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_instantion(self):
        """ Test if we can instantiate a grid object """
        position = Position('33E')
        self.assertEqual(type(position), Position)

    def test_init(self):
        """ Test initialization of parameters in init method """
        pos_str = '31E'
        position = Position(pos_str)
        self.assertEqual(position.x_coord, 3)
        self.assertEqual(position.y_coord, 1)
        self.assertEqual(position.direction, 'E')

    def test_turn_left(self):
        """ Test a turn to the left """
        pos_str = '31E'
        position = Position(pos_str)

        coords = position.turn('L')
        self.assertEqual(position.direction, 'N')
        self.assertEqual(coords, '31N')

    def test_turn_right(self):
        """ Test a turn to the right """
        pos_str = '31E'
        position = Position(pos_str)

        coords = position.turn('R')
        self.assertEqual(position.direction, 'S')
        self.assertEqual(coords, '31S')

    def test_turn_edge_left(self):
        pos_str = '31N'
        position = Position(pos_str)

        coords = position.turn('L')
        self.assertEqual(position.direction, 'W')
        self.assertEqual(coords, '31W')

    def test_turn_edge_right(self):
        pos_str = '31W'
        position = Position(pos_str)

        coords = position.turn('R')
        self.assertEqual(position.direction, 'N')
        self.assertEqual(coords, '31N')


if __name__ == '__main__':
    unittest.main()