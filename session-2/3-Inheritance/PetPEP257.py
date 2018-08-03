# -*- coding: utf-8 -*-
"""

This module contains a single base class from which to create different pets.

It also follows PEP257 style guide to commenting. You can find out more about
this here: https://www.python.org/dev/peps/pep-0257/

Example:

    Test this script conforms to PEP257 by installing PEP257 and then process
    the script. You can do this by typing these commands:

    $ pip install pep257
    $ pep257 PetPEP257.py

Todo:
    * Consider the results of food???

"""

class Pet:
    """
    Base class for generic pet.

    This is a base class to define a pet. This should never be used
    directly but instead, inherited from to create a variety of domestic
    pets.

    """

    def __init__(self):
        """instantiate a basic pet."""
        print('What started as a pet...')
        self.posX = 0
        self.posY = 0
        self.name = 'unknown'
        self.foodKg = 1
        self.sleep = 1
        self.exercise = 1
        self.speed = 1

    def eat(self):
        """Execute the eat behaviour and output result."""
        for x in range(self.foodKg):
            println('nom ')

    def sleep(self):
        """Sleep for the required time."""
        for x in range(self.sleep):
            println('z ')

    def exercise(self):
        """Calculate the distance travelled in exercise and moves pet there."""
        dist += self.exercise * self.speed
        self.xPos+= dist
        println(self.name + ' has travelled ' + dist + ' mile')
