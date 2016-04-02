# -*- coding: utf-8 -*-
""" Test suite to test the control center which is in contact
with the rovers.
"""

import unittest

from challenge.controlcenter import ControlCenter
from challenge.grid import Grid


class ControlCenterSuite(unittest.TestCase):
    """ Unit tests for control center """

    def test_input(self):
        """ Test if a given input string given to the command center has the
        expected output from the center itself.
        """
        input_str = '55\n'  # Max X Y coords of grid
        input_str += '12N\n'  # Starting pos of 1th rover
        input_str += 'LMLMLMLMM\n'  # Movement for 1th rover
        input_str += '33E\n'  # Starting pos of 2th rover
        input_str += 'MMRMMRMRRM'

        output_str = '13N\n51E'

        control = ControlCenter()
        return_value = control.input_command(input_str)

        # The control object has a grid attribute
        self.assertTrue(hasattr(control, 'grid'))
        # This grid attribute is from the Grid class
        self.assertEqual(type(control.grid), Grid)
        # There are three rovers present
        self.assertEqual(len(control.rovers), 3)

        # TODO: call control center and execute command
        self.assertEquals(output_str, return_value)

    def test_add_rover(self):
        """ Test if a rover can be added using the control center
        """
        control = ControlCenter()
        rover = control.add_rover('00N')

        # Currently there is one rover active
        self.assertEqual(1, len(control.rovers))
        # And rover returned by control is the same as the rover in the list
        self.assertEqual(rover, control.rovers[0])

    def test_multiple_rovers(self):
        """ Test if multiple rovers can be added to the control center """
        control = ControlCenter()
        first = control.add_rover('00N')
        second = control.add_rover('32S')
        third = control.add_rover('05E')

        # Currently there are three rovers active
        self.assertEqual(3, len(control.rovers))
        # Test if each rover is present in control center
        self.assertEqual(first, control.rovers[0])
        self.assertEqual(second, control.rovers[1])
        self.assertEqual(third, control.rovers[2])

    def control_center_singleton(self):
        """ Instantiate control center and check if there can be
        only one control center.
        """
        # TODO: call control center multiple times and check we have
        # the same center every time
        first = ControlCenter()
        second = ControlCenter()

        first.rovers = 'spam bacon ham eggs'
        # There can be only one control center
        self.assertEqual(first.rovers, second.rovers)


if __name__ == '__main__':
    unittest.main()