import numpy as np
from baseoptimizer import BaseOptimizer

class SimulatedAnnealing(BaseOptimizer):
    def __init__(self, fn, t_init=0.5, t_min=0.001, M=1000):
        super().__init__(fn=fn)
        self.t_init = t_init
        self.t_min = t_min
        self.M = M
        self.factor = None

    def __call__(self, population):

        if self.n_dim is None:
            self.n_dim = len(population[0].x)

        if self.factor is None:
            self.factor = np.power(self.t_min / self.t_init, 1.0 / self.M)

        for individual in population:

            if "t_current" not in individual.keys():
                individual["t_current"] = self.t_init

            x = individual.x.copy()
            fn_x = individual.fn_x

            v = self.random_direction()
            x_next = x + np.random.uniform() * individual.t_current * v
            fn_x_next = self.fn(x_next)

            if np.random.uniform() < 1 / (
                1 + np.exp(max(-50, min(50, (fn_x_next - fn_x) / individual.t_current)))
            ):
                individual.x = x_next
                individual.fn_x = fn_x_next

            individual.t_current = max(self.t_min, self.factor * individual.t_current)

        return population
