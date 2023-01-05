import random
from pygame.math import Vector2
import core
from agent import Agent
from body import Body
from creep import Creep
from obstacle import Obstacle


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("agents", [])
    core.memory("creeps", [])
    core.memory("obstacles", [])

    for i in range(0, 5):
        core.memory("agents").append(Agent(Body()))

    for i in range(0, 50):
        core.memory("creeps").append(Creep())

    for i in range(0, 3):
        core.memory("obstacles").append(Obstacle())

    print("Setup END-----------")


def computePerception(agent):
    allObjects = core.memory("agents") + core.memory("creeps") + core.memory("obstacles")
    agent.listPerceptron = []
    for obj in allObjects:
        if agent.body.fustrum.inside(obj) and obj.uuid != agent.uuid:
            if hasattr(obj, "body"):
                agent.listPerceptron.append(obj.body)
            else:
                agent.listPerceptron.append(obj)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.applyDecision()


def updateEnv():
    for a in core.memory("agents"):

        for c in core.memory("creeps"):
            if a.body.position.distance_to(c.position) <= a.body.mass:
                c.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
                c.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                a.body.mass += 1

        for o in core.memory("obstacles"):
            if a.body.position.distance_to(o.position) <= a.body.mass:
                core.memory("agents").remove(a)

        for b in core.memory("agents"):
            if b.uuid != a.uuid:
                if a.body.position.distance_to(b.body.position) <= a.body.mass + b.body.mass:
                    if a.body.mass < b.body.mass:
                        b.body.mass += a.body.mass/2
                        core.memory("agents").remove(a)
                    else:
                        a.body.mass += b.body.mass/2
                        core.memory("agents").remove(b)

def run():
    core.cleanScreen()

    #Display
    for agent in core.memory("agents"):
        agent.show()
    
    for creep in core.memory("creeps"):
        creep.show()

    for obstacle in core.memory("obstacles"):
        obstacle.show()
        
    for agent in core.memory("agents"):
        computePerception(agent)
        
    for agent in core.memory("agents"):
        computeDecision(agent)
    
    for agent in core.memory("agents"):
        applyDecision(agent)
    
    updateEnv()
    
    
     
core.main(setup, run)
