# -*- coding: utf-8 -*-
from challenge.grid import Grid
from challenge.rover import Rover

import unittest


class GridTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_instantion(self):
        """ Test if we can instantiate a rover object """
        grid = Grid(5, 5)
        self.assertEqual(type(grid), Grid)

    def test_xy_max(self):
        """ Test if a given coords are set in the grid """
        max_x = 7
        max_y = 9

        grid = Grid(max_x, max_y)
        self.assertEqual(grid.max_x, max_x)
        self.assertEqual(grid.max_y, max_y)

    def test_turn(self):
        """ Test a turn movement in the grid """

        starting_pos = '12N'
        turn = 'L'

        grid = Grid(5, 5)
        output = grid.move(starting_pos, turn)

        self.assertEqual(output, '12W')

    def test_movement(self):
        """ Test a forward movement in the grid """
        starting_pos = '12W'
        movement = 'M'

        grid = Grid(5, 5)
        output = grid.move(starting_pos, movement)

        self.assertEqual(output, '02W')


if __name__ == '__main__':
    unittest.main()