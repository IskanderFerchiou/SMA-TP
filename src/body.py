import random

from pygame.math import Vector2

import core
from fustrum import Fustrum


class Body:

    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.fustrum = Fustrum(self, 150)
        self.vitesse = Vector2()
        self.vMax = 10
        self.acc = Vector2()
        self.accMax = 5
        self.mass = 10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def applyDecision(self):
        if self.acc.length() > self.accMax/self.mass:
            self.acc.scale_to_length(self.accMax/self.mass)

        self.vitesse += self.acc

        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        self.position += self.vitesse

        self.acc = Vector2()

        self.edge()

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)

    def edge(self):
        if self.position.x <= 0:
            self.vitesse.x *= -1
        if self.position.x >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= 0:
            self.vitesse.y *= -1
        if self.position.y >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1