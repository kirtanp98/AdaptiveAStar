import random
from src.Path.Astar import Astar
from src.Path.Generator import Generator
from src.Utility.Helper import Helper
from src.Path.RepeatedAstar import RepeatedAstar, BinaryHeapQueue

if __name__ == '__main__':
    generator = Generator()
   # generator.generateRandomMap(2,2,"test")

    matrix = generator.decode("resources/map3")

    start = generator.startState
    goal = generator.goalState

    # algo = Astar()
    #
    # state = algo.search(matrix,start,goal)
    #
    # helper = Helper()

    algo = RepeatedAstar()
    algo.matrix = matrix
    algo.goal = goal

    state = algo.repeatedAstar(start, goal)

    helper = Helper()

    # creates a solution file with the path image
    helper.generate_sol_file(matrix,start)



