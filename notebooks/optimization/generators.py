import numpy as np
from individual import Individual

class RandomUniform:
    #
    # Genera una población inicial aleatoria
    # con valores uniformemente distribuidos
    #
    def __init__(self, pop_size, low, high, **kwargs):
        self.pop_size = pop_size
        self.low = low
        self.high = high
        self.kwargs = kwargs

    def __call__(self):
        population = [
            Individual(
                {
                    **{
                        "x": np.random.uniform(low=self.low, high=self.high),
                        "fn_x": None,
                    },
                    **self.kwargs
                }
            )
            for _ in range(self.pop_size)
        ]
        
        return population
