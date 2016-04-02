""" Python module for a robotic rover """


class Grid(object):
    """ This grid represents a rectangular plateau """

    def __init__(self, max_x, max_y):
        """ Initialize rover """
        if type(max_x) != int:
            raise ValueError(u'Max coordinate for X axis is not a number ')
        elif type(max_y) != int:
            raise ValueError(u'Max coordinate for Y axis is not a number ')

        self.max_x = max_x
        self.max_y = max_y

    def move(self, position, cmd):
        """ Process a move command and return a new coordinate """
        # TODO: process a movement from a given position
