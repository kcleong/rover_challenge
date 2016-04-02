""" The control center module to control robotic rovers """
from challenge.rover import Rover


class ControlCenter(object):
    """ Control center to add rovers and to control the movements
    of a rover. This class is a singleton, there can only be one Houston.
    """

    __shared_state = {}

    def __init__(self):
        """ Initialize control center """
        self.__dict__ = self.__shared_state

    def input_command(self, cmd):
        """ Input command to control rovers """

    def add_rover(self, position):
        """ Add a rover to the plateau """

        return Rover(position)