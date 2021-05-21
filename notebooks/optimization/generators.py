
import numpy as np
from individual import Individual

class RandomUniform:
    #
    # Genera una población inicial aleatoria
    # con valores uniformemente distribuidos
    #
    def __init__(self, pop_size, low, high, sigma=None, sigmas=None):
        self.pop_size = pop_size
        self.low = low
        self.high = high
        self.sigma = sigma
        self.sigmas = sigmas

    def __call__(self):
        #
        #
        #
        population = [
            Individual(
                {
                    "x": np.random.uniform(low=self.low, high=self.high),
                    "fn_x": None,
                }
            )
            for _ in range(self.pop_size)
        ]

        #
        #
        #
        if self.sigma is not None:
            for individual in population:
                individual["sigma"] = self.sigma

        #
        #
        #
        if self.sigmas is not None:
            if isinstance(self.sigmas, (int, float)):
                n_dim = len(self.low)
                self.sigmas = np.array([self.sigmas] * n_dim)
            for individual in population:
                individual["sigmas"] = np.array(self.sigmas)

        return population
