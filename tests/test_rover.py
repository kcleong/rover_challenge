# -*- coding: utf-8 -*-
from challenge.grid import Grid
from challenge.rover import Rover

import unittest


class RoverTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_instantion(self):
        """ test if we can instantiate a rover object """
        rover = Rover('00N')

        self.assertEqual(type(rover), Rover)

    def test_position(self):
        """ Test if the rover can return the current position
        """
        pos = '00N'
        rover = Rover(pos)
        self.assertEqual(rover.position, pos)

    def test_movement(self):
        """ Test one movement to turn of move the rover
        """
        # TODO: instantiate new rover and move into position
        self.assertTrue(None)

    def test_movement_delegation(self):
        """ The move method in a rover uses a grid object to calculate
        movement. The grid object is given as parameter in the move method.
        """
        class DummyGrid(object):
            def move(self, position, cmd):
                """ simple method for this test"""
                return '{0}-{1}'.format(position, cmd * 2)

        pos = '22S'
        rover = Rover(pos)
        grid = DummyGrid()  # Create a dummy grid
        output = rover.move(grid, 'L')  # Pass grid and movement to move method

        # The output should be equal to 22S-LL
        self.assertEqual(output, '{0}-LL'.format(pos))



if __name__ == '__main__':
    unittest.main()