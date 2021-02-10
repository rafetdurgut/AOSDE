import numpy as np


class Individual:

    def __init__(self, problem=None, solution=None):
        self.problem = problem
        self.cost = 0
        if solution is None:
            self.initial()
        else:
            self.solution = solution
        self.evaluate()

    def evaluate(self):
        self.cost = self.problem.objective_function(self.solution)

    def initial(self):
        self.solution = self.problem.lower_bound + np.random.random(self.problem.dimension)*(self.problem.upper_bound - self.problem.lower_bound)
        self.evaluate()

    def get_better(self, candidate):
        if candidate.cost > self.cost:
            return candidate
        else:
            return self

    def __str__(self):
        return f'Solution:{self.solution}, Cost:{self.cost}'
