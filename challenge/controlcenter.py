""" The control center module to control robotic rovers """
from challenge.grid import Grid
from challenge.rover import Rover


class ControlCenter(object):
    """ Control center to add rovers and to control the movements
    of a rover. This class is a singleton, there can only be one Houston.
    """

    __shared_state = {}

    def __init__(self):
        """ Initialize control center """
        self.__dict__ = self.__shared_state
        self.rovers = []
        self.grid = None

    def input_command(self, cmd):
        """ Input command to control rovers """
        commands = cmd.split('\n')
        if len(commands) < 3:
            raise ValueError(
                u'Input command does not contain enough lines')

        commands.reverse()  # Reverse command so first command is on top

        coords = commands.pop()
        if len(coords) != 2:
            raise ValueError(
                u'First line with maximum grid coordinates is incorrect')

        max_x = int(coords[0])
        max_y = int(coords[1])
        self.grid = Grid(max_x, max_y)

        # TODO: process input commands

    def add_rover(self, position):
        """ Add a rover to the plateau """
        rover = Rover(position)
        self.rovers.append(rover)
        return rover
