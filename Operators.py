import numpy as np
import math
import copy


class AbstractOperator:
    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def get_candidate(self, i, k):
        raise Exception("Should not call AbstractOperator!")


class DE_RAND_1(AbstractOperator):
    def get_candidate(self, i):
        random_perm = np.random.permutation(self.algorithm.NP)
        a = random_perm[0]
        b = random_perm[1]
        c = random_perm[2]
        i = self.algorithm.individuals[a].solution + self.algorithm.F * (self.algorithm.individuals[b].solution - self.algorithm.individuals[c].solution)
        i = np.clip(i,self.algorithm.problem.lower_bound, self.algorithm.problem.upper_bound)
        return i


