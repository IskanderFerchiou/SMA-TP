import random

from pygame.math import Vector2

import core
from fustrum import Fustrum

from epidemie import epidemie

class Body:

    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.fustrum = Fustrum(self, epidemie["distanceMinContagion"])
        self.vitesse = Vector2()
        self.vMax = 10
        self.acc = Vector2()
        self.accMax = 5
        self.mass = 10

    def applyDecision(self):
        if self.acc.length() > self.accMax:
            self.acc.scale_to_length(self.accMax)
        self.vitesse += self.acc

        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)
        self.position += self.vitesse

        self.acc = Vector2(0, 0)

        self.edge()

    def edge(self):
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x < 0:
            self.position.x = 0
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y < 0:
            self.position.y = 0