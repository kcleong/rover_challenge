""" Python module for the grid and a position in a grid """


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
        position = Position(self, position)

        if cmd in ('L', 'R'):
            return position.turn(cmd)
        else:
            return position.move()


class Position(object):
    """ Represent a position in the grid """

    def __init__(self, grid, position):
        """
        """
        self.grid = grid
        self.x_coord = int(position[0])
        self.y_coord = int(position[1])
        self.direction = position[2]

    @property
    def formatted(self):
        return '{0}{1}{2}'.format(self.x_coord, self.y_coord, self.direction)

    def turn(self, side):
        """ Turn left or right, calculate which direction we are
        pointed to after turning.
        """

        directions = ['N', 'E', 'S', 'W']
        options = {'L': -1, 'R': 1}

        idx = directions.index(self.direction)
        sum = options.get(side)

        movement = idx + sum
        # At the end of the directions list, move index pointer to
        # the other side.
        if movement >= len(directions):
            movement = 0

        new_direction = directions[movement]
        self.direction = new_direction
        return self.formatted

    def move(self):
        """ Move one position forward
        """
        directions = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        movement = directions.get(self.direction)
        x_coord = self.x_coord + movement[0]
        y_coord = self.y_coord + movement[1]

        invalid = False
        if x_coord < 0 or x_coord > self.grid.max_x:
            raise ValueError('X coordinates are out of bounds')
        if y_coord < 0 or y_coord > self.grid.max_y:
            raise ValueError('Y coordinates are out of bounds')

        self.x_coord = x_coord
        self.y_coord = y_coord
        return self.formatted