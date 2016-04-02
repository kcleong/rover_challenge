# -*- coding: utf-8 -*-
""" Test suite to test the control center which is in contact
with the rovers.
"""

import unittest


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

        # TODO: call control center and execute command
        self.assertEquals(None, output_str)

    def test_add_rover(self):
        """ Test if a rover can be added using the control center
        """
        # TODO: call control center and add rover
        # control = ControlCenter().add_rover('12N')
        self.assertTrue(None)

    def control_center_singleton(self):
        """ Instantiate control center and check if there can be
        only one control center.
        """
        # TODO: call control center multiple times and check we have
        # the same center every time
        self.assertTrue(None)


if __name__ == '__main__':
    unittest.main()