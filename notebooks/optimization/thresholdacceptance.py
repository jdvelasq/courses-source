
import numpy as np
from baseoptimizer import BaseOptimizer


class ThresholdAcceptance(BaseOptimizer):
    def __init__(self, fn, threshold=10, R=1.0, M=1000, seed=None):
        super().__init__(fn=fn, seed=seed)
        self.threshold = threshold
        self.R = R
        self.M = M
        self.factor = None

    def __call__(self, population):

        population = self.cloning(population) 
        
        if self.n_dim is None:
            self.n_dim = len(population[0].x)

        if self.factor is None:
            self.factor = np.power(1e-6 / self.threshold, 1.0 / self.M)

        for individual in population:

            if "TA_threshold" not in individual.keys():
                individual["TA_threshold"] = self.threshold

            x = individual.x.copy()
            fn_x = individual.fn_x

            v = self.random_direction()
            x_next = x + self.rng.uniform() * self.R * v
            fn_x_next = self.fn(x_next)

            if (fn_x_next - fn_x) <= individual.TA_threshold:
                individual.x = x_next
                individual.fn_x = fn_x_next
                individual.TA_threshold = individual.TA_threshold * self.factor

        return population
