Rover challenge
===============

Problem Objective
-----------------

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the
rovers so that their on-board cameras can get a complete view of the
surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of
x and y co-ordinates and a letter representing one of the four cardinal
compass points. The plateau is divided up into a grid to simplify
navigation. An example position might be 0, 0, N, which means the rover
is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The
possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin
90 degrees left or right respectively, without moving from its current
spot. 'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

Running tests
-------------

In the current directory run the following commands::

    # install package using setup.py in editable mode
    pip install -e .
    # Install nose test from dependencies
    pip install -r requirements.txt
    # Run all the tests
    nosetests -w ./tests


Structure
---------

Source code of this challenge can be found in the `challenge` directory, the
 tests can be found in the `test` directory. In
 `tests.test_control.ControlCenterSuite:test_input` and example can be found
 with a command input which is given, and an output which is returned by the
 command center.