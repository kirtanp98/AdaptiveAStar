import random
from src.Path.Astar import Astar
from src.Path.Generator import Generator
from src.Utility.Helper import Helper
from src.Path.RepeatedAstar import RepeatedAstar, BinaryHeapQueue

if __name__ == '__main__':
    generator = Generator()

    matrix = generator.decode("resources/map5")

    start = generator.startState
    goal = generator.goalState

    agent_matrix = generator.generateAgentMatrix(matrix, start)
    agent_start = agent_matrix[start.xPos][start.yPos]
    agent_goal = agent_matrix[goal.xPos][goal.yPos]
    algo = RepeatedAstar()

    algo.real_matrix = matrix
    algo.observe_matrix = agent_matrix
    algo.o_start = agent_start
    algo.o_goal = agent_goal

    state = algo.repeatedAstar(start, goal)

    helper = Helper()

    helper.generate_sol_file(matrix,state)



