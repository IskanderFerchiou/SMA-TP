import core
from agent import Agent
from body import Body

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    TOTAL_AGENTS = 50

    core.memory("totalAgents", TOTAL_AGENTS)
    core.memory("agents", [])
    core.memory("S", TOTAL_AGENTS)
    core.memory("I", 0)
    core.memory("R", 0)
    core.memory("D", 0)

    for i in range(0, TOTAL_AGENTS):
        core.memory("agents").append(Agent(Body()))

    print("Setup END-----------")


def computePerception():
    for a1 in core.memory("agents"):
        a1.listPerception = []
        for a2 in core.memory("agents"):
            if a1.body.fustrum.inside(a2.body) and a2.uuid != a1.uuid:
                a1.listPerception.append(a2)


def computeDecision():
    for agent in core.memory("agents"):
        agent.randomMove()


def applyDecision():
    for agent in core.memory("agents"):
        agent.body.applyDecision()
        agent.update()


def updateEnv():
    core.memory("S", 0)
    core.memory("I", 0)
    core.memory("R", 0)

    for a in core.memory("agents"):
        if a.status == 'S':
            core.memory("S", core.memory("S") + 1)
        elif a.status == 'I':
            core.memory("I", core.memory("I") + 1)
        elif a.status == 'R':
            core.memory("R", core.memory("R") + 1)
        elif a.status == 'D':
            # On retire les agents morts au lieu de continuer à les dessiner
            core.memory("agents").remove(a)

    core.memory("D", core.memory("totalAgents") - len(core.memory("agents")))


def displayStats():
    textColor = (135,206,235) # skyblue
    core.Draw.text(textColor, f'S : {round((core.memory("S") / core.memory("totalAgents")) * 100, 2)}%', (0, 0))
    core.Draw.text(textColor, f'I : {round((core.memory("I") / core.memory("totalAgents")) * 100, 2)}%', (150, 0))
    core.Draw.text(textColor, f'R : {round((core.memory("R") / core.memory("totalAgents")) * 100, 2)}%', (0, 40))
    core.Draw.text(textColor, f'D : {round((core.memory("D") / core.memory("totalAgents")) * 100, 2)}%', (150, 40))

def run():
    core.cleanScreen()

    # Reset button
    if core.getKeyPressList("r"):
        setup()

    # Mouse left click
    if core.getMouseLeftClick():
        mousePosition = core.getMouseLeftClick()
        nearestAgent = None
        nearestAgentDistance = 100000
        for agent in core.memory("agents"):
            if agent.body.position.distance_to(mousePosition) <= nearestAgentDistance:
                nearestAgent = agent
                nearestAgentDistance = agent.body.position.distance_to(mousePosition)
        if nearestAgent is not None and nearestAgent.status == 'S':
            nearestAgent.status = 'I'

    # Display agents
    for agent in core.memory("agents"):
        agent.show()

    # Simulation
    computePerception()
    computeDecision()
    applyDecision()
    updateEnv()
    displayStats()


core.main(setup, run)
