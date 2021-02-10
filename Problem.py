import numpy as np

class Sphere():
    def __init__(self, name, dimension):
        self.name = name
        self.dimension = dimension
        self.lower_bound = np.ones((dimension))* -100
        self.upper_bound = np.ones((dimension)) * 100

    def objective_function(self, solution):
        return np.sum(solution**2)