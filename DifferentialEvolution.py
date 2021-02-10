from Individual import *
from Problem import *


class DifferentialEvolution:
    def __init__(self, problem, NP, Cr=0.2, TC=0.1):
        self.individuals = [Individual(problem) for _ in range(NP)]

p = Sphere('Sphere',10)
algo = DifferentialEvolution(p,10)

print(algo.individuals[0])