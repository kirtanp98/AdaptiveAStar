from src.Path.RepeatedAstar import RepeatedAstar
from src.Path.Generator import Generator
from src.Utility.Helper import Helper
from src.Path.AdaptiveAstar import AdaptiveAstar


class AlgorithmPicker:

    gen = Generator()
    def executeForwardAstar(self,fileName):
        matrix = self.gen.decode(fileName)

        start = self.gen.startState
        goal = self.gen.goalState

        agent_matrix = self.gen.generateAgentMatrix(matrix, start)
        agent_start = agent_matrix[start.xPos][start.yPos]
        agent_goal = agent_matrix[goal.xPos][goal.yPos]
        algo = RepeatedAstar()

        algo.real_matrix = matrix
        algo.observe_matrix = agent_matrix
        algo.o_start = agent_start
        algo.o_goal = agent_goal

        state = algo.repeatedAstar(start, goal)

        helper = Helper()
        helper.generate_sol_file(matrix, state)

    def executeBackwardsAStar(self, fileName):
        matrix = self.gen.decode(fileName)

        start = self.gen.goalState
        goal = self.gen.startState

        agent_matrix = self.gen.generateAgentMatrix(matrix, start)

        agent_start = agent_matrix[start.xPos][start.yPos]
        agent_goal = agent_matrix[goal.xPos][goal.yPos]
        algo = RepeatedAstar()

        algo.real_matrix = matrix
        algo.observe_matrix = agent_matrix
        algo.o_start = agent_start
        algo.o_goal = agent_goal

        state = algo.repeatedAstar(start, goal)

        helper = Helper()
        helper.generate_sol_file(matrix, state)

    def executeAdaptiveAStar(self, fileName):
        matrix = self.gen.decode(fileName)

        start = self.gen.goalState
        goal = self.gen.startState

        agent_matrix = self.gen.generateAgentMatrix(matrix, start)

        agent_start = agent_matrix[start.xPos][start.yPos]
        agent_goal = agent_matrix[goal.xPos][goal.yPos]

        algo = AdaptiveAstar()

        algo.real_matrix = matrix
        algo.observe_matrix = agent_matrix
        algo.o_start = agent_start
        algo.o_goal = agent_goal

        state = algo.repeatedAstar(start, goal)

        algo.closeSetReevaluate()

        if state:
            state = algo.adaptiveAstar(start, goal)

        helper = Helper()
        helper.generate_sol_file(matrix, state)

