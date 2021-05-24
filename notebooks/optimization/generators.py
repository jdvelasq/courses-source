import numpy as np
from individual import Individual

class RandomUniform:
    #
    # Genera una población inicial aleatoria
    # con valores uniformemente distribuidos
    #
    def __init__(self, pop_size, low, high, seed=None):
        
        self.pop_size = pop_size
        self.low = low
        self.high = high
        
        if seed is None:
            self.rng = np.random.default_rng()
        else:
            self.rng = np.random.default_rng(seed)

    def __call__(self):
        #
        # En cada llamada genera una población diferente
        #
        population = [
            Individual(
                {                   
                    "x": self.rng.uniform(low=self.low, high=self.high),
                    "fn_x": None,   
                }
            )
            for _ in range(self.pop_size)
        ]
        
        return population

    
class RandomBinary:
    #
    # Genera una población inicial aleatoria
    # con valores uniformemente distribuidos
    #
    def __init__(self, pop_size, n_bits, **kwargs):
        self.pop_size = pop_size
        self.n_bits = n_bits
        self.kwargs = kwargs

    def __call__(self):
        population = [
            Individual(
                {
                    **{
                        "x": np.where(np.random.uniform(size=self.n_bits) < 0.5, 0., 1.),
                        "fn_x": None,
                    },
                    **self.kwargs
                }
            )
            for _ in range(self.pop_size)
        ]
        
        return population
