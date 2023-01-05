import random

from pygame.math import Vector2

import core


class Creep(object):

    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.mass = 5
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.uuid = random.randint(100000, 9999999999999999)

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)

