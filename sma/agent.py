import random
import core

from pygame.math import Vector2

from epidemie import epidemie


class Agent:

    def __init__(self, body=None):
        self.body = body
        self.listPerception = []
        self.uuid = random.randint(100000, 9999999999999999)
        self.status = "S"
        self.epidemie = epidemie.copy()
        self.startIncubation = False


    def randomMove(self):
        self.body.acc = Vector2(random.randint(-10, 10), random.randint(-10, 10))

    def update(self):
        # Gestion de l'incubation
        if self.status == "S":
            if self.startIncubation:
                self.epidemie["dureeIncubation"] -= 1
            if self.epidemie["dureeIncubation"] == 0:
                self.status = "I"

        # Gestion de la contamination
        if self.status == "I":
            if self.epidemie["dureeAvantContagion"] == 0:
                # la taille du frustrum est la distance minimum de contagion
                for agent in self.listPerception:
                    if agent.status == "S":
                        if random.random() < self.epidemie["pourcentageContagion"]:
                            agent.startIncubation = True
            else:
                self.epidemie["dureeAvantContagion"] -= 1

            # Gestion des décès et des guérisons
            if self.epidemie["dureeAvantDeces"] == 0:
                if random.random() < self.epidemie["pourcentageMortalite"]:
                    self.status = "D"
                else:
                    self.status = "R"
            else:
                self.epidemie["dureeAvantDeces"] -= 1

    def show(self):
        color = (255, 255, 255)

        if self.status == "I":
            color = (255, 0, 0)
            core.Draw.circle(color, self.body.position, self.body.fustrum.radius, 1)
        elif self.status == "R":
            color = (0, 255, 0)

        core.Draw.circle(color, self.body.position, self.body.mass)


