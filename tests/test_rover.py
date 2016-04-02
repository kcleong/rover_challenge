# -*- coding: utf-8 -*-
from challenge.rover import Rover
from .context import challenge

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


if __name__ == '__main__':
    unittest.main()