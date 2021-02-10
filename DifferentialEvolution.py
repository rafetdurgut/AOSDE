from Individual import *
from Problem import *
from copy import deepcopy
from Operators import *

class DifferentialEvolution:
    def __init__(self, problem, NP, operator, max_iteration=1000, F=0.9, CR=0.2):
        self.NP = NP
        self.F = F
        self.CR = CR
        self.problem = problem
        self.individuals = [Individual(problem) for _ in range(NP)]
        self.max_iter = max_iteration
        self.iter = 0
        self.operator = operator
        self.global_best = Individual(problem)
        self.convergence = []

    def memorize(self):
        best_solution = min(self.individuals, key=lambda b: b.cost)
        if best_solution.cost < self.global_best.cost:
            self.global_best = deepcopy(best_solution)
            self.convergence.append((self.iter, best_solution.cost))
            print(self.global_best.cost)

    def Run(self):
        while self.iter < self.max_iter:
            for ind, individual in enumerate(self.individuals):
                # Mutate
                v = np.copy(individual.solution)
                v = self.operator.get_candidate(v)

                # Crossover
                d1 = np.random.randint(0, self.problem.dimension - 1)
                u = np.copy(individual.solution)
                for i in range(self.problem.dimension):
                    if i == d1 or np.random.rand() < self.CR:
                        u[i] = v[i]
                new_cost = self.problem.objective_function(u)

                # Memorize
                if new_cost < individual.cost:
                    individual.solution = np.copy(u)
                    individual.cost = new_cost
            self.memorize()
            self.iter += 1




