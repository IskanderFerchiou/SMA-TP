import random

from pygame.math import Vector2

from body import Body
from creep import Creep
from obstacle import Obstacle


class Agent:

    def __init__(self, body=None):
        self.body = body
        self.listPerceptron = []
        self.uuid = random.randint(100000, 9999999999999999)

    def filtre(self):
        creeps = []
        obstacles = []
        predators = []
        preys = []
        for i in self.listPerceptron:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Creep):
                creeps.append(i)
            if isinstance(i, Obstacle):
                obstacles.append(i)
            if isinstance(i, Body):
                if i.mass > self.body.mass:
                    predators.append(i)
                else:
                    preys.append(i)
        creeps.sort(key=lambda x: x.dist, reverse=False)
        obstacles.sort(key=lambda x: x.dist, reverse=False)
        predators.sort(key=lambda x: x.dist, reverse=False)
        preys.sort(key=lambda x: x.dist, reverse=False)
        return creeps, obstacles, predators, preys

    def update(self):
        creeps, obstacles, predators, preys = self.filtre()
        if len(creeps) > 0:
            target = creeps[0].position
            self.body.acc = target - self.body.position
        else:
            target = Vector2(random.randint(-1, 1),  random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(1, 1))

        # target.scale_to_length(target.length() * self.coefCreep)

        if len(preys) > 0:
            target = preys[0].position - self.body.position

        if len(obstacles) > 0:
            target = self.body.position - obstacles[0].position
            # target.scale_to_length(1 / target.length() == 2)

        if len(predators) > 0:
            target = self.body.position - predators[0].position

        self.body.acc += target



    def show(self):
        self.body.show()


