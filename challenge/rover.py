""" Python module for a robotic rover """


class Rover(object):
    """ Robotic rover which can be moved """

    def __init__(self, position):
        """ Initialize rover """
        self.position = position

    def move(self, grid, cmd):
        """ Move rover one movement at a time """
        return grid.move(self.position, cmd)
